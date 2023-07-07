Toto je pokus o vytvoření ukolu č.3

Funkce programu je naseldující: 
Program exportuje z vybraného Okresu jednotlivé okrsky uloží je do uživatelem definováného souboru.

1) Nainstalujte jednotliové knihovny s requirments.txt
2) vyberte Okres z volby.cz napřiklad: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103
3) spustě program pomocí tohoto příkazu: 
python3 main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103" "datovy.csv"

první podmínka je volební okres: "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103"
druha podmínka je jmeno csv souboru: "datovy.csv"

Při správné funkci program vyexportuje volební hlasy jednotlivých okrsků do CSV souboru se kterýma je možné dále pracovat. 

import do excel provádejte pomocí "soubor import vybrte kodování utf 8 a oddělovač je středník ;
