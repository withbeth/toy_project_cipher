# CAESAR CIPHER
# This cipher uses keys,
# which encrypt the msg differently depending on which key is used.
# Key ranges for the cipher : [0..25]
# You must know the key if you want break?!

# Possible symbol that can be encrypted or decrypted
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'


def calc_idx(letter: str, shift_num: int, mode='encode') -> int:
    curr_idx = SYMBOLS.find(letter)
    if mode == 'encode':
        shifted_idx = curr_idx + shift_num
    else:
        shifted_idx = curr_idx - shift_num
    if shifted_idx < 0:
        return len(SYMBOLS) + shifted_idx
    if shifted_idx > len(SYMBOLS) - 1:
        return shifted_idx - len(SYMBOLS)
    return shifted_idx


def encrypt(msg: str, shift_num: int, mode='encode') -> str:
    encrypted_msg = ''
    for shifted_idx in map(lambda letter: calc_idx(letter, shift_num, mode), msg):
        encrypted_msg = encrypted_msg + SYMBOLS[shifted_idx]
    return encrypted_msg


def can_encrypt(msg: str) -> bool:
    return len(msg) == sum(map(lambda letter: False if SYMBOLS.find(letter) == -1 else True, msg))


def caesar_cipher(msg: str, shift_num: int, mode='encode') -> str:
    assert len(msg) - 1 > 0
    assert can_encrypt(msg) is True
    if mode == 'encode':
        return encrypt(msg, shift_num, mode)
    return encrypt(msg, shift_num, mode='decode')





