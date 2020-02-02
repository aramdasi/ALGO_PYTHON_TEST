# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 12:38:28 2020
@author: JAY GANESH
"""
"""
Function to Generate Rank
"""
def generate_rank(A): 
      
    # create rank vector 
    R = [0 for i in range(len(A))] 
  
    # Create an auxiliary array of tuples 
    # Each tuple stores the data as well 
    # as its index in A 
    T = [(A[i], i) for i in range(len(A))] 
  
    # T[][0] is the data and T[][1] is 
    # the index of data in A 
  
    # Sort T according to first element 
    T.sort(key=lambda x: x[0]) 
  
    (rank, n, i) = (1, 1, 0) 
  
    while i < len(A): 
        j = i 
  
        # Get no of elements with equal rank 
        while j < len(A) - 1 and T[j][0] == T[j + 1][0]: 
            j += 1
        n = j - i + 1
  
        for j in range(n): 
  
            # For each equal element use formula 
            # obtain index of T[i+j][0] in A 
            idx = T[i+j][1] 
            R[idx] = rank + (n - 1) * 0.5
  
        # Increment rank and i 
        rank += n 
        i += n 
  
    return R 


myList=[]
non_key_column_names=[]
Wstat_matrix=[]
"""
Opening the file in read mode
"""
with open('Algo_Test.csv', mode='r') as csv_file:
    line_count = 0
    for row in csv_file:
        if line_count == 0:
            temp_list=row.split(',')
            #reading the header and making non_key_columns
            for temp in temp_list:
                non_key_column_names.append(temp.rstrip())
            #print("No Of columns :",len(temp_list))
            print("Key Product :",non_key_column_names[1])
            line_count += 1
        #print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
        else:            
            temp_list=row.split(',');            
            """
            Creating temp dictionary for further calculation along with new extra columns like diff, abs_diff, rank
            """
            
            temp_dict={'customer':temp_list[0],'key_product':temp_list[1]}
            #print("Length",len(non_key_column_names))
            #k=2;
            for k in range(len(non_key_column_names)):
                if k>1:
                    column_name='col'+str(k)
                    diff_column_name='col'+str(k)+'_diff'
                    abs_diff_column_name='col'+str(k)+'_abs_diff'
                    rank_column_name='col'+str(k)+'_rank'
                    temp_dict[column_name]=temp_list[k]
                    temp_dict[diff_column_name]=0
                    temp_dict[abs_diff_column_name]=0
                    temp_dict[rank_column_name]=0
                    #k=k+1
            #temp_dict={'customer':temp_list[0],'key_product':temp_list[1],'col1':temp_list[2],'col1_diff':0,'col1_abs_diff':0,'rank':0}
            
            myList.append(temp_dict)
        line_count += 1
    print(f'Lines for processing {line_count}.')

#print(non_key_column_names)


#print(myList)
    """
    For Each dictionary in List
        First try to get the difference, absulute difference and save it back to dictionary
    """
for myDict in myList:
    #print(myDict.get("customer"))
      for i in range(len(non_key_column_names)):
                if i>1:
                    column_name='col'+str(i)
                    diff_column_name='col'+str(i)+'_diff'
                    abs_diff_column_name='col'+str(i)+'_abs_diff'
                    rank_column_name='col'+str(i)+'_rank'
                    difference=float(myDict[column_name]) - float(myDict.get("key_product"))
                    myDict[diff_column_name]=difference
                    myDict[abs_diff_column_name]=abs(difference)
    
"""for myDict in myList:
    print(myDict)
"""    
#logic for sorting and finding rank for each column added
#for myDict in myList:
    #print(myDict.get("customer"))
"""
For each non key columns
    Sort the list based on abs difference
    Send this list to generate_rank method to generate rank
    Save ranks back in dictionary
    Calculate T Positive, T Negative and finally Wstat (W Test Statics)
    Save WStat to Wstat_Matrix
"""
for i in range(len(non_key_column_names)):
          if i>1:
              #print("Counter",i)
              #print("Checking for Column",non_key_column_names[i])
              column_name='col'+str(i)
              diff_column_name='col'+str(i)+'_diff'
              abs_diff_column_name='col'+str(i)+'_abs_diff'
              rank_column_name='col'+str(i)+'_rank'
              mySortedList=sorted(myList, key=lambda i:(float(i[abs_diff_column_name])))
              listforrank=[]
              
              for mySortedDict in mySortedList:
                  listforrank.append(mySortedDict[abs_diff_column_name])
                  
              rankList=generate_rank(listforrank)
              m=0
              for mySortedDict in mySortedList:
                  mySortedDict[rank_column_name]=rankList[m]
                  m=m+1
              # calculating T+ & T- sum
              T_pos=sum(myDict[rank_column_name] for myDict in myList if myDict[diff_column_name]>=0)
              T_neg=sum(myDict[rank_column_name] for myDict in myList if myDict[diff_column_name]<0)
             # print("T Positive",T_pos)
             # print("T Negative",T_neg)
              w_stat=min(T_pos,T_neg)
             # print("Wstat",w_stat)
              wstatDict={"Column Name":non_key_column_names[i],"T Positive":T_pos,"T Negative":T_neg,"Wstat":w_stat}
              Wstat_matrix.append(wstatDict)


"""
Display Final Output
"""
#Final Output
for wstatDict in Wstat_matrix:
    print(wstatDict)                    
    
