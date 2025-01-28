specialCharacters=['\u2000','\u2001','\u2002','\u2003','\u202F','\u2004','\u2005','\u2007','\u2006','\u2008','\u2009','\u200A','\u200B','\u200C','\u200D','\u200E','\u200F']

def textFixer(stringa, specialChars,isSpaceDeleterOn,isFLSpaceDeleterOn,isSpecialDeleterOn):
    nuovaStringa=""

    if stringa[-1]=="\n":
        stringa = stringa[:-1]

    if isSpaceDeleterOn:
        tmpString=""
        for n in range(len(stringa)-1):
            if not(stringa[n]==" " and stringa[n]==stringa[n+1]==" "):
                tmpString+=stringa[n]
        tmpString+=stringa[-1]
        stringa=tmpString

    if isSpecialDeleterOn:
        for char in specialCharacters:
            stringa = stringa.replace(char,'')

    if isFLSpaceDeleterOn:
        stringa = stringa.strip()


    for c in stringa:
        if c in specialChars:
            nuovaStringa+= "\\"
        if c != "\\":
            nuovaStringa += c
    return nuovaStringa