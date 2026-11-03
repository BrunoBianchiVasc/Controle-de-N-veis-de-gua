# 💧 Controle de Níveis de Água

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Colorama](https://img.shields.io/badge/Colorama-0.4.6-2ea44f?style=for-the-badge)
![Terminal](https://img.shields.io/badge/Terminal-CLI-4D4D4D?style=for-the-badge&logo=gnometerminal&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Projeto-181717?style=for-the-badge&logo=github&logoColor=white)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen?style=for-the-badge)

## 📌 Sobre o projeto

O **Controle de Níveis de Água** é um sistema simples de monitoramento de reservatório, executado no terminal. Seu objetivo é exibir mensagens de alerta com **cores diferentes** conforme o nível de água, facilitando a visualização de cada situação.

Projeto desenvolvido para a **Agenda 11 – Bibliotecas** (Desenvolvimento de Sistemas I, Curso Técnico em Desenvolvimento de Sistemas).

## 🛠️ Tecnologias utilizadas

| Tecnologia | Uso no projeto |
|------------|----------------|
| 🐍 **Python** | Linguagem principal do sistema |
| 🎨 **colorama** | Biblioteca externa para colorir o texto no terminal |
| 🎲 **random** | Biblioteca padrão para simular a leitura do sensor |
| 💻 **VS Code** | Editor utilizado no desenvolvimento |
| 🐙 **GitHub** | Versionamento e publicação do código |

## 🚦 Níveis do reservatório

| Nível | Situação | Cor |
|-------|----------|-----|
| 1 | 🔴 Muito baixo (crítico) | Vermelho |
| 2 | 🟡 Baixo | Amarelo |
| 3 | 🟢 Médio | Verde |
| 4 | 🔵 Alto | Ciano |
| 5 | 🔷 Muito alto (alerta) | Azul |

## 🧮 Fórmula / lógica utilizada

Este sistema **não realiza cálculos matemáticos**. Ele funciona por associação entre o nível e a mensagem/cor correspondente:

- **Mensagem do nível:** as situações ficam em uma lista, e o nível é convertido em índice com a fórmula:

  ```
  índice = nível - 1
  ```

  Exemplo: nível 1 → `situacoes[0]`; nível 5 → `situacoes[4]`.

- **Cor do nível:** a função `definir_cor(nivel)` usa estruturas condicionais (`if / elif / else`) para retornar a cor certa.

- **Leitura do sensor (simulada):** `nivel_atual = random.randint(1, 5)` sorteia um nível entre 1 e 5.

## 📁 Estrutura do projeto

```
📦 controle-niveis-agua
 ┣ 📜 reservatorio.py
 ┗ 📜 README.md
```

## ⚙️ Requisitos

- ✅ Python 3.8 ou superior
- ✅ Biblioteca `colorama`

## 🚀 Como executar

**1. Clone o repositório**

```bash
git clone https://github.com/BrunoBianchiVasc/controle-niveis-agua.git
cd controle-niveis-agua
```

**2. Instale a dependência**

```bash
pip install colorama
```

**3. Execute o programa**

```bash
python reservatorio.py
```

## 🖥️ Exemplo de saída

```
=== Monitoramento do Reservatório ===

Nível 1: Muito baixo (crítico)
Nível 2: Baixo
Nível 3: Médio
Nível 4: Alto
Nível 5: Muito alto (alerta)

Leitura atual do sensor:
Nível 3: Médio
```

> 🎨 No terminal, cada linha aparece na cor do seu nível. A leitura atual do sensor muda a cada execução.

## 📝 Observação

Para usar um valor fixo em vez de sorteado, troque a leitura do sensor por, por exemplo, `nivel_atual = 2`.

## 👨‍💻 Autor

Desenvolvido por Bruno 🚀

