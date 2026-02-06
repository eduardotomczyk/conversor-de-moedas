# Conversor de Moedas

![Python](https://img.shields.io/badge/python-3.x-blue?logo=python)

**Conversor de moedas em Python usando taxas de câmbio reais via API.**

---

## 🚀 Funcionalidades

- Conversão entre moedas: **USD, EUR, BRL**  
- Validação de valores e moedas  
- Mensagens de erro amigáveis  
- Loop interativo para múltiplas conversões  
- Taxas de câmbio em tempo real usando API  

---

## 🛠️ Tecnologias

- Python 3.x  
- Biblioteca `requests` para consumir API  
- Dicionários, funções e tratamento de erros (`try/except`)  

---

## 💻 Como usar

1. **Clone o repositório:**

```bash
git clone https://github.com/eduardotomczyk/conversor-de-moedas.git
cd conversor-de-moedas
```
2. **Instale a biblioteca necessária:**

```bash
pip install requests
```

3. **Adicione sua API Key:**

No arquivo `converter.py`, substitua `SUA_API_KEY_AQUI` pela sua própria chave da API (ExchangeRate-API ou similar).
```python
API_KEY = "SUA_API_KEY_AQUI"
```
4. **Execute o programa:**

```bash
python converter.py
```

## 📝 Exemplo de uso

```
Bem-vindo ao conversor de moedas!
Moedas disponíveis: USD, BRL, EUR
Valor: 10
De (ex: USD): USD
Para (ex: BRL): BRL

Resultado: 49.80 BRL

Quer converter outra moeda? (sim/não): sim

Moedas disponíveis: USD, BRL, EUR
Valor: 20
De (ex: EUR): EUR
Para (ex: USD): USD

Resultado: 21.80 USD

Quer converter outra moeda? (sim/não): não

Obrigado por usar o conversor! Até a próxima 👋
```