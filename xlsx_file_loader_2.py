!pip install xlwings

df = xw.Book('./파일명.xlsx').sheets[0].range('A1').options(pd.DataFrame, index=False, expand='table').value
