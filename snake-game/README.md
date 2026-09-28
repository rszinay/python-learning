# Hadí hra (verze 2)

Klasická hra had napsaná v Pythonu pomocí knihovny `turtle`. Verze 2 je přepsaná do objektů (třídy `Snake`, `Food`, `Scoreboard`, `Message`).

Ovládáte hada, sbíráte červená jablka a snažíte se nenarazit do okraje okna ani do vlastního těla. Za každé jablko dostanete 10 bodů a had se prodlouží. Když nabouráte, hra ukáže vaše skóre (a případně blahopřeje k rekordu) a začne znovu.

## Požadavky

- Python 3.8 nebo novější
- knihovna `turtle` (je součástí Pythonu; potřebuje `tkinter`)

Nic se neinstaluje, žádné další balíčky nejsou potřeba.

Kontrola, že vše funguje:

```bash
python3 -c "import tkinter; print('OK')"
```

Pokud vypíše chybu, u Pythonu z Homebrew doinstalujte `brew install python-tk`.

## Spuštění

```bash
cd ~/Desktop/snake-game-v2
python3 main.py
```

## Ovládání

| Klávesa | Akce |
|---------|------|
| **W** | nahoru |
| **S** | dolů |
| **A** | doleva |
| **D** | doprava |
| **Esc** | ukončit hru (zavře okno) |

Hra začne stisknutím kterékoli z kláves W, A, S, D. Had se nemůže otočit o 180° (třeba z pohybu doprava rovnou doleva). Okno jde ukončit také zavřením křížkem.

## Nejvyšší skóre

Nejvyšší skóre se ukládá do souboru `highscore.json`, který se vytvoří vedle skriptů při prvním rekordu. Po dalším spuštění se načte a hra na něj naváže. Když chcete začít znovu od nuly, soubor smažte.

## Struktura projektu

| Soubor | Co obsahuje |
|--------|-------------|
| `main.py` | okno hry, ovládání a herní smyčka (`ontimer` + `mainloop`) |
| `snake.py` | třída `Snake` – tělo hada, pohyb, růst, kolize |
| `food.py` | třída `Food` – jablko, které se objevuje na náhodném místě mimo hada |
| `scoreboard.py` | třída `Scoreboard` – skóre, nejvyšší skóre, rekord, načítání a ukládání do souboru |
| `message.py` | třída `Message` – úvodní návod a hláška GAME OVER |
| `highscore.json` | uložené nejvyšší skóre (vznikne samo při prvním rekordu) |

## Nápady na vylepšení

- Uložení **jména** hráče k nejvyššímu skóre. Po rekordu se zeptat na jméno (`screen.textinput`), uložit ho do `highscore.json` vedle skóre a zobrazit ho ve skóre nahoře.
- Ovládání šipkami.
- Zrychlování hada s rostoucím skóre.
