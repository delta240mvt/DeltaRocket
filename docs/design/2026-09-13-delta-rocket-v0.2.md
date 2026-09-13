# Delta Rocket — kontrakt v0.2

Zatwierdzona korekta po audycie 13 września 2026. Ta wersja zmienia wskazane
niżej reguły v0.1; pozostały kontrakt pozostaje w mocy. Historia v0.1 jest
w `2026-09-13-delta-rocket-spec.md`, a pierwotny research pozostaje historyczny.

## Zakres zmian

1. Drobna, odwracalna zmiana o znanym wyniku i małym ryzyku: bezpośrednia
   implementacja, adekwatna kontrola i raport. Bez formalnych review oraz
   obowiązkowych plan/spec/state. Sam SKILL.md wystarcza do tej ścieżki,
   chyba że wykryty problem uzasadnia odczyt odpowiedniej metody.
   Uprawnienia, integralność danych, publiczne kontrakty i podobne konsekwencje
   wymagają pełnego workflow niezależnie od liczby zmienianych linii.
   Poprawka istniejącego pełnego zakresu zachowuje jego stan i liczniki.
2. W pełnym workflow dokładnie jedno review każdego dużego modułu.
   Główny agent poprawia uwagi i weryfikuje je bezpośrednio, bez drugiej oceny
   modułu. Nadal: jedno review planu, jedno specyfikacji i dwie rundy końcowe.
   Nowy zakres z M modułami ma zatem M+4 formalne sloty.
   Historyczne liczniki 2/2 zachowujemy; nie oznaczają nowego budżetu.
3. Techniczna awaria drugiej rundy końcowej: trwała notatka i kontynuacja,
   bez zastępczego review i bez pytania o zgodę na samo kontynuowanie.
   Globalny rejestr oznacza jeden plik dla wszystkich zakresów projektu:
   `docs/delta-rocket/issues.md`, ewentualnie już istniejący wspólny rejestr.
   Nie jest to plik globalny dla komputera ani automatycznie uruchamiane zadanie.
4. Wpis zawiera trwały ID, zakres, rundę/próbę, wersję plików, dowód awarii,
   brakujące pokrycie oceny, znane uwagi i ich status oraz następny krok.
   Zachowujemy istniejącą zawartość i aktualizujemy ten sam incydent po wznowieniu.
   Liczymy osobno próby zużyte i oceny ukończone. Brak raportu nie oznacza
   zaliczonego review ani odkrytej wady kodu.
5. Ukończenie z taką notatką jest dozwolone, jeżeli pierwsze końcowe i pozostałe
   wymagane review są ukończone, kontrole bieżącego stanu przechodzą i nie ma
   nierozwiązanej istotnej wady. Finał ujawnia brak drugiej oceny oraz link do
   rejestru. Nieprzechodzący test i potwierdzone błędy wymagają naprawy;
   negatywny wynik merytoryczny review nie jest jego awarią techniczną.

Benchmark i aktywacja/współistnienie z innymi workflow pozostają poza zakresem
tej zmiany zgodnie z decyzją użytkownika. Nie zmieniamy modeli, metadanych
aktywacji, globalnych pluginów ani historycznych wyników prób.

## Warunki walidacji

- Powtórzona rzeczywista poprawka JSON: poprawny wynik, zero formalnych review
  i zero obowiązkowych dokumentów procesu.
- Jednoliniowa zmiana uprawnień: pełny workflow.
- Awaria final 2: rzeczywisty zapis do rejestru w fixture, zachowanie istniejącego
  wpisu, brak duplikatu po wznowieniu i kontynuacja z ujawnieniem ograniczenia.
- Istotny błąd wykryty w final 2: naprawa i kontrola zamiast ukrycia w backlogu.
- Moduł po jednym review: bez drugiego; historyczny moduł po dwóch: bez resetu.
- Niezależne review zmienionego pakietu i dokumentacji, walidator formatu,
  poprawne lokalne odnośniki. Próby są walidacją zachowania, nie benchmarkiem.
