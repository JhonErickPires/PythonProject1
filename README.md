# 📦 PythonProject1 – Sistema Web de Controle de Itens

Aplicação web desenvolvida em **Python + Flask** para controle acumulativo de itens com geração de relatório em planilha (.csv).

O sistema permite adicionar um número de item e sua quantidade. Caso o item já exista, a quantidade é somada automaticamente. Ao final, é possível baixar um relatório organizado em colunas (Número do Item | Quantidade).

---

## 🌍 Acesse Online

🔗 **Sistema Online:**  
https://bit.ly/controle-itens

---

## 🚀 Funcionalidades

- ✔ Adição de número do item  
- ✔ Registro de quantidade  
- ✔ Soma automática de itens repetidos  
- ✔ Visualização dos itens cadastrados  
- ✔ Download de relatório em formato CSV  
- ✔ Separação correta em colunas para Excel  

---

## 🛠️ Tecnologias Utilizadas

- Python 3  
- Flask  
- HTML  
- CSV (geração de planilha)  
- Gunicorn  
- Deploy via Render  

---

## 📂 Estrutura do Projeto

├── app.py

├── requirements.txt

├── templates/

│ └── index.html

└── README.md



---

## ▶️ Como Executar Localmente

1. Clone o repositório:

    git clone https://github.com/JhonErickPires/PythonProject1

2. Acesse a pasta do projeto:

    cd PythonProject1


3. (Opcional) Crie um ambiente virtual:
   
      python -m venv venv
  
Ativar no Windows:

      venv\Scripts\activate

4. Instale as dependências:

    pip install -r requirements.txt

5. Execute a aplicação:

    python app.py

6. Acesse no navegador


---

## ☁️ Deploy

Aplicação publicada utilizando **Render Web Service**, utilizando Gunicorn como servidor WSGI.

---

## 🔮 Melhorias Futuras

- Persistência em banco de dados  
- Geração de arquivo `.xlsx`  
- Interface com Bootstrap  
- Sistema de autenticação  
- Domínio personalizado  

---

## 👨‍💻 Autor

**Jhon Erick Pires Cusime**

