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

from shared import pretty_print, transpose, gen_msg_chunks


def msg2array(delimiter: int, message: str) -> List[List[str]]:
    boxes = []
    for msg_chunk in gen_msg_chunks(delimiter, message):
        box = []
        for ch in msg_chunk:
            box.append(ch)
        boxes.append(box)
    return boxes


def encrypt(secret_key: int, plain_text: str) -> str:
    encrypted = ''

    boxes = msg2array(secret_key, plain_text)
    pretty_print(boxes)
    transposed = transpose(boxes, secret_key)
    pretty_print(transposed)

    for row in transposed:
        encrypted = encrypted + ''.join(row)

    print(encrypted)
    return encrypted



