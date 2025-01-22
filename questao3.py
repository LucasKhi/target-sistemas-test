from leitor_json import load_json


def calculate_revenue_stats(revenue_data):
    revenue_values = [entry["valor"] for entry in revenue_data if entry["valor"] > 0]

    min_revenue = min(revenue_values)

    max_revenue = max(revenue_values)

    average_revenue = sum(revenue_values) / len(revenue_values)

    days_above_average = len([value for value in revenue_values if value > average_revenue])

    return min_revenue, max_revenue, days_above_average

file_path = 'faturamento.json'

try:
    revenue_data = load_json(file_path)

    if revenue_data:
        min_revenue, max_revenue, days_above_average = calculate_revenue_stats(revenue_data)

        print(f"Menor faturamento: R${min_revenue:.2f}")
        print(f"Maior Faturamento: R${max_revenue:.2f}")
        print(f"Número de dias com faturamento acima da média mensal: {days_above_average}")
except Exception as e:
    print(f"Erro inesperado: {e}")
