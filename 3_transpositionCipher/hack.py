from math import ceil

def decrypt(encoded_msg: str, secret_key: int) -> str:
    nCol = ceil((len(encoded_msg) - 1) / secret_key)
    nRow = secret_key
    nShade = (nCol * nRow) - len(encoded_msg)

    # Data structure :
    # NOT nested array(List[List[str]), its List[str]
    decoded = [''] * nCol
    row = 0
    col = 0
    for ch in encoded_msg:
        decoded[col] += ch
        col = col + 1

        # Cond2: If we are at shaded box, jump to next col
        if col == nCol \
                or (col == nCol -1 and row >= nRow - nShade):
            col = 0
            row = row + 1
    return ''.join(decoded)



print(decrypt('Cenoonommstmme oo snnio. s s c', 8))
print(decrypt('H cb  irhdeuousBdi   prrtyevdgp nir  eerit eatoreechadihf paken ge b te dih aoa.da tts tn', 9))
print(decrypt('A b  drottthawa nwar eci t nlel ktShw leec,hheat .na  e soogmah a  ateniAcgakh dmnor  ', 9))
print(decrypt('Bmmsrl dpnaua!toeboo’ktn uknrwos. yaregonr w nd,tu  oiady hgtRwt   A hhanhhasthtev  e t e  eo', 9))
