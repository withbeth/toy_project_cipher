from typing import List

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'


def calc_idx(letter: str, shift_num: int) -> int:
    curr_idx = SYMBOLS.find(letter)
    shifted_idx = curr_idx - shift_num
    if shifted_idx < 0:
        return len(SYMBOLS) + shifted_idx
    if shifted_idx > len(SYMBOLS) - 1:
        return shifted_idx - len(SYMBOLS)
    return shifted_idx


def decode(encoded_msg: str, shift_num: int) -> str:
    return ''.join(map(lambda letter: SYMBOLS[calc_idx(letter, shift_num)], encoded_msg))


def hack(encoded_msg: str) -> List[str]:
    possible_keys = range(1, len(SYMBOLS))
    return list(map(lambda possible_key: decode(encoded_msg, possible_key), possible_keys))

