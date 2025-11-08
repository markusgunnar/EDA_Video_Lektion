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

def loans_by_genre(df: pd.DataFrame) -> pd.Series:
	"""
	What is loaned the most?
	Sorts the dataframe by genre and counts the number of loans per genre.
	"""

	return (
		df.groupby("genre", dropna=False)["loan_id"]
		.nunique()
		.sort_values(ascending=False)
		.reset_index(name="loans")
	)

def loans_by_branch(df: pd.DataFrame) -> pd.Series:
	"""
	Where are the most loans made?
	Sorts the dataframe by branch and counts the number of loans per branch.
	"""

	return (
		df.groupby("branch", dropna=False)["loan_id"]
		.nunique()
		.sort_values(ascending=False)
		.reset_index(name="loans")
	)

def loans_over_time(df: pd.DataFrame, freq: str="M") -> pd.Series:
	"""
	When are the loans made?
	Groups the dataframe by month and counts the number of loans per month.
	"""

	ts = (
		df.set_index("checkout_date")
		.sort_index()
		.resample(freq)["loan_id"]
		.nunique()
		.rename("loans")
		.reset_index()
	)

	return ts

