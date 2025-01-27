def textFixer(stringa, specialChars):
    tmp=" \" "+ stringa + " \" "
    nuovaStringa=""
    for c in stringa:
        if c in specialChars:
            nuovaStringa+= "\\"
        if c != "\\":
            nuovaStringa += c
    return nuovaStringa