with open('data.json') as f:
    content = json.load(f)

    cnames = ['State_UT', ' year', 'Primary_Boys', 'Primary_Girls', 'Primary_Total', 'Upper Primary_Boys','Upper Primary_Girls','Upper Primary_Total','Secondary _Boys','Secondary _Girls','Secondary _Total','HrSecondary_Boys','HrSecondary_Girls','HrSecondary_Total']
    df = pd.DataFrame(columns= cnames)
    i = 0

    for x in content['data']:
        y = []
        y =x
        df.loc[i] = y
        i = i +1
    df
    new_df = df.replace({"NR":np.nan , "Uppe_r_Primary" : None})
    new_df
    notnull_df = new_df[pd.notnull(new_df['HrSecondary_Total'])]
    notnull_df
    mean_nn_df = notnull_df.groupby('State_UT')[['HrSecondary_Total']].mean()
    mean_nn_df.sort_values('HrSecondary_Total', ascending= True)
