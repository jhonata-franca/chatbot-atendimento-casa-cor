import os
import anthropic

# Lê as instruções da Cora direto do arquivo
with open("02-instrucoes-v5.md", "r", encoding="utf-8") as f:
    system_prompt = f.read()

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

historico = []

print("=" * 50)
print("  Cora — Assistente Virtual da Casa & Cor")
print("  (digite 'sair' para encerrar)")
print("=" * 50)

while True:
    entrada = input("\nVocê: ").strip()

    if entrada.lower() == "sair":
        print("\nCora: Até mais! 👋")
        break

    if not entrada:
        continue

    historico.append({"role": "user", "content": entrada})

    resposta = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        system=system_prompt,
        messages=historico,
    )

    texto = resposta.content[0].text
    historico.append({"role": "assistant", "content": texto})

    print(f"\nCora: {texto}")
