#!/usr/bin/env python3

class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    def last_name(self):
        return self.name.split()[-1]
    def give_raise(self, percent):
        self.pay *= (1.0 + percent)

asta = Worker("Astryda Malinowska", 120000)
markus = Worker("Astrydzia Markus", 150000)

print(asta.last_name())
print(markus.last_name())
markus.give_raise(.10)
print(markus.pay)