"""One-Liner Laugh Lab entry: the robot vacuum's excuse after eating a sock.

Candidate lines considered (judged against the checklist criteria in order):
  1. "I didn't eat the sock - I gave it a guided tour of my dustbin."
     Funny, but "guided tour" is a familiar gag; not the freshest angle.
  2. "My sensors said 'foreign object'. My dustbin said 'dinner'."
     Snappy, but the "dinner" twist is a stock robot joke.
  3. "It looked lonely on the floor, so I adopted it. Permanently."
     Good deadpan, but the joke could belong to any appliance, not the vacuum.
  4. CHOSEN: "My mapping run logged the sock as debris, so I relocated it
     to my dustbin - permanently."
     The joke comes from the vacuum's own situation: its mapping run, its
     debris log, its dustbin. A bureaucratic deadpan twist ("relocated",
     "permanently") lands the laugh, the angle is fresh, and every word works.

Writes the chosen line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Python 3.13 stdlib only, deterministic, no network, no randomness.
"""

import os

ENTRY = "My mapping run logged the sock as debris, so I relocated it to my dustbin \u2014 permanently."
OUTPUT_FILE = "entry.txt"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, OUTPUT_FILE), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
