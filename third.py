import time
import math

def je_prvocislo(cislo):
    cislo = int(cislo)
    if cislo <= 1:
        return False
    
    i = 0
    hranice = int(cislo**0.5) + 1
    
    for delitel in range(2, hranice):
        time.sleep(0.001)
        if cislo % delitel == 0:
            print(f'Iterace {i}')
            return False
        i += 1
        
    print(f'Iterace: {i}')
    return True

def vrat_prvocisla(maximum):
    maximum = int(maximum)
    results = []
    for i in range(2, maximum + 1):
        if je_prvocislo(i):
            results.append(i)
    return results

if __name__ == "__main__":
    cislo = input("Zadej maximum: ")
    prvocisla = vrat_prvocisla(cislo)
    print(prvocisla)