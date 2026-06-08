import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

# carregar dataset
df = pd.read_csv("data/creditcard.csv")
df.columns = df.columns.str.strip()

target = "Class" if "Class" in df.columns else "class"

fraude = df[df[target] == 1]
normal = df[df[target] == 0]

# downsample da classe normal (evita modelo viciado)
normal_sample = normal.sample(len(fraude) * 3, random_state=42)

df_balanced = pd.concat([fraude, normal_sample])

df_balanced = df_balanced.sample(frac=1, random_state=42)

X = df_balanced[["V1", "V2", "V3", "Amount"]]
y = df_balanced[target]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# modelo mais sensível a fraude
model = RandomForestClassifier(
    n_estimators=300,
    max_depth=12,
    min_samples_leaf=2,
    class_weight="balanced",
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

=joblib.dump(model, "model/fraude.pkl")

print("Modelo treinado com sucesso!")