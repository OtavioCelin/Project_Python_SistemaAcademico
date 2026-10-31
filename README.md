# Sistema de Gestão Acadêmica em Python

Sistema desenvolvido em Python para simular a gestão acadêmica de uma instituição de ensino diretamente pelo terminal, aplicando conceitos fundamentais de programação estruturada e Orientação a Objetos (POO).

---

## 🎯 Objetivo
Demonstrar o domínio integrado de conteúdos essenciais da linguagem Python, como variáveis, estruturas condicionais, laços de repetição, coleções (listas e dicionários), funções, classes, atributos protegidos por convenção, encapsulamento, tratamento de erros e organização modular do código.

---

## ⚙️ Requisitos Atendidos

* **Cadastro de Estudantes:** Criação da classe `Aluno` e do sistema gerenciador com geração automática e única de números de matrícula aleatórios (de 4 dígitos), além de validação contra campos vazios.
* **Registro de Avaliações:** Permite adicionar múltiplas notas por aluno, aceitando exclusivamente valores entre **0 e 10**, com tratamento de erros que impede a quebra do programa em caso de entradas inválidas.
* **Cálculo de Média e Situação:** 
  * Média $\ge 7,0$: **Aprovado**
  * Média $\ge 5,0$ e $< 7,0$: **Recuperação**
  * Média $< 5,0$: **Reprovado**
  * Sem notas registradas: **"Sem avaliações"** (sem erros de divisão por zero).
* **Orientação a Objetos (POO):** Utilização das classes `Aluno` e `SistemaAcademico`, empregando `__init__`, `self` e visibilidade por convenção (`_` para atributos protegidos).
* **Organização Modular:** Código separado em três módulos distintos seguindo as boas práticas de arquitetura de software em Python.

---

## 📁 Estrutura do Projeto

O projeto está dividido nos seguintes arquivos:

```text
📦 sistema-academico/
 ┣ 📜 aluno.py               # Contém a classe Aluno e regras de cálculo de notas/situação
 ┣ 📜 sistema_academico.py   # Contém a classe SistemaAcademico (gerenciamento e relatórios)
 ┗ 📜 main.py                # Ponto de entrada com o menu interativo em loop
