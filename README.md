# 💸 Finity

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit">
  <img src="https://img.shields.io/badge/SQLite-Database-blue?style=for-the-badge&logo=sqlite">
  <img src="https://img.shields.io/badge/Plotly-Graphs-3f4f75?style=for-the-badge&logo=plotly">
</p>

<p align="center">
  <strong>Gerenciador financeiro pessoal desenvolvido em Python para ajudar no controle de receitas, gastos e metas financeiras.</strong>
</p>

---

## ✨ Funcionalidades

✅ Dashboard interativo com indicadores financeiros
✅ Cadastro de receitas e despesas
✅ Controle de metas financeiras
✅ Relatórios detalhados
✅ Gráficos interativos com Plotly
✅ Banco de dados local utilizando SQLite
✅ Categorias automáticas

---

## 📸 Preview

> Adicione aqui algumas imagens do sistema.

```md
/assets/dashboard.png
/assets/gastos.png
/assets/relatorios.png
```

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia   | Descrição            |
| ------------ | -------------------- |
| 🐍 Python    | Linguagem principal  |
| 🎨 Streamlit | Interface web        |
| 🗄️ SQLite   | Banco de dados       |
| 📊 Plotly    | Gráficos interativos |
| 🐼 Pandas    | Manipulação de dados |

---

## 📂 Estrutura do Projeto

```bash
Finity/
├── app.py
├── requirements.txt
│
├── database/
│   ├── conexao.py
│   ├── models.py
│   └── banco.db
│
├── pages/
│   ├── 1_Dashboard.py
│   ├── 2_Receitas.py
│   ├── 3_Gastos.py
│   ├── 4_Metas.py
│   └── 5_Relatorios.py
│
├── services/
│   ├── calculos.py
│   ├── analise_financeira.py
│   └── relatorios_service.py
│
├── charts/
│   └── graficos.py
│
└── assets/
    └── style.py
```

---

# 🚀 Como executar o projeto

## 1️⃣ Clone o repositório

```bash
git clone https://github.com/Micaelsan022/Finity--Gerenciador-Financeiro.git
cd Finity--Gerenciador-Financeiro
```

## 2️⃣ Crie o ambiente virtual

```bash
python -m venv venv
```

### Ative o ambiente

**Linux/macOS**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

---

## 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Crie o banco de dados

```bash
python database/models.py
```

> As categorias padrão são criadas automaticamente.

---

## 5️⃣ Execute a aplicação

```bash
streamlit run app.py
```

Acesse:

```text
http://localhost:8501
```

---

# 🌿 Contribuindo

```bash
git checkout -b feature/minha-feature

git add .
git commit -m "feat: descrição"

git push origin feature/minha-feature
```

Depois, abra um **Pull Request** para a branch `main`.

> ⚠️ Evite realizar commits diretamente na `main`.

---

# 📌 Roadmap

* [ ] Exportação de relatórios em PDF
* [ ] Sistema de login e autenticação
* [ ] Inteligência artificial para previsão de gastos
* [ ] Metas financeiras avançadas
* [ ] Modo escuro

---

## 🤝 Contribuidores

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/Micaelsan022">
        <img src="https://github.com/Micaelsan022.png" width="100px;" alt=""/>
        <br />
        <sub><b>Micael Santos</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/LightList18375">
        <img src="https://avatars.githubusercontent.com/u/244845150?v=4" width="100px;" alt=""/>
        <br />
        <sub><b>Pedro San</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/joaovictorsoaresreis6-cell">
        <img src="https://avatars.githubusercontent.com/u/268621453?v=4" width="100px;" alt=""/>
        <br />
        <sub><b>João Victor</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/danilo-joshue">
        <img src="https://avatars.githubusercontent.com/u/241025165?v=4" width="100px;" alt=""/>
        <br />
        <sub><b>Danilo Joshue</b></sub>
      </a>
    </td>
  </tr>
</table>
