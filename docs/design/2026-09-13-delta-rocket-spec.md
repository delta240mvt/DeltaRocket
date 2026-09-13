# DeltaRocket — specyfikacja v0.1

Realizuje projekt zatwierdzony w rozmowie 2026-09-13, z późniejszą korektą
użytkownika: do dwóch rund review każdego dużego modułu oraz dokładnie dwie
rundy końcowe całej implementacji. Plan: `2026-09-13-delta-rocket-plan.md`.

## Kontrakt

R1. Jeden samodzielny skill `.agents/skills/delta-rocket`, bez zależności od
instalacji źródłowych frameworków. Mały `SKILL.md` ładuje tylko instrukcje
potrzebne na danym etapie. Metadane mają nazwę `delta-rocket`, opis zastosowania
i przykładowe wywołanie. Automatyczne dopasowanie pozostaje domyślne.

R2. Kolejność: brainstorming → plan modułów → jedno review planu i poprawki →
specyfikacja → jedno review specyfikacji i poprawki → uzgodnienie planu ze
specyfikacją → wykonanie modułów → dwie końcowe rundy review. Uzgodnienie planu
nie jest automatycznym ponownym review. Materialna sprzeczność wymaga decyzji,
nie cichego zaakceptowania dokumentu.

R3. Brainstorming rozwiązuje niewiadome celu, zakresu, zachowania i kompromisów.
Agent czyta dostępny kontekst przed pytaniem. Zadaje jedno konkretne pytanie
naraz, przedstawia rekomendację i konsekwencje. Odpowiedzi już udzielone
spełniają bramki. Akceptacja projektu nie musi być ponawiana dla każdego
modułu. Zmiana istotnego kontraktu wraca do użytkownika; rutynowe wybory
implementacyjne rozstrzyga agent. Przy małym zakresie dokumenty mogą być
krótkimi sekcjami jednego pliku, przy zachowaniu kolejności i budżetów.

R4. Plan definiuje trwałe identyfikatory dużych modułów, wynik, granice,
zależności, obszary plików i weryfikację. Specyfikacja określa zachowanie,
interfejsy, błędy, ograniczenia i kryteria akceptacji powiązane z modułami.
Nie kopiujemy całego kodu do planu. Nowy moduł musi mieć samodzielny sens
funkcjonalny; rozbijanie pracy nie może służyć uzyskaniu nowych review.

R5. Główny agent implementuje i poprawia kod. Po zbudowaniu i sprawdzeniu
każdego modułu odbywa się pierwsze review. Drugie odbywa się, gdy pierwsze
wykazało potrzebę poprawek wymagających ponownej oceny. Maksymalnie dwie rundy
na moduł, bez recenzji jego drobnych podpunktów. Po wszystkich modułach:
pierwsze review całości → poprawki i testy → drugie review całości → ewentualne
poprawki i testy. Druga runda końcowa jest wymagana także po czystej pierwszej.

R6. Jedna runda to jedna ograniczona ocena określonego zakresu przez jednego
recenzenta; obejmuje łącznie zgodność ze specyfikacją i jakość. Recenzent może
być subagentem; nie edytuje ani nie deleguje. Bez dostępnych subagentów agent
przeprowadza jawną ocenę sam, z tym samym licznikiem, zaznaczając ograniczenie
niezależności. Testy, diagnoza i bezpośrednie sprawdzenie konkretnej poprawki
przez wykonawcę nie są rundą. Każde nowe zlecenie oceny recenzentowi, także
oceny pojedynczej poprawki, oraz jawne ponowne review inline zużywają rundę.
Ponowny szeroki audyt jest rundą niezależnie od nazwy.

R7. Stan zapisuje zakres, etap, decyzje, statusy modułów, liczniki review
dokumentów/modułów/całości, identyfikatory ocenionych wersji, wyniki testów,
uwagi i następny krok. Rezerwuje rundę przed uruchomieniem recenzenta.
Wznowienie, błąd narzędzia, nowy commit, zmiana nazwy lub podział modułu nie
resetują budżetu. Nieznany stan wymaga odtworzenia dowodów, nie założenia zera.
Wyłącznie jednoznaczne potwierdzenie, że recenzent nie wystartował, pozwala
zwolnić rezerwację. Zmiana limitu wymaga jawnej decyzji użytkownika.

R8. Po limicie agent nadal poprawia potwierdzone błędy i wykonuje testy, lecz
nie uruchamia kolejnego review. Materialne nierozwiązane wymagania lub nieudana
weryfikacja wykluczają gotowość. Jeśli przyczyna blokady jest odkrywalna,
agent kontynuuje diagnozę; prosi o decyzję dopiero przy rzeczywistej zależności.

R9. Review obejmuje cały wskazany zakres, również zmiany staged, unstaged,
nowe pliki i wcześniejsze commity. Nie zakłada `HEAD~1`, dostępnego `HEAD`
ani czystego drzewa. Recenzent dostaje kontrakt, zakres i dowody; wynik zawiera
istotne uwagi z lokalizacją, skutkiem i uzasadnieniem. Autor weryfikuje feedback
przed poprawką; preferencje stylistyczne nie tworzą pętli.

R10. Zachowujemy metody code review, odbierania feedbacku, systematic debugging,
TDD i weryfikacji jako samodzielne adaptacje. Diagnoza poprzedza poprawki,
testy sprawdzają zachowanie, a dowody poprzedzają twierdzenia o ukończeniu.
Prostota nie usprawiedliwia usuwania wymaganej walidacji, testów ani komentarzy
wyjaśniających nietypowe decyzje.

R11. Komunikacja w języku użytkownika: krótki wynik lub istotna zmiana stanu,
bez przepisywania kodu i logów. Pytania pozostają zrozumiałe, dokumentacja
kompletna, a kod czytelny. Skill nie kontroluje kart narzędzi hosta i nie
gwarantuje procentowej oszczędności tokenów ani technicznego wymuszenia limitu.

R12. Skill korzysta z faktycznych możliwości hosta, bez wymuszania modelu,
reasoning effort, konfiguracji agentów, powłoki czy worktree. Nie deklaruje
pierwszeństwa nad instrukcjami systemowymi/deweloperskimi. Użytkownik wybiera
workflow; adaptacje nie uruchamiają oryginalnego executing-plans ani SDD.
Nie zmieniamy istniejących skilli, globalnej konfiguracji ani uprawnień.

## Weryfikacja i granice dowodu

- Walidator frontmatter, metadane YAML, lokalne odnośniki i kompletność pakietu.
- Scenariusze: nieznane wymaganie, zatwierdzony projekt, granice modułu,
  wznowienie z wyczerpanym limitem, final 1 bez uwag, poprawka po final 2,
  brak subagentów, nowy plik w pustym repo, błędny feedback.
- Kontrola bez DeltaRocket pokazuje zachowanie źródłowego procesu;
  próby z nowym skillem sprawdzają decyzje i ślady wykonania w izolowanym miejscu.
- Dwie końcowe oceny pakietu; bez benchmarku oszczędności i bez twierdzenia,
  że krótki test dowodzi niezawodności dla wszystkich przyszłych zadań.
