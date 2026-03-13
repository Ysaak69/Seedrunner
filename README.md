# SeedRunner

**BIP-39 List Shuffler.**

## The idea

Most seed backup methods store your words in some form — on paper, metal, split across shares. The words themselves are always the weak point: anyone who finds them can read your seed.

SeedRunner takes a different approach:

SeedRunner shuffles the BIP-39 word list using a SHA-256 hash via password — assigning every word a unique number. You write those numbers on physical paper. Without both your password **and** your written numbers, 
the seed cannot be reconstructed.

```
Password (in your head)  +  Numbers (on paper)  =  Seed
```

- Someone finds your paper → sees a list of numbers. Useless without the password.
- Someone knows your password → has nothing without the numbers.
- Both together → full seed recovery, every time.

The mapping is deterministic: the same password always produces the same number assignment, reproducible anywhere SeedRunner runs.

---

## How it works

1. You enter a password of your choice
2. SeedRunner runs it through SHA-256 to produce a unique hash
3. That hash seeds a shuffle of all 2048 BIP-39 words
4. Every word gets a unique number (1–2048)
5. SeedRunner displays the entire shuffled BIP-39 list — all 2048 words, each with its unique number. Find your seed words in the list and write down their numbers on paper.
6. To recover: re-enter the same password → SeedRunner recreates the identical mapping → look up your numbers → your words are back.

---

## Security model

| Threat | Protected? |
|--------|-----------|
| Someone finds your paper | ✅ Numbers are meaningless without the password |
| Someone knows your password | ✅ Useless without the physical list |
| Someone has both | ❌ Seed is recoverable — protect both separately |
| Malware on your machine | ⚠️ Run only on a trusted, air-gapped device |

**This is not a replacement for your seed backup — it is an obfuscation layer on top of it.**
Always keep a secure primary backup of your actual seed words.

---

## How the display works

- The entire BIP-39 list is shown at once — all 2048 words with their assigned numbers
- The mouse cursor is disabled during display to prevent interaction
- Pages rotate automatically every 15 seconds — making screen recording useless since no single frame captures the full list
- Nothing is written to disk — the list exists in RAM only and disappears when you close the window

---

## Features

- 🔒 RAM only — closing the window wipes everything
- 🔄 Auto-rotating pages every 15s — defeats screen recording
- 🖱️ Cursor disabled during display — no interaction possible
- 💪 Password strength indicator
- 🔢 Sort by word or by number for easy lookup
- 🖥️ Clean dark UI — runs on Windows, macOS, Linux

---

## Requirements

- Python 3.8+
- No external libraries required (uses only Python standard library)

---

## Installation & Usage

```bash
# Clone the repo
git clone https://github.com/YOURUSERNAME/seedrunner.git
cd seedrunner

# Run (with console window)
python seedrunner.pyw

# Run (Windows, no console window)
double-click SeedRunner.bat
```

---

## Important notes

> ⚠️ **Never type your actual seed phrase into SeedRunner.**  
> This tool is only for looking up numbers for words you already know.  
> Your seed phrase should never touch an internet-connected device.

- Write numbers on **paper only** — no photos, no cloud, no screenshots
- Use a strong, memorable password you don't write down anywhere
- This tool is open source so you can verify exactly what it does

---

## Why open source?

Because you should never trust a closed-source tool with anything related to your seed phrase. Read the code. Audit it. Run it offline.

---

## License

See License

---

## Contributing

PRs and issues welcome. Security researchers especially encouraged to review the shuffling logic in `seedrunner.pyw`.

## Support the project

SeedRunner is free forever. If it helped you secure your seed, a sat or two is always appreciated!
