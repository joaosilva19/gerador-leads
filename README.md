# Gerador de Leads Avançado

Este aplicativo Streamlit localiza empresas reais por setor e cidade, extrai e-mails e telefones através de scraping de TeleListas.

## Como usar

1. Faça o clone ou baixe este repositório.
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute:
   ```bash
   streamlit run app.py
   ```
4. No app, informe **Cidade**, **Setor** e **Quantidade**. Clique em **Buscar Leads**.
5. Visualize os resultados e baixe o CSV.

## Observações

- Limite de resultados configurável. O Google pode bloquear requests se exagerar.
- TeleListas permite encontrar e-mails/telefones embutidos na página da empresa.
- Modifique o *User-Agent* em `app.py` se encontrar bloqueios.