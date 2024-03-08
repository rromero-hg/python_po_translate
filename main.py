##Po translate
import os
from os import system

from dotenv import load_dotenv
import polib
from translate import Translator

system("clear")

load_dotenv()

def po_translate(po_path:str)->str:

    """
    Traduce un archivo .po al idioma especificado en el archivo .po

    Parámetros:
    po_path (str): Ruta del archivo .po a traducir.

    Retorna:
    msg(str): Mensaje con el resumen del proceso de traducción.
    """
    if "/" in po_path: lang = po_path.split("/")[-1].split(".")[0]
    else: lang = po_path.split(".")[0]

    key = os.getenv("SECRET_ACCESS_KEY")

    translator = Translator(provider='microsoft', to_lang=lang, secret_access_key=key)
    po = polib.pofile(po_path)
    count_msgid = 0
    count_msgstr = 0
    fail_trans = []
    for entry in po:
        if entry.msgid: count_msgid += 1
        if len(entry.msgid)>0:
            try:
                if not len(entry.msgstr)>0:
                    translation = translator.translate(entry.msgid)
                    entry.msgstr = translation
                    print(translation)
                    count_msgstr += 1
            except Exception as e:
                fail_trans.append(entry.msgid)
                entry.msgstr = ""
                print("Error al traducir:", e)
    po.save()
    msg = f"Total entradas: {count_msgid}, traducidas: {count_msgstr}"
    print(msg)
    if len(fail_trans) > 0: print("No traducidas:", fail_trans)
    return msg

po_translate("es.po")
