# PythonPractice
PracticingPython


#### TIL
1. Python alphanumeric function implementation is ````str.islanum()```
2. Python list comprehension expression ````new_list = [expression for member in iterable (if conditional)]````
eg. ````alpha_num = [x.lower() for x in list if x.isalnum()]````
3. Python lambda expresssion ````lambda arguments: expression````
eg. `````double = lambda x: x * 2````
4. ASCII value for A is 65 and a is 97 with a "'space" of 32. Also ASCII value for space is 32.
5. ASCII value for 0 is 48. 48-32 = 16. In computer evolution 32-bit models replaced 16-bit ones. [https://www.computerhistory.org/timeline/computers/]
6. Map blueprint ```map(function_to_apply, list_of_inputs)```
eg. ````squared = list(map(lambda x: x**2, items))``
eg. ````less_than_zero = list(filter(lambda x: x < 0, number_list))`
eg. `````from functools import reduce```` 
````product = reduce((lambda x, y: x * y), [1, 2, 3, 4])````
7. Decrementing for loop achieved with -1 step ````ans = [x for x in range(5,0, -1)]````
8. Integers within the 32-bit signed integer range: [−2**31,  2**31 − 1]
9. middle value for divide and conquer should be ```middle = low + (high - low)//2`` [https://ai.googleblog.com/2006/06/extra-extra-read-all-about-it-nearly.html]
10. https://systemdesignprimer.com/
11. In Java, array copy is

Simple Array:
````
String[] array = new String[] {"John", "Mary", "Bob"};
System.out.println(Arrays.toString(array));
````
Output:
````
[John, Mary, Bob]
````
Nested Array:
````
String[][] deepArray = new String[][] {{"John", "Mary"}, {"Alice", "Bob"}};
System.out.println(Arrays.toString(deepArray));
//output: [[Ljava.lang.String;@106d69c, [Ljava.lang.String;@52e922]
System.out.println(Arrays.deepToString(deepArray));
````
Output:
````
[[John, Mary], [Alice, Bob]]
````
12. In java, array copy is using
`````public static void arraycopy(Object src, int srcPos, Object dest, int destPos, int length)```