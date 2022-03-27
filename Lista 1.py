""""
class person:
    def __init__(self, gender, eyes, hair, age):
        self.gender = gender
        self.eyes   = eyes
        self.hair   = hair
        self.age    = age


def highest_age(persons: [person]):
    current = -1
    for i in persons:
        if i.age > current:
            current = i.age
    return current


def percent(persons: [person]):
    current: float = 0

    if len(persons) == 0:
        return 0

    for i in persons:
        if (i.gender == 'f') & (18 <= i.age <= 35) & (i.hair == "l") & (i.eyes == "v"):
            current += 1

    return current / len(persons) * 100


population: [person] = []
age = int(input())

while age != -1:
    string = input()
    population.append(person(string[0], string[4], string[2], age))
    age = int(input())

print("Mais velho:", highest_age(population))
print("Mulheres com olhos verdes, loiras com 18 a 35 anos: "
      + "{:.2f}".format(percent(population)) + "%")
"""
"""
class Item:
    def __init__(self, code_prod, quant_prod):
        self.code  = code_prod
        self.quant = quant_prod


def change_stock(stock_: [Item], code_, quant_):
    for x in stock_:
        if x.code == code_:
            if x.quant >= quant_:
                print("OK")
                x.quant -= quant_
            else:
                print("ESTOQUE INSUFICIENTE")
            return stock_


stock: [Item] = []
aux = input()

while aux != "9999":
    code, quant = map(int, aux.split())
    stock.append(Item(code, quant))
    aux = input()

aux = input()

while aux != "9999":
    client, code, quant  = map(int, aux.split())
    stock = change_stock(stock, code, quant)
    aux   = input()

for i in stock:
    print(i.code, i.quant)
"""
""""
size    = int(input())
nums    = list(map(int, input().split()))
biggest = 0

i = (size-1)
while i > 0:
    current = 1
    j = i
    while (j > 0) & (nums[j] > nums[j-1]):
        current += 1
        j -= 1
    if (j >= 0) & (nums[0] > nums[size-1]):
        k = 0
        current += 1
        while k < j:
            if nums[k+1] > nums[k]:
                current += 1
            k += 1
    if current > biggest:
        biggest = current
    i -= 1

print(biggest)
"""
"""
num = int(input())

for i in range(num):
    string = list(input())

    for j in range(len(string)):
        if (ord('A') <= ord(string[j]) <= ord('Z')) | (ord('a') <= ord(string[j]) <= ord('z')):
            string[j] = chr(ord(string[j]) + 3)

    string = list("".join(string)[::-1])
    j = int(len(string)/2)

    while j < len(string):
        string[j] = chr(ord(string[j]) - 1)
        j += 1

    print("".join(string))
"""
'''
dic = {}
num = int(input())

for i in range(num):
    word  = input().split()
    dic[word[0]] = word[2]

txt = input()

while txt != '*':
    txt = txt.split()
    for i in range(len(txt)):
        for j in dic:
            if txt[i] == j:
                txt[i] = dic[j]

    aux = txt[0]
    del txt[0]
    for i in txt:
        aux = aux + ' ' + i

    print(aux)
    txt = input()
'''
'''
class Bet:
    def __init__(self, name: str, nums: [int]):
        self.name = name
        self.nums = nums
        self.hits = 0
        self.out  = name + ' '

    def __str__(self):
        return self.out

def crit(bet: Bet):
    return bet.hits

def sort_bet(bets_s: [Bet]):
    bets.sort(key=crit)
    stp = False

    while not stp:
        stp = True
        for x in range(len(bets_s) - 1):
            if (bets_s[x].hits == bets_s[x+1].hits) & (bets_s[x].name > bets_s[x+1].name):
                stp = False
                bets_s[x], bets_s[x+1] = bets_s[x+1], bets_s[x]

    return bets_s

bets: [Bet] = []
aux = input()

while aux != "FIM":
    aux_int: [int] = []
    aux = aux.split()
    i = 1
    put = True

    while i < len(aux):
        aux_int.append(aux[i])
        i += 1
    for j in range(len(bets)):
        if bets[j].name == aux[0]:
            bets[j].nums = aux_int
            put = False

    if put:
        bets.append(Bet(aux[0], aux_int))

    aux = input()

result = (input().split('-'))

for i in range(len(bets)):
    for j in range(len(bets[i].nums)):
        for k in result:
            if bets[i].nums[j] == k:
                bets[i].hits += 1
                bets[i].out += '+'

bets = sort_bet(bets)
for i in bets:
    print(i)
'''

class Pair:
    def __init__(self, letters):
        self.pair = letters
        self.num  = 1

    def hit(self):
        self.num += 1

    def __str__(self):
        return self.pair

def make_pair(a: chr, b: chr):
    if (ord(a) < 65) | (ord(a) > 122) | (90 < ord(a) < 97):
        return "NAO"

    if (ord(b) < 65) | (ord(b) > 122) | (90 < ord(b) < 97):
        return "NAO"

    return (a + b).lower()


string = input()

while string != "NAO QUERO MAIS":
    num_s = 0
    num_a = 0
    pairs: [Pair] = []
    for i in string:
        if i == ' ':
            num_s += 1

        elif (i == 'a') | (i == 'A'):
            num_a += 1

    for i in range(len(string) - 1):
        found = False
        aux   = make_pair(string[i], string[i+1])

        if aux != "NAO":
            for j in range(len(pairs)):
                if pairs[j].pair == aux:
                    pairs[j].hit()
                    found = True

            if not found:
                pairs.append(Pair(aux))

    print(num_s)
    print(num_a)

    if pairs:
        current = pairs[0]
        for i in pairs:
            if i.num > current.num:
                current = i

        print(current.num)
        print(current.pair)

    else:
        print("NENHUM PAR")

    string = input()
'''
'''
dic = {}

while True:
    aux = input().upper()
    dic[aux] = float(input())
    aux = input().upper()
    if aux == "FIM":
        break

curr_max = ["", 0]
curr_min = ["", 100]

for i in dic:
    if dic[i] > curr_max[1]:
        curr_max[0] = i
        curr_max[1] = dic[i]

    if dic[i] < curr_min[1]:
        curr_min[0] = i
        curr_min[1] = dic[i]

print(curr_min[0])
print(curr_max[0])
'''