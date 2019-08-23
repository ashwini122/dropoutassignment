# dropoutassignment
Based on the Json Data received, the Meta Data and the actual data we in two different feilds. 

a)Created a empty dataframes with all the Fields mentioned in the Meta data which seems like this below.

Empty DataFrame
  Columns: [State_UT,  year, Primary_Boys, Primary_Girls, Primary_Total, Upper Primary_Boys, Upper Primary_Girls, Upper Primary_Total,   Secondary _Boys, Secondary _Girls, Secondary _Total, HrSecondary_Boys, HrSecondary_Girls, HrSecondary_Total]
Index: []

b) Replaced all not Reported data wit "NR" with NaN and all rest other "Uppe_r_Primary" as None
   
    new_df = df.replace({"NR":np.nan , "Uppe_r_Primary" : None})

c) And then created a Not Null dataframe based on Not not values for HrSecondary_Total coloumns.

    notnull_df = new_df[pd.notnull(new_df['HrSecondary_Total'])]

1) Find state with the highest percent of students finishing their schooling.
Ans) Here if we go through the question and data given are of drop_rates given so the state with the least dropout rate of higher
     secondary students will be the state who has highest passing student. so I grouped the data based on state and  took a mean of 
     dat all the years given on 'HrSecondary_Total' data.
     
       mean_nn_df = notnull_df.groupby('State_UT')[['HrSecondary_Total']].mean()

       mean_nn_df.sort_values('HrSecondary_Total', ascending= True)

   Result is in the solution1 file.
   
 3. How can we find average drop_out rate for secondary school boys.
 
ans)  Similar to 1st Question, removed all the "NR" Data from Secondary_Boys.
       
       notnull_df = new_df[pd.notnull(new_df['Secondary _Boys'])]
       
   Grouped By state and found the mean of drop out rates and sorted it in descending order.
       
        mean_nn_df1 = notnull_df.groupby('State_UT')[['Secondary _Boys']].mean()
	mean_nn_df1.sort_values('Secondary _Boys', ascending= False)
   This will give the lit of data i.e. states along with the highest average dropout rates of Secondary_Boys
	
       
