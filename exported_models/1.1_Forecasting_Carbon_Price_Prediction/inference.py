from xgboost import XGBRegressor

model = XGBRegressor()
model.load_model("exported_models/xgb_EU_ETS.json")
