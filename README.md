# PointSend - Registro de Ponto com Interface Gráfica em PyQt5

Este projeto é uma aplicação de registro de ponto com autenticação via API, construída em Python usando **PyQt5** para a interface gráfica.

Após o login, o usuário pode selecionar uma data e hora, e a aplicação envia os dados de ponto para um endpoint protegido com token OAuth2.

---

## 🖥️ Funcionalidades

- Tela de login com campos de email e senha
- Botão para mostrar/ocultar senha
- Autenticação via OAuth2 com client_id/client_secret
- Seleção de data e hora com componente gráfico
- Envio do registro de ponto para a API
- Mensagens de sucesso/erro com `QMessageBox`

---

## 📂 Estrutura do Projeto

```
.
├── Frontend.py        # Interface gráfica (PyQt5)
├── backend.py         # Módulo backend com funções de autenticação e envio
├── .env               # Contém a variável de ambiente 'Route'
└── README.md
```

---

## ✅ Requisitos

- Python 3.7+
- [PyQt5](https://pypi.org/project/PyQt5/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- requests

---

## 📦 Instalação

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/pointsend.git
cd pointsend
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

Se não tiver um `requirements.txt`, instale manualmente:

```bash
pip install PyQt5 requests python-dotenv
```

3. Crie um arquivo `.env` com o conteúdo:

```
Route=https://sua-url-da-api.com
```

---

## 🚀 Como executar

```bash
python Frontend.py
```

---

## 🔐 Segurança

- A autenticação é feita com `grant_type=password`
- O token de acesso é usado para enviar dados ao endpoint `/api/mobile/time/cards`

---

## 🛠️ Customização

Você pode alterar os seguintes itens conforme seu ambiente:

- `Route` → no `.env`

---

## 📌 Exemplo de uso

1. Digite seu e-mail e senha
2. Clique em **Logar**
3. Escolha a data e hora desejada
4. Clique em **Confirmar**
5. A aplicação envia o ponto à API

---

## 📄 Licença

Este projeto é apenas um exemplo de integração com API para fins educacionais.

---

## ✨ Autor

Jamir Rodrigues  
[LinkedIn](https://www.linkedin.com/in/jamir-rodrigues/)
