# Conversor PDF para DOCX

Aplicativo web simples para converter arquivos PDF em documentos DOCX.

## Como executar

1. Crie um ambiente virtual e instale as dependências:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Inicie o servidor:

```bash
python app.py
```

3. Acesse `http://localhost:5000` no navegador.

## Observações

- O arquivo convertido é gerado temporariamente e não fica armazenado.
- O tamanho máximo de upload é de 20 MB.
