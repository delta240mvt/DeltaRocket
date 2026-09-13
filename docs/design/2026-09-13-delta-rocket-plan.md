# Delta Rocket — plan modułów

Status: projekt zatwierdzony w rozmowie; jedno niezależne review planu wykonane,
bez istotnych uwag. Szczegóły liczników i zakończenia określa specyfikacja.

## Cel i decyzje użytkownika

Jeden przenośny skill do budowania z AI: proces Superpowers, prostota Ponytail,
zwięzła komunikacja inspirowana Caveman. Brainstorming z bramkami sokratycznymi,
plan modułów, review planu, szczegółowa specyfikacja, review specyfikacji,
wykonanie przez głównego agenta. Maksymalnie dwa review każdego dużego modułu,
następnie dwie rundy review całej implementacji. Dobre metody debugowania,
odbierania review i weryfikacji zostają zachowane.

## M1 — sterowanie procesem

- Wynik: `.agents/skills/delta-rocket/SKILL.md`, metadane Codexa oraz referencje
  dla brainstormingu, planowania, specyfikacji, wykonania i polityki review.
- Odpowiedzialność: kolejność etapów, bramki, granice modułów, autorstwo kodu,
  trwały stan i budżety review, krótka komunikacja.
- Zależności: uzgodnienia w rozmowie i research; bez zależności od instalacji
  Superpowers, Ponytail lub Caveman.
- Weryfikacja: realistyczne scenariusze wznowienia pracy, niejasnych wymagań,
  wyczerpanego budżetu i dwóch rund końcowych; walidator struktury skilla.

## M2 — metody jakości i przekazanie do użycia

- Wynik: ładowane na żądanie metody code review, odbierania feedbacku,
  systematic debugging, TDD i weryfikacji; dokumentacja użycia i pochodzenia.
- Odpowiedzialność: zachowanie wartościowych technik bez importowania
  sprzecznych wyzwalaczy delegacji i nieograniczonych pętli.
- Zależność: kontrakt sterowania z M1.
- Weryfikacja: recenzent ma dostęp do całego zakresu, w tym nowych plików;
  błędny feedback jest weryfikowany; błędy diagnozowane przed poprawką;
  końcowe twierdzenia o jakości odpowiadają rzeczywiście wykonanym kontrolom.

## Granice

Nie budujemy pluginu, silnika wykonawczego, telemetrii ani własnego systemu
agentów. Nie zmieniamy globalnej konfiguracji, nie instalujemy globalnie i nie
publikujemy na GitHubie w tym kroku. Repo jest źródłem skilla; `.agents/skills`
zapewnia lokalizację projektu rozpoznawaną przez Codexa.

## Kolejność

Sprawdzenie planu → specyfikacja → sprawdzenie specyfikacji i zgodności planu →
M1 → M2 → walidacja zachowania i struktury → końcowe review i poprawki →
drugie końcowe review → ponowna weryfikacja zmienionych elementów.

Budowa nie wymaga przykładowej aplikacji ani kompletu kodu w planie.
