import requests
from bs4 import BeautifulSoup
import csv
import sys

url_2 = sys.argv[1]
jmeno_souboru = sys.argv[2]
url_3 = url_2.split("ps2017nss/")[0] + "ps2017nss/"

# vyextrahovani jmena zucastněných stran
strany = []
url1 = 'https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=12&xobec=506761&xvyber=7103'

response = requests.get(url1)
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')
tables = soup.find_all('table', {'class': 'table'})

for table in tables[1:3]:
    tabulka_a = table.find_all('tr')
    for row in tabulka_a:
        cells = row.find_all('td')
        if cells:
            strany.append(cells[1].text.strip())

with open(jmeno_souboru, 'w', newline='', encoding='utf-8') as csv_file:
    csv_file.write("Číslo obce," "Jméno obce," "Seznam," "Vydané," "Platné,")
    for i, stran in enumerate(strany):
        stran = stran.replace(',', '.')
        if i != len(strany) - 1:
            csv_file.write(stran + ',')
        else:
            csv_file.write(stran + '\n')

pocitadlo = 0

while pocitadlo <= 2:
    response = requests.get(url_2)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    tables = soup.find_all('table', {'class': 'table'})
    table = tables[pocitadlo]
    rows = table.find_all('tr')

    with open(jmeno_souboru, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        for row in rows:
            cells = row.find_all('td')
            if cells:
                obec_cislo = cells[0].text.strip()
                jmeno_obce = cells[1].text.strip()
                link_cell = cells[0].find('a')
                if link_cell:
                    podstranka_url = link_cell['href']

                    url = url_3 + podstranka_url
                    hlasy = []
                    response = requests.get(url)
                    html_content = response.content
                    soup = BeautifulSoup(html_content, 'html.parser')
                    tables = soup.find_all('table', {'class': 'table'})

                    for table in tables[1:3]:
                        tabulka_a = table.find_all('tr')

                        for row in tabulka_a:
                            cells = row.find_all('td')
                            if cells:
                                hlasy.append(cells[2].text.strip())

                    response = requests.get(url)
                    html_content = response.content
                    soup = BeautifulSoup(html_content, 'html.parser')
                    tables = soup.find_all('table', {'class': 'table'})
                    table = tables[0]
                    rows = table.find_all('tr')

                    for row_B in rows:
                        cells = row_B.find_all('td')
                        if cells:
                            v_seznamu = cells[3].text.strip()
                            vydane_obalky = cells[4].text.strip()
                            odevzdane = cells[7].text.strip()
                            writer.writerow(([obec_cislo, jmeno_obce, v_seznamu, vydane_obalky, odevzdane])+hlasy)

    pocitadlo += 1
