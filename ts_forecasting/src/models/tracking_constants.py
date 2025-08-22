from enum import Enum
from pyspark.sql import SparkSession
from pyspark.dbutils import DBUtils
    
spark = SparkSession.builder.getOrCreate()
dbutils = DBUtils(spark)

user = dbutils.notebook.entry_point.getDbutils().notebook().getContext().userName().get()

class ModelTracking(Enum):
    EXPERIMENT_NAME = f"/Users/{user}/my_forecasting_experiment"
    TUNE_TRAIN_RUN_NAME = "forecaster_train_run"
    ARTIFACT_PATH = "skforecast_model"
    ARTIFACT_NAME = "foreacaster"
