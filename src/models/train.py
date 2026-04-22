
# src/models/train.py

from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import joblib

from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

from xgboost import XGBClassifier

# 👇 agrega esto
BASE_DIR = Path(__file__).resolve().parents[2]
DATA_PATH = BASE_DIR / "data" / "raw" / "hotel_bookings.csv"
MODEL_PATH = BASE_DIR / "models" / "hotel_cancel_model.pkl"


class HotelBookingTrainer:
    def __init__(self, data_path: str):
        self.data_path = data_path
        self.model = None

    def load_data(self):
        df = pd.read_csv(DATA_PATH)
        print(f"Dataset cargado: {df.shape}")
        return df

    def split_data(self, df):
        leakage_cols = [
            "is_canceled",
            "reservation_status",
            "reservation_status_date"
        ]

        X = df.drop(columns=leakage_cols, errors="ignore")
        y = df["is_canceled"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y,
            test_size=0.2,
            random_state=42,
            stratify=y
        )

        return X_train, X_test, y_train, y_test

    def build_pipeline(self, X_train):

        # separar columnas
        numeric_features = X_train.select_dtypes(include=["int64", "float64"]).columns
        categorical_features = X_train.select_dtypes(include=["object"]).columns

        # pipelines internos
        numeric_transformer = Pipeline(steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler())
        ])

        categorical_transformer = Pipeline(steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore"))
        ])

        preprocessor = ColumnTransformer(
            transformers=[
                ("num", numeric_transformer, numeric_features),
                ("cat", categorical_transformer, categorical_features)
            ]
        )

        # modelo XGBoost
        model = XGBClassifier(
            n_estimators=200,
            learning_rate=0.1,
            max_depth=6,
            subsample=0.8,
            colsample_bytree=0.8,
            eval_metric="logloss",
            random_state=42,
            scale_pos_weight=15033/8845
        )

        pipeline = Pipeline(steps=[
            ("preprocessor", preprocessor),
            ("model", model)
        ])

        return pipeline

    def train(self):
        df = self.load_data()
        X_train, X_test, y_train, y_test = self.split_data(df)

        pipeline = self.build_pipeline(X_train)

        cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

        # 🔥 VALIDACIÓN CRUZADA
        print("\n🔁 Ejecutando validación cruzada...")
        cv_scores = cross_val_score(
            pipeline,
            X_train,
            y_train,
            cv=cv,
            scoring="roc_auc",
            n_jobs=-1
        )

        print(f"ROC-AUC CV Scores: {cv_scores}")
        print(f"ROC-AUC CV Mean: {cv_scores.mean():.4f}")

        # 🔥 Entrenamiento final
        print("\n🚀 Entrenando modelo final...")
        pipeline.fit(X_train, y_train)

        # predicciones
        y_pred = pipeline.predict(X_test)
        y_prob = pipeline.predict_proba(X_test)[:, 1]

        # evaluación
        print("\n📊 Classification Report:")
        print(classification_report(y_test, y_pred))

        print("ROC-AUC Test:", roc_auc_score(y_test, y_prob))

        self.model = pipeline

        return pipeline, X_test, y_test



    def save_model(self):
        joblib.dump(self.model, MODEL_PATH)
        print(f"Modelo guardado en: {MODEL_PATH}")


if __name__ == "__main__":
    trainer = HotelBookingTrainer(DATA_PATH)
    model, X_test, y_test = trainer.train()
    trainer.save_model()