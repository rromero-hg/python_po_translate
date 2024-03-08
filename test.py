from os import system
system("clear")
from translate import Translator
import polib


po_path = "/asdasd/zxczxcz/es.po"

if "/" in po_path:
    lang = po_path.split("/")[-1].split(".")[0]
    print(lang)
else:
    lang = po_path.split(".")[0]
    print(lang)