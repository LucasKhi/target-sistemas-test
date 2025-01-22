import json

def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Erro: O arquivo {file_path} não foi encontrado.")
        return None
    except json.JSONDecodeError:
        print(f"Erro: O arquivo {file_path} está mal formatado.")
        return None