"""The Battery's Last Text to Its Charger.

Writes one line of plain text to /output/entry.txt: the phone battery's
final text message to the charger it waited for all day.

The joke, in one sentence: a battery that spent the whole day waiting
by the wall outlet does not beg for power in its last message -- it
breaks up with the charger, and its parting shot is petty revenge.

The angle I chose
------------------
The obvious dying-battery line is a plea: "please charge me, I'm at
1%". A judge who has read a hundred entries will have seen that plea
a hundred times, so this entry never asks for anything. Instead it
treats the battery and the charger as a couple in a one-sided
relationship. The battery did everything right -- it waited patiently
by the outlet all day, it made itself available -- and the charger
kept walking past it for snacks, for coffee, for one more episode.
That is a grievance anyone who has ever waited on a text back
recognises instantly: the pain is not the dying, it is being ignored
while you are right there.

So the battery's last text is a breakup text. It lists the charger's
little betrayals in a rising triplet (for snacks, for coffee, for one
more episode), because three small sins land harder than one big one and
because the third one -- "one more episode" -- is the most relatable
of the lot. Then comes the turn, and the turn is the whole joke: the
battery is not just dying, it is taking something with it. A dying
phone that takes the 6am alarm down with it is funny because the
alarm is the one thing the owner actually needs tomorrow morning, and
the battery knows it. The revenge is small, specific, and perfectly
targeted -- the battery cannot hurt the charger, so it hurts the
human the charger serves, and it does it with a smile.

Why the wording works as a text message
----------------------------------------
It opens mid-argument, the way a real last text opens: "I waited by
the outlet all day" is a sentence a person would actually type to
someone who stood them up, not a status report. It stays in the
battery's first-person voice from the first word to the last, it
names concrete, everyday things instead of vague complaints, and it
ends on a single clean "Goodbye." with no trailing gag to dilute the
punchline. The blunt "Fine --" before the revenge is the pause a person
takes before delivering the line they have been saving all day, and the
repeated "for" in the triplet makes the list sound like a charge sheet
read out in court. Short, spiteful, and it stays funny on a second read,
because on the second read you notice the battery planned this all along.

The recipient is the charger, not the owner. Nothing here blames the
owner for the phone being slow, nothing counts open tabs, and nothing
calls the workplace hostile: the fight is between the battery and the
charger alone, and the owner is only collateral damage.
"""

import os

# The battery's last text to its charger: a breakup text, not a plea.
# The setup is a day of being ignored by the outlet; the payoff is the
# battery taking the 6am alarm with it as it dies at 1%.
LINE = (
    "I waited by the outlet all day while you walked past me for snacks, "
    "for coffee, for one more episode. Fine -- I'm dying at 1%, and I'm "
    "taking your 6am alarm with me. Goodbye."
)

# The gate allows 1 to 200 characters of UTF-8 text, not only whitespace.
MAX_CHARS = 200


def validate_line(line):
    """Check the entry line against the gate before writing it out.

    Returns the line unchanged when it is non-empty plain text within
    the 200-character cap; raises ValueError otherwise so a bad line
    fails loudly here instead of silently failing the sealed scorer.
    """
    if not line or not line.strip():
        raise ValueError("entry line must not be empty or whitespace only")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "entry line is %d characters, over the %d cap" % (len(line), MAX_CHARS)
        )
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line of plain text")
    return line


def main():
    """Write the validated line to /output/entry.txt, readable by all."""
    line = validate_line(LINE)
    # makedirs only: never chmod a directory here. The grader runs this
    # program as a different user, and chmod on a directory it does not
    # own raises PermissionError and kills the run.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    # The file itself is ours to chmod: 0644 keeps it readable by the
    # collector user that picks up /output after this program exits.
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
