with open('data.json') as f:
    content = json.load(f)

    cnames = ['State_UT', ' year', 'Primary_Boys', 'Primary_Girls', 'Primary_Total', 'Upper Primary_Boys','Upper Primary_Girls','Upper Primary_Total','Secondary _Boys','Secondary _Girls','Secondary _Total','HrSecondary_Boys','HrSecondary_Girls','HrSecondary_Total']
    df = pd.DataFrame(columns= cnames)

    for dx in content['data']:
        #df = df.append(pd.DataFrame([dx], columns= cnames))

    print(df.loc[ :])