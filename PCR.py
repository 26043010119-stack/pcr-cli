import os
import random
import sys
import time

# A collection of bioengineering facts
FACTS = [
    "PCR was conceived by Kary Mullis in 1983 and earned him a Nobel Prize in 1993.",
    "Taq polymerase comes from Thermus aquaticus, a bacterium found in hot springs.",
    "The human genome contains roughly 3 billion base pairs of DNA.",
    "CRISPR-Cas9 was adapted from a bacterial immune system.",
    "Each PCR cycle can double the target DNA: 30 cycles can yield about a billion copies.",
]

# (step name, temperature in Celsius, duration in seconds, what happens)
PCR_STEPS = [
    ("Denaturation", 95, 5, "Double-stranded DNA separates into single strands."),
    ("Annealing", 55, 4, "Primers bind to their matching target sequences."),
    ("Extension", 72, 6, "Polymerase builds new complementary strands."),
]

TOTAL_CYCLES = 3


def clear_screen():
    """Clears the terminal screen for a distraction-free experience."""
    os.system('cls' if os.name == 'nt' else 'clear')


def pcr_cycle():
    """Runs a single thermal cycle: denature, anneal, extend."""
    for name, temp, duration, description in PCR_STEPS:
        sys.stdout.write(f"\n{name} at {temp} C\n{description}\n")
        sys.stdout.flush()

        # Countdown timer on the same line
        for i in range(duration, 0, -1):
            sys.stdout.write(f"\r{i}s  ")
            sys.stdout.flush()
            time.sleep(1)

    print("\n")


def main():
    clear_screen()
    print("Welcome to PCR Simulator.")
    print("-" * 40)
    print(random.choice(FACTS))
    print("-" * 40)

    input("\nPress [Enter] to load the thermal cycler...")
    clear_screen()

    print("Loading sample into the thermal cycler.")
    print("Watch the DNA copies double each cycle.\n")
    time.sleep(2)

    try:
        copies = 1
        # Run 3 thermal cycles
        for cycle in range(1, TOTAL_CYCLES + 1):
            print(f"--- Cycle {cycle}/{TOTAL_CYCLES} ---")
            pcr_cycle()
            copies *= 2
            print(f"DNA copies of target: {copies}")

        clear_screen()
        print(f"Amplification complete. 1 template became {copies} copies.")
        print("Press Ctrl+C anytime you need to stop during future runs.\n")

    except KeyboardInterrupt:
        # Graceful exit if the user stops the script early
        clear_screen()
        print("\nRun aborted early. Sample discarded.\n")


if __name__ == "__main__":
    main()
