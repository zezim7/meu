# Conversor PDF para DOCX

Aplicativo web simples para converter arquivos PDF em documentos DOCX.

## Como executar

Você **não é obrigado** a usar ambiente virtual. Ele é apenas uma boa prática.

### Opção 1: com ambiente virtual (recomendado)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

### Opção 2: sem ambiente virtual

```bash
pip install -r requirements.txt
python app.py
```

Depois acesse `http://localhost:5000` no navegador.

## Observações

- O arquivo convertido é gerado temporariamente e não fica armazenado.
- O tamanho máximo de upload é de 20 MB.
- Para usar diretamente na web (Internet), você pode publicar este app em um serviço de hospedagem Python (ex.: Render, Fly.io, Railway, etc.) e expor o endereço público.
