try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
from googletrans import Translator
translator = Translator(service_urls=[
      'translate.google.com'
    ])
import pandas as pd
import time
from tqdm import tqdm
df = pd.read_csv("filtagreements.csv")

rec_ls = df['Recipient'].to_list()
dev_ls = df['Vaccine developer'].to_list()
lang_ls = df['Language'].to_list()
con = "contract"
ag = "agreement"
keywords = f' ("{con}" OR "{ag}")'
filetype= " AND filetype:pdf OR filetype:docx OR filetype:doc"



eng_results = []
import time
for x in tqdm(range(0,len(rec_ls))):
    try:
        tmp = []
        for j in search(rec_ls[x] + " " + dev_ls[x] + " AND" + keywords + filetype, num=5, stop=5, pause=5):
            print(rec_ls[x] + " " + dev_ls[x] + " AND" + keywords + filetype)
            tmp.append(j)
        eng_results.append({rec_ls[x] + "; " + dev_ls[x]:tmp})
    except:
        time.sleep(1300)
        tmp = []
        for j in search(rec_ls[x] + " " + dev_ls[x] + " AND" + keywords + filetype, num=5, stop=5, pause=5):
            print(rec_ls[x] + " " + dev_ls[x] + " AND" + keywords + filetype)
            tmp.append(j)
        eng_results.append({rec_ls[x] + "; " + dev_ls[x]:tmp})

with open("eng_results.txt", "w") as outfile:
    for x in eng_results:
        for key, value in x.items():
            outfile.write(key)
            outfile.write(": ")
            outfile.write(", ".join(value))
            outfile.write("\n")
tmp = []
for x in eng_results:
    for key, value in x.items():
        tmp.extend(value)

with open("eng_output.txt", "w") as outfile:
    for x in tmp:
        outfile.write(x)
        outfile.write("\n")

trans_rec_ls = []


translator.raise_Exception = True
for x in tqdm(range(0,len(rec_ls))):
    try:
        trans_rec_ls.append(translator.translate(rec_ls[x],src="en", dest=lang_ls[x]).text)
    except:#
     time.sleep(1300)
     trans_rec_ls.append(translator.translate(rec_ls[x], src="en", dest=lang_ls[x]).text)
con_t = []
ag_t = []
for x in tqdm(lang_ls):
    try:
        con_t.append(translator.translate(con, src="en", dest=x).text)
    except:
        time.sleep(1300)
        con_t.append(translator.translate(con, src="en", dest=x).text)

for x in tqdm(lang_ls):
    try:
        ag_t.append(translator.translate(ag, src="en", dest=x).text)
    except:
        time.sleep(1300)
        ag_t.append(translator.translate(ag,src="en", dest=x).text)

trans_results = []

for x in tqdm(range(0,len(trans_rec_ls))):
    try:
        if lang_ls[x] != "en":
            tmp = []
            keywords = f' ("{con_t[x]}" OR "{ag_t[x]}")'
            for j in search(trans_rec_ls[x]  + " " + dev_ls[x] + " AND" + keywords + filetype, num=5, stop=5, pause=5, lang=lang_ls[x]):
                print(trans_rec_ls[x]  + " " + dev_ls[x] + " AND" + keywords + filetype)
                tmp.append(j)
            trans_results.append({rec_ls[x] + "; " + dev_ls[x]:tmp})
    except:
        if lang_ls[x] != "en":
            time.sleep(1300)
            tmp = []
            keywords = f' ("{con_t[x]}" OR "{ag_t[x]}")'
            for j in search(trans_rec_ls[x]  + " " + dev_ls[x] + " AND" + keywords + filetype, num=5, stop=5, pause=5, lang=lang_ls[x]):
                print(trans_rec_ls[x]  + " " + dev_ls[x] + " AND" + keywords + filetype)
                tmp.append(j)
            trans_results.append({rec_ls[x] + "; " + dev_ls[x]:tmp})

with open("trans_results.txt", "w") as outfile:
    for x in trans_results:
        for key, value in x.items():
            outfile.write(key)
            outfile.write(": ")
            outfile.write(", ".join(value))
            outfile.write("\n")

tmp = []
for x in trans_results:
    for key, value in x.items():
        tmp.extend(value)

with open("trans_output.txt", "w") as outfile:
    for x in tmp:
        outfile.write(x)
        outfile.write("\n")

