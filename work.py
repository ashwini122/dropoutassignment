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
    new_df = df.replace("NR", 0)
    new_df
    state_grp = new_df.groupby('State_UT')
