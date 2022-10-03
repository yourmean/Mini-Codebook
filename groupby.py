# https://www.datamanim.com/dataset/99_pandas/pandasMain.html


Ans = df.groupby('host_name').size().\
                to_frame().rename(columns={0:'counts'}).\
                sort_values('counts',ascending=False)
