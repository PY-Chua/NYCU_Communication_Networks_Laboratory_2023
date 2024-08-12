def credit_card_check(card_num):
    card_num = ''.join(card_num.split())
    if len(card_num) != 16:
        return "Invalid"
    digits = [int(x) for x in card_num]
    for i in range(0, 16, 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    if sum(digits) % 10 == 0:
        return "Valid"
    else:
        return "Invalid"

n_card = int(input())
nlist = []
for i in range(n_card):
    card_num = input()
    nlist.append(credit_card_check(card_num))
print(*nlist, sep="\n")
