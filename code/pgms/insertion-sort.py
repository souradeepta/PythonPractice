from typing import List

def insertion_sort(input: List):
    length = len(input)
    
    for step in range(1, length):
        key = input[step]
        
        j = step - 1
        
        while j >= 0 and key < input[j]:
            input[j+1] = input[j]
            j = j - 1
            
        input[j+1] = key        
    
    return input
    
def main():
    sample = [7,4,5,1,0,9,1,4]
    result = insertion_sort(sample)
    print(f"output is: {result}")
    
if __name__ =="__main__":
    main()