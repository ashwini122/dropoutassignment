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
    -------------------------------------------------------------------------------------------
Ans) Here if we go through the question and data given are of drop_rates given so the state with the least dropout rate of higher
     secondary students will be the state who has highest passing student. so I grouped the data based on state and  took a mean of 
     dat all the years given on 'HrSecondary_Total' data.
     
       mean_nn_df = notnull_df.groupby('State_UT')[['HrSecondary_Total']].mean()

       mean_nn_df.sort_values('HrSecondary_Total', ascending= True)

   Result is in the solution1 file.
   
 3. How can we find average drop_out rate for secondary school boys.
 -------------------------------------------------------------------------------------------------
 
ans)  Similar to 1st Question, removed all the "NR" Data from Secondary_Boys.
       
       notnull_df = new_df[pd.notnull(new_df['Secondary _Boys'])]
       
   Grouped By state and found the mean of drop out rates and sorted it in descending order.
       
        mean_nn_df1 = notnull_df.groupby('State_UT')[['Secondary _Boys']].mean()
	mean_nn_df1.sort_values('Secondary _Boys', ascending= False)
   This will give the lit of data i.e. states along with the highest average dropout rates of Secondary_Boys
   
   
   4. Imagine we get individual student's data with their activity of attendance of every school in India, Please suggest some solution       (In words, Not code) to find the same answers to above questions. Please be as detailed as possible. 
      One sample record for above question(Q.4): DATETIME FORMAT : yy-MM-dd HH:mm:ss,SSS ZZZZ 
         
	 {"state":"Gujarat","schoolId":"10f658d42","standard":"11","studentId":"37e6893a7978c","Attended":"1","timestamp":"11-02-11 
         16:47:35,985 +0000"}   
	
  4.1) So as per the first question "Find state with the highest percent of students finishing their schooling.?"
   
   Firstly, stundents who have attended Standard 12 are considered as students who have finished schooling.
   
   Assuming we have dataframe with whole data per student for each day.
   
   Count the sum of records where standard "12" and attended is "1" and perform a group by operation on student id, state, year 
   -----------------------------------------------------------------------------------------------------------------
   This will help me to fetch students attendence total for a specific year and for specific state.
   
   Now considering 40% attendence is minimum requirement to complete 12th standard we can filter out records whose attendance sum 
    is less than 100.
    
  remove students whose sum(attended) is less 100
  ------------------------------------------------------
  
  After this we can do a count(studentID) by doing a group by on state an year on the above result which we received
  ---------------------------------------------------------------------------------------------------------------
  
  this will return the number students who attended 12th for that particular year for that particular state
  
  Again to do a goup by on state and do a sum(count(student(id)) for all the years and store it as total
  -------------------------------------------------------------------------------------------
  
 This will give the sum total sum of students for all years in one particular state.
  Now to find percentage we can apply the below :
  df['state_percent'] = df['total']/df1['total].sum()
  
  This will percentage for each state and we can sort this in descending order to get top states with highest schooling
   
	
  4.3) How can we find average drop_out rate for secondary school boys.
  
  Similar to the above solution we secondary school is standards 10th and as the geneder of the students is not mentioned 
  in data set we are considering the whole stundents who are in starndard 10.
  
   Count the sum of records where standard "10" and attended is "0" and perform a group by operation on student id, state, year 
   --------------------------------------------------------------------------------------------------------------------------------
   
   This will help me to fetch students attendence total for a specific year and for specific state.
  
   Now considering 40% attendence is minimum requirement to complete 12th standard we can select records whose attendance sum 
    is less than 100.
    
   select students whose sum(attended) < 100
   ---------------------------------------------------------------------------
   
   After this we can do a count(studentID) by doing a group by on state an year on the above result which we received
  ---------------------------------------------------------------------------------------------------------------
  
   this will return the number students who have not attended 10th for that particular year for that particular state
   
   Do  goup by on state and do a sum(count(student(id)) for all the years and store it as total
  -------------------------------------------------------------------------------------------
  
   This will give the sum total sum of students for all years in one particular state who have not attended 10th 
    and then we can do a mean() on the result to get the average of students who have not are dropped out for each state.
   
