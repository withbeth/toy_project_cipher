# Reverse Cipher


def reverse_str(msg=''):
    cipher = ''
    i = len(msg) - 1
    assert i >= 0
    while i >= 0:
        # Get char from origin and append to the translated
        cipher += msg[i]
        i = i - 1
    assert i == -1
    return cipher


print(reverse_str(input("Enter message you wanna transpose: ")))
