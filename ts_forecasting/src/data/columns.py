from enum import Enum

class Columns(Enum):
    DATE = "SETTLEMENT_DATE"
    AMOUNT = "AMOUNT"
    NAME = "NAME"
    PRED_UB_COL = "upper_bound"
    PRED_LB_COL = "lower_bound"
