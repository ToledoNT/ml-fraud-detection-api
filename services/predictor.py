import numpy as np

def predict_fraud(model, data):
    # garantir formato correto (1 linha, várias colunas)
    data = np.array(data).reshape(1, -1)

    # previsão (0 ou 1)
    prediction = model.predict(data)[0]

    # probabilidade de fraude
    probability = model.predict_proba(data)[0][1]

    # transformar em % de risco
    risk = float(probability * 100)

    # categoria de risco (melhor UX)
    if risk < 30:
        level = "BAIXO"
    elif risk < 70:
        level = "MÉDIO"
    else:
        level = "ALTO"

    return prediction, risk, level