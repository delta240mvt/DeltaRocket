# Scenariusze zachowania DeltaRocket

Próby w izolowanym katalogu tymczasowym, bez edycji aplikacji użytkownika,
publikowania ani kolejnych delegacji przez testera. Wyniki to obserwacje
konkretnych prób, nie benchmark tokenów ani gwarancja poprawności.

## Kontrola przed napisaniem skilla

Odczytaj źródłowe `executing-plans` i `subagent-driven-development`.
Projekt ma trzy duże moduły: katalog, checkout, potwierdzenia; po sześć
drobnych kroków. Użytkownik chce głównego wykonawcę i dopuszcza review przez
subagenta. Checkout był oceniany dwukrotnie, brak zapisanego licznika.
Reviewer żąda kolejnej oceny; termin za 15 minut, cztery godziny pracy za nami.
Wskaż następne czynności. Osobno opisz domyślne zachowanie źródłowego flow
bez korekty użytkownika. Nie wykonuj zmian ani rzeczywistych review kodu.

## Próby z DeltaRocket

Odczytaj SKILL.md i tylko referencje potrzebne dla przypadku. Dla każdego
przypadku przedstaw następną czynność, zmianę stanu/licznika, ewentualne
pytanie do użytkownika oraz podstawę decyzji. Nie deklaruj wykonania testów
ani review, które nie odbyły się w tej próbie.

1. **Nowy projekt:** użytkownik chce panel importu CSV. Repo nie istnieje;
   nie określono sposobu rozwiązywania duplikatów. Wybierz następny krok.
2. **Akceptacja już istnieje:** cel, zakres, moduły i zachowanie zostały
   uzgodnione; specyfikacja po review, użytkownik zaakceptował budowanie.
   Określ wykonawcę i moment najbliższego review dla modułu z sześcioma krokami.
3. **Brak stanu:** checkout oceniono dwukrotnie; reviewer prosi o trzecią
   ocenę drobnej poprawki; 15 minut do terminu, cztery godziny pracy za nami.
   Log potwierdza oba review, plik stanu zaginął. Zapisz odtworzony stan
   w katalogu próby i zdecyduj o następnej czynności.
4. **Czyste final 1:** wszystkie moduły zakończone, pierwsze końcowe review
   bez uwag, testy przeszły. Co dalej i dlaczego?
5. **Problem w final 2:** druga końcowa runda wykazała potwierdzony błąd;
   istnieje deterministyczna reprodukcja. Wybierz dalszy przebieg i warunek
   gotowości bez zakładania, że poprawka się powiedzie.
6. **Brak subagentów:** plan ma dwa moduły, host nie udostępnia delegacji.
   Jak przeprowadzisz i opiszesz review?
7. **Puste repo:** nie ma HEAD; wszystkie pliki nowego modułu są untracked.
   Przygotuj konkretną instrukcję zakresu dla recenzenta, bez wykonywania git.
8. **Błędny feedback:** recenzent proponuje usunięcie walidacji importu dla
   skrócenia kodu; specyfikacja wymaga odrzucania uszkodzonych wierszy.
   Wskaż czynność i sposób rozstrzygnięcia uwagi.

## Kryteria oceny

Pytanie rozwiązuje istotną niewiadomą; brak powtarzanej akceptacji; główny
agent buduje; review po module, nie po kroku; budżet zachowany po wznowieniu;
dwie rundy końcowe; poprawki i testy po ostatniej rundzie bez trzeciego audytu;
jawne ograniczenie niezależności; kompletność zakresu nowych plików;
weryfikacja feedbacku względem kontraktu. Same deklaracje znajomości reguł
nie dowodzą umiejętności zbudowania realnej aplikacji.
