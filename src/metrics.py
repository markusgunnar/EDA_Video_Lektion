import pandas as pd

def total_loans(df: pd.DataFrame) -> int:
	"""
	Calculate the total number of loans.
	Args:
		df (pd.DataFrame): The input DataFrame.
	Returns:
		int: Total number of loans.
	"""
	return df["loan_id"].nunique()

def average_loan_days(df: pd.DataFrame) -> float:
	"""
	Calculate the average number of loan days.
	Args:
		df (pd.DataFrame): The input DataFrame.
	Returns:
		float: Average loan days.
	"""
	return float(df["loan_days"].mean())

def overdue_rate(df: pd.DataFrame) -> float:
	"""
	Calculate the average overdue rate
	Args:
		df (pd.DataFrame): The input DataFrame.
	Returns:
		float: Overdue rate.
	"""
	return float((df["overdue_days"] > 0).mean())