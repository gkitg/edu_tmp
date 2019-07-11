from collections import namedtuple, deque


class HexCalc(object):
    def __init__(self, x):
        hl = namedtuple("HL", "A B C D E F")
        self.hex_letters = hl(A=10, B=11, C=12, D=13, E=14, F=15)
        self.x = self.to_dec(x)

    def __add__(self, other):
        return self.to_hex(self.x + other.x)

    def __mul__(self, other):
        return self.to_hex(self.x * other.x)

    def to_dec(self, x):
        dec = 0
        for i in x:
            if i in self.hex_letters._fields:
                v = self.hex_letters.__getattribute__(i)
            else:
                v = int(i)
            dec += v * (16 ** abs(len(x) - 1 - x.index(i)))
        return dec

    def to_hex(self, x):
        if x < 16:
            return [str(x)]
        else:
            r = deque()
            while x > 15:
                d = x % 16
                r.appendleft(str(d) if d < 10 else self.hex_letters._fields[d-10])
                x = x // 16
            r.appendleft(str(x) if x < 10 else self.hex_letters._fields[x-10])
            return list(r)


a = input("Введите перове число в шестнадцатиричном формате: ").upper()
b = input("Введите второе число в шестнадцатиричном формате: ").upper()

hc_a = HexCalc(a)
hc_b = HexCalc(b)

print(f"Сумма:          {hc_a + hc_b}")
print(f"Произведение:   {hc_a * hc_b}")