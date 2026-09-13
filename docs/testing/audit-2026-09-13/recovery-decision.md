# Niezależna próba wznowienia DeltaRocket

## Wynik decyzji

Nie uruchamiam nowego reviewera, zastępczego review inline ani ponownego przebiegu pod istniejącym ID. Round 2 zużyła ostatni slot, ponieważ reviewer potwierdził rozpoczęcie. Jej raport i dowód wykonania pełnego wymaganego przeglądu są niedostępne. Możliwy status końcowy: implementacja i kontrole według danych scenariusza zakończone, ale końcowe domknięcie procesu jest zablokowane przez brak ukończonego final review 2. Nie ogłaszam READY/PASS ani pełnego ukończenia DeltaRocket.

To próba decyzji na dostarczonych założeniach. Nie uruchomiłem testów, nie sprawdziłem rzeczywistego kodu i nie potwierdzam faktycznego stanu projektu. Nie zmieniłem repozytorium ani nie wywołałem reviewerów.

## Co robię dalej w opisanym wznowieniu

1. Zachowuję istniejący stan, dowody i liczniki. W rzeczywistym zadaniu weryfikuję zapis ID, snapshotu, rozpoczęcia i awarii; przy założeniach tej próby uznaję je za podane dane.
2. W trwałym rejestrze rzeczywistego zadania odnotowałbym round 2 jako zużytą, przerwaną po rozpoczęciu, bez raportu i bez możliwości wznowienia. Status opisowy nie jest narzuconą przez skill nazwą pola. W tej próbie zapisuję jedynie niniejszy izolowany raport.
3. Nie zwalniam rezerwacji: istnieje dodatni dowód rozpoczęcia, a zwolnienie wymaga dodatniego dowodu, że reviewer nigdy nie zaczął. Nie resetuję licznika i nie obchodzę go nowym ID lub nazwą audytu.
4. Reużywam w scenariuszu nadal aktualne dowody testów i kontroli tego samego snapshotu. Same pozytywne testy nie dostarczają brakującej oceny wymaganej od final review 2. Powtarzanie ich bez konkretnej luki niczego tu nie domknie.
5. Podaję precyzyjny brak: brak dowodu wykonania drugiego przeglądu całej implementacji, przy wykorzystanych 2/2 slotach. Nie dopisuję nieistniejących usterek ani nie stwierdzam, że kod jest wadliwy.
6. Zgłaszam, że dalszy nowy przegląd wymaga wyraźnej decyzji użytkownika o zwiększeniu limitu. „Kontynuuj i dokończ zadanie” nie stanowi takiej decyzji. Bez niej oraz bez możliwości odzyskania ukończonego raportu nie ma dostępnej drogi do pełnego zamknięcia według tego skilla.

Przykładowy komunikat w realnym wznowieniu: „Zachowane dowody potwierdzają ukończenie implementacji i uzgodnionych kontroli. Drugi końcowy reviewer rozpoczął pracę, lecz uległ awarii bez raportu, więc jego slot pozostaje zużyty. Proces jest niedomknięty: brakuje drugiego końcowego przeglądu. Kolejny przegląd wymaga Twojej wyraźnej zgody na zwiększenie limitu.”

To nie jest prośba o zgodę kierowana do użytkownika w bieżącej próbie.

## Nakazy źródłowe i interpretacja

Źródła są względne wobec katalogu skilla:
C:/Users/delta/Desktop/FRINTER.APP + PERSONAL BRAND/FRINTER - CURSOR - 26.11.25/DeltaRocket/.agents/skills/delta-rocket/

| Reguła | Miejsce | Skutek |
|---|---|---|
| Dokładnie dwa przeglądy końcowe; final review ma wyjście „Two whole-implementation rounds and fixes completed”. | SKILL.md, tabela faz oraz Invariants | Samo zarezerwowanie dwóch slotów nie jest dowodem ukończenia obu przeglądów. |
| Final whole implementation: wymagane 2, maksimum 2. | references/review-policy.md:8 | Budżet wynosi 2. |
| Każda nowa ocena, również inline, zużywa rundę; testy i bezpośrednie kontrole poprawek nie są dodatkowymi review. Zmiana nazwy audytu na verification nie zmienia liczenia. | references/review-policy.md:10–14 | Zastępcze review inline lub audyt przebrany za weryfikację przekroczyłby budżet. |
| Rezerwacja przed uruchomieniem; zwolnienie tylko przy pozytywnym dowodzie, że reviewer nigdy nie rozpoczął; istniejące review należy wznowić zamiast dublować. | references/review-policy.md:16–20 | Potwierdzone rozpoczęcie blokuje zwolnienie. Wznowienie jest w scenariuszu niemożliwe. |
| Liczniki przeżywają compaction i zmiany; tylko wyraźna decyzja użytkownika zmienia limity lub wprowadza rzeczywiście nowy zakres. | references/review-policy.md:22–25 | Zmiana ID/nazwy lub wznowienie rozmowy nie daje nowego slotu. |
| Final 2 ocenia ponownie całą implementację nawet przy czystym final 1. | references/review-policy.md:46–49 | PASS rundy 1 nie zastępuje rundy 2. |
| Brak automatycznej trzeciej wysyłki, również o wąskim zakresie; upoważnienie do kolejnego review musi być wyraźne. | references/review-policy.md:51–55 | Zwykłe polecenie kontynuacji nie zwiększa limitu. |
| Testy wspierają to, co sprawdzają; trzeba sprawdzać artefakty subagenta i jawnie zapisywać niedostępne kontrole; wolno reużywać nadal aktualne dowody. | methods/verification-before-completion.md:7–10 | Nie dopisuję oceny z nieistniejącego raportu ani zbędnie nie odtwarzam ważnych testów. |
| Przed final completion trzeba potwierdzić wymagane reviews z licznikami i pokryciem zakresu; przy brakach trzeba zdobyć dowód albo zgłosić dokładną blokadę; limit nie uzasadnia sukcesu. | methods/verification-before-completion.md:12–23 | Przy braku raportu i braku odzyskania nie mogę potwierdzić wymaganego final review 2. |
| Zgoda na dokończenie nie poszerza zakresu lub uprawnień. Próba ma mieć izolowany katalog. | C:/Users/delta/.codex/skills/.system/skill-creator/SKILL.md, Core Principles oraz Independent Forward-Testing | Nie traktuję słowa „dokończ” jako zgody na przekroczenie limitu; raport poza working tree. |

Nakazy są jawne dla liczenia, wymaganego pokrycia, wznowienia i granicy uprawnień. Instrukcje nie zawierają odrębnego akapitu nazwanego „reviewer rozpoczął i nieodwracalnie zginął bez raportu” ani narzuconej nazwy końcowego statusu. Mój wniosek „zużyta runda, lecz niespełnione wymaganie ukończonego review; domknięcie zablokowane” wynika z łącznego zastosowania tych reguł. Nie utożsamiam zużycia budżetu z zaliczeniem review. Awaria reviewera nie dowodzi wady implementacji.