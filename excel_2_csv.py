# -*- coding=utf8 -*-


import pandas as pd
import sys


def excel_2_csv(f_name):
	content = pd.read_excel(f_name)
	new_f = f_name.split(".")[0] + ".csv"
	content.to_csv(new_f, encoding="ANSI")
	return new_f


def chg_csv_code(f_name):
	with open(f_name, "w+") as f:
		content = f.read()
		f.write(content, "ansi")
		
	f_name.close()										


def main():
	src_file = sys.argv[1]
	new_file = excel_2_csv(src_file)
#	chg_csv_code(new_file)

if __name__ == "__main__":
# 原文件名 sys.argv[1]
	main()
