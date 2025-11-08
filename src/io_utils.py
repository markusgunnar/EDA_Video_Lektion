import pandas as pd

REQUIRED = [
	"loan_id", "checkout_date", "branch", "genre", "item_type", "patron_age_group", "loan_days", "returned_date", "overdue_days", "fine_amount"
]

def load_data(_path: str) -> pd.DataFrame:
	"""
	Load library loans data from a CSV file into a dataframe.
	Args:
		path (str): The file path to the CSV file.
	Returns:
		pd.DataFrame: DataFrame containing the library loans data.
	"""
	df = pd.read_csv(_path, parse_dates=["checkout_date", "returned_date"])
	missing = [req for req in REQUIRED if req not in df.columns]

	if missing:
		raise ValueError(f"Missing required columns: {missing}")
	
	return df

def coerce_numeric(_df: pd.DataFrame) -> pd.DataFrame:
	"""
	Ensures that numeric columns actually are numeric types.
	Args:
		df (pd.DataFrame): The input DataFrame.
	Returns:
		pd.DataFrame: DataFrame with coerced numeric columns.
	"""
	coerced_df = _df.copy()
	for col in ["loan_days", "overdue_days", "fine_amount"]:
		coerced_df[col] = pd.to_numeric(coerced_df[col], errors="coerce")

	return coerced_df