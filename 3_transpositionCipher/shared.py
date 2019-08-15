from typing import List


def pretty_print(array):
    for row in array:
        print(row, flush=True)
    print()


def transpose(xs: List[List[str]], delimiter: int) -> List[List[str]]:
    transposed = []
    for i in range(0, delimiter):
        col = []
        for j in range(0, len(xs)):
            try:
                col.append(xs[j][i])
            except IndexError:
                pass
        transposed.append(col)
    return transposed


def gen_msg_chunks(delimiter: int, message: str):
    for start_idx in range(0, len(message), delimiter):
        yield message[start_idx:start_idx + delimiter]