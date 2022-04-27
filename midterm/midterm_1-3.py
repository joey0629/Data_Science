import pandas as pd
df = pd.read_csv('pandas_data.csv')
df2 = df.groupby('City').agg(
        total_male_population = pd.NamedAgg(column='Male population',aggfunc='sum'),
        total_female_population = pd.NamedAgg(column = 'Female population',aggfunc = 'sum'),
        area = pd.NamedAgg(column = 'Area',aggfunc = 'sum')
    )
df2['population'] =  df2['total_male_population']+df2['total_female_population']
df2['density'] = df2['population']/df2['area']
df2.sort_values(by=['density'],inplace=True,ascending=False)
del df2['total_male_population']
del df2['total_female_population']
df2 = df2.reindex(columns = ['population','area','density'])
print(df2)

