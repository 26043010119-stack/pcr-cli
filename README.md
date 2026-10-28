# pcr-cli

> Simulate a PCR thermal cycler, right from your terminal.

Polymerase Chain Reaction (PCR) is one of the most important techniques in bioengineering. **pcr-cli** is a zero-dependency Python script that walks you through the three PCR steps and shows how a single DNA template doubles with every cycle.

## Features

- **Zero Dependencies:** Built entirely with Python's standard library. No `pip install` required.
- **Visual Reset:** Automatically clears your terminal for a clean, distraction-free display.
- **Thermal Cycling:** Simulates denaturation (95 C), annealing (55 C) and extension (72 C) with live countdown timers.
- **Exponential Growth:** Tracks and displays the number of DNA copies after each cycle.
- **Bioengineering Facts:** Shows a randomized fact before every run.

## Quickstart

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/pcr-cli.git
   cd pcr-cli
   ```

2. Run the script:

   ```bash
   python PCR.py
   ```

3. Press **Enter** to start, then watch the 3 thermal cycles run.

Press `Ctrl+C` at any time to abort the run.

## How It Works

| Step         | Temperature | Time | What happens                              |
|--------------|-------------|------|-------------------------------------------|
| Denaturation | 95 C        | 5 s  | DNA strands separate                      |
| Annealing    | 55 C        | 4 s  | Primers bind to the target                |
| Extension    | 72 C        | 6 s  | Polymerase synthesizes new strands        |

Times are shortened for demonstration. Real PCR steps usually take 30 to 60 seconds.

## Project Structure

```
pcr-cli/
├── PCR.py
├── README.md
└── requirements.txt
```

## License

MIT
