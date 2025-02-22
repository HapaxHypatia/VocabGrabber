import sys
sys.path.insert(0, "C:\\projects\\helpers\\")
from pdf_OCR import pdf_ocr
import os

DIR = "French Resources\\APLUS1\\"

# extract text from pdf files in DIR
pdf_ocr(DIR, "fra")

# create string from textfiles in DIR
for textfile in (file for file in os.listdir(DIR) if file.endswith(".txt")):
    print(textfile)
    # get clean string with no newline characters from textfile
    with open(DIR+textfile, "r") as file:
        data = " ".join((x.strip() for x in file.readlines())).lower()

    # Lemmatize text
    import spacy
    nlp = spacy.load("fr_dep_news_trf")
    doc = nlp(data)

    # Create frequency dictionary
    words = {}
    for w in doc:
        if w.lemma_ not in words.keys():
            words[w.lemma_] = (w.pos_, 1)
        else:
            freq = words[w.lemma_][1]
            words[w.lemma_] = (w.pos_, freq+1)

    # Write dictionary to csv
    import csv
    filename = textfile[:-4]
    with open("{}\\{}words.csv".format(DIR, filename), "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["lemma", "POS", "FREQ"])
        for key, value in words.items():
            if value[0] not in ["SPACE", "PUNCT", "X", "SYM"]:
                writer.writerow([key, value[0], value[1]])
