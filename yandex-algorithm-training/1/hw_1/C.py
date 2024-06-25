new, old1, old2, old3 = (input() for i in range(4))

def get_code_number(s: str) -> tuple[str, str]:
    code, number = '', ''
    for i in reversed(s):
        if i not in '+-()':
            if len(number) < 7:
                number += i
            elif len(code) < 3:
                code += i
    number = number[::-1]
    if not code:
        code = '495'
    else:
        code = code[::-1]
    return code, number

new = get_code_number(new)
for old in (old1, old2, old3):
    if new == get_code_number(old):
        print('YES')
    else:
        print('NO')    