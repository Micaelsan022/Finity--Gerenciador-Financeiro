# 💸 Finity
> Gerenciador financeiro pessoal feito em Python com dashboard interativo, gráficos e alertas inteligentes.

---

## 🛠️ Tecnologias

| Tecnologia | Função |
|---|---|
| Python | Linguagem principal |
| Streamlit | Interface visual |
| SQLite | Banco de dados |
| Plotly | Gráficos interativos |
| Pandas | Manipulação de dados |

---

## 📂 Estrutura do Projeto

```
Finity/
├── app.py
├── requirements.txt
│
├── database/
│   ├── conexao.py        # Conecta ao banco
│   ├── models.py         # Cria as tabelas
│   └── banco.db          # Gerado automaticamente
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
```

---

## ▶️ Como rodar o projeto

### 1. Clone o repositório
```bash
git clone https://github.com/Micaelsan022/Finity--Gerenciador-Financeiro..git
cd Finity--Gerenciador-Financeiro.
```

### 2. Crie o ambiente virtual
```bash
python -m venv venv
```

Ative o venv:

```bash
# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

> Você sabe que o venv está ativo quando aparece `(venv)` no início do terminal.

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Crie o banco de dados
```bash
python database/models.py
```

### 5. Rode o projeto
```bash
streamlit run app.py
```

Acesse no navegador: `http://localhost:8501`

---

## 🔁 Como salvar suas alterações no GitHub

Sempre que fizer alguma mudança no projeto, rode no terminal:

```bash
git add .
git commit -m "descreva o que você fez aqui"
git push
```

Exemplos de mensagens de commit:
- `feat: adiciona tela de metas`
- `fix: corrige cálculo de saldo`
- `docs: atualiza README`

---

## 🌿 Como trabalhar em equipe sem conflito

Cada integrante deve criar uma branch antes de mexer no código:

```bash
# Cria e entra na branch
git checkout -b feature/nome-da-sua-parte

# Depois de terminar, sobe pro GitHub
git add .
git commit -m "feat: descrição do que foi feito"
git push origin feature/nome-da-sua-parte
```

Depois abre um **Pull Request** no GitHub pra juntar com a `main`.

> Nunca commitar diretamente na `main`.

---

## 📌 Próximas funcionalidades

- [ ] Exportar relatórios em PDF
- [ ] IA para previsão de gastos

