import pandas as pd
import math
import os
import csv
import sys
import time

sys.path.append("../Sorting_Algorithms")
from sorting_algos import merge_sort

def min_heapify(arr, n, i, columns):
    smallest = i
    left = 2*i
    right = 2*i+1

    k=1
    if left<n:
        while k<len(arr[0]):
            
            if(type(arr[left][k])==str and type(arr[smallest][k])==str):
                if(arr[left][k].strip()<arr[smallest][k].strip()):
                    smallest=left
                    break
                elif(arr[left][k].strip()==arr[smallest][k].strip() and k+1<len(arr[0])):
                    k+=1
                    continue
            elif(type(arr[left][k]) == int and type(arr[smallest][k]) == int):
                if(arr[left][k]<arr[smallest][k]):
                    smallest=left
                    break
                elif(arr[left][k]==arr[smallest][k] and k+1<len(arr[0])):
                    k+=1
                    continue
            break
    
    k=1
    if right<n:
        while k<len(arr[0]):
            
            if(type(arr[right][k])==str and type(arr[smallest][k])==str):
                if(arr[right][k].strip()<arr[smallest][k].strip()):
                    smallest=right
                    break
                elif(arr[right][k].strip()==arr[smallest][k].strip() and k+1<len(arr[0])):
                    k+=1
                    continue
            elif(type(arr[right][k]) == int and type(arr[smallest][k]) == int):
                if(arr[right][k]<arr[smallest][k]):
                    smallest=right
                    break
                elif(arr[right][k]==arr[smallest][k] and k+1<len(arr[0])):
                    k+=1
                    continue
            break
    
    if smallest!=i:
        temp=arr[i]
        arr[i]=arr[smallest]
        arr[smallest]=temp
        min_heapify(arr,n,smallest,columns)

def max_heap(arr, n, i, columns):
    """
    arr: the input array that represents the binary heap
    n: The number of elements in the array
    i: i is the index of the node to be processed
    columns: The columns to be used for comparison

    The max_heapify function is used to maintain the max heap property
    in a binary heap. It takes as input a binary heap stored in an array,
    and an index i in the array, and ensures that the subtree rooted at
    index i is a max heap.
    """
    largest = i
    left = 2*i
    right = 2*i+1

    k=1
    if left<n:
        while k<len(arr[0]):
            
            if(type(arr[left][k])==str and type(arr[largest][k])==str):
                if(arr[left][k].strip()>arr[largest][k].strip()):
                    largest=left
                    break
                elif(arr[left][k].strip()==arr[largest][k].strip() and k+1<len(arr[0])):
                    k+=1
                    continue
            elif(type(arr[left][k]) == int and type(arr[largest][k]) == int):
                if(arr[left][k]>arr[largest][k]):
                    largest=left
                    break
                elif(arr[left][k]==arr[largest][k] and k+1<len(arr[0])):
                    k+=1
                    continue
            break
    
    k=1
    if right<n:
        while k<len(arr[0]):
            
            if(type(arr[right][k])==str and type(arr[largest][k])==str):
                if(arr[right][k].strip()>arr[largest][k].strip()):
                    largest=right
                    break
                elif(arr[right][k].strip()==arr[largest][k].strip() and k+1<len(arr[0])):
                    k+=1
                    continue
            elif(type(arr[right][k]) == int and type(arr[largest][k]) == int):
                if(arr[right][k]>arr[largest][k]):
                    largest=right
                    break
                elif(arr[right][k]==arr[largest][k] and k+1<len(arr[0])):
                    k+=1
                    continue
            break
    
    if largest!=i:
        temp=arr[i]
        arr[i]=arr[largest]
        arr[largest]=temp
        max_heap(arr,n,largest,columns)

def build_heap(arr, n, i, columns):

    for i in range(n//2-1,-1,-1):
        max_heap(arr,n,i,columns)

def min_heap_sort(arr, columns):

    n=len(arr)
    build_heap(arr,n,0,columns)
    for i in range(n-1,0,-1):
        temp = arr[i]
        arr[i] = arr[0]
        arr[0] = temp
        max_heap(arr,i,0,columns)

    #return Sorted array
    return arr

column_names= ['tconst', 'primaryTitle', 'originalTitle', 'startYear',
               'runtimeMinutes', 'genres', 'averageRating', 'numVotes', 'ordering',
               'category', 'job', 'seasonNumber', 'episodeNumber', 'primaryName', 'birthYear',
               'deathYear', 'primaryProfession']

####################################################################################
# Donot Modify this Code
####################################################################################
class FixedSizeList(list):
    def __init__(self, size):
        self.max_size = size

    def append(self, item):
        if len(self) >= self.max_size:
            raise Exception("Cannot add item. List is full.")
        else:
            super().append(item)

####################################################################################
# Mystery_Function
####################################################################################
def Mystery_Function(file_path, memory_limitation, columns):
    """
    # file_path :  file_path for Individual Folder (datatype : String)
    # memory_limitation : At each time how many records from the dataframe can be loaded (datatype : integer : 2000)
    # columns : the columns on which dataset needs to be sorted (datatype : list of strings)
    # Load the 2000 chunck of data every time into Data Structure called List of Sublists which is named as "chuncks_2000"
    # **NOTE : In this Mystery_Function records are accessed from only the folder Individual.

    #Store all the output files in Folder named "Final".
    #The below Syntax will help you to store the sorted files :
                # name_of_csv = "Final/Sorted_" + str(i + 1)
                # sorted_df.reset_index(drop=True).to_csv(name_of_csv, index=False)
    #Output csv files must be named in the format Sorted_1, Sorted_2,...., Sorted_93
    # ***NOTE : Every output csv file must have 2000 sorted records except for the last ouput csv file which might have less
                #than 2000 records.
    """

    #Need to Code
    #Helps to Sort all the 1,84,265 rows with limitation.
    #Load the 2000 chunck of data every time into Data Structure called List of Sublists which is named as "chuncks_2000"
    chuncks_2000=FixedSizeList(2000)

    column_indxes = [0]
    for i in columns:
        column_indxes.append(column_names.index(i))
    
    skip=0
    n_files=len(os.listdir(file_path))
    m=memory_limitation//n_files
    df=pd.DataFrame()
    for i in range(1,n_files+1):
        temp=pd.read_csv(file_path+'/Sorted_'+str(i)+'.csv',skiprows=skip,nrows=m)
        df=pd.concat([df,temp])
    
    skip=m
    map_skip={}
    for i in range(1,n_files):
        map_skip[str(i)]=[skip, memory_limitation]
    i=n_files
    last_file_length=len(pd.read_csv(file_path+'/Sorted_'+str(i)+'.csv'))
    map_skip[str(i)]=[skip,last_file_length]

    i=1
    count=1
        
    chuncks_2000=df.values.tolist()
    for j in range(0,len(chuncks_2000)):
        chuncks_2000[j][0]=str(i)+(chuncks_2000[j][0]).strip()
        if(count==m):
            count=1
            i+=1
            continue
        count+=1
    chuncks_2000=min_heap_sort(chuncks_2000,column_indxes)
    
    flag=True
    i=1

    name_of_csv = "Final/Sorted_1.csv"
    pd.DataFrame(columns=['tconst']+columns).reset_index(drop=True).to_csv(name_of_csv,index=False)
    while flag:
        
        file_idx=chuncks_2000[0][0].split('tt')[0]
        skip=map_skip.get(file_idx)[0]
        chuncks_2000[0][0]='tt'+chuncks_2000[0][0].split('tt')[1]
        sorted_df=pd.DataFrame([chuncks_2000[0]])
        df=pd.read_csv(name_of_csv)
        if(not df.empty and (df.shape[0]==memory_limitation)):
            i+=1
        name_of_csv = "Final/Sorted_" + str(i) +'.csv'
        sorted_df.to_csv(name_of_csv, mode='a', index=False, header=False)

        if(skip<map_skip.get(file_idx)[1]):
            df=pd.read_csv(file_path+'/Sorted_'+str(file_idx)+'.csv',skiprows=skip,nrows=1)
            chuncks_2000[0]=df.values.tolist()[0]
            chuncks_2000[0][0]=file_idx+(chuncks_2000[0][0]).strip()
            map_skip.get(file_idx)[0]=skip+1
            
        else:
            del chuncks_2000[0]
            chuncks_2000=min_heap_sort(chuncks_2000,column_indxes)
        if(len(chuncks_2000)==0):
            break
        min_heapify(chuncks_2000,len(chuncks_2000),0,column_indxes)



####################################################################################
# Data Chuncks
####################################################################################
def data_chuncks(file_path, columns, memory_limitation):
        """
        # file_path : dataset file_path for imdb_dataset.csv (datatype : String)
        # columns : the columns on which dataset needs to be sorted (datatype : list of strings)
        # memory_limitation : At each time how many records from the dataframe can be loaded (datatype : integer)
        # Load the 2000 chunck of data every time into Data Structure called List of Sublists which is named as "chuncks_2000"
        # NOTE : This data_chuncks function uses the records from imdb_dataset. Only 2000 records needs to be loaded at a
                # Time in order to process for sorting using merge sort algorithm. After sorting 2000 records immediately
                # Store those 2000 sorted records into Floder named Individual by following Naming pattern given below.
        #Store all the output files in Folder named "Individual".
        #Output csv files must be named in the format Sorted_1, Sorted_2,...., Sorted_93
        #The below Syntax will help you to store the sorted files :
                    # name_of_csv = "Individual/Sorted_" + str(i + 1)
                    # sorted_df.reset_index(drop=True).to_csv(name_of_csv, index=False)

        # ***NOTE : Every output csv file must have 2000 sorted records except for the last ouput csv file which
                    might have less than 2000 records.

        Description:
        This code reads a CSV file, separates the data into chunks of data defined by the memory_limitation parameter,
        sorts each chunk of data by the specified columns using the merge_sort algorithm, and saves each sorted chunk
        as a separate CSV file. The chunk sets are determined by the number of rows in the file divided by the
        memory_limitation. The names of the sorted files are stored as "Individual/Sorted_" followed by a number
        starting from 1.
        """
        #Load the 2000 chunck of data every time into Data Structure called List of Sublists which is named as "chuncks_2000"
        chuncks_2000=FixedSizeList(2000)
        column_indxes = [0]
        for i in columns:
            column_indxes.append(column_names.index(i))
        #Write code for Extracting only 2000 records at a time from imdb_dataset.csv
        skiprecords=0
        i=0
        flag=True
        while flag:
            chuncks_2000=pd.read_csv(file_path,skiprows=skiprecords,nrows=memory_limitation)
            
            if chuncks_2000.shape[0]!=memory_limitation:
                flag=False

            chuncks_2000=chuncks_2000.values.tolist()
            #Passing the 2000 Extracted Records and Columns indices for sorting the data
            #column_indxes are Extracted from the imdb_dataset indices by mapping the columns need to sort on which are
            #passed from the testcases.
            chuncks_2000=merge_sort(chuncks_2000,column_indxes)

            sorted_df=pd.DataFrame(chuncks_2000,columns=column_names)
            sorted_df=sorted_df.iloc[:,column_indxes]
            name_of_csv = "Individual/Sorted_" + str(i + 1) + '.csv'
            sorted_df.reset_index(drop=True).to_csv(name_of_csv, index=False)

            skiprecords+=memory_limitation
            i+=1


#Enable only one Function each from data_chuncks and Mystery_Function at a time

#Test Case 13
data_chuncks('imdb_dataset.csv', ['startYear'], 2000)

#Test Case 14
#data_chuncks('imdb_dataset.csv', ['primaryTitle'], 2000)

#Test Case 15
#data_chuncks('imdb_dataset.csv', ['startYear','runtimeMinutes' ,'primaryTitle'], 2000)


#Test Case 13
Mystery_Function("Individual", 2000, ['startYear'])

#Test Case 14
#Mystery_Function("Individual", 2000, ['primaryTitle'])

#Test Case 15
#Mystery_Function("Individual", 2000, ['startYear','runtimeMinutes' ,'primaryTitle'])
