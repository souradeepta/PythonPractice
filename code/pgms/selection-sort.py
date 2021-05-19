from typing import List

def selection_sort(input: List):
    length = len(input)
    if length < 1:
        return None
    
    for i in range(length - 1):
        min_index  = i
        
        for j in range( i+1, length - 1):
            if input[j] < input[min_index]:
                min_index = j
        
        input[i], input[min_index] = input[min_index], input[i]
            
    return input

def main():
    sample = [7,4,5,1,0,9,1,4]
    result = selection_sort(sample)
    print(f"output is: {result}")
    
if __name__ =="__main__":
    main()
    
    
            
            