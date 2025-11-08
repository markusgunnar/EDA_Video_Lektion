import pandas as pd

def total_loans(_df: pd.DataFrame) -> int:
	"""
	Calculate the total number of loans.
	Args:
		df (pd.DataFrame): The input DataFrame.
	Returns:
		int: Total number of loans.
	"""
	return _df["loan_id"].nunique()

def average_loan_days(_df: pd.DataFrame) -> float:
	"""
	Calculate the average number of loan days.
	Args:
		df (pd.DataFrame): The input DataFrame.
	Returns:
		float: Average loan days.
	"""
	return float(_df["loan_days"].mean())

def overdue_rate(_df: pd.DataFrame) -> float:
	"""
	Calculate the average overdue rate
	Args:
		df (pd.DataFrame): The input DataFrame.
	Returns:
		float: Overdue rate.
	"""
	return float((_df["overdue_days"] > 0).mean())

def loans_by_genre(_df: pd.DataFrame) -> pd.Series:
	"""
	What is loaned the most?
	Sorts the dataframe by genre and counts the number of loans per genre.
	"""

	return (
		_df.groupby("genre", dropna=False)["loan_id"]
		.nunique()
		.sort_values(ascending=False)
		.reset_index(name="loans")
	)

def loans_by_branch(_df: pd.DataFrame) -> pd.Series:
	"""
	Where are the most loans made?
	Sorts the dataframe by branch and counts the number of loans per branch.
	"""

	return (
		_df.groupby("branch", dropna=False)["loan_id"]
		.nunique()
		.sort_values(ascending=False)
		.reset_index(name="loans")
	)

def loans_over_time(_df: pd.DataFrame, _freq: str="M") -> pd.Series:
	"""
	When are the loans made?
	Groups the dataframe by month and counts the number of loans per month.
	"""

	ts = (
		_df.set_index("checkout_date")
		.sort_index()
		.resample(_freq)["loan_id"]
		.nunique()
		.rename("loans")
		.reset_index()
	)

	return ts

