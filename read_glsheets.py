#!/usr/bin/python

# READ GOOGLE SHEETS USING PYTHON

import pandas

def read_glsheets(glsheet_link: str) -> list:
	"""
		Google Sheet link should be publicly readable
	"""

	# google visualization (gviz) API to extract output as CSV
	gviz = "gviz/tq?tqx=out:csv"
	
	# modifying google sheet link to extract output as CSV 
	splited_link = glsheet_link.split("/")
	splited_link[-1] = gviz

	modified_link = "/".join(splited_link)

	sheet_data = pandas.read_csv(modified_link)
	records = sheet_data.to_dict("records")

	return records
