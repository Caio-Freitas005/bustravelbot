# Bot Especialista - Política de Reembolso de Viagens (TechX)

## Descrição do Projeto

Este projeto implementa um chatbot especialista baseado no modelo Google Gemini. O bot atua como um assistente de Recursos Humanos treinado exclusivamente com as diretrizes de reembolso de despesas de viagens corporativas da empresa fictícia "TechX". 

Ele foi projetado para não alucinar sobre assuntos fora do seu escopo e está programado para responder exatamente a **três perguntas** do usuário. Ao concluir a terceira resposta, o bot gera automaticamente um resumo completo da interação e encerra o atendimento.

## Como reproduzir a execução

1. **Clone o repositório:**

   ```bash
   git clone <url-do-repositorio>
   cd <nome-da-pasta>
   ```

2. **Instale as dependências:**

    ```bash
    uv sync
    ```

3. **Insira sua chave no arquivo** `.env`.

4. **Execute o script:**

    ``` bash
    uv run main.py
    ```
