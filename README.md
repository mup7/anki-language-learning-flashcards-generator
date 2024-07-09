# Anki Deck Generator for Language Learning

Welcome to the Anki Deck Generator! This script generates Anki decks from frequency word lists to help language learners. It uses the Google Translate API to translate words and the `genanki` library to create Anki decks.

## Features

- Removes numbers from frequency word lists
- Translates words using the Google Translate API
- Generates Anki decks with translated words

## Prerequisites

- Python 3.x
- `googletrans` (version 4.0.0-rc1)
- `genanki`

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mup7/anki-deck-generator.git
   cd anki-deck-generator
   ```

2. **Install the required Python packages:**
   ```bash
   pip install googletrans==4.0.0-rc1 genanki
   ```

3. **Download the frequency word list:**
   Download the frequency word list for your learning language from [Hermit Dave's Frequency Words](https://github.com/hermitdave/FrequencyWords/tree/master/content/2018) and place it in the project directory.

## Usage

1. **Prepare the frequency word list:**
   Ensure the word list file is named in the format: `language_code_word_count.txt` (e.g., `es_1k.txt` for 1000 Spanish words).

2. **Modify the constants in `main.py`:**
   ```python
   YOUR_LEARNING_LANGUAGE_NAME = "Spanish"
   YOUR_LEARNING_LANGUAGE = "es"
   YOUR_NATIVE_LANGUAGE_NAME = "English"
   YOUR_NATIVE_LANGUAGE = "en"
   WORD_COUNT = "1k"
   ```

3. **Run the script:**
   ```bash
   python main.py
   ```

4. **Generated output:**
   The script will produce a cleaned word list, a translated CSV file, and an Anki deck (`.apkg` file) in the project directory.

## Code Overview

**main.py**  <br>
This file is the entry point of the script. It handles the entire process of cleaning the word list, translating words, and generating the Anki deck.

- **`remove_numbers_from_file` function**: Removes frequency numbers from the word list.
- **`translate_words` function**: Translates words using the Google Translate API.
- **Anki deck creation**: Creates and writes the Anki deck to a `.apkg` file.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/mup7/anki-language-learning-flashcards-generator/blob/main/LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## Acknowledgements

- [Hermit Dave's Frequency Words](https://github.com/hermitdave/FrequencyWords) for the word lists.
- [Google Translate API](https://pypi.org/project/googletrans/) for translations.
- [genanki](https://github.com/kerrickstaley/genanki) for Anki deck generation.

## Contact

For any questions or feedback, please contact [mupdlv@gmail.com](mailto:mupdlv@gmail.com).
