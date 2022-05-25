cols = ['열1', '열2', '열3']

df['만들열이름'] = df[cols].apply(lambda x: '합친열사이구분자'.join(x.values.as_type(str)), axis=1)
