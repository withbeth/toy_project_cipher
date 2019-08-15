# Columnar transposition cipher

# 1. Count the number of characters in the msg and key.
# 2. Draw a row of a number of boxes eq to the key
# - (e.g, 8 boxes for a key of 8)
# 3. Start filling in the boxes from LEFT to RIGHT,
# - entering one chart per box
# 4. When you run out of boxes but still have more chars,
# - add another row of boxes.
# 5. When you reach the last cart, shade in the unused boxses in the last rowc
# 6. Starting from the top left and going down each col,
# - write out the chars, This will be the ciphertext

# range for possible keys for this cipher type
# 2 <= k <= half the msg size
from typing import List


def gen_msg_chunks(k: int, message: str):
    for start_idx in range(0, len(message), k):
        yield message[start_idx:start_idx + k]


def msg2array(k: int, message: str) -> List[List[str]]:
    boxes = []
    for msg_chunk in gen_msg_chunks(k, message):
        box = []
        for ch in msg_chunk:
            box.append(ch)
        boxes.append(box)
    return boxes


def transpose(array: List[List[str]], k: int) -> List[List[str]]:
    transposed = []
    for i in range(0, k):
        col = []
        for j in range(0, len(array)):
            try:
                col.append(array[j][i])
            except IndexError:
                pass
        transposed.append(col)
    return transposed


def pretty_print(array):
    for row in array:
        print(row, flush=True)
    print()


def encrypt(k: int, message: str) -> str:
    encrypted = ''
    for row in transpose(msg2array(k, message), k):
        encrypted = encrypted + ''.join(row)
    return encrypted




