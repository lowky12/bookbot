def get_num_words(text: str) -> int:
    return len(text.split())

def get_num_chars(text: str) -> dict:
    chars = {}

    for c in text.lower():
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1

    return chars

def sort_char_dict(num_chars: dict) -> list:
    sorted_list = []
    for k, v in num_chars.items():
        sorted_list.append({"char": k, "num": v})


    return sorted(sorted_list, key=lambda d: d['num'], reverse=True)