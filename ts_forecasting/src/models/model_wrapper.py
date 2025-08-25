import mlflow.pyfunc
import pickle
from mlflow.models.signature import ModelSignature
from mlflow.types.schema import Schema, ColSpec
from src.models.tracking_constants import ModelTracking

ARTIFACT_NAME = ModelTracking.ARTIFACT_NAME.value

class SkforecastWrapper(mlflow.pyfunc.PythonModel):

    def load_context(self, context):
        # Carica il forecaster serializzato
        with open(context.artifacts[ARTIFACT_NAME], "rb") as f:
            self.forecaster = pickle.load(f)

    def predict(self, context, model_input):
        """
        model_input: dict con chiavi:
            - 'last_window': pd.Series
            - 'exog': pd.DataFrame
            - 'steps': int
        """
        # Validazione minima
        if not isinstance(model_input, dict):
            raise ValueError("model_input must be a dict with keys: 'last_window', 'exog', 'steps'.")

        last_window = model_input.get("last_window")
        exog = model_input.get("exog")
        steps = model_input.get("steps")

        if last_window is None or exog is None or steps is None:
            raise ValueError("Missing one or more required inputs: 'last_window', 'exog', 'steps'.")

        # Previsione
        return self.forecaster.predict(
            steps=steps,
            last_window=last_window,
            exog=exog
        )

    @classmethod
    def get_signature(cls):
        signature = ModelSignature(
                        inputs=None,
                        outputs=Schema([
                            ColSpec(type="double", name="forecast")
                        ])
                    )
        return signature


class SkforecastWrapperBS(mlflow.pyfunc.PythonModel):

    def load_context(self, context):
        # Carica il forecaster serializzato
        with open(context.artifacts[ARTIFACT_NAME], "rb") as f:
            self.forecaster = pickle.load(f)

    def predict(self, context, model_input):
        """
        model_input: dict con chiavi:
            - 'last_window': pd.Series
            - 'exog': pd.DataFrame
            - 'steps': int
            - 'interval': list
            - 'n_boot': int
        """
        # Validazione minima
        if not isinstance(model_input, dict):
            raise ValueError("model_input must be a dict with keys: 'last_window', 'exog', 'steps'.")

        for key in ['last_window', 'exog', 'steps', 'interval', 'n_boot']:
            if model_input.get(key) is None:
                raise ValueError(f"Missing required input: '{key}'.")

        last_window = model_input.get("last_window")
        exog = model_input.get("exog")
        steps = model_input.get("steps")
        interval = model_input.get("interval")
        n_boot = model_input.get("n_boot")

        # Previsione
        return self.forecaster.predict_interval(
            steps=steps,
            last_window=last_window,
            exog=exog,
            interval=interval,
            n_boot=n_boot,
            use_in_sample_residuals=False,
            use_binned_residuals=False
        )

    @classmethod
    def get_signature(cls):
        signature = ModelSignature(
                        inputs=None,
                        outputs=Schema([
                            ColSpec(type="double", name="forecast")
                        ])
                    )
        return signature