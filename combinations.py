"""
QUESTION 2
Calculate all permutations of the non-key columns.  Using 100% equal weighting calculate the weighted combination of the non-key columns and the run through the Wilkoxon Signed Rank test.  Note:  This must be coded in Python and should handle any number of columns.  The current example is 1 key product and 5 non-key, but another example could be 1 key product and 3 non-key. Or 8 non-key etc… Additional Note:  Please see the tab titled, "Question2 - Permut & Weights" for additional help with this question.
"""

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
                    column_name='col'+str(non_key_column_names[k])
                    diff_column_name='col'+str(non_key_column_names[k])+'_diff'
                    abs_diff_column_name='col'+str(non_key_column_names[k])+'_abs_diff'
                    rank_column_name='col'+str(non_key_column_names[k])+'_rank'
                    temp_dict[column_name]=temp_list[k]
                    temp_dict[diff_column_name]=0
                    temp_dict[abs_diff_column_name]=0
                    temp_dict[rank_column_name]=0
                    #k=k+1
            #temp_dict={'customer':temp_list[0],'key_product':temp_list[1],'col1':temp_list[2],'col1_diff':0,'col1_abs_diff':0,'rank':0}
            
            myList.append(temp_dict)
        line_count += 1
    print(f'Lines for processing {line_count}.')

del non_key_column_names[0:2]

finalCombinations=[]
for i in range(len(non_key_column_names)):
    if i>0:
        from itertools import combinations
        finalCombinations.extend(list(combinations(non_key_column_names,i+1)))

#print(finalCombinations)        
#calculating weighted average of combinations        
for myCombination in finalCombinations:
    for myDict in myList:
        weighted_score=0;
        weighted_column_name="W"
        for t in myCombination:
            column_name='col'+str(t)
            weighted_score=weighted_score + float(myDict[column_name])
            weighted_column_name=weighted_column_name+"_"+str(t)
        weighted_score= weighted_score / 2
        print(weighted_score)
        print(weighted_column_name)
        myDict[weighted_column_name]=weighted_score
        
"""
Now we have all columns added to our myList which list of dictionary        
From here we can follow the same logic to find Wstats which is followed in wilcoxon_test.py script
"""

        
            
    

        
    