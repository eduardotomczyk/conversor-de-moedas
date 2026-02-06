import requests

AVAILABLE_CURRENCIES = {"USD", "EUR", "BRL"}

API_KEY = "SUA_API_KEY_AQUI" 
API_URL = "https://v6.exchangerate-api.com/v6/{}/latest/{}"

def convert_currency(amount, from_currency, to_currency):
    """Converte o valor usando API"""
    url = API_URL.format(API_KEY, from_currency)
    response = requests.get(url)

    if response.status_code != 200:
        raise ValueError("Erro ao acessar a API de câmbio.")

    data = response.json()

    if "conversion_rates" not in data:
        raise ValueError("Resposta inválida da API.")

    rates = data["conversion_rates"]

    if to_currency not in rates:
        raise ValueError(f"Conversão para {to_currency} não disponível.")

    rate = rates[to_currency]
    return amount * rate

def main():
    print("Bem-vindo ao conversor de moedas!")
    
    while True:
        # Mostra as moedas disponíveis
        print("Moedas disponíveis:", ", ".join(AVAILABLE_CURRENCIES))

        try:
            # Ler valor com validação
            amount_input = input("\nValor: ")
            if not amount_input.replace('.', '', 1).isdigit():
                raise ValueError(f"Valor inválido: {amount_input}")
            amount = float(amount_input)

            # Ler moedas
            from_currency = input("De (ex: USD): ").upper()
            to_currency = input("Para (ex: BRL): ").upper()

            # Validar moedas
            if from_currency not in AVAILABLE_CURRENCIES:
                raise ValueError(f"Moeda de origem inválida: {from_currency}")
            if to_currency not in AVAILABLE_CURRENCIES:
                raise ValueError(f"Moeda de destino inválida: {to_currency}")

            # Converter
            result = convert_currency(amount, from_currency, to_currency)
            print(f"\nResultado: {result:.2f} {to_currency}")

        except ValueError as e:
            print(f"Erro: {e}")

        # Perguntar se quer continuar
        again = input("\nQuer converter outra moeda? (sim/não): ").strip().lower()
        if again not in ("sim", "s"):
            print("\nObrigado por usar o conversor! Até a próxima 👋")
            break

if __name__ == "__main__":
    main()