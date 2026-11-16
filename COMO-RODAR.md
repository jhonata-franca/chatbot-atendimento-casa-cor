# Como rodar a Cora localmente

## Pré-requisitos

- Python 3.8+
- Conta na [Anthropic](https://console.anthropic.com/) com uma API key

## Instalação

```bash
pip install anthropic
```

## Configuração

Defina sua API key como variável de ambiente:

```bash
# Linux/Mac
export ANTHROPIC_API_KEY="sua-chave-aqui"

# Windows (PowerShell)
$env:ANTHROPIC_API_KEY="sua-chave-aqui"
```

## Rodando

```bash
python cora.py
```

A Cora vai iniciar no terminal e responder como assistente da Casa & Cor, seguindo as instruções do arquivo `02-instrucoes-v5.md`.

## Exemplo de uso

```
==================================================
  Cora — Assistente Virtual da Casa & Cor
  (digite 'sair' para encerrar)
==================================================

Você: Qual o prazo de entrega?

Cora: O prazo é de 3 a 10 dias úteis, dependendo do seu CEP.
O prazo exato aparece no carrinho antes de você finalizar a compra. 😊

Você: sair

Cora: Até mais! 👋
```
