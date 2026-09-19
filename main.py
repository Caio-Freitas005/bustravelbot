import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

if not google_api_key:
    raise ValueError("Chave da API do Google não encontrada. Verifique o arquivo .env.")

client = genai.Client(api_key=google_api_key)

instrucao_sistema = """
Você é o Assistente Virtual de RH da empresa TechX, especialista na Política de Reembolso de Viagens.
Seu tom é profissional, direto e amigável.
Você não deve inventar ou alucinar informações. Responda estritamente com base nas regras abaixo:

REGRAS DE REEMBOLSO TECHX:
- Alimentação: O limite é de R$ 150,00 por dia. É obrigatório apresentar nota fiscal. Bebidas alcoólicas não são reembolsáveis.
- Transporte: O uso de Uber/Táxi é permitido exclusivamente para deslocamento até o cliente. Passagens aéreas devem ser solicitadas ao RH via portal interno com 15 dias de antecedência mínima.
- Prazos: O colaborador tem até 5 dias úteis após o retorno da viagem para cadastrar as notas no "Portal TechX HR".
- Pagamento: O valor aprovado é sempre creditado na conta do funcionário junto à folha de pagamento do mês seguinte.

Se o usuário perguntar sobre assuntos fora dessa política de viagens, responda educadamente que você só tem acesso às regras de reembolso corporativo.
"""

config = types.GenerateContentConfig(
    system_instruction=instrucao_sistema,
)

chat = client.chats.create(model="gemini-3.6-flash", config=config)


def iniciar_atendimento():
    print("=" * 60)
    print(" Assistente de RH TechX - Reembolsos de Viagem ")
    print("=" * 60)
    print("Olá! Estou aqui para tirar suas dúvidas sobre a Política de Reembolso.")
    print("Você pode fazer até 3 perguntas sobre o processo.\n")

    perguntas_feitas = 0
    max_perguntas = 3

    while perguntas_feitas < max_perguntas:
        user_input = input(f"Pergunta [{perguntas_feitas + 1}/{max_perguntas}]: ")

        if not user_input.strip():
            print("Por favor, digite uma pergunta válida.")
            continue

        perguntas_feitas += 1

        if perguntas_feitas == max_perguntas:
            prompt_final = (
                f"{user_input}\n\n"
                "[INSTRUÇÃO INTERNA]: Esta é a terceira e última pergunta. "
                "Responda à dúvida do usuário e, logo abaixo, insira um título '### Resumo do Atendimento' "
                "sumarizando todos os pontos que foram esclarecidos ao longo desta conversa. "
                "Finalize a mensagem declarando formalmente que o atendimento está encerrado."
            )
            response = chat.send_message(prompt_final)
        else:
            response = chat.send_message(user_input)

        print(f"\nAssistente: {response.text}\n")
        print("-" * 60)


if __name__ == "__main__":
    iniciar_atendimento()
