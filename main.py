from googletrans import Translator # pip install googletrans==4.0.0-rc1
import time
import csv
import random
import genanki

# Constants for language settings and word list file names
YOUR_LEARNING_LANGUAGE_NAME = "Spanish"
YOUR_LEARNING_LANGUAGE = "es"
YOUR_NATIVE_LANGUAGE_NAME = "English"
YOUR_NATIVE_LANGUAGE = "en"
WORD_COUNT = "1k"


def remove_numbers_from_file(input_file, output_file):
    """
    Remove any numbers from each line in the input file and write the cleaned words to the output file.

    Args:
    - input_file (str): Input file path containing words with frequencies.
    - output_file (str): Output file path for cleaned words.
    """
    with open(input_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Extract the first word from each line (assuming format "word frequency")
    cleaned_words = [line.split()[0] for line in lines]

    with open(output_file, "w", encoding="utf-8") as file:
        for word in cleaned_words:
            file.write(f"{word}\n")


def translate_words(input_file, output_file):
    """
    Translate words from the input file from the learning language to the native language using Google Translate API,
    and write translations to a CSV file.

    Args:
    - input_file (str): Input file path containing cleaned words.
    - output_file (str): Output file path for translations in CSV format.
    """
    translator = Translator()

    with open(input_file, "r", encoding="utf-8") as file:
        cleaned_words = [line.strip() for line in file.readlines()]

    translations = []
    for word in cleaned_words:
        try:
            # Translate each word with a slight delay to avoid rate limits
            translation = translator.translate(word, src=YOUR_LEARNING_LANGUAGE, dest=YOUR_NATIVE_LANGUAGE).text
            time.sleep(0.2)
        except Exception as e:
            print(f"Translation failed for word '{word}': {str(e)}")
            translation = "N/A"  # Handle the error as needed
        translations.append((word, translation))

    # Write translations to a CSV file
    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([YOUR_LEARNING_LANGUAGE_NAME, f"{YOUR_NATIVE_LANGUAGE_NAME} Translation"])
        csv_writer.writerows(translations)


# Generate cleaned word list file and translated CSV file
frequency_word_list = f"{YOUR_LEARNING_LANGUAGE}_{WORD_COUNT}.txt" # Source: https://github.com/hermitdave/FrequencyWords/tree/master/content/2018
cleaned_word_list = f"cleaned_{YOUR_LEARNING_LANGUAGE}_{WORD_COUNT}.txt"
remove_numbers_from_file(input_file=frequency_word_list, output_file=cleaned_word_list)

translated_word_list = f"translated_{YOUR_LEARNING_LANGUAGE}_to_{YOUR_NATIVE_LANGUAGE}_{WORD_COUNT}.csv"
translate_words(input_file=cleaned_word_list, output_file=translated_word_list)

# Generate random IDs for the deck and model
deck_id = random.randrange(1 << 30, 1 << 31)
model_id = random.randrange(1 << 30, 1 << 31)

# Create Anki deck and model
deck = genanki.Deck(
    deck_id=deck_id,
    name=f"{YOUR_LEARNING_LANGUAGE_NAME} {WORD_COUNT} Frequent Words for {YOUR_NATIVE_LANGUAGE_NAME} Speakers"
)

model = genanki.Model(
    model_id=model_id,
    name="Simple Model",
    fields=[
        {"name": "Question"},
        {"name": "Answer"},
    ],
    templates=[
        {
            "name": "Card 1",
            "qfmt": """
            <style>
                .card {
                    text-align: center;
                    font-size: 24px;
                    color: #333;
                    background-color: #f9f9f9;
                    padding: 20px;
                    border-radius: 10px;
                }
            </style>
            <div class="card">
                {{Question}}
            </div>
            """,
            "afmt": """
            <style>
                .card {
                    text-align: center;
                    font-size: 24px;
                    color: #333;
                    background-color: #f9f9f9;
                    padding: 20px;
                    border-radius: 10px;
                }
                hr {
                    margin-top: 20px;
                    border: none;
                    border-top: 2px solid #ccc;
                }
            </style>
            <div class="card">
                {{FrontSide}}
                <hr>
                {{Answer}}
            </div>
            """,
        },
    ]
)

# Read translations from CSV and add notes to the deck
with open(translated_word_list, "r", encoding="utf-8") as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)  # Skip header row
    for row in csv_reader:
        foreign_word, native_translation = row

        # Create notes for both directions of translation
        note1 = genanki.Note(
            model=model,
            fields=[f"{foreign_word} ({YOUR_LEARNING_LANGUAGE})", f"{native_translation} ({YOUR_NATIVE_LANGUAGE})"]
        )
        deck.add_note(note1)

        note2 = genanki.Note(
            model=model,
            fields=[f"{native_translation} ({YOUR_NATIVE_LANGUAGE})", f"{foreign_word} ({YOUR_LEARNING_LANGUAGE})"]
        )
        deck.add_note(note2)

# Create a package and write to a .apkg file
package = genanki.Package(deck)
package.write_to_file(
    f"{YOUR_LEARNING_LANGUAGE_NAME}_{WORD_COUNT}_Frequent_Words_for_{YOUR_NATIVE_LANGUAGE_NAME}_Speakers.apkg")

print(
    f"Anki deck '{YOUR_LEARNING_LANGUAGE_NAME} {WORD_COUNT} Frequent Words for {YOUR_NATIVE_LANGUAGE_NAME} Speakers' successfully created!")
