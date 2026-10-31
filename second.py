def cislo_text(cislo):
    n = int(cislo)
    
    jednotky = {
        0: "nula", 1: "jedna", 2: "dva", 3: "tři", 4: "čtyři",
        5: "pět", 6: "šest", 7: "sedm", 8: "osm", 9: "devět",
        10: "deset", 11: "jedenáct", 12: "dvanáct", 13: "třináct",
        14: "čtrnáct", 15: "patnáct", 16: "šestnáct", 17: "sedmnáct",
        18: "osmnáct", 19: "devatenáct"
    }
    
    desitky = {
        2: "dvacet", 3: "třicet", 4: "čtyřicet", 5: "padesát",
        6: "šedesát", 7: "sedmdesát", 8: "osmdesát", 9: "devadesát"
    }
        
    if n == 100:
        return "sto"
    elif n < 20:
        return jednotky[n]
    else:
        d = n // 10
        j = n % 10
        
        if j == 0:
            return desitky[d]
        else:
            return f"{desitky[d]} {jednotky[j]}"

if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)