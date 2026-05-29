# Zadanie

Dnešním úkolem je připravit strategii pro obchodování v aukcích. Ve skutečnosti je třeba připravit dvě strategie - jednu pro aukci s rostoucí cenou a jednu pro aukci s klesající cenou. U jednoduchých aukcí jednotlivých objektů by strategie byly jednoduché, proto je situace v zadání trochu složitější. Budeme simulovat aukci řady různých objektů (za různé ceny). Pro každý z těchto objektů dostanete svou vnitřní hodnotu a vaším cílem je maximalizovat skóre, které spočítáme jako 
M+V, kde M jsou zbývající peníze, V je vaše vnitřní hodnota objektů, které jste koupili. Částka M nemůže být záporná. Aby se celá záležitost ještě více zkomplikovala, dostanete omezený rozpočet na obchodování (počáteční množství peněz).

K implementaci použijte připravené zdrojové kódy. Příklad strategie je implementovaný v strategies/example.py. Tato strategie se zajímá o jakýkoli objekt, pokud je jeho cena nižší než jeho hodnota a strategie má dostatek peněz na jeho koupi. Pro implementaci vlastní strategie doporučuji vytvořit novou kopii tohoto souboru (s novým a jedinečným názvem) a implementovat vlastní třídu. Komentáře k jednotlivých metodám ve třídě vysvětlují, co metoda dělá a kdy je volána. Nejdůležitější je, že musíte implementovat metodu interested, která vrací True, jestliže má strategie zájem koupit objekt za danou cenu.

V souboru je také třeba napsat dvě funkce - strategy_ascending a strategy_descending, které vrátí vaši strategii pro anglickou, respektive holandskou verzi aukce. Obě metody mají pouze jeden parametr - počet strategií v turnaji. Můžete mít jednu strategii pro obě verze turnaje, nicméně doporučuji mít dvě různé strategie (tj. implementovat dvě různé třídy).

