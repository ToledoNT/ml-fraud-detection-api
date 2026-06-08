from flask import Flask, request, render_template
import joblib
import os
from services.predictor import predict_fraud

app = Flask(__name__)

MODEL_PATH = "model/fraude.pkl"

if not os.path.exists(MODEL_PATH):
    raise Exception("Modelo não encontrado. Rode train.py primeiro!")

model = joblib.load(MODEL_PATH)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        v1 = float(request.form.get("v1") or 0)
        v2 = float(request.form.get("v2") or 0)
        v3 = float(request.form.get("v3") or 0)
        amount = float(request.form.get("amount") or 0)

        # ⚠️ IMPORTANTE: reshape correto para ML
        data = [v1, v2, v3, amount]

        result, risk, level = predict_fraud(model, data)

        if result == 1:
            texto = f"🚨 FRAUDE DETECTADA ({risk:.1f}% - {level})"
        else:
            texto = f"✔ Transação normal ({risk:.1f}% - {level})"

        return render_template("result.html", resultado=texto)

    except Exception as e:
        return render_template(
            "result.html",
            resultado=f"Erro na predição: {str(e)}"
        )


if __name__ == "__main__":
    app.run(debug=True)