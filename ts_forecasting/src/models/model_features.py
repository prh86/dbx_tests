from src.data.columns import Columns
from skforecast.preprocessing import RollingFeatures
from src.models.exogenous_variables.exog import get_day, get_month, get_dayofweek
from functools import partial
import pandas as pd

features_exog = {
    "day": partial(get_day, date_col=Columns.DATE.value),
    "month": partial(get_month, date_col=Columns.DATE.value),
    "day_of_week": partial(get_dayofweek, date_col=Columns.DATE.value)
}


# for custom window features..
# https://skforecast.org/0.14.0/user_guides/window-features-and-custom-features.html
window_features = RollingFeatures(
    stats=["mean", "mean", "std", "std", "coef_variation"], window_sizes=[10, 5, 10, 5, 10]
)


def apply_functions(y, features_to_func):
    cols = []
    for fn in features_to_func:
        cols.append(y.apply(features_to_func[fn], axis=1).rename(fn))
    df_out = pd.concat(cols, axis=1)
    df_out.index = y.index
    return df_out

