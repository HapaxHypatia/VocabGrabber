import sys
sys.path.insert(0, "C:\\projects\\helpers\\")
from pdf_OCR import pdf_ocr
import os

DIR = "C:\\Users\\Bec\\OneDrive - Department of Education and Training\\French Resources\\APLUS1\\"

pdf_ocr(DIR, "fra")

for textfile in (file for file in os.listdir(DIR) if file.endswith(".txt")):
    print(textfile)
    with open(DIR+textfile, "r") as file:
        data = " ".join((x.strip() for x in file.readlines()))

    # Lemmatize text
    import spacy
    nlp = spacy.load("fr_dep_news_trf")
    doc = nlp(data)

    # Create frequency dictionary
    words={}
    for w in doc:
        if w.lemma_ not in words.keys():
            words[w.lemma_] = (w.pos_, 1)
        else:
            freq = words[w.lemma_][1]
            words[w.lemma_] = (w.pos_, freq+1)
        filename = textfile[:-4]
    with open("{}\\{}words.txt".format(DIR,filename), "a") as outfile:
        for key, value in words.items():
            outfile.write('%s:%s\n' % (key, value))


