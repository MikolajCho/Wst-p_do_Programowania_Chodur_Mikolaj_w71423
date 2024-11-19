import math

def pole_kola(r):
    if r < 0:  
        print("Promień nie może być liczbą ujemną.")
    elif r == 0:
        print("Pole wynosi 0")
    else:
        pole = math.pi * r**2 
        print(f"Pole koła o promieniu {r} wynosi {pole:.2f}")


pole_kola(5)   
pole_kola(-3)
pole_kola(0)
