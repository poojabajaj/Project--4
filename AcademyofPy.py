
# coding: utf-8

# In[1]:


#importing dependencies
import pandas as pd
import numpy as np
import os


# In[2]:


#Reading the csv file in a dataframe
students_df = pd.read_csv('Resources/students_complete.csv')
print(students_df.head())
#checking the dimensions of a dataframe
print(students_df.shape)
students_df= students_df.reset_index(drop = True)
print(students_df.head())


# In[3]:


#Reading the csv file in a dataframe
schools_df = pd.read_csv('Resources/schools_complete.csv')
print(schools_df.head())
print(schools_df.shape)
schools_df= schools_df.reset_index(drop = True)
print(schools_df.head())


# In[4]:


#Merging the two dataframes
students_school_df = pd.merge(students_df, schools_df, how = 'left', left_on = 'school', right_on = 'name',
                              left_index = True)
print(students_school_df.head())
print(students_school_df.shape)


# In[5]:


#Saving the merged dataframe into a csv file
students_school_df.to_csv("Output/students_school.csv")


# In[6]:


def dollar_sign(number):
    # Creates a string of rounded number using previously defined function
    string_round2 = round(number, 2)
    string = str(string_round2)
    # Add dollar sign
    string = '$'+string
    return string


# In[7]:


#District Summary
#Create a high level snapshot (in table form) of the district's key metrics, including:


# In[8]:


schools_district_df= schools_df[schools_df.type == 'District']
schools_district_df = schools_district_df.reset_index(drop = True)
schools_district_df.head()


# In[9]:


students_school_district_df= students_school_df[students_school_df.type== 'District']
students_school_district_df = students_school_district_df.reset_index(drop = True)
students_school_district_df.head()


# In[10]:


#Total Schools
Total_Schools_district = schools_district_df.shape[0]
Total_Schools_district 
#Total_Schools.shape


# In[11]:


#Total Students
Total_Students_district = students_school_district_df.shape[0]
Total_Students_district


# In[12]:


#Total Budget
Total_Budget_district = schools_district_df['budget'].sum()
Total_Budget_district = dollar_sign(Total_Budget_district)
Total_Budget_district


# In[13]:


#Average Math Score
Average_Math_Score_district = students_school_district_df["math_score"].mean()
Average_Math_Score_district


# In[14]:


#Average Reading Score
Average_Reading_Score_district = students_school_district_df["reading_score"].mean()
Average_Reading_Score_district


# In[15]:


#% Passing Math
Passing_Math_district = students_school_district_df[students_school_district_df['math_score'] >=70]
Per_Passing_Math_district = 100*(Passing_Math_district['math_score'].count())/Total_Students_district
Per_Passing_Math_district


# In[16]:


#% Passing Reading
Passing_Reading_district = students_school_district_df[students_school_district_df['reading_score'] >=70]
Per_Passing_Reading_district = 100*(Passing_Reading_district['reading_score'].count())/Total_Students_district
Per_Passing_Reading_district


# In[17]:


#Overall Passing Rate (Average of the above two)
Overall_Passing_Rate_district = (Per_Passing_Math_district+Per_Passing_Reading_district)/2
Overall_Passing_Rate_district


# In[18]:


#District Summary
#Create a high level snapshot (in table form) of the district's key metrics, including:
#Total Schools
#Total Students
#Total Budget
#Average Math Score
#Average Reading Score
#% Passing Math
#% Passing Reading
#Overall Passing Rate (Average of the above two)
district_summary_table = pd.DataFrame({
    "Total_Schools":Total_Schools_district,
    "Total_Students":Total_Students_district,
    "Total_Budget":Total_Budget_district,
    "Average_Math_Score":Average_Math_Score_district,
    "Average_Reading_Score":Average_Reading_Score_district,
    "% Passing_Math":Per_Passing_Math_district,
    "% Passing_Reading":Per_Passing_Reading_district,
    "% Overall_Passing_Rate":Overall_Passing_Rate_district
}, index=[0])

#Reordering column names so they apeear in the order provided
district_summary_table = district_summary_table[["Total_Schools", "Total_Students", "Total_Budget", "Average_Math_Score", 
                          "Average_Reading_Score", "% Passing_Math", "% Passing_Reading",
                           "% Overall_Passing_Rate"]]
district_summary_table


# In[19]:


schools_df.set_index('name', inplace=True)
schools_df.head(2)


# In[20]:


#School Summary
#Create an overview table that summarizes key metrics about each school


# In[21]:


#grouping merged dataframe by school
df_group=students_school_df.groupby("school")
#df_group.head(0)


# In[22]:


#School Name
School_Name = df_group["school"].unique()
#School_Name
#School_Name.shape


# In[23]:


#School Type
School_Type = schools_df["type"]
School_Type
#a= School_Type.tolist()
#a[0]
#type(School_Type)


# In[24]:


#Total Students
Total_Students = df_group["name_x"].count()
Total_Students
#Total_Students.shape


# In[25]:


#Total School Budget
#Total_School_Budget = df_group["budget"].unique()
Total_Budget = schools_df["budget"]
Total_School_Budget = Total_Budget.map(dollar_sign)
Total_School_Budget
#Total_School_Budget.shape


# In[26]:


#Per Student Budget
Per_Budget = Total_Budget/Total_Students
Per_Student_Budget = Per_Budget.map(dollar_sign)
Per_Student_Budget
#Per_Student_Budget.shape


# In[27]:


#Average Math Score
Average_Math_Score = df_group["math_score"].sum()/Total_Students
Average_Math_Score
#Average_Math_Score.shape


# In[28]:


#Average Reading Score
Average_Reading_Score = df_group["reading_score"].sum()/Total_Students
Average_Reading_Score
#Average_Reading_Score.shape


# In[29]:


#% Passing Math
Passing_Math = students_school_df[students_school_df['math_score'] >=70]
Per_Passing_Math = 100*(Passing_Math.groupby('school')['math_score'].count())/Total_Students
Per_Passing_Math
#Per_Passing_Math.shape
#a.shape


# In[30]:


#% Passing Reading
Passing_Reading = students_school_df[students_school_df['reading_score'] >=70]
Per_Passing_Reading = 100*(Passing_Reading.groupby('school')['reading_score'].count())/Total_Students
Per_Passing_Reading
#Per_Passing_Reading.shape


# In[31]:


#Overall Passing Rate (Average of the above two)
Overall_Passing_Rate = (Per_Passing_Math+Per_Passing_Reading)/2
Overall_Passing_Rate
#Overall_Passing_Rate.shape


# In[32]:


# Creating a School Summary table
school_summary_table = pd.DataFrame({
    #"School_Name":School_Name,
    "School_Type":School_Type,
    "Total_Students":Total_Students,
    "Total_School_Budget":Total_School_Budget,
    "Per_Student_Budget":Per_Student_Budget,
    "Average_Math_Score":Average_Math_Score, 
    "Average_Reading_Score":Average_Reading_Score,
    "% Passing_Math":Per_Passing_Math, 
    "% Passing_Reading":Per_Passing_Reading, 
    "% Overall_Passing_Rate":Overall_Passing_Rate})

#Reordering columns so they apeear in the order provided
school_summary_table = school_summary_table[[ "School_Type", "Total_Students", "Total_School_Budget", 
                          "Per_Student_Budget", "Average_Math_Score", "Average_Reading_Score", "% Passing_Math",
                          "% Passing_Reading", "% Overall_Passing_Rate"]]



school_summary_table


# In[33]:


def top_highest(df,col,top = 5):
    list_of_top = df.sort_values(col, ascending=False).head(top)
    return list_of_top


# In[34]:


#Top Performing Schools (By Passing Rate)
#Create a table that highlights the top 5 performing schools based on Overall Passing Rate. Include:


# In[35]:


#top 5 performing schools based on Overall Passing Rate
top_5_performing_school = top_highest(school_summary_table, "% Overall_Passing_Rate")
top_5_performing_school

#Reordering columns so they apeear in the order provided
top_5_performing_school = top_5_performing_school[[ "School_Type", "Total_Students", "Total_School_Budget", 
                          "Per_Student_Budget", "Average_Math_Score", "Average_Reading_Score", "% Passing_Math",
                          "% Passing_Reading", "% Overall_Passing_Rate"]]

top_5_performing_school


# In[36]:


def bottom_lowest(df,col,bottom = 5):
    list_of_bottom = df.sort_values(col, ascending=True).head(bottom)
    return list_of_bottom


# In[37]:


#Bottom Performing Schools (By Passing Rate)
#Create a table that highlights the bottom 5 performing schools based on Overall Passing Rate. Include all of the same metrics as above.
#School Name
#School Type
#Total Students
#Total School Budget
#Per Student Budget
#Average Math Score
#Average Reading Score
#% Passing Math
#% Passing Reading
#Overall Passing Rate (Average of the above two)


# In[38]:


#bottom 5 performing schools based on Overall Passing Rate
bottom_5_performing_school = bottom_lowest(school_summary_table, "% Overall_Passing_Rate", 5)
bottom_5_performing_school

#Reordering columns so they apeear in the order provided
bottom_5_performing_school = bottom_5_performing_school[[ "School_Type", "Total_Students", "Total_School_Budget", 
                          "Per_Student_Budget", "Average_Math_Score", "Average_Reading_Score", "% Passing_Math",
                          "% Passing_Reading", "% Overall_Passing_Rate"]]

bottom_5_performing_school


# In[39]:


#Math Scores by Grade
#Create a table that lists the average Math Score for students of each grade level (9th, 10th, 11th, 12th) 
#at each school.
#9th grade math score
grade_9th= students_school_df[students_school_df['grade'] =='9th']
math_score_9th = grade_9th.groupby("school")["math_score"].mean()
math_score_9th
#10th grade math score
grade_10th= students_school_df[students_school_df['grade'] =='10th']
math_score_10th = grade_10th.groupby("school")["math_score"].mean()
math_score_10th
#11th grade math score
grade_11th= students_school_df[students_school_df['grade'] =='11th']
math_score_11th = grade_11th.groupby("school")["math_score"].mean()
math_score_11th
#12th grade math score
grade_12th= students_school_df[students_school_df['grade'] =='12th']
math_score_12th = grade_12th.groupby("school")["math_score"].mean()
math_score_12th


# In[40]:


#Math Scores by Grade
#Create a table that lists the average Math Score for students of each grade level (9th, 10th, 11th, 12th) 
#at each school.
math_score_summary_table = pd.DataFrame({
    "9th": math_score_9th,
    "10th":math_score_10th,
    "11th":math_score_11th,
    "12th":math_score_12th
   })

#Reordering columns so they apeear in the order provided
math_score_summary_table = math_score_summary_table[["9th", "10th", "11th", "12th"]]

math_score_summary_table


# In[41]:


#Reading Scores by Grade
#Create a table that lists the average Reading Score for students of each grade level (9th, 10th, 11th, 12th) 
#at each school.

#9th grade reading score
reading_score_9th = grade_9th.groupby("school")["reading_score"].mean()
reading_score_9th

reading_score_10th = grade_10th.groupby("school")["reading_score"].mean()
reading_score_10th

#11th grade reading score
reading_score_11th = grade_11th.groupby("school")["reading_score"].mean()
reading_score_11th

#12th grade reading score
reading_score_12th = grade_12th.groupby("school")["reading_score"].mean()
reading_score_12th


# In[42]:


#Reading Scores by Grade
#Create a table that lists the average Math Score for students of each grade level (9th, 10th, 11th, 12th) 
#at each school.
reading_score_summary_table = pd.DataFrame({
    "9th": reading_score_9th,
    "10th":reading_score_10th,
    "11th":reading_score_11th,
    "12th":reading_score_12th
   })

#Reordering columns so they apeear in the order provided
reading_score_summary_table = reading_score_summary_table[["9th", "10th", "11th", "12th"]]

reading_score_summary_table


# In[43]:


#resetting index
#school_summary_table = school_summary_table.reset_index(drop = True)
#school_summary_table.head(2)


# In[44]:


#Scores by School Spending
#Create a table that breaks down school performances based on average Spending Ranges (Per Student). 
#Use 4 reasonable bins to group school spending. Include in the table each of the following:
#Average Math Score
#Average Reading Score
#% Passing Math
#% Passing Reading
#Overall Passing Rate (Average of the above two)


# Create the bins for budget
# Bins are less than 585, 585 to 615, 615 to 645, 645 to 675
bins = [0, 585, 615, 645, 675]

# Create the names for the four bins
group_names = ['<$585', '$585-615', '$615-645', '$645-675']

Scores_by_School_Spending = school_summary_table.loc[:, ["Average_Math_Score", "Average_Reading_Score", "% Passing_Math", 
                                                  "% Passing_Reading", "% Overall_Passing_Rate"]]

# Cut post per student budget and place the scores into bins
Scores_by_School_Spending["Spending Ranges (Per Student)"] = pd.cut(Per_Budget, 
                                                                    bins, labels = group_names)


Scores_by_School_Spending = Scores_by_School_Spending[["Spending Ranges (Per Student)","Average_Math_Score", "Average_Reading_Score", "% Passing_Math", 
                                                  "% Passing_Reading", "% Overall_Passing_Rate"]]
Scores_by_School_Spending = Scores_by_School_Spending.groupby("Spending Ranges (Per Student)").mean()
Scores_by_School_Spending


# In[45]:


#Scores by School Size
#Repeat the above breakdown, but this time group schools based on
#a reasonable approximation of school size (Small, Medium, Large).

#print(school_summary_table["Total_Students"].min())
#print(school_summary_table["Total_Students"].max())

# Create the bins for budget
# Bins are 427, 4976
#0 to 1000, 1000 to 2000, 2000 to 3000, 3000 to 4000, 4000 to 5000
bins = [0, 1000, 2000, 3000, 4000, 5000]

# Create the names for the four bins
group_names = ['Small (<1000)', 'Medium (1000-2000)', 'Big (2000-3000)', 
               'Large (3000-4000)', 'Very Large (4000-5000)']

Scores_by_School_Size = school_summary_table.loc[:, ["Total_Students","Average_Math_Score", "Average_Reading_Score", "% Passing_Math", 
                                                  "% Passing_Reading", "% Overall_Passing_Rate"]]

Scores_by_School_Size["School Size"] = pd.cut(Scores_by_School_Size["Total_Students"], 
                                                                    bins, labels = group_names)

Scores_by_School_Size = Scores_by_School_Size[["School Size","Average_Math_Score", "Average_Reading_Score", "% Passing_Math", 
                                                  "% Passing_Reading", "% Overall_Passing_Rate"]]

Scores_by_School_Size = Scores_by_School_Size.groupby("School Size").mean()
Scores_by_School_Size


# In[46]:


#Scores by School Type
#Repeat the above breakdown, but this time group schools based on school type (Charter vs. District).

# Create the bins for budget
# Bins are ['District', 'Charter']
bins = ['District', 'Charter']

# Create the names for the four bins
group_names = ['District', 'Charter']

Scores_by_School_Type = school_summary_table.loc[:, ["School_Type","Average_Math_Score", "Average_Reading_Score", 
                                              "% Passing_Math", "% Passing_Reading", "% Overall_Passing_Rate"]]

#Scores_by_School_Type["School Type"] = pd.cut(Scores_by_School_Size["School_Type"], 
#                                                                    bins, labels = group_names)

Scores_by_School_Type = Scores_by_School_Type[["School_Type","Average_Math_Score", "Average_Reading_Score", 
                                               "% Passing_Math", "% Passing_Reading", "% Overall_Passing_Rate"]]

#print(Scores_by_School_Type.head(10))
Scores_by_School_Type = Scores_by_School_Type.groupby("School_Type").mean()
Scores_by_School_Type


# In[ ]:


#Analysis
#Looking at top performing school and bottom performing school data - all top performing school are charter school 
#while all bottom performing school are district school.
#There seems to be no relation in terms of school performance and total budget or per student budget.
#There does not seem to be much difference in performance among grades. 
#If a school is good or performs at a certain level, it performs reasonably same from 9th to 12 th grade.
#School size seems to have a negative impact on performance of school; as school size increases performances decreases.

