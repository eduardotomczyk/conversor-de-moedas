AVAILABLE_CURRENCIES = {"USD", "EUR", "BRL"}


# Dicionário com taxas de câmbio fixas
EXCHANGE_RATES = {
    ("USD", "BRL"): 4.98,
    ("EUR", "BRL"): 5.42,
    ("BRL", "USD"): 0.20,
    ("BRL", "EUR"): 0.18,
    ("USD", "EUR"): 0.92,
    ("EUR", "USD"): 1.09,
}

def convert_currency(amount, from_currency, to_currency):
    key = (from_currency, to_currency)
    rate = EXCHANGE_RATES.get(key)
    
    if rate is None:
        raise ValueError(f"Conversão não disponível.")

    return amount * rate

def main():
    print ("Bem-vindo ao conversor de moedas!")
    print("Moedas disponíveis:", ", ".join(AVAILABLE_CURRENCIES))

    try:
        # Ler valor com validação
        amount_input = input("Valor: ")
        if not amount_input.replace('.', '', 1).isdigit():
            raise ValueError(f"Valor inválido: {amount_input}")
        amount = float(amount_input)

        from_currency = input("De (ex: USD): ").upper()
        to_currency = input("Para (ex: BRL): ").upper()

        if from_currency not in AVAILABLE_CURRENCIES:
            raise ValueError(f"Moeda de origem inválida: {from_currency}")

        if to_currency not in AVAILABLE_CURRENCIES:
            raise ValueError(f"Moeda de destino inválida: {to_currency}")

        result = convert_currency(amount, from_currency, to_currency)
        print(f"\nResultado: {result:.2f} {to_currency}")

    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()