NomedoHeroi = input("Digite aqui o nome do Herói: ")
XPnivel = int(input("Digite o XP: "))

if XPnivel <= 1000:
    print("O Herói de nome", NomedoHeroi, "está no nível de Ferro")
elif 1001 <= XPnivel <= 2000:
    print("O Herói de nome", NomedoHeroi, "está no nível de Bronze")
elif 2001 <= XPnivel <= 5000:
    print("O Herói de nome", NomedoHeroi, "está no nível de Prata")
elif 5001 <= XPnivel <= 7000:
    print("O Herói de nome", NomedoHeroi, "está no nível de Ouro")
elif 7001 <= XPnivel <= 8000:
    print("O Herói de nome", NomedoHeroi, "está no nível de Platina")
elif 8001 <= XPnivel <= 9000:
    print("O Herói de nome", NomedoHeroi, "está no nível de Ascendente")
elif 9001 <= XPnivel <= 10000:
    print("O Herói de nome", NomedoHeroi, "está no nível de Imortal")
elif XPnivel >= 10001:
    print("O Herói de nome", NomedoHeroi, "está no nível de Radiante")
