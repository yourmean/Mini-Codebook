#pip install xwings

import xwings as xw

xw.App(visible=False)
df = xw.Book('파일경로/이름.xlsx')
df = df.sheet(1).used_range(pdf.DataFrame).value.reset_index()
