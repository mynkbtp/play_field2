import statistics as st
import pandas as pd
import csv
import re
from wordcloud import wordcloud, WordCloud
import matplotlib.pyplot as plt
from PIL import Image


#Last_date_Modification: August 3,2019
#Author: Mayank Chaturvedi_M.Tech_Yr1
#csv_file_used: NBA.csv
#csv_file_description: Records of NBA Players-their Names,Team,Age,Weight,Salary

list1=[]
list2=[]
list3=[]
list4=[]

with open("NBA.csv", mode="r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for lines in csv_reader:
      #print(lines[0])
      list1.append(lines[0])
      list2.append(lines[1])
      list3.append(lines[2])
      list4.append(lines[3])

print(list1[:10])
del(list1[0],list2[0],list3[0],list4[0])
print("--------------------------$$$$$------------")
print(list2[:10])
#print(type(list2[0]))

wrd_count={}

res_dic={}

#def mean_calc(int_val):


def int_dtype_check(str2):

    reg1=re.compile("\d+")
    match_check1=reg1.match(str2)
    if(match_check1):
        return("INT")
    else:
        return("NOT_INT")



def str_dtype_check(str1):
    regex = re.compile("[A-Z]+|[a-z]+|\W+")
    match_check = regex.match(str1)

    if (match_check):
        return("STR")
        #res_dic[list1[i]] = "STR"

    else:
        return(int_dtype_check(str1))

def mean_calc(val_list):
    return(st.mean(val_list))



for i in range(len(list1)):
    print(list1[i],"\n")

    ret_val=str_dtype_check(list1[i])
    print(ret_val)
                #regex=re.compile("[A-Z]+|[a-z]+|\W+")
                 #match_check=regex.match(list1[i])

                            #if(match_check):
    res_dic[list1[i]]=ret_val
       # wrd_split=list1[i].split
    for i in range(len(list1)):
        wrd_count[i]=len(list1[i].split())


#---------------------------------------column1 done-------------------
res_disc1={}
list2_int=[]
int_cnt=0
for i in range(len(list2)):
    print(">",list2[i],"\n")

    ret_val1=str_dtype_check(list2[i])
    print(ret_val1)
                #regex=re.compile("[A-Z]+|[a-z]+|\W+")
                 #match_check=regex.match(list1[i])

                            #if(match_check):
    res_disc1[list2[i]]=ret_val1

       # wrd_split=list1[i].split

for i in range(len(res_disc1)):
    if(res_disc1[list2[i]]=="INT"):
        int_cnt=int_cnt+1
if(int_cnt==len(res_disc1)):  #** ***** comaparing whether all keys have equal number of INT value as thr number of records
                              # ie checking whether all the records are int or not--> if yes, we will take the mean ****** **
        print("All data is in INTeger")
        list2_int=[int(i) for i in list2]

#calculating mean
print(list2_int)
mean1=mean_calc(list2_int)
print(">>>>>>>>>>>>>>>>MEan value _column1")
print(mean1,"\n\n")




#---------------------------------------column2 done-------------------
print(list1[:10],"\n")

print(">>>-------------------------------------------Result_dictionary--DATA_TYPE against each Row entry-------------------------------------- :\n")
print(res_dic,"\n")


total_sentnce_wrds={}
print(list1[0].split())

print("------------------------")
print(len(list1),"entries")
print("-------------------------------------word_count_dictionary____ Each key_entry indicate one cell entry in string column------------------------------------------\n\n")

print(wrd_count,"\n")
print("------------------------------------------------------------------------------------DATAFRAMES---------------------------------------------------------------------------------------------------")
#Word_Count=[]
#for i in range(len(wrd_count)):
 #    Word_Count=wrd_count[i]
#print(Word_Count)





df=pd.DataFrame(list1,columns=["Player_Details"])
print(df)

final_wrd_count=[]
for i in range(len(wrd_count)):
    temp=wrd_count[i]
    final_wrd_count.append(temp)

#print("final_wrd_count---------->")
#print(final_wrd_count)

df.insert(1,"Word_Count",final_wrd_count,True)
print(df)

#ALREADY CHECKED ABOVE THAT ALL COLUMNS ENTRIES ARE PRESENT
print("--------------------Weights Columns DataFrame--------------------")
df1=pd.DataFrame(list2_int,columns=["Weights"])
print(df1)
print("Mean:")
print(df1.mean())


list3_int = [int(i) for i in list3]
print("-----------------------Age Column Dataframe----------")
df2=pd.DataFrame(list3_int,columns=["Age"])
print(df2)
print("Mean:")
print(df2.mean())

#print(list4)

#cHECKING IF ANY ENTRY IS BLANK OR NOT
for i in range(len(list4)):
    if(list4[i]==''):
        #print(i,"-->",list4[i])
        list4[i]=0


list4_int = [int(i) for i in list4]
print("-----------------------Salary Column Dataframe----------")
df3=pd.DataFrame(list4_int,columns=["Salary"])
print(df3)
print("Mean:")
print(df3.mean())


#print("------------------------------------->list1-----------------")
#print(list1)
sentence=list1[0]
#print("----------------------sentence for wordcloud (testing)")
#print(sentence)
for i in range(20):
   sentence=sentence+list1[i]
print("----------------------sentence for wordcloud (final)")
print(sentence)




word_cloud = WordCloud( max_font_size=50, max_words=180,background_color = "cyan").generate(sentence)

plt.imshow(word_cloud)
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()



