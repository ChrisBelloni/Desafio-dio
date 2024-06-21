numerodevitoria = int(input("Digite aqui a quantidade de vitórias: "))
numerodederrota = int(input("Digite aqui a quantidade de derrotas: "))
total = numerodevitoria - numerodederrota

def ranking(saldoVitorias):
    if saldoVitorias <= 10:
        nivel = "Ferro"
    elif 11 <= saldoVitorias <= 20:
        nivel = "Bronze"
    elif 21 <= saldoVitorias <= 50:
        nivel = "Prata"
    elif 51 <= saldoVitorias <= 70:
        nivel = "Ouro"
    elif 71 <= saldoVitorias <= 80:
        nivel = "Platina"
    elif 81 <= saldoVitorias <= 90:
        nivel = "Ascendente"
    elif 91 <= saldoVitorias <= 100:
        nivel = "Imortal"
    elif saldoVitorias >= 101:
        nivel = "Radiante"
    
    return f"O Herói tem saldo de {saldoVitorias} está no nível de {nivel}"

print(ranking(total))
