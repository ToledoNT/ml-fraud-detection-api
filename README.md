# 💳 Fraud Detection System (Flask + Machine Learning)

Sistema de detecção de fraude em transações financeiras utilizando Machine Learning com interface web em Flask.

---

## 📌 Sobre o projeto

Este projeto foi desenvolvido com o objetivo de simular um sistema de detecção de fraudes em transações financeiras em tempo real.

O usuário insere dados de uma transação e o modelo de Machine Learning retorna:

- ✔ Transação normal
- 🚨 Possível fraude
- 📊 Nível de risco estimado

---

## 📊 Dataset utilizado

O modelo foi treinado utilizando o dataset:

👉 **Credit Card Fraud Detection (Kaggle)**  
Fonte: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

### 🔎 Características do dataset:

- Dados reais anonimizados de transações financeiras
- Variáveis V1 a V28 (transformadas por PCA)
- Coluna `Amount` (valor da transação)
- Coluna `Class`:
  - `0` → Transação normal
  - `1` → Fraude

---

## 🧠 Tecnologias utilizadas

- Python 🐍
- Flask 🌐
- Pandas 📊
- Scikit-learn 🤖
- Joblib 💾
- HTML + CSS 💻

---

## ⚙️ Como funciona

1. O dataset do Kaggle é utilizado para treinar o modelo
2. O modelo de Machine Learning é treinado e salvo em `.pkl`
3. O Flask carrega o modelo treinado
4. O usuário insere os dados via interface web
5. O sistema retorna:
   - Resultado da transação
   - Percentual de risco
   - Nível de suspeita

---