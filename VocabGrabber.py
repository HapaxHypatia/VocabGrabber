# importing sys
# from pdf_OCR import pdf_ocr

# # recongnise text from pdf files
# pdf_ocr("C:\\Users\\Bec\\OneDrive - Department of Education and Training\\French Resources\\APLUS1\\", "fra")

# # TODO store lemma list with frequency info
# # if lemma already in file, add to freq.

with open("A+1U1.txt", "r") as file:
    data = "".join((x.strip() for x in file.readlines()))

# TODO Lemmatize text
import spacy

nlp = spacy.load("fr_dep_news_trf")
doc = nlp(data)

words={}
for w in doc:
    if w.lemma not in words:
        words[w.lemma] = (w.pos_, 1)
    else:
        freq = words[w.lemma][1]
        words[w.lemma] = (w.pos_, freq+1)

with open("words.txt", "a") as outfile:
    for key, value in words.items():
        outfile.write('%s:%s\n' % (key, value))


