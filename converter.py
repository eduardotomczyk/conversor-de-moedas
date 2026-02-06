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
    if key not in EXCHANGE_RATES:
        raise ValueError(f"Conversão de {from_currency} para {to_currency} não suportada.")
    rate = EXCHANGE_RATES[key]
    return amount * rate

def main():
    print ("Bem-vindo ao conversor de moedas!")

    try:
        amount = float(input("Valor: "))
        from_currency = input("De (ex: USD): ").upper()
        to_currency = input("Para (ex: BRL): ").upper()

        result = convert_currency(amount, from_currency, to_currency)
        print(f"\nResultado: {result:.2f} {to_currency}")
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()