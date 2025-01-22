from leitor_json import load_json

file_path = 'faturamento_estados.json'

faturamento_estados = load_json(file_path)

if faturamento_estados is not None:
    faturamento_total = sum(faturamento_estados.values())

    for estado, faturamento in faturamento_estados.items():
        percentual = faturamento / faturamento_total * 100

        print(f"{estado}: R${faturamento:.2f} ({percentual:.2f}%)")