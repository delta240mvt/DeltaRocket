# Delta Rocket

<div align="center">

<pre align="left">
                                                          ▄▄▀
                                                    ▄▄▄████▀
                                               ▄▄▄█████████
                                             ▄████████████
                                           ▄█████████████▀
                                         ▄███▓▓▓████████▀
                                       ▄██▓▓     ▓██████
                                   ▄▄▄████▓▄     ▓▓███▀
                            ▄▄▄▓▓▓▓▓██████▓▓▄▄ ▄▄▓██▀
                    ▄▄▄▄▓▓▓▓▓▓▓▓▓▓██████████▓▓▓▓▓█▀
                     ▀▓▓▓▓▓▓▓▓▓▓████████████████▀
                       ▓▓▓▓▓▓▓████████████████▀
                        ▀▓▓▓█▓▓▓█████████████▓
                         ▄█████▓▓▓█████████▓▓
                         ▒███████▓▓▓█████▓▓▓▓
                        ▒▒▒▒███████▓▓▓█▓▓▓▓▓
                         ▒▒▒▒▒███████▓▓▓▓▓▓▀
                     ▒▒▒▒  ▒▒▒▒▒▀█▀▓▓▓▓▓▓▓▓
                   ▒▒▒▒▒▒▒▒  ▒▒     ▀▓▓▓▓▓▀
                ▒▒▒▒▒▒▒▒▒▒▒            ▀▓▓
             ░░░░▒▒▒▒▒▒▒▒                ▀
          ░ ░ ░░░░░▒▒▒▒▒
             ░░░░░░░░▒▒
            ░░░░░░  ░░
           ░░░░     ░
         ░░

                ██████╗ ███████╗██╗  ████████╗ █████╗
                ██╔══██╗██╔════╝██║  ╚══██╔══╝██╔══██╗
                ██║  ██║█████╗  ██║     ██║   ███████║
                ██║  ██║██╔══╝  ██║     ██║   ██╔══██║
                ██████╔╝███████╗███████╗ ██║   ██║  ██║
                ╚═════╝ ╚══════╝╚══════╝ ╚═╝   ╚═╝  ╚═╝

        ██████╗  ██████╗  ██████╗██╗  ██╗███████╗████████╗
        ██╔══██╗██╔═══██╗██╔════╝██║ ██╔╝██╔════╝╚══██╔══╝
        ██████╔╝██║   ██║██║     █████╔╝ █████╗     ██║
        ██╔══██╗██║   ██║██║     ██╔═██╗ ██╔══╝     ██║
        ██║  ██║╚██████╔╝╚██████╗██║  ██╗███████╗   ██║
        ╚═╝  ╚═╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝   ╚═╝

                           BY DELTA240MVT
</pre>

**Od pomysłu do działającego kodu. Jasne decyzje, duże moduły, konkretne review.**

[![Codex Skill](https://img.shields.io/badge/Codex-Skill-111111?style=flat-square)](.agents/skills/delta-rocket/SKILL.md) [![Version](https://img.shields.io/badge/Version-0.1-4a8d83?style=flat-square)](docs/design/2026-09-13-delta-rocket-spec.md) [![Module reviews](https://img.shields.io/badge/Module_reviews-max_2-f4c542?style=flat-square)](.agents/skills/delta-rocket/references/review-policy.md) [![Final reviews](https://img.shields.io/badge/Final_reviews-2-9b7bdb?style=flat-square)](.agents/skills/delta-rocket/references/review-policy.md)

**Jeden główny wykonawca · Prosty, czytelny kod · Krótka komunikacja**

[Szybki start](#szybki-start) · [Workflow](#workflow) · [Review](#zasady-review) · [Dokumentacja](#dokumentacja)

</div>

---

Delta Rocket to skill do budowania z AI, który łączy proces Superpowers,
prostotę Ponytail i zwięzłość Caveman. Agent pomaga doprecyzować pomysł,
planuje moduły, zapisuje specyfikację i prowadzi implementację. Recenzje mają
określony zakres i budżet, a kolejne sesje korzystają z zapisanych ustaleń.

## Co robi Delta Rocket

| Możliwość | Znaczenie w praktyce |
| --- | --- |
| Brainstorming z bramkami sokratycznymi | Pytania o cel, zakres, zachowanie i kompromisy, które rzeczywiście zmieniają rozwiązanie. |
| Plan dużych modułów | Spójne funkcjonalności z zależnościami i kryteriami ukończenia. |
| Szczegółowa specyfikacja | Kontrakty, przypadki brzegowe i testowalne wymagania przed implementacją. |
| Jeden główny wykonawca | Główny agent buduje i poprawia kod; subagent może wykonać review. |
| Ograniczone rundy review | Do dwóch ocen na duży moduł oraz dwie końcowe oceny całej implementacji. |
| Sprawdzone metody jakości | Code review, weryfikacja feedbacku, systematic debugging, TDD i sprawdzenie przed zakończeniem. |
| Trwały stan pracy | Decyzje, postęp, wyniki kontroli i liczniki review przetrwają wznowienie sesji. |
| Zwięzła komunikacja | Krótkie aktualizacje przy zachowaniu czytelnego kodu, komentarzy i pełnej dokumentacji. |

## Workflow

```text
POMYSŁ
  |
  v
Brainstorming + bramki sokratyczne
  |
  v
Plan dużych modułów -------> Review planu + poprawki
  |
  v
Szczegółowa specyfikacja --> Review specyfikacji + poprawki
  |
  v
Implementacja modułu ------> Testy + review modułu (max 2)
  |                              |
  |  następny moduł              | poprawki głównego agenta
  +------------------------------+
  |
  v
Review całej implementacji: runda 1
  |
  v
Poprawki + testy
  |
  v
Review całej implementacji: runda 2
  |
  v
Ostatnie poprawki + weryfikacja
```

Plan opisuje podział pracy i podejście. Specyfikacja ustala dokładne zachowanie.
Agent korzysta z wcześniejszych odpowiedzi i akceptacji; pyta ponownie, gdy
nowe odkrycie wymaga istotnej zmiany uzgodnionego rozwiązania.

## Zasady review

| Zakres | Budżet |
| --- | --- |
| Plan modułów | Jedno review i poprawki. |
| Specyfikacja | Jedno review i poprawki. |
| Każdy duży moduł | Jedno obowiązkowe review; drugie, gdy poprawki wymagają ponownej oceny. |
| Cała implementacja | Dokładnie dwie rundy po ukończeniu wszystkich modułów. |

Drobne kroki wewnątrz modułu nie uruchamiają osobnych recenzji. Drugie końcowe
review odbywa się również wtedy, gdy pierwsze nie wykazało problemów.
Po ostatniej rundzie główny agent wprowadza uzasadnione poprawki i uruchamia
odpowiednie kontrole. Wyczerpany budżet nie oznacza automatycznie gotowości.

Pełne reguły liczenia, wznowienia i rozstrzygania uwag:
[polityka review](.agents/skills/delta-rocket/references/review-policy.md).

## Szybki start

### W tym repozytorium

```bash
git clone https://github.com/delta240mvt/DeltaRocket.git
cd DeltaRocket
```

Otwórz katalog w Codexie i wywołaj:

```text
$delta-rocket Zbuduj panel importu CSV z podglądem danych i obsługą błędów.
```

Skill jest zapisany w `.agents/skills/delta-rocket`, czyli katalogu skilli
projektu rozpoznawanym przez Codexa. Jeśli nie pojawia się na liście,
uruchom ponownie Codexa.

### W innym projekcie

Skopiuj cały katalog [`delta-rocket`](.agents/skills/delta-rocket) do
`.agents/skills/` wybranego projektu. Zachowaj referencje, metody i notices.
Wywołuj go w ten sam sposób. Nie wymaga instalowania Superpowers, Ponytail
ani Caveman.

## Mapa projektu

```text
.agents/skills/delta-rocket/
  SKILL.md                  wejście i sterowanie procesem
  agents/openai.yaml        metadane Codexa
  references/               instrukcje etapów i polityka review
  methods/                  metody jakości ładowane na żądanie
  SOURCES.md                pochodzenie i zakres adaptacji
  THIRD_PARTY_NOTICES.md     informacje licencyjne źródeł
docs/
  design/                   plan i specyfikacja skilla
  research/                 analiza źródeł
  testing/                  scenariusze i wyniki walidacji
```

## Walidacja i zakres v0.1

Wersja v0.1 przeszła walidację struktury, osiem symulowanych scenariuszy
procesowych oraz dwie końcowe oceny pakietu. Szczegóły i granice tych prób
znajdziesz w [raporcie walidacji](docs/testing/2026-09-13-results.md).

Skill jest zestawem instrukcji dla agenta. Nie wymusza technicznie limitów,
nie kontroluje kart narzędzi Codexa i nie gwarantuje procentowych oszczędności
tokenów. Korzysta z możliwości i modelu dostępnego w danym hoście; istniejące
skille i konfiguracja pozostają bez zmian.

## Dokumentacja

- [Plan modułów](docs/design/2026-09-13-delta-rocket-plan.md)
- [Specyfikacja v0.1](docs/design/2026-09-13-delta-rocket-spec.md)
- [Deep research](docs/research/2026-09-13-delta-rocket-deep-research.md)
- [Scenariusze zachowania](docs/testing/scenarios.md)
- [Wyniki walidacji](docs/testing/2026-09-13-results.md)

## Pochodzenie projektu

Delta Rocket rozwija własny workflow na podstawie
[Superpowers](https://github.com/obra/superpowers),
[Ponytail](https://github.com/dietrichgebert/ponytail) i
[Caveman](https://github.com/juliusbrussee/caveman).
Źródłowe instrukcje zostały zaadaptowane do głównego wykonawcy, dużych modułów
i ograniczonych rund review.

Dokładne wersje i zakres zmian opisuje [SOURCES.md](.agents/skills/delta-rocket/SOURCES.md).
Informacje licencyjne adaptowanych materiałów znajdują się w
[THIRD_PARTY_NOTICES.md](.agents/skills/delta-rocket/THIRD_PARTY_NOTICES.md).

---

<div align="center"><strong>DELTA ROCKET · BY DELTA240MVT</strong><br><em>Przemyśl. Zbuduj. Sprawdź.</em></div>
