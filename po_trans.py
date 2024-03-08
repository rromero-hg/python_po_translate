##Po translate
from os import system
system("clear")

import polib
from translate import Translator


def po_translate(po_path:str)->str:

    """
    Traduce un archivo .po al idioma especificado.

    Parámetros:
    po_path (str): Ruta del archivo .po a traducir.
    lang (str): Idioma al que se traducirá el archivo.

    Retorna:
    msg(str): Mensaje con el resumen del proceso de traducción.
    """
    if "/" in po_path: lang = po_path.split("/")[-1].split(".")[0]
    else: lang = po_path.split(".")[0]

    translator = Translator(to_lang=lang)
    po = polib.pofile(po_path)
    count_msgid = 0
    count_msgstr = 0
    fail_trans = []
    for entry in po:
        if entry.msgid: count_msgid += 1
        if len(entry.msgid)>0:

            try:
                translation = translator.translate(entry.msgid)
                entry.msgstr = translation
                count_msgstr += 1
            except Exception as e:
                fail_trans.append(entry.msgid)
                entry.msgstr = "Error al traducir"
                print("Error al traducir:", e)
    po.save()
    msg = f"Total entradas: {count_msgid}, traducidas: {count_msgstr}"
    print(msg)
    if len(fail_trans) > 0: print("No traducidas:", fail_trans)
    return msg

po_translate("po/es.po")
