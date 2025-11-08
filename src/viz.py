
import pandas as pd

def _cat_for_plot(_string, _missing_label="Unknown"):
	if hasattr(_string, "astype"):
		_string = _string.astype("object")
	try:
		return _string.fillna(_missing_label)
	except Exception:
		return _string

def _num_for_plot(_string):
	try:
		return pd.to_numeric(_string, errors="coerce").fillna(0)
	except Exception:
		return _string

def bar(_ax, _x, _y, _title, _xlabel, _ylabel, grid: bool = True):
	_x = _cat_for_plot(_x)
	_y = _num_for_plot(_y)
	_ax.bar(_x, _y)
	_ax.set_title(_title)
	_ax.set_xlabel(_xlabel)
	_ax.set_ylabel(_ylabel)
	_ax.grid(grid, axis='y')
	return _ax

def line(_ax, _x, _y, _title, _xlabel, _ylabel, grid: bool = True):
	_y = _num_for_plot(_y)

	data = pd.DataFrame({"x": pd.to_datetime(_x), "y": _y}).dropna()
	data = data.sort_values("x")

	if data["x"].duplicated().any():
		data = (data
		  .groupby(data["x"].to_period("M"))["y"]
		  .sum()
		  .reset_index()
		)
		data["x"] = data["x"].dt.to_timestamp()

	_ax.plot(data["x"], data["y"], marker="o", linestyle='-')
	_ax.set_title(_title)
	_ax.set_xlabel(_xlabel)
	_ax.set_ylabel(_ylabel)
	_ax.grid(grid)
	return _ax

def box_h(_ax, _values, _title, _xlabel, grid: bool = True):
	_values = _num_for_plot(_values)
	_ax.boxplot(_values, vert=False)
	_ax.set_title(_title)
	_ax.set_xlabel(_xlabel)
	_ax.grid(grid, axis="x")
	return _ax



