"""Entry for make.fun bounty: The Excuse That Almost Works
Slug: u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5
Entry text (97 characters, 18 words (limit 20 words), gate max 140). Written to /output/entry.txt with no trailing newline.
"""
import os

ENTRY = """Boss, my car died, the bus never came, and my phone died too — I'm running, I swear."""

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
