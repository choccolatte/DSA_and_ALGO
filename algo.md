# DSA

## algorithm
- a set of steps a program takes to finish a task. 
- understanding when to apply a certain algo  requires properly understanding the problem at hand.
- if you have a problem, an algorithm is a set of steps that solves that problem. 

## algorithmic thinking - 
- quickly establish the bounds/rules of the problem when you are stuck/asked a problem. No solution works on every problem. 
- So, an important part of algorithmic thinking is, to clearly define what the problem set is, and clarify what values count as inputs.  
- there is no best solution to a problem. What you should focus on is to figure out what solution would be the best for the problem at hand. 
- when you encounter a problem, before rushing in and thinking of a solution, what you want to do is work through the guidelines. What you want to do is break down the problem into any possible number of smaller problems where each problem can be clearly defined in terms of input and output. 

## Guidelines for an algorithm - 
- Clearly defined Problem Statement, input and output. 
- The steps in the algorithm must be in a very specific order, it should have a specific set of instructions in a particular order.
- each guideline/rule shouldnt be complex, it should be explicitly clear - the steps also need to be distinct.
- algorithm should produce a result.
- algorithm should actually complete and not take an infinite amount of time - it should complete in a finite amount of time. 

## Time Complexity & Space Complexity - 
- time complexity basically means the time it takes for an algo to finish a task. Best case - 1, worst case - n.
- space complexity means the space it takes for the algo on RAM (or the space it occupies) to run and complete its task. The best case here would be for an algo to take as less of space as possible to complete its task so that other running programs dont get hampered. 


## Linear Search - 
- takes as much time as there are elements to go over - n-times.
	- best case runtime - 1
	- avg case runtime - n/2
	- worst case runtime - n

# DSA

- Data Structures is about how data can be stored in different structures.

- Algorithms is about how to solve different problems, often by searching through and manipulating data structures.

- Theory about Data Structures and Algorithms (DSA) helps us to use large amounts of data to solve problems efficiently.


## Data Structures

A data structure is a way to store data. We structure data in different ways depending on what data we have, and what we want to do with it.

First, let's consider an example without computers in mind, just to get the idea.

If we want to store data about people we are related to, we use a family tree as the data structure. We choose a family tree as the data structure because we have information about people we are related to and how they are related, and we want an overview so that we can easily find a specific family member, several generations back.

With such a family tree data structure visually in front of you, it is easy to see, for example, who my mother's mother is—it is 'Emma,' right? But without the links from child to parents that this data structure provides, it would be difficult to determine how the individuals are related.

Data structures give us the possibility to manage large amounts of data efficiently for uses such as large databases and internet indexing services.

Data structures are essential ingredients in creating fast and powerful algorithms. They help in managing and organizing data, reduce complexity, and increase efficiency.

Types of data structures -
**Primitive Data Structures** are basic data structures provided by programming languages to represent single values, such as integers, floating-point numbers, characters, and booleans.

**Abstract Data Structures** are higher-level data structures that are built using primitive data types and provide more complex and specialized operations. Some common examples of abstract data structures include arrays, linked lists, stacks, queues, trees, and graphs.


## Algorithms

An algorithm is a set of step-by-step instructions to solve a given problem or achieve a specific goal.

A cooking recipe written on a piece of paper is an example of an algorithm, where the goal is to make a certain dinner. The steps needed to make a specific dinner are described exactly.

When we talk about algorithms in Computer Science, the step-by-step instructions are written in a programming language, and instead of food ingredients, an algorithm uses data structures.

Algorithms are fundamental to computer programming as they provide step-by-step instructions for executing tasks. An efficient algorithm can help us to find the solution we are looking for, and to transform a slow program into a faster one.

By studying algorithms, developers can write better programs.

Algorithm examples:

- Finding the fastest route in a GPS navigation system
- Navigating an airplane or a car (cruise control)
- Finding what users search for (search engine)
- Sorting, for example sorting movies by rating

The algorithms we will look at in this tutorial are designed to solve specific problems, and are often made to work on specific data structures. For example, the 'Bubble Sort' algorithm is designed to sort values, and is made to work on arrays.


Data structures and algorithms (DSA) go hand in hand. A data structure is not worth much if you cannot search through it or manipulate it efficiently using algorithms, and the algorithms in this tutorial are not worth much without a data structure to work on.

DSA is about finding efficient ways to store and retrieve data, to perform operations on data, and to solve specific problems.

By understanding DSA, you can:

- Decide which data structure or algorithm is best for a given situation.
- Make programs that run faster or use less memory.
- Understand how to approach complex problems and solve them in a systematic way.


## Terminology

Algorithm - A set of step-by-step instructions to solve a specific problem.

Data Structure - A way of organizing data so it can be used efficiently. Common data structures include arrays, linked lists, and binary trees.

Time Complexity - A measure of the amount of time an algorithm takes to run, depending on the amount of data the algorithm is working on.

Space Complexity - A measure of the amount of memory an algorithm uses, depending on the amount of data the algorithm is working on.

Big O Notation - A mathematical notation that describes the limiting behavior of a function when the argument tends towards a particular value or infinity. Used in this tutorial to describe the time complexity of an algorithm.

Recursion - A programming technique where a function calls itself.

Divide and Conquer - A method of solving complex problems by breaking them into smaller, more manageable sub-problems, solving the sub-problems, and combining the solutions. Recursion is often used when using this method in an algorithm.

Brute Force - A simple and straight forward way an algorithm can work by simply trying all possible solutions and then choosing the best one.


## A simple Algorithm

### Fibonacci No Algo

- to generate a fib number, all we need to do is add two previous Fib numbers.
- since we already know what the next number will be (current no + prev no = next no), we can write an algo to create as many fib no as possible.

- algo first 20 fib numbers
    - start with the two first fib numbers 0 and 1
        - add the two previous numbers together to create a new Fib number.
        - update the value of the two prev numbers.
    -  do point a and b 18 times.

#### using loops vs recursion

- we will implement fib numbers using for loop
- we will implement fib numbers using recursion - function calling function
- finding nth fib number using recursion


**using for loop**

- here's what the code must contain - 
    - two variables to hold the previous two Fib numbers
    - a for loop that runs 18 times
    - create new fib numbers by adding the two previous one
    - print the new fib numbers
    - update the variables that hold the previous two fib numbers


**using for loop**
`
a = 0
b = 1

print (a)
print (b)

for fib in range(18):
    newFib = a + b
    print (newFib)
    b = a
    a = newFib
` 

**using recursion**

- recursion is a function calling itself.
- to implement the Fib algo, we need most of the same thigns as the for loop example above, but we also need to replace the for loop with recursion.
- to replace the for loop with recursion, we need to encapsulate much of the code in a functioin, and we need the function to call itself to create a new Fib number as long as the produced number of Fib numbers is below, or equal to 25.

`
print(0)
print(1)
count = 2

def fib(prev1, prev2):
    if count <=25:
        newFib = prev1 + prev2
        print (newFib)
        prev2 = prev1
        prev1 = newFib
        count += 1
        fib(prev1, prev2)

    else:
        return

fib(0, 1)     
`

**finding nth fibonacci number using recursion**

- to find the nth fibonacci number, we cna write a code based on the maths formula for Fibonacci number - 
    F(n) = F(n - 1) + F(n-2)

- this just means that for example the 10th fib number is the sun of 9th and 8th fib numbers.

- when using this concept with recursion, we can let the function call itself as long as n is less than, or equal to 1. If n <=1, then it means that the code execution has reached one of the first two Fib numbers 1 or 2.

- the code will look like this -  
`
def F(n):
    if n <= 1:
        return n
    else:
        return F(n-1) + f(n-2)

print(F(20)) #calling function
`

- here, the recursion we wrote calls itself twice - this means that the number of function calls will double every time we increase the Fib number we want by one.
- here, two things to note, the amount of function calls and the amount of times the function is called with the same arguments.
- so, even though the code is fascinating and shows how recursion works, but the actual code execution is slow and ineffective to use for creating large Fib numbers. 


## DSA Arrays

- arrays are data structures used to store multiple elements.
- they are used in algorithms.
- example, an algo can be used to look through an array to find the lowest value.
- example in py
`
array_new=[1, 2, 3, 4, 5, 6, 7, 8, 9]
`
- note that the above code will generate a list in python, list is a data type in py, but here, it can also be used in the same way as an array.

**array properties**

- arrays are indexed, meaning that each element in the array has an index number that says where in the array the elelment is located. Py used 0-based indexing in arrays, meaning it starts from 0.

- so, when you want to access an item from the array, we do this - 
`
print(array_new[2]) #will give value of item at index 2 => 3 
`

### Algo - finding the lowest value in an array

- pseudocode for the above algo 
    - go through the values in the array one by one
    - check if the current value is the lowest so far, and if it is, then store it
    - after looking at all the values, the stored value will be the lowest of all values in the array.

**Implementation**

- before we implement the algo using an actual programming language, we should write the algo as a step-by-step procedure.
- here, we would have to write the algo in something between a human language and programming language, the algorithm will be easier to implement later because we avoid drowning in all the details of the programming language syntax.

- **pseudo code**
    - create a variable 'minVal' and set its value equal to the first value of the array
    - go through every element in the array
    - if the current element has a lower value than 'minval', update minval with the new lower value
    - after looking at all the elements in the array, the 'minVal' variable now contains the lowest value.

- writing the algo in a more programming language like way using the above pseudo code - 
    - Variable 'minVal' = array[0]
    - for each element in the array:
        - if current element < minVal:
            - minVal = current element

- now we code -
`
my_arr=[1, 2, 22, 312, 121, 23, 456, 45656, 23424342, 2121, 0, 1, 2, 3, 45, 65]
minVal=my_arr[0] #step 1

for i in my my_arr: #step 2
    if i < minVal: #step 3
        minVal = i #step 4 - update value

print('lowest value in array: ', minVal) #step5, printing

`

### Algorithm Time Complexity

- When exploring algorithms, we often look at how much time an algorithm takes to run relative to the size of the data set.

- in our example above, the time the algorithm needs to run is proportional, or linear, to the size of the data set. This is becasue the algorithm must visit every array element one time to find the lowerst value. the loop must run 5 times since there are 5 values inthe array. and if the array had 1000 values, the loop would have to run 1000 times - in other words - the more values there are in the array, the more time it will take for the loop to run. 


## Bubble Sort

- bubble sort is an algorithm that sorts an array from the loweest value to the highest value.

- the word 'bubble' comes from how this algorithm works, it makes the highest values 'bubble up' and then sent to back, the smaller values pushed forward.

- **how it works?**

- 1. go through the array, one value at a time.
- 2. for each value, compare the value with the next value.
- 3. if the value is higher than the next one, swap the values so that the highest value comes last.
- 4. go through the array as many times as there are values in the array.

**Manual Run Through**

- before we implement the Bubble Sort Algo in a programming language, we will manually run through a short array only one time, just to get the idea.

    1. We start with an unsorted array.
`
[7, 12, 9, 11, 3]

`
    2. We look at the first two values. Does the lowest value come first? Yes, so we dont need to swap them.
`
[7, 12, 9, 11, 3]

`
    3. Take one step forward and look at values 12 adn 9. Does the lowest value come first? No.
`
[7, 12, 9, 11, 3]

`
    4. So, we need to swap them so that 9 comes first.
`
[7, 9, 12, 11, 3]

`
5. Taking one step forward, looking at 12 and 11.
`
[7, 9, 12, 11, 3]

`
6. We must swap so that 11 comes before 12.
`
[7, 9, 11, 12, 3]

`
7. Looking at 12 and 3, do we need to swap them? Yes.
`
[7, 9, 11, 12, 3]

`
8. Swapping 12 and 3 so that 3 comes first.
`
[7, 9, 11, 3, 12]

`

- is it fully sorted? No. How do we solve this? What could we have done more to fully sort it?
- We must understand what happened in this first run through to fully understand the algorithm, so that we can implement the algorithm in a programming language.
- Can you see what happened to the highest value 12? It has bubbled up to the end of the array, where it belongs. But the rest of the array remains unsorted.
- So the Bubble Sort algorithm must run through the array again, and again, and again, each time the next highest value bubbles up to its correct position. The sorting continues until the lowest value 3 is left at the start of the array. This means that we need to run through the array 4 times, to sort the array of 5 values.
- And each time the algorithm runs through the array, the remaining unsorted part of the array becomes shorter.


### Bubble Sort Implementation

- to implement the Bubble Sort algo, in a programming language, we need - 
    - an array with values to sort
    - an inner loop that goes through the array and swaps the values if the first value is higher than the next value. This loop must loop through one less value each time it runs.
    - An outer loop that controls how many times the inner loop must run. for an array with n values, this outer loop must run n-1 times.

- in code - 
`
my_array=[64, 34, 25, 12, 22, 11, 90, 5]
n = len(my_array)

for i in range(n-1):
    for j in range(n-i-1):
        if my_array[j] > my_array [j+1]:
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]

print('Sorted array: ', my_array)
`

### Bubble Sort Improvement

- the above bubble-sort can be improved as well.
- what if the array is alredy sorted, it will still lead to the loop running without swapping the values, because it will keep checking the next value.
- to stop that, we can find a way to make some changes - if the algorithm goes through the array one time without swapping any values, the array must be finished sorted, adn we can stop the algo right there - for that, we need to put a condition in place.

`
for i in range(n-1):
    swapped = False
    for j in range(n-i-1):
        if my_array[j] > my_array[j+1]:
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
            swapped = True
    if not swapped:
        break
`

### Bubble Sort Time Complexity

- we saw earlier, bubble sort algo loops through every value in the array, comparing it to the value next to it. So, for an array of n values, there must be n such comparisons in one loop.
- and after one loop, the array is looped through again and again n times.
- this means, there are n.n comparisons done in total, so the time complexity for Bubble sort is - Big O (n * n) //or n squared.
- so, the run time increases really fast when the size of the array is increased.
- luckily, there are sorting algorithms that are faster than this, like Quicksort.


## Selection Sort

- this algorithm finds the lowest value in an array and moves it to the front of the array.
- the algo looks through the array again and again, moving the next lowest values to the front, until the array is sorted.

**How it works?**

- go through the array to find the lowest value.
- move the lowest value to the front of the unsorted part of the array.
- go through the array again as many times as there are values in the array.

### Manual Run Through

- here, before we implement the Selection SOrt algo, we have to manually run through a short array only one time - 
    - 1. we start with an unsorted array. - [ 7, 12, 9, 11, 3]
    - 2. we go through the array, one value at a time. Which value is the lowest? 3 - [ 7, 12, 9, 11, 3]
    - 3. Move the lowest value 3 to the front of the array. - [ 3, 7, 12, 9, 11]
    - 4. look through the rest of the values, starting with 7. 7 is the lowest value, and already at the front of the array, so we dont need to move it. - [ 3, 7, 12, 9, 11]
    - 5. look through the rest of the array - 12, 9, 11. 9 is the lowest now. - [ 3, 7, 12, 9, 11]
    - 6. move 9 to the front. - [ 3, 7, 9, 12, 11]
    - 7. looking at 12 and 11, 11 is the lowest. - [ 3, 7, 9, 12, 11]
    - 8. move it to the front. - [ 3, 7, 9, 11, 12]
    - 9. array sort first go through complete.


**Explaining how it happened?**

- the lowest value - 3, is moved to the front of the array, where it belongs, but at that step, the rest of the array remains unsorted.

- selection sort algo must run through the array again and again, and each time, the next lowest value is moved in front of the unsorted part of array, to its correct position. That sorting continues until the highest value 12 is left at the end of the array. this means that we need to run through the array 4 times, to sort the array of 5 values.

- each time the algo runs through the array, the remaining unsorted part of the array becomes shorter.

### Selection Sort Pseudo-code Implementation

- an array with values to sort - random array
- an inner loop that goes through the array, finds the lowest value, and moves it to the front of the array.
- the loop must loop through one less value each time it runs.
- an outer loop that controls how many times the inner loop must run. for an array with n values, this outer loop must run n-1 times.

**in code**

`
my_array = [64, 34, 25, 5, 22, 11, 90, 12]

n = len(my_array)
for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        if my_array[j] < my_array[min_index]:
            min_index = j
    min_value = my_array.pop(min_index)
    my_array.insert(i, min_value)

print("Sorted array:", my_array)

`

### Selection Sort Shifting Problem

- the above selection sort algo can be improved a little bit.

- in the code above, the lowest value element is removed (my_array.pop(min_index)), adn then inserted in front of the array (my_array.insert(i, min_value)).

- so, each time the next lowest value array element is removed, all the following elements must be shifted one place down to make up for that removal. 

- these shifting operations takes a lot of time, and we are not even done yet. after the lowest value (5) is found and removed, it is then insertedf at the start of the array, causing all the following values to shift one position up and make space for the new value, basically, we add that lowest value in front and the rest of the values are shifted one value, which is almost rewriting the entire array loop after loop - which is redundant process.

**Solution to that problem?**

- instead of all the shifting, we should swap the lowest value(5) with the first value (64) - swapping the lowest value with the index it should be at.

- and since the other value is not yet sorted, so it doenst matter where we keep it, we can also keep it at the end, which will leave the rest of the array unchanged and unshifted - saving us time and memory.

- so now, we write the improved selection sort algo - 

`
my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)
for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if my_array[j] < my_array[min_index]:
            min_index = j

    my_array[i], my_array[min_index] = my_array[min_index], my_array[i]

print('Sorted array: ', my_array)

`

### Selection Sort Time COmplexity 

- selection sort sorts an array of n values.
- on average, about n/2 elements are compared to find the lowest value in each loop.
- and selection sort must run the loop to find the lowest value approximately n times.
- so we have got a time complexity of - Big O(n/2 * n) = Big O(n * n) - (n squared)
- it means that, the run time of selection sort is the same as Bubble Sort. The run time increases really fast when the size of the array is increased.

- the most significant difference from Bubble sort is that we can notice in this sort is that the best and the worst case is actually almost the same for selection sort (O(n*n)), but for Bubble sort, the best case runtime is only (O(n)).
- the difference in best and worst case for selection sort is mainly the number of swaps. In the best case scenario, selection sort does not have to swap any of the values because the array is already sorted. And in the worst case scenario, where the array is sorted but in the wrong order, so selection sort must do as many swaps as there are values in the array.


## Insertion Sort

- insertion sort algorithm uses one part of the array to hold the sorted values, and the other part of the array to hold values that are not sorted yet.

- this algorithm takes one value at a time from the unsorted part of the array and puts it into the right place in the sorted part of the array, until the array is sorted.

**how it works?**

- take the first value from the unsorted part of the array.
- move the value into the correct place in the sorted part of the array.
- go through the unsorted part of the array again as many times as there are values.

### Manual Run Through

- before we implement the insertionsort algorithm in a programming language, we will manually run through them in few steps - 
    - 1. we start with an unsorted array. - [ 7, 12, 9, 11, 3]
    - 2. we can consider the first value as the initial sorted part of the array. If it is just one value, it must be sorted, right? - [ 7, 12, 9, 11, 3]
    - 3. The next value 12 should now be moved into the correct position in the sorted part of the array. But 12 is higher than 7, so it is already in the correct position. - [ 7, 12, 9, 11, 3]
    - 4. consider the next value 9. - [ 7, 12, 9, 11, 3]
    - 5. the value 9 must now be moved into the correct posiotion inside the sorted part of the array, so we move 9 in between 7 and 12. - [ 7, 9, 12, 11, 3]
    - 6. the next value is 11. - [ 7, 9, 12, 11, 3]
    - 7. we move it in between 9 and 12 in the sorted part of the array. - [ 7, 9, 11, 12, 3]
    - 8. the last value to insert into the correct position is 3. - [ 7, 9, 11, 12, 3]
    - 9. we insert 3 in front of all the other values because it is the lowest value of the array. - [ 3,7, 9, 11, 12]


### Manual Run Through

- We must understand what happened above to fully understand the algorithm, so that we can implement the algorithm in a programming language.

- The first value is considered to be the initial sorted part of the array.

- Every value after the first value must be compared to the values in the sorted part of the algorithm so that it can be inserted into the correct position.

- The Insertion Sort Algorithm must run through the array 4 times, to sort the array of 5 values because we do not have to sort the first value.

- And each time the algorithm runs through the array, the remaining unsorted part of the array becomes shorter.

### Insertion Sort Implementation in Code

To implement the Insertion Sort algorithm in a programming language, we need:
    -1. an array with values to sort.
    -2. an outer loop that picks a value to be sorted. For an array with n values, this outer loop skips the first value, and must run n - 1 times.
    -3. an inner loop that goes through the sorted part of the array, to find where to insert the value. If the value is sorted is at index i, the sorted part of the array starts at index 0, and ends at index i-1.

The code looks like this - 
`
my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)
for i in range(1, n):
    insert_index = i
    current_value = my_array.pop(i)
    
    for j in range (i-1, -1, -1):
        if my_array[j] > current_value:
            insert_index = j

    my_array.insert(insert_index, current_value)

print('Sorted array:', my_array)

`

### Insertion Sort Improvement

- the above code is correct, but it can be improved.

- the way the above code works - it first removes a value and then inserts it somewhere else - pop() and then insert().

- it is how we would do insertion sort physically with a hand of cards for example. If the low value cards are sorted to the left, you pick up a new unsorted card, and then insert it in the correct place between the other already sorted cards.

- the problem with this way of programming it is that when removing a value from the array, all the other elements must be shifted one index place down.

- and when inserting the removed value into the array again, there are also many shift operations that must be done: all following elements must shift one position up to make place for the inserted value.

- these shifting operations can take a lot of time, especially for an array with many elements.

- **hidden memory shifts** - you will not see these shifting operations happening in the code if you are using a high-level programming language like Pythoini or JS, but the shifting operations are still happening in the background. Such shifting operations require extra time for the computer to do, which can be a problem.

- **C and Java code examples above and below are the same:** The issue of memory shifts happening behind the scenes is only relevant for high-level programming languages like Python or JavaScript, where arrays are dynamic, which means you can easily remove and insert elements. In lower-level programming languages like C and Java, where arrays have a fixed length, elements cannot be removed or inserted. As a result, there are no such memory shifts happening, and therefore the example codes above and below for C and Java remain the same.


### Improved Insertion Sort

- we can avoid most of these shift operations by only shifting the values necessary - the ones we are using.

- so, in an array - [3, 4, 6, 11, 12, 7, 13, 19, 2, 5, 15], first the value 7 is copied, then values 11 and 12 are shifted one place up in the array, and then the last value 7 is put where value 11 was before.

- the number shifting operations is reduced from 12 to 2 in this case as we are not shifting the entire array.

- imrpoved version demo in code - 

`
my_arr = [64, 34, 25, 12, 22, 11, 90, 5]

len_arr = len(my_arr)
for i in range(1, n):
    insert_index = i
    current_value = my_arr[i]
    
    for j in range (i-1, -1, -1):
        if my_arr[j] > current_value:
            my_arr[j+1] = my_arr[j]
            insert_index = j
        else:
            break

    my_arr[insert_index] = current_value

print('Sorted array:', my_arr)
`

- in the code above, we are also breaking out of the inner loop with the else block. That is because there is no need to continue comparing values when we have already found the correct place for the current vlaue.


### Insertion Sort Time Complexity

- Insertion sort sorts an array of n values.

- on average, each value must be compared to about n/2 other values to find the correct place to insert it.

- Insertion sort must run the loop to insert a value in its corrct place approximately n times.

- we get a time complexity for Insertion sort - 
    Big O(n/2 * n) = Big O(n * n) ->(n squared)

- for Insertion sort, there is a big difference between best, worst, and average case scenarios.


## Quick Sort

- it is one of the fastest sorting algorithm.

- the quicksort algorithm takes an array of values, chooses one of the values at the 'pivot' element, and moves the other values so that the lower values are on the left of the pivot (any singular element) element, and the higher values are on the right of it.

- note that, here, we are choosing the last element of the array to be the pivot element, but we could also have chosen the first element of the array, or any other element of the array.

- then, the quicksort algo does the same operation recursively on the sub-arrays to the left and right side of the pivot element. This continues until the array is sorted.


**what is recursion?**
- its when a function calls itself.
- after the quicksort algorithm has put the pivot element in between a sub-array with lower values on the left side, adn a sub-array with higher values on the right side, the algorithm calls itself twice, so that quicksort runs again for the sub-array on the left side, and for the sub-array on the right side. the quicksort algorithm continues to call itself until the sub-arrays are too small to be sorted.

- describing the quicksort algorithm - steps - 

    -1. choose a value in the array to be the pivot element.
    -2. order the rest of the array so that eh lower values than the pivot element are on the left, and higher values on the right.
    -3. swap the pivot element with the first element of the higher values so that the pivot element lands in between the lower and higher values. 
    -4. do the same operations (recursively) for the sub-arays on the left adn right side of the pivot element.


### Manual Run Through

- before we implement the quicksort algorithm in a programming language, lets manually run through a short array - 
    
    -1. we start with an unsorted array. -[ 11, 9, 12, 7, 3]
    -2. we choose the last valuue 3 as the pivot element. - [ 11, 9, 12, 7, 3]
    -3. the rest of the values in the array are all greater than 3, and must be on the right side of 3. Swap with 11. - [ 3, 9, 12, 7, 11]
    -4. value 3 is now in the correct position. We need to sort the values to the right of 3. We choose the last value 11 as the new pivot element. = [ 3, 9, 12, 7, 11]
    -5. the value 7 must be on the left of the pivot value 11, adn 12 must be to the right of it. Move 7 and 12. - [ 3, 9, 7, 12, 11]
    -6. swap 11 with 12, so that lower values 9 and 7 are on the left side of 11, and 12 is on the right side. - [ 3, 9, 7, 11, 12]
    -7. 11 and 12 are in the correct posotions. we choose 7as the pivot element in the sub-array [9,7], to the left of 11. - [ 3, 9, 7, 11, 12]
    -8. we must swap 9 with 7. The array is now sorted. - [ 3, 7, 9, 11, 12]


**Understanding what happened above?**

- before we implement the algorithm in a programming language we need to go through what happened above in more detail.
- we have already seen that last value of the array is choisen as the pivot elerment, and the rest of the values are arranged so that the values lower than the pivot value are to the left, and the higher values are to the right.
- after that, the pivot element is swapped with the first of the higher values. This splits the original array in two, with the pivot element in between the lwoer and the higher values. 
- now we need to do the same as above with the sub-arrays on the left and right side of the old pivot element. And if a sub-array has length 0 or 1, we consider it finished sorted.
- to sum it all up, the quicksort algorithm makes the sub-arrays become shorter and shorter until the array is sorted.

### Quicksort Implementation

- to write a quicksort algorithm method that splits the array into shorter and shorter sub-arrays we use recursion. This means that the quicksort method must call itself with the new sub-arrays to the left and right of the pivot element.

- to implement the quicksort algorithm in a programming language, we need these - 
    - an array with values to sort.
    - a quicksort method that calls itself (recursion) if the sub-array has a size larger than 1.
    - a partition method that receives a sub-array, moves the values around, swaps the pivot element into the sub-array and returns the index where the next split in sub-arrays happens.

**implementing in code**
`
def partition(array, low, high):
    pivot = array[high]
    i = low -1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quicksort (array, low=0, high=None):
    if high is None:
        high = len(array) -1

    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, picot_index-1)
        quicksort(array, pivot_index + 1, high)

my_array = [64, 34, 25, 12, 22, 11, 90, 5]
quicksort(my_array)
print('Sorted array:', my_array)
`

### Quicksort Time Complexity

- the worst case scenario for quicksort is Big O(n * n) - n squared. This is when the pivot element is either the highest or lowest value in every sub-array, which leads to a lot of recursive calls. With our implementation above, this happens when the array is already sorted.

- But on average, the time complexity for quicksort is actually just Big O(n log n), which is a lot better than for the previous sorting algos we have looked at. THis is why quicksort is good for sorting arrays quickly.

- the recursion part of the quicksort algorithm is actually a reason why the average sorting scenario is so fast, because for good picks of the pivot element, the array will be split in half somewhat evenly each time the algorithm calls itself. So the number of recursive calls do not double, even if the number of the values of n double.



## Counting Sort

- the counting sort algo sorts an array by counting the number of times each value occurs.

- counting sort does not comapre values like the previous sorting algos, and only works on non negative integers.

- also, counting sort is fast when the range of possible values k is smaller than the number of values n.

**how counting sort works? (pseudocode)**

1. create a new array for counting how many values there are of the different values.
2. go through the array that needs to be sorted.
3. for each value, count it by increasing the counting array at the corresponding index.
4. after counting the values, go through the counting array to create the sorted array.
5. for each count in the counting array, create the correct number of elements, with the values that correspond to the counting array index.


### Conditions for Counting Sort

- these are the resons why Counting Sort is said to only work for a limited range of non-negative integer values - 
    - integer values - Counting Sort relies on counting the occurances of distinct values, so they must be integers. With integers, each value fits with an index (for non-negative values), and there is a limited number of different values, so that the number of possible different values k is not too big compared to the number of values n.
    - non negative values - Counting Sort is usually implemented by creating an array for counting. When the algorithnm goes through teh values to be sorted, value x is counted by increasing the counting array value at index x. If we tried sorting negative values, we would get in trouble with sorting values -3, because index -3 would be outside the Counting array.
    - limited range of values - if the number of possible different values to be sorted k is larger than the number of values to be sorted n, the counting array we need for sorting will be larger than the original array we have that needs sorting, and the algorithm becomes ineffective.


### Manual Run Through

- before we implement the Counting Sort algorithm in a programming language, lets manually run through a short array, just to get the idea - 
    1. we start with an unsorted array. - myArray = [ 2, 3, 0, 2, 3, 2]
    2. we create another array for counting how many there are of each value. The array had 4 elements, to hold values - 0 through 3. - 
        - myArray = [ 2, 3, 0, 2, 3, 2]
        countArray = [ 0, 0, 0, 0]
    3. now, lets start counting. The first element is 2, so we must increment the counting array element at index 2. - myArray = [ 2, 3, 0, 2, 3, 2]
    countArray = [ 0, 0, 1, 0]
    4. after counting a value, we can remove it, and count the next value, which is 3. - 
        myArray = [ 3, 0, 2, 3, 2]
        countArray = [ 0, 0, 1, 1]
    5. the next value we count is 0 (in the array), so we increment index 0 in the counting array. - 
    myArray = [ 0, 2, 3, 2]
    countArray = [ 1, 0, 1, 1]
    6. we continue like this until all values are sorted. - myArray = [ ]
    countArray = [ 1, 0, 3, 2]
    7. now, we will recreate the elements from the initial array, and we will do it so that the elements are ordered lowest to highest.
    - the first element in the counting array tells us that we have 1 element with value 0. So, we push 1 element with value 0 into the array, and we decrease the element at index 0 in the counting array with 1. 
    - myArray = [ 0]
    countArray = [ 0, 0, 3, 2]
    8. from the counting array, we se that we do not need to create any elements with value 1.
    - myArray = [ 0]
    countArray = [ 0, 0, 3, 2]
    9. we push 3 elements withg value 2 into the end of the array. And as we create these elements we also decrease the counting array at index 2.
    - myArray = [ 0, 2, 2, 2]
    countArray = [ 0, 0, 0, 2]
    10. at last, we must add 2 elements with value 3 at the end of the array. THe array is sorted now.
    - myArray = [0, 2, 2, 2, 3, 3]
    countArray = [ 0, 0, 0, 0]

### Manual Run Through of the pseudo code above

- before we implement the algorithm in a programming language we need to go through what happened above in more detail -
- we have already seen that the Counting Sort algorithm works in two steps - 

    1. each value gets counted by incrementing at the correct index in the counting array. After a value is counted, it is removed.
    2. the values are recreated in the right order by using the count, and the index of the count, from the Counting array.


### Counting Sort Implementation in Code - python

- To implement the Counting Sort algorithm in a programming language, we need - 
    - an array with values to sort.
    - a 'countingSort' method that receives an array of Integers.
    - an array inside the method to keep count of the values.
    - a loop inside the method that counts and removes values, by incrementing elements in a counting array.
    - a loop inside the method that recreates the array by using the counting array, so that the elements appear in the right order.

- Another thing is that - we need to find out what the highest value in the array is, so that the counting array can be created with the correct size. For example, if the highest value is 5, the counting array must be 6 elements in total, to be able to count all the possible non-negative integers like 0, 1, 2, 3, 4 and 5.

- the code looks like this - 
`
def countingSort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)

    while len(arr) > 0:
        num = arr.pop(0)
        count[num] += 1

    for i in range(len(count)):
        while count[i] > 0:
            arr.append(i)
            count[i] -= 1

    return arr

unsortedArr = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
print('Unsorted array:', unsortedArr)

sortedArr = countingSort(unsortedArr)
print('Sorted array:', sortedArr)
`

### Counting Sort Time Complexity

- how fast the Counting Sort algo runs depends on both the range of possible values k, and the number of values n.

- in general, the time complexity for Counting Sort is Big O(n + k).

- in the best case scenario, the range of possible different values k is very small compared to the number of values n, and the Counting Sort has time complexity - Big O(n).

- btu in a worst case scenario, the range of possible different values k is very big compared to the number of values n, and Counting Sort can have time complexity - Big O(n * n) -> n squared, or even worse.

- it is important to consider the range of values compared to the number of values to be sorted before choosing Counting Sort as your algorithm. Also, as mentioned at the top of the page, keep in mind that Counting Sort only works for non negative integer values.

- As mentioned previously: if the numbers to be sorted varies a lot in value (large k), and there are few numbers to sort (small n), the Counting Sort algorithm is not effective.

- If we hold n and k fixed, the "Random", "Descending" and "Ascending" alternatives in the simulation above results in the same number of operations. This is because the same thing happens in all three cases: A counting array is set up, the numbers are counted, and the new sorted array is created.

## Radix Sort

- the Radix Sort algo sorts an array by individual digits, starting with the least significant digit(the rightmost one).

- the Radix (or base) is the number of unique digits in a number system. In a decimal system, we normally use, there are 10 different digits from 0 till 9.

- Radix Sort uses the radix so that decimal values are put into 10 different buckets (or containers) corresponding to the digit that is in focus, then put back into the array before moving on to the next digit.

- Radix Sort is a non comparative algorithm that only works with non-negative integers.  

**how it works?**

- start with the least significant digit(rightmost digit).
- sort the values based on the digit in focus by first putting the values in the correct bucket based on the digit in focus, and then put them back into array in the correct order.
- move to the next digit, and sort again, like in the step above, until there are no digits left.

### Stable Sorting

- Radix Sort must sort the elements in a stable way for the results to be sorted correctly.

- a stable sorting algorithm is an algorithm that keeps the order of elements with teh same value before and after the sorting. Lets say we have two elements, 'K' and 'L', where K comes before L, and they both have the value '3'. A sorting algorithm is considered stable if element K still comes before L after the array is sorted.

- It makes little sense to talk about stable sorting algorithms for the previous algorithms we have looked at individually, because the result would be same if they are stable or not. But it is important for Radix Sort that the the sorting is done in a stable way because the elements are sorted by just one digit at a time.

- So after sorting the elements on the least significant digit and moving to the next digit, it is important to not destroy the sorting work that has already been done on the previous digit position, and that is why we need to take care that Radix Sort does the sorting on each digit position in a stable way.

- If you choose to sort in an unstable way, that will lead to an incorrect result. The sorting is made unstable by simply putting elements into buckets from the end of the array instead of from the start of the array.


### Manual Run Through - pseudocode

- here, we are going to use pseudocode to manually run through the Radix sort to get an even better understanding of how Radix sort works before actually implementing it in a programming language - 

    1. we start with an unsorted array, and an empty array to fit values with corresponding radices 0 till 9.
        - myArray = [ 33, 45, 40, 25, 17, 24]
            radixArray = [ [], [], [], [], [], [], [], [], [], [] ]

    2. we start sorting by focusing on the least significant digit.
        - myArray = [ 33, 45, 40, 25, 17, 24]
        radixArray = [ [], [], [], [], [], [], [], [], [], [] ]

    3. now we move the elements into the correct positions in the radis array according to the digit in focus. Elements are taken from the start of myArray and pushed into the correct position in the radixArray.
    - myArray = [ ]
    radixArray = [ [40], [], [], [33], [24], [45, 25], [], [17], [], [] ]

    4. we move the elements back into the initial array, and the sorting is now done for the least significant digit. Elements are taken from the end radixArray, and put into the start of myArray.
    - myArray = [ 40, 33, 24, 45, 25, 17 ]
    radixArray = [ [], [], [], [], [], [], [], [], [], [] ]

    5. we move focus to the next digit, notice that values 45 adn 25 are still in the same order relative to each other as they were to start with, becasue we sort in a stable way.
    - myArray = [ 40, 33, 24, 45, 25, 17 ]
    radixArray = [ [], [], [], [], [], [], [], [], [], [] ]

    6. we move elements into the radix array according to the focused digit.
    - myArray = [ ]
    radixArray = [ [], [17], [24, 25], [33], [40, 45], [], [], [], [], [] ]

    7. we move elements back into the start of myArray, from the back of radixArray. The sort is finished now.
    - myArray = [ 17, 24, 25, 33, 40, 45 ]
    radixArray = [ [], [], [], [], [], [], [], [], [], [] ]


### Manual Run Through. Explanation of what happened?

we will now do the sorting manually, just to get an even better understanding of how Radix sort works before actually implementing it in a programming language - 

1. we start with an unsorted array, and an empty array to fit values with corresponding radices 0 till 9.
`
myArray = [ 33, 45, 40, 25, 17, 24]
radixArray = [ [], [], [], [], [], [], [], [], [], [] ]
`
2. we start sorting by focusing on the least significant digit.
`
myArray = [ 33, 45, 40, 25, 17, 24]
radixArray = [ [], [], [], [], [], [], [], [], [], [] ]
`
3. now we move the elements into the correct positions in the Radix array according to the digit in focus. Elements are taken from the start of myArray and pushed into the correct position in the radixArray.
`
myArray = [ ]
radixArray = [ [40], [], [], [33], [24], [45, 25], [], [17], [], [] ]
`
4. we then move the elements back into the initial array, and the sorting is now done for the least significant digit. ELements are now taken from the end radixArray, and put into the start of myArray.
`
myArray = [ 40, 33, 24, 45, 25, 17 ]
radixArray = [ [], [], [], [], [], [], [], [], [], [] ]
`
5. we move focus to the next digit. Notice that values 45 and 25 are still in the same order relative to each other as they were to start with, becasue we sort in a stable way.
`
myArray = [ 40, 33, 24, 45, 25, 17 ]
radixArray = [ [], [], [], [], [], [], [], [], [], [] ]
`
6. we move elements into the radix array according to the focused digit.
`
myArray = [ ]
radixArray = [ [], [17], [24, 25], [33], [40, 45], [], [], [], [], [] ]
`
7. we move elements back into the start of myArray, from the back of radixArray. Our array is now sorted. 
`
myArray = [ 17, 24, 25, 33, 40, 45 ]
radixArray = [ [], [], [], [], [], [], [], [], [], [] ]
`


**Manual Run Through: What Happened?**

- we see that the values are moved from the array and placed in the radix array according to the current radix in focus. And then, the values are moved back into the array we want to sort.

- this moving of values from the array we want to sort and back again must be done as many times as the maximum number of digits in a value. So for example, if 437 is the highest number in the array that needs to be sorted, we know we must sort three times, once for each digit. 

- we also see that the radix array needs to be two-dimensional so that more than one value on a specific radix, or index.

- we must move values between two arrays in a way that keeps the order of values with the same radix in focus, so the sorting is stable. 


### Radix Sort Implementation

To implement the Radix sort algo, we require - 

1. an array with non negative integers that needs to be sorted.
2. a two dimensional array with index 0 to 9 hold vales with the current radix in focus.
3. a loop that takes values from the unsorted array and places them in the correct position in the two dimensional radix array.
4. a loop that puts values back into the initial array from the radix array.
5. an outer loop that runs as manyu times as there are digints in the highest value.

in code -
`
myArray =  [170, 45, 75, 90, 802, 24, 2, 66]
print('Original Array: ', myArray)

radixArray=[[], [], [], [], [], [], [], [], [], []]
maxVal = max(myArray)
exp = 1

while maxVal // exp > 0:  #line 7
    while len(myArray) > 0:
        val = myArray.pop()
        radixIndex = (val//exp) % 10  # line 11
        radixArray[radixIndex].append(val)

    for bucket in radixArray:
        while len(bucket) > 0:
            val = bucket.pop()
            myArray.append(val)

    exp *= 10

print('Sorted array: ', myArray)
`

- on line 7 we use the floor division ('//'), to divide the maximum value 802 by 1 the first time the while loop runs, the next time it is divided by 10, and the last time it is divided by 100. When using the floor division '//', any number neyond the decimal point are disregarded, and an integar is returned.

- also, on line 11, it is decided where to put a value in the radixArray based on its radix, or digit in focus. For example, the second time the outer while loop runs, the exp will be 10. Value 170 divided by 10 will be 17. The '%10' operation divided by 10 and returns what is left. In this case, 17 is divided by 10 one time, and 7 is left. So, value 170 is placed in index 7 in the radixArray.


### Radix Sort using other Sorting Algorithms

Radix sort can acautlly be implemented together with any other sorting algorithm as long as it is Stable. This means that when it comes down to sorting on a specific digit, any stable sorting algorithm will work just fine, such as counting sort or bubble sort.

Below is an implementation of Radix sort that uses Bubble Sort to sort out the individual digits - 

`
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def radixSortWithBubbleSort(arr):
    maxVal = max(arr)
    exp = 1

    while maxVal // exp > 0:
        radixArray = [[],[],[],[],[],[],[],[],[],[]]

        for num in arr:
            radixIndex = (num // exp) % 10
            radixArray[radixIndex].append(num)
            
        for bucket in radixArray:
            bubbleSort(bucket)

        i = 0
        for bucket in radixArray:
            for num in bucket:
                arr[i] = num
                i += 1

        exp *= 10

myArray = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original array:", myArray)
radixSortWithBubbleSort(myArray)
print("Sorted array:", myArray)
`

### Radix Sort TIme Complexity 

- the time complexity for radix sort is - Big O (n * k)

- it means that radix sort depends both on the values that needs to be sorted n, and the number of digits in the highest value k.

- a best case scenario for radix sort is if there are lots of values to sort, but the values have few digits. For example, if there are more than a million values to sort, and the highest value is 999, with just three digits. In such a case, the time complexity Big O(n * k) can be simplified to just Big O(n).

- a worst case scenario for Radix sort would be if there are as many digits in the highest value as there are values to sort. This is perhaps not a common scenario, but the time complexity would be Big O(n * n) - n squared.

- the most average or common case is perhaps if the number of diogits k is something like k(n) = log n. If so, Radix sort gets time complexity Big O(n * log n). An exampl of such a case would be if there are 1 million values to sort, and the values have 6 digits.


## Merge Sort

Merge Sort algorithm is a divide-and-conquer algorithm that sorts an array by first breaking it down into smaller arrays, and then building the array back together the correct way so that it is sorted.

- Divide - the algorithm starts with breaking up the array into smaller and smaller pieces until one such sub-array only consists of one element.

- Conquer - the algorithm merges the small pieces of the array back together by putting the lowest values first, resulting in a sorted array.

the breaking down and building up of the array to sort the array is done recursively.

The merge sort algorithm can be described like below - 

**How it works?**
1. divide the unsorted array into two sub-arrays, half the size of the original.
2. continue to divide the sub-arrays as long as the current piece of the array has more than one element.
3. merge the two sub-arrays together by always putting the lowest value first.
4. keep merginv until there are no sub-arrays left.

If we see merge sort from a different perspective, we see that the array is split into smaller and smaller pieces until it is merged back together. As the merging is happening, values from each sub-array are compared so that the lowest value comes first.


### Manual Run Through

to get a better understanding of how merge sort works, we have understand it by breaking those steps down before actually implementing them into a programming languge. 

1. we start with an unsorteed array, and we know that it splits in half until the sub-arrays only consist of one element. The Merge Sort function calls itself two times, once for each half of the array. That means that the first sub-array will split into the smallest pieces first.
`
[ 12, 8, 9, 3, 11, 5, 4]
[ 12, 8, 9] [ 3, 11, 5, 4]
[ 12] [ 8, 9] [ 3, 11, 5, 4]
[ 12] [ 8] [ 9] [ 3, 11, 5, 4]

`
2. the splitting of the first sub-array is finished now. and now its time to merge. 8 and 9 are the first two elements to be merged. 8 is the lowest value, so that comes before 9 in the first merged sub-array.
`[ 12] [ 8, 9] [ 3, 11, 5, 4]
`
3. the next sub-arrays to be merged is [12] and [8,9]. Values in both the arrays are compared from the start. 8 is lower than 12, so 8 comes first, and 9 is also lower than 12.
`
[ 8, 9, 12] [ 3, 11, 5, 4]
`
4. now the second big sub-array is split recursively.
`
[ 8, 9, 12] [ 3, 11, 5, 4]
[ 8, 9, 12] [ 3, 11] [ 5, 4]
[ 8, 9, 12] [ 3] [ 11] [ 5, 4]
`
5. 3 and 11 are merged back together in the same order as they are shown because 3 is lower than 11.
`[ 8, 9, 12] [ 3, 11] [ 5, 4]
`
6. sub-array with values 5 and 4 is split now, then meged so that 4 comes before 5.
`[ 8, 9, 12] [ 3, 11] [ 5] [ 4]
[ 8, 9, 12] [ 3, 11] [ 4, 5]
`
7. the two sub-arrays on the right are merged. Comparisons are done to create elements in the new merged array - 
    1. 3 is lower than 4
    2. 4 is lower than 11
    3. 5 is lower than 11
    4. 11 is the last remaining value
`[ 8, 9, 12] [ 3, 4, 5, 11]
`
8. the two last remaining sub-arrays are merged now. Lets look at how the comparisons are done in mroe details to create the new merged and finished sorted array - 
    1. 3 is lower than 8 -
    `Before [ 8, 9, 12] [ 3, 4, 5, 11]
    After: [ 3, 8, 9, 12] [ 4, 5, 11]
    `
9. 4 is lower than 8 - 
`Before [ 3, 8, 9, 12] [ 4, 5, 11]
After: [ 3, 4, 8, 9, 12] [ 5, 11]
`
10. 5 is lower than 8 - 
`
Before [ 3, 4, 8, 9, 12] [ 5, 11]
After: [ 3, 4, 5, 8, 9, 12] [ 11]
`
11. 8 and 9 are lower than 11 - 
`
Before [ 3, 4, 5, 8, 9, 12] [ 11]
After: [ 3, 4, 5, 8, 9, 12] [ 11]
`
12. 11 is lower than 12 - sorting is complete now - 
`Before [ 3, 4, 5, 8, 9, 12] [ 11]
After: [ 3, 4, 5, 8, 9, 11, 12]
`

### Manual Run through: What happened?

- we see that the algorithm has two stages - first - splitting, then - merging. 

- although it is possible to implement the Merge Sort algorithm without recursion, we will use recursion because that is the most common approach.

- we cannot see it in the steps above, but to split an array in two, the length of the array is divided by two, and then rounded down to get a value we call 'mid'. This 'mid' value is used as an index for where to split the array. 

- after the array is split, the sorting function calls itself with each half, so that the array can be split again recursively. This splitting stops when a sub-array only consists of one element.

- at the end of the Merge Sort function, the sub-arrays are merged so that the sub-arrays are always sorted as the array is built back up. To merge two sub-arrays so that the result is sorted, the values of each sub-array are compared, and the lowest value is put into the merged array. After that the next value in each of the two sub-arrays are compared, putting the lowest one into the merged array.  

### Merge Sort Implementation

to implement the Merge Sort algorithm, we need - 

1. an array with values that needs to be sorted.
2. a function that takes an array, splits it in two, and calls itself with each half of that array so that the arrays are split again, and again recursively, until a sub-array only consist of one value.
3. Another function that merges the sub-arrays back together in a sorted way.

the code looks like this - 
`
def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = arr[:mid] #line 6
    rightHalf = arr[mid:] # line 7

    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)
    
    return merge(sortedLeft, sortedRight)

def merge(left, right):
    result =[]
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:]) #lines 26
    result.extend(right[j:]) #lines 27

    return result

unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
sortedArr = mergeSort(unsortedArr)
print('Sorted Array:', sortedArr)

`

- on line 6, arr[:mid] takes all values from the array up until, but not including, the value on index 'mid'.

- on line 7, arr[mid:] takes all the values from the array, starting at the value on index 'mid' and all the next values.

- on lines 26-27, the first part of the merging is done. At this point the values of the two sub-arays are compared, and either the left sub-array or the right sub-array is empty, so the result array can just be filled with the remaining values from either the left or the right sub-array. These lines can be swapped, and the result will be the same.


### Merge Sort without Recursion

since merge sort is a divide and conquer algorithm, recursion is the most intuitive code to use for implementation. The recursive implementation of merge sort is also perhaps easier to understand, and uses less code lines in general.

but merge sort can also be implemented without the use of recursion, so that there is no function calling itself.

- here's an example of merge sort without recursion -  
`
def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

def mergeSort(arr):
    step = 1 # starting with sub-arrays of length 1
    length = len(arr)

    while step < length:
        for i in range(0, length, 2 * step):
            left = arr[i:i + step]
            right = arr[i + step : i + 2 * step]

            merged = merge(left, right)

            #place the merged array back into the original array
            for j, val in enumerate(merged):
                arr[i + j] = val

        step *= 2 #double the sub-aray length for the next iteration

    return arr

unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
sortedArr = mergeSort(unsortedArr)
print("Sorted array:", sortedArr)

`

- here, in the code above, you might notice that the merge functions are exactly the same in the two merge sort implementation above, but in the implementation right above here, the while loop inside the mergeSort function is used to replace the recursion. The while loop does the splitting and merging of the array in place, and that makes the code a bit harder to understand.

- to put it simply, the while loop inside the mergeSort function uses short step lengths to sort tiny pieces (sub-arrays) of the initial array using the merge function. Then the step length is increased to merge and sort larger pirces of the array until the whole arrayis sorted.

### Merge Sort Time Complexity

- the time complexity of merge sort is - Big O(n * log n)

- and the time complexity is pretty much the same for different kinds of arrays. The algorithm needs to split the array and merge it back together whether it is already sorted or completely shuffled.

- if we hold the number of values n fixed, the number of operations needed for the merge sort algo running to be almost the same.

- merge sort performs almost the same every tiem because the array is split, and merged using comparison, both if the array is already sorted or not.


## Linear Search

the linear search algorithm searches through an array and returns the index of the value it searches for.

if the array is alredy sorted, it is better to use the much faster Binary Search algorithm.

a big difference between sorting algorithms and searching algorithms is that sorting algorithms modify the array, but searching algorithms leave the array unchanged.

### How it works? Pseudocode

1. go through the array value by value from the start.
2. compare each value to check if it is equal to the value we are looking for.
3. if the value is found, return the index of that value.
4. if the end of the array is reached and the value is not found, return -1 to indicate that the value was not found.

### Manual Run Through

here, we will be searching the numbers manually, just to get an even better understanding of how linear search works before actually implementing it in code.

- We are searching the value 11

1. we start with an array of random values.
[ 12, 8, 9, 11, 5, 11]

2. we look at the first value in the array, is it equal to 11?
[ 12, 8, 9, 11, 5, 11]

3. we move on to the next value at index 1, and compare it to 11 to see if it is equal to 11.
[ 12, 8, 9, 11, 5, 11]

4. we check the next value at index 2.
[ 12, 8, 9, 11, 5, 11]

5. we move on to the next value at index 3, is it equal to 11? yes, we found our index no.
[ 12, 8, 9, 11, 5, 11]


### Manual Run THrough: What Happened?

this algorithm is straight forward. Every value is checked from the start of the array to see if the value is equal to 11 - thats the value we are trying to find.

when the value is found, the searching is stopped, and the index where the value is found is returned.

if the array is searched through without finding the value, -1 is returned.

### Linear Search Implementation

to implement the Linear Search algo, we need - 
    1. an array with the values to search through.
    2. a target value to search for.
    3. a loop that goes through the array from start to end.
    4. an if-statement that compares the current value with the target value, and returns the curent index if the target is found.
    5. after the loop, return -1, because at this point we know the target value has not been found.

in code - 
`
def linearSearch(arr, targetVal):
    for i in range(len(arr)):
        if arr[i] == targetVal:
            return i
        return -1

arr = [3, 7, 2, 9, 5]
targetVal = 9

result = linearSearch(arr, targetVal)

if result != -1:
    print('Value', targetVal, 'found at index', result)
else:
    print('Value', targetVal, 'not found')
`

### Linear Search Time Complexity

- if linear search runs and finds the target value as the first array value in an array with n values, only one compare is needed.

- but if linear search runs through the whole array of n values, without finding the target value, n compares are needed. 

- this means, that the time complexity for linear search is - Big O(n).


## Binary Search

the blinary search algorithm searches through an array and returns the index of the value it searches for.

it is much faster than linear search, but requires a sorted array to work.

the blinary search algorith, works by checking the value in the center of the array. if the target value is lower, the next value to check is in the center of the left half of the array. This way of searching means that the search area is always half of the previous search area and this is why blinary search algorithm is so fast.

this process of halving the search area happens until the target value is found, or until the search area of the array is empty.

**How it works?**

1. check the value in the center of the array.
2. if the target value  is lower, search the left half of the array. If the target value is higher, search the right half.
3. continue step 1, and step 2 for the new reduced part of the array until the target value is found or until the search area is empty.
4. if the value is found, return the target value index. If the target value is not found, return -1.

### Manual Run Through

- here, we will try to do searching manually, just tog et an even better understanding of how Binary Search works before actually implementing it in a programming language. We will search the value 11.

1. We start with an array. - [ 2, 3, 7, 7, 11, 15, 25]
2. the value in the middle of the array at index 3, is it equal to 11? - [ 2, 3, 7, 7, 11, 15, 25]
3. 7 is less than 11, so we must search for 11 to the right of index 3. The values to the right of index 3 are [11, 15, 25]. The next value to check is the middle value 15, at inedx 5. - [ 2, 3, 7, 7, 11, 15, 25]
4. 15 is higher than 11, so we must search for 11 tot he right of index 3. The values to the right of index 3 are [11, 15, 25]. the next value to check is the middle value 15, at index 5. - [ 2, 3, 7, 7, 11, 15, 25]
5. 15 is higher than 11, so we must search to the left of index 5. We have already checked index 0-3, so index 4 is the only value left to check.
6. We have found our value. Value 11 is found at index 4. Returning index position 4. Binary search is now finished.

### Manual Run Through: What happened?

- to start with, the algorithm mhas two variables - `left` and `right`.
- left is 0 and represents the index of the first value  in the array, and right is 6 and represents the index of the last value in the array.
- (left + right)/2 = (0+6)/2 = 3 - is the first index used to check if the middle value (7) is equal to the target value (11).
- 7 is lower than the target value 11, so in the next loop the search area must be limited to the right side of the middle value - [11, 15, 25], on index 4-6.
- to limit the search area and find a new middle value, 'left' is updated to index 4, 'right' is still 6. 4 and 6 are the indexes for the first and last values in the new search area, the right side of the previous middle valyue. the new middle value index is - (left + right)/2 = (4+6)/2 = 10/2 = 5.
- the new middle value on index 5 is checked - 15 is higher than 11, so if the target value 11 exists in the array, it must be on the left side of index 5. The new search area is created by updating 'right' from 6 to 4. Now, both 'left' and 'right' is 4, (left + right)/2 = (4+4)/2 = 4, so now, there is only index 4 left to check. The target value 11 is found at index 4, so index 4 is returned.
- so, in general, this is the way the Binary search algorithm continues to halve the array search area until the target value is found.
- when the target value is found, the index of the target value is returned. if the target value is not found, -1 is returned.

### Binary Search Implementation

- to implement the binary search algo, we need - 
    - a sorted array with values to search through.
    - a target value to search for.
    - a loop that runs as long as left index is less than, or equal to, the right index.
    - an if-statement that compares the middle value with the target value, and returns the index if the target value is found.
    - an if-statement that checks if the target value is less than, or larger than, the middle value, and updates the 'left' or 'right' variables to narrow down the search area.
    - after the loop, return -1, because at this point, we know the target value has not been found.

- now, the code looks like this - 

`
def binarySearch(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == targetVal:
            return mid

        if arr[mid] < targetVal:
            left = mid + 1
        else:
            right = mid - 1

    return -1

myArray = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
myTarget = 15

result = binarySearch(myArray, myTarget)

if result != -1:
    print ('Value', myTarget, 'found at ', result)
else:
    print('target value not found in array.')
`

### Binary Search Time Complexity

- each time a binary search checks a new value to see if it is the target value, the search area is halved.
- this means that even in the worst case scenario, where the binary search cant find the target value, it still only needs log2n comparisons to look through a sorted array of n values(length).
- So, the time complexity of binary search is - Big O(log2n)

- note that, when writing the time complexity using Big O notation, we could also just have written Big O(log n), but Big O(log2n) reminds us that the array search area is halved for every new comparison, which is the basic concept of binary search, so we will just keep the base 2 indication in this case.


## Linked Lists

- a linked list is a list where the nodes are linked together. each node contains data and a pointer (to the next data node). The way they are linked together is that each node points to where in the memory the next node is placed.

- a linked list consists of nodes with some sort of data, and a pointer, or link, to the next node.

- a big benefit with using linked lists is that nodes are stored wherever there is free space in memory, the nodes do not have to be stored contiguously right after each other like elements are stored in arrays. Another nice thing with linked lists is that when adding or removing nodes, the rest of the nodes in the list do not have to be shifted.

### Linked Lists vs Arrays

- linked lists consists of nodes, and is a linear data structure we make ourselves, unlike arrays which is an existing data structure in a programming language we use.
- nodes in a linked list store links to other nodes, but array elements do not need to store links to other elements.

- here's a table comparing linked list to arrays to give you a better understanding of what linked lists actually are - 

| idea | arrays | linked lists |
| an existing data structure in the programming language | yes |no |
| fixed size in memory | yes |no |
| elements, or nodes, are stored right after each other in memory (contiguously) | yes |no |
| memory usage is low (each node only contains data, no links to other nodes) | yes |no |
| elements, or nodes, can be accessed directly (random access) | yes |no |
| elements, or nodes, can be inserted or deleted in constant time, no shifting operations in memory needed | no |yes |


## Linked Lists in Memory

### Computer Memory

- to explain what linked lists are, and how linked lists are different from arrays, we need to understand some basics about how computer memory works.
- computer memory is the storage your program uses when it is running. This is where your variables, arrays and linked lists are stored.

### Variables in Memory

- lets imagine, that we want to store the integer '17' in a variable called myNumber. For simplicity,lets assume the integer is stored as two bytes (16 bits - 8 bits x 2), and the address in memory to `myNumber` is `0x7F30`.
- `0x7F30` is actually the address to the first of the two bytes of memory where the `myNumber` integer valus is stored. when the computer goes to 0x7F30, to read an integer value, it knows that it must read both the first and the second byte, since integers are two bytes on this specific computer.

### Arrays in Memory

- to understand linked lists, it is useful to first know how arrays are stored in memory.
- elements in an array are stored contiguously in memory. That means that each element is stored right after the previous element.
- so an array, lets say of `myArray = [3, 4, 13, 2]` will be stored in memory - 0xF28 0xF29, 0xF30 0xF31, 0xF32 0xF33, 0xF34 0xF35. The memory spaces for arrays are contiguous, we use a simple kind of memory here with two bytes for each integer, like in the prev example of linked lists.
- the computer has only got the address of the first byte of `myArray` in array, so to access the 3rd element with the code `myArray[2]` the computer starts at `0x7F28` and jumps over the two first integers. the computer knows that an integer is stored in two bytes, so it jumps 2x2 bytes forward from `0x7F28` and reads value 13 starting at address - `0x7F32`.
- when removing or inserting elements in an array, every element that comes after must be either be either shifted up to make place for the new element, or shifted down to take the removed element's place. Such shifting operations are time consuming, and can cause problems in real-time systems for example.

- manipulating arrays is also something you must think about if you are programming in C, where you have to explicitly move other elements when inserting or removing an element. In C, this does not happen in the background.
- in C, you also need to make sure that you have allocated enough space for the array to start with, so that you can add more elements later.

### Linked Lists in Memory

- instead of storing a collection of data as an array, we can create a linked list.
- linked lists are used in many scenarios, like dynamic data storage, stack and queue implementation or graph representation, to mention some of them.
- a linked list consists of nodes with some sort of data, and at least one pointer, or link, to other nodes.
- a big benefit with using linked lists is that nodes are stored wherever there is free space in memory, the nodes do not have to be stored contiguously right after each other like elements are stored in arrays. Another nice thing with linked lists is that when adding or removing nodes, the rest of the nodes in the list do not have to be shifted.

- eg. - if `myLinkedList = [3, 5, 13, 2]`, lets say 3 is at `0x7F28`, 5 is at `0x7F42`, 13 is at `0x7F3D`, 2 is at `0x7F35`. Here, in our linked list with four nodes, each node has a pointer to the next node in the list.
- each node in the example takes up four bytes. Two bytes are used to store an integer value, and two bytes are used to store the address to the next node in the list. As mentioned before, how many bytes are needed to store integers and addresses depends on the architecture of the computer.
- to make it easier to see how the nodes relate to each other, we will display the nodes in a linked list in a simpler way, less related to their memory location.
    | data |
    | next | ->

- if we put the same four nodes from the previous example together using this new visualization, it would look like this -
    head node     node         node        tail node
    0x7F28        0x7F42        0x7F3D        0x7F35
    | 3 |        | 5 |        | 13 |        | 2 |
    | 0x7F42 | -> |0x7F3d| -> |0x7F35| -> | null |

- note that, the arrows will point to the values (memory location for the next value in the linked list.)

- also, here, the first node in a linked list is called a 'head', and the last node a - 'tail'.
- unlike with arrayus, the nodes in a linked list are not placed right after each other in memory. This means that when inserting or removing a node, shifting of other nodes is not necessary, so that is a good thing.
- something not so good with linked lists is that we cannot access a node directly like we can with an array by just writing - `myArray[5]` - for example. To get to node number 5 in a liked list, we must start with the first node - head, use that node's pointer to get to the next node, and do so while keeping track of the number of nodes we have visited until we reach node number 5.

### Memory in Modern Computers

- memory in a modern computer works in the same way in principle as memory in an 8-bit microcontroller, but more memory is used to store integers, and more memory is used to store memory addresses.
- the code below (in C) gives you the size of an integer and the size of a memory address on the server - 
- written in C lang
`
#include <stdio.h>

int main(){
    int myVal = 15;

    printf("Value of integer 'myVal': %d\n", myVal);
    printf("Size of integer 'myVal': %lu bytes\n", sizeof(myVal)); // 4 bytes
    printf("Address to 'myVal': %p\n", &myVal);
    printf("Size of the address to 'myVal': %lu bytes\n", sizeof(&myVal)); // 8 bytes

    return 0;
}
`

- the code above only runs in C because Java and Python runs on an abstraction level above specific/direct memory allocation.

### Linked List Implementation in C

- here, we are going to implement linked list in C to see a concrete example of how linked lists are stored in memory.
- in the code below, after includiong the libraries, we create a node struct which is like a class that represents what a node is - the node contains data and a pointer to the next node.
- the `createNode()` function allocates memory for a new node, fills in the data part of the node with an integer given as an argument to the function, and returns the pointer (memory address) to the new node.
- the `printList()` function is just for going through the linked list and printing each node's value.
- inside the `main()` function, four nodes are created, linked together, printed, adn then the memory is freed. It isa good practise to free memory after we are done using it to avoid memory leaks. Memory leak is when memory is not freed after use, gradually taking up more and more memory.

- eg. - here, we are creating a basic linked list in C.
`
#include <stdio.h>
#include <stdlib.h>

typedef struct node{
    int data;
    struct Node* next;
} Node;

Node* createNode(int data){
    Node* newNode = (Node*)malloc(sizeof(Node));
    if (!newNode){
        printf('Memory allocation failed!\n');
        exit(1)
    }

    newNode -> data = data;
    newNode -> next = NULL;
    return newNode;
}

void printList (Node* node){
    while (node){
        printf('%d -> ', node -> data);
        node = node -> next;
    }

    printf('null\n');
}

int main(){
    Node* node1 = createNode(3);
    Node* node2 = createNode(5);
    Node* node3 = createNode(13);
    Node* node4 = createNode(2);

    node1->next = node2;
    node2->next = node3;
    node3->next = node4;

    printList(node1);

    //freeing memory
    free(node1);
    free(node2);
    free(node3);
    free(node4);

    return 0;
}
`

- to print the linked list in the code above, `printList()` function goes from one node to the next using the 'next' pointers, and that is called 'traversing' or 'traversal' of the linked list.

### Linked List Implementation in Python and Java

- in python code for linked list, the `Node` class represents what a node is - the node contains data and a link to the next node.
- the `Node` class is used to create four nodes, the nodes are then linked together, and printed at the end.
- the python code is a lot shorter than C code, and perhaps better if you just want to understand the concept of linked lists, and how they are stored in memory.
- The Java code is also very similar to Python code for linked lists.

- eg. - linked list code example in python - 
`
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(3)
node2 = Node(3)
node3 = Node(13)
node4 = Node(2)

node1.next = node2
node2.next = node3
node3.next = node4

currentNode = node1
while currentNode:
    print(currentNode.data, end = ' -> ')
    currentNode = currentNode.next

print('null')
`

## Linked Lists Types

- there are usually three basic types of linked lists - 
    - singly linked lists
    - doubly linked lists
    - circular linked lists


**Singly linked lists**

- a singly linked list is the simplest kind of linked list. It takes up less space in memory because each node has only one address to the next node.

-   | data |    | data |    | data |
    | next | -> | next | -> | next | -> null (these next arrows will poit to data in the next node not next itself)


**Doubly linked lists**

- A doubly linked list has nodes with addresses to both the previous and the next node, and therefore takes up more memory. But doubly linked lists are good if you want to be able to move both up and down in the list.

- null <-| prev | <- | prev | <- | prev |
        | data |    | data |    | data |
        | next | -> | next | -> | next | -> null (these next arrows will poit to data in the next node not next itself)

**Circular linked lists**

- a circular linked list is like a singly or doubly linked list with the first node, the 'head', and the last node, the 'tail', connected.
- in singly or doubly linked list, we can find the start and end of a list by just checking if the links are `null`. But for circular linked list, more complex code is needed to explicitly check for start and end nodes in certain applications.
- circular linked lists are good for lists you need to cycle through continuously.

- note that, what kind of linked list you need depends on the problem you're trying to solve.


### Linked List Implementations

- here are the basic implementations of -
    - singly linked list
    - doubly linked list
    - circular singly linked list
    - circular doubly linked list


#### Singly Linked List Implementation

-   | data |    | data |    | data |
    | next | -> | next | -> | next | -> null (these next arrows will poit to data in the next node not next itself) 
    
- example implementation of singly linked list -
- here's a basic singly linked list in py -
`
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(3)
node2 = Node(5)
node3 = Node(13)
node4 = Node(2)

node1.next = node2
node2.next = node3
node3.next = node4

currentNode = node1
while currentNode:
    print(currentNode.data, end=' -> ')
    currentNode = currentNode.next

print('null')
`

#### Doubly Linked List Implementation

- null <-| prev | <- | prev | <- | prev |
        | data |    | data |    | data |
        | next | -> | next | -> | next | -> null (these next arrows will poit to data in the next node not next itself)

- example implementation of doubly linked list -
- here's a basic doubly linked list in py -
`
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

node1 = Node(3)
node2 = Node(5)
node3 = Node(13)
node4 = Node(2)

node1.next = node2

node2.prev = node1
node2.next = node3

node3.prev = node2
node3.next = node4

node4.prev = node3

print('\nTraversing forward: ')

currentNode = node1

while currentNode:
    print(currentNode.data, end=' -> ')
    currentNode = currentNode.next
print('null')

print('\nTraversing backward: ')
currentNode = node4

while currentNode:
    print(currentNode.data, end= ' -> ')
    currentNode = currentNode.prev
print('null')
`

#### Circular Singly Linked List Implementation

-   | data |    | data |    | data |
    | next | -> | next | -> | next | -> node1 (these next arrows will poit to data in the next node not next itself)

- example implementation of circular singly linked list -
- here's a basic circular singly linked list in py -
`
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(3)
node2 = Node(5)
node3 = Node(13)
node4 = Node(2)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node1 // this makes the singly list into a circular one

currentNode = node1
startNode = node1 // this is how the program knows when to stop so that it only goes through the list one time.
print(currentNode.data, end=' -> ')
currentNode = currentNode.next

while currentNode != startNode:
    print(currentNode.data, end=' -> ')
    currentNode = currentNode.next

print('...')
`

#### Circular Doubly Linked List Implementation

- null <-| prev | <- | prev | <- | prev |
        | data |    | data |    | data |
        | next | -> | next | -> | next | -> null (these next arrows will poit to data in the next node not next itself)

- example implementation of circular doubly linked list -
- here's a basic circular doubly linked list in py -
`
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

node1 = Node(3)
node2 = Node(5)
node3 = Node(13)
node4 = Node(2)

node1.next = node2
node1.prev = node4 // this makes the doubly linked list into a circular one

node2.prev = node1
node2.next = node3

node3.prev = node2
node3.next = node4

node4.prev = node3
node4.next = node1 // this makes the doubly linked list into a circular one

print('\nTraversing forward: ')

currentNode = node1
startNode = node1 // this is how the program knows when to stop so that it only goes through the list one time.

print(currentNode.data, end=' -> ')
currentNode = currentNode.next

while currentNode != startNode:
    print(currentNode.data, end=' -> ')
    currentNode = currentNode.next
print('...')

print('\nTraversing backward: ')
currentNode = node4
startNode = node4
print(currentNode.data, end=' -> ')
currentNode = currentNode.prev

while currentNode != startNode:
    print(currentNode.data, end= ' -> ')
    currentNode = currentNode.prev
print('...')
`



## Linked Lists Operations

- basic things we can do with linked lists are -
    - traversal
    - removing a node
    - inserting a node
    - sorting

### Traversal of a Linked List

- traversing a linked list means to go through the linked list by following the links from one node to the next.
- traversal of linked lists is typically done to search for a specific node, and read or modify the node's content, remove the node, or insert a node right before or after the node.
- to traverse a singly linked list, we start with the first node in the list, the head node, and follow that node's next link, and the next node's next link and so on, until the next address is null.

- here, the code below prints out the node values as it traverses along the linked list - in the example below, we are traversing a singly linked list in py -
`
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverseAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end = ' -> ')
        currentNode = currentNode.next

    print('null')

node1 = Node(70)
node2 = Node(170)
node3 = Node(700)
node4 = Node(70453)
node5 = Node(702311)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

traverseAndPrint(node1)
`

### Find the Lowest Value in a Linked List

- here, we want to find the lowest value in a singly linked list by traversing it and checking each value.
- finding the lowest value ina linked list is very similar to how we found the lowest value in an array, except that we need to follow the next link to get to the next node.
- to find the lowest value, we need to traverse the list like in the previous code. But in addition to traversing the list, we must also update the current lowest value when we find a node with a lower value.

- eg. - here, we are finding the lowest value in a singly linked list by creating a function in py -
`
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def findLowestValue(head):
    minValue = head.data
    currentNode = head.next
    
    while currentNode:
        if currentNode.data < miValue:
            minValue = currentNode.data
        currentNode = currentNode.next
    return minValue

node1 = Node(702311)
node2 = Node(170)
node3 = Node(700)
node4 = Node(70453)
node5 = Node(70)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print('Lowest valie in the linked list is: ', findLowestValue(node1))

`

- in the algorithm above, these lines are the core lines for the algo. The initial lowest value is set to be the value of the first node. Then, if a lower value is found, the lowest value variable is updated.
`
    minValue = head.data

        if currentNode.data < minValue:
            minValue = currentNode.data
`

### Delete a Node in a Linked List

- here, in this case, we have the link (or pointer or address) to a node that we want to delete.
- it is important to connect the nodes on each side of the node before deleting it, so that the linked list is not broken.
- so, before deleting the node, we need to get the next pointer from the previous node, and connect the previous node to the new next node before deleting the node in between.
- in a singly linked list, like we have here, to get the next pointer from the previous node, we actually need to traverse the list from the start, because there is no way to go backwards fromthe node we want to delete.

- also, its a good idea to first connect the next pointer to the node after the node we want to delete, before we delete it. This is to avoid a 'dangling' pointer that points to nothing, even if it is just for a brief moment.
- in the code below, the algorithm to delete a node is moved into a function called deleteSpecificNode.
- eg. - here, we are deleting a specific node in a singly linked list in py - 
`
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverseAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end='->')
        currentNode = currentNode.next
    print('null')

def deleteSpecificNode(head, nodeToDelete):
    if head == nodeToDelete:
        return head.next

    currentNode = head
    while currentNode.next and currentNode.next != nodeToDelete:
        currentNode = currentNode.next

    if currentNode.next is None:
        return head

    currentNode.next = currentNode.next.next

    return head

node1 = Node(70)
node2 = Node(170)
node3 = Node(700)
node4 = Node(70453)
node5 = Node(702311)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print('Before node deletion: ')
traverseAndPrint(node1)

#deleting node 2
node1 = deleteSpecificNode(node1, node2)

print('After node deletion: ')
traverseAndPrint(node1)
`

- in the `deleteSpecificNode` function above, the return value is the new head of the linked list. So, for example, if the node to be deleted is the first node, the new head returned will be the next node.


### Insert a Node in a Linked List

- inserting a node into a linked list is very similar to deleting a node, because in both cases we need to take care of the next pointers to make sure we do not break the linked list.
- to insert a node in a linked list, we first need to create the node, amd then at the position where we insert it, we need to adjust the pointers so that the previous node points to the new node, and the new node points to the correct next node.

- here's how it will work - 
    - new node is created
    - node 1 is linked to new node
    - new node is linked to next node 

- eg - here, we are inserting a node in a singly linked list in py - 
`
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverseAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end='->')
        currentNode = currentNode.next
    print('null')

def insertNodeAtPosition(head, newNode, position):
    if position == 1:
        newNode.next = head
        return newNode

    currentNode = head
    for _ in range(position - 2):
        if currentNode is None:
            break
        currentNode = currentNode.next

    newNode.next = currentNode.next
    currentNode.next = newNode
    return head

node1 = Node(70)
node2 = Node(170)
node3 = Node(700)
node4 = Node(70453)
node5 = Node(702311)

node1.next = node2
node2.next = node3
node3.next = node4

print('Original list: ')
traverseAndPrint(node1)

#inserting a new node with value = 9899 at position 3
newNode = Node(9899)
node1 = insertNodeAtPosition(node1, newNode, 3)

print('\nAfter inserting: ')
traverseAndPrint(node1)
`

- in the `insertNodeAtPosition()` function above, the return value is the new head of the linked list. So, for example, if the node is inserted at the start of the linked list, the new head returned will be the new node.

### Other Linked Lists Operations

- other than the three basic linked list operations - traversal(or search), node deletion, and node insertion, there are a lot of other operations that could be done with a linked list, like sorting.
- we could perform many sorting algorithms on linked lists as well. Like selection sort for example, in selection sort, we find the lowest value, remove it, and insert it at the beginning. We could do the same with a linked list as well.
- note that, we cant sort linked lists with sorting algorithm like Counting sort, Radix sort, or Quicksort, because they use indexes to modify an array elements directly based on their position.

### Differences between a Linked List and an Array

here're some properties of linked lists compared to arrays -

- linked lists are not allocated to a fixed size in memory like arrays are, so linked lists do not require to move the whole list into a larger memory space when the fixed memory space fills up, like arrays must.

- linked list nodes are not laid out one right after the other in memory (contiguous), so linked list nodes do not have to be shifted up or down in memory when one node is inserted or deleted. They just need to be pointed to, whatever space in memory they are located at.

- linked list nodes require more memory to store one or more links to the other nodes. Array elements do not require that much memory, because array elements do not contain links to the other elements.

- linked list operations are usually harder to program and require more lines of code than similar array operations, because programming languages have better built in support for arrays.

- we must traverse a linked list to find a node at a specific position, but with arrays, we can access an element directly by writing `myArray[5]`.

note that, when using arrays in a programming language like Java or Pythion, even though we do not need to write code to handle when an array fills uip its memory space, and we do not have to shift elements up or down in memory when an element is removed or inserted, these thigns still happen in the background and can cause problems in time critical applications.

### Time Complexity of Linked Lists Operations

here, we discuss the time complexity of linked list operations and comapre them to the arrays ones - 

- remember that, time complexity just says something about the approximate number of operations needed by the algorithm based on a large set of data `n`, and it does not tell us the exact time a specific implementation of an algorithm takes.

- what it means is that - even though linear search is aid to have the same time complexity for arrays as for linked lists - `Big O(n)`, it does not mean they take the same amount of time. The exact time it takes for an algorithm to run depends on the programming language, compuuter hardware, differences in time needed for operations on arrays vs linked lists, and other things as well.

- linear search for a linked list works the same as it does for arrays. A list of unsorted values are traversed from the head node until the node with the specific valus is found. Time complexity is - `Big O(n)`.

- binary search, however, is not possible for linked lists, because the algorithm is based on jumping  directly to different array elements, and that is not possible with linked lists.

- sorting algorithms have the same time complexities as for arrays. But remember that sorting algorithms that are based on directly accessing an array element based on an index, do not work on linked lists.


## Stacks

- a stack is a data structure that can hold many elements.
- think of stacks like a pile of pancakes - one on top of the other.
- so, in a pile of pancakes, the pancakes are both added and removed from the top. So, when removing a pancake, it will always be the last pancake you added. This way of organizing elements is called LIFO - Last In, First Out.

- basic operations for stacks we can do are - 
    - Push - adds a new element on top of the stack.
    - Pop - removes and returns the top element from the stack.
    - Peek - returns the top element on the stack.
    - isEmpty - checks if the stack is empty or not.
    - Size - finds the number of elements in the stack.

- stacks can be implemented by using arrays or linked lists.
- stacks can be used to implement undo mechanisms, to revert to previous states, to create algorithms for depth-first search in graphs, or for backtracking.
- stacks are often mentioned together with Queues, which is a similar data structure.

### Stack Implementation using Arrays

- reasons to implement stacks using arrays - 
    - Memory Efficient - array elements do not hold the next element address like linked lists nodes do.
    - Easier to Implement and Understand - using arrays to implement stacks require less code than using linked lists, and for this reason, it is typically easier to understand as well.

- a reason for NOT using arrays to implement stacks -
    - Fixed size - an array occupies a fixed part of the memory. This means that it could take up more memory than needed, or if the array fills up, it can't hold more elements.

- note that, when using arrays in python, we are using lists data type instead of arrays - because python doesnt have arrays. However, lists can also be used in the same way as an array.

- also, since python lists has good support for functionality needed to implement stacks, we start with creating a stack and do stack operatios with just a few lines like the example below.

- eg. - using python - implementing stacks - 
`
stack = [] #empty stack

#push
stack.append('X')
stack.append('Y')
stack.append('Z')
print('Stack: ', stack)

#pop
element = stack.pop()
print('Popped element: ', element)

#Peek
topElement = stack[-1]
print('Peeked element: ', topElement)

#isEmpty
isEmpty = not bool(stack)
print('isEmpty: ', isEmpty)

#size
print('Stack's size: ', len(stack))
`

- however, to explicitly create a data structure for stacks, with basic operations, we should create a stack class instead. This way of creating stacks in python is also more similar to how stacks can be created in other programming languages like C and Java.

- eg. - creating a stack data structure in py -  
`
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty:
            return 'Stack is Empty'
        return self.stack.pop()

    def peek(self);
        if self.isEmpty:
            print('Stack is empty')
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

#creating a new stack
newStack = Stack()

newStack.push('O')
newStack.push('P')
newStack.push('Q')

print("Stack: ", newStack.stack)

print("Pop: ", newStack.pop())

print("Peek: ", newStack.peek())

print("isEmpty: ", newStack.isEmpty())

print("Size: ", newStack.size())
`

### Stack Implementation using Linked Lists

- a reason for using linked lists to implement stacks - 
    - Dynamic Size - the stack can grow and shrink dynamically, unlike with arrays.

- reasons for NOT using linked lists to implement stacks -
    - Extra memory - each stack element must contain the address to the next element (the next linked list node)
    - Readability - the code might be harder to read and write for some beacuse it is longer and more complex.

- implementing stacks using linked lists in py -
`
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return 'Stack is empty'
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.value

    def peek(self):
        if self.isEmpty():
            return 'Stack is empty'
        return self.head.value

    def isEmpty(self):
        return self.size == 0

    def stackSize(self):
        return self.size

newStack = Stack()
newStack.push('M')
newStack.push('N')
newStack.push('O')

print("Pop: ", newStack.pop())
print("Peek: ", newStack.peek())
print("isEmpty: ", newStack.isEmpty())
print("Size: ", newStack.stackSize())
`

## Queues

- a queue is a data structure that can hold many elements.
- think of queue as people standing in line in a supermarket.
- the first person to stand in line is also the first who can pay and leave the supermarket. This way of organizing elements is called FIFO - First In, FIrst Out.

- basic operations you can do on queues are -
    - Enqueue - adds a new element to the queue.
    - Dequeue - removes and returns the first (front) element from the queue.
    - Peek - returns the first element in the queue.
    - isEmpty - checks if the queue is empty.
    - Size - finds the number of elements in teh queue.

- queues can be implemented by using arrays or linked lists.
- queues can be used to implement job scheduling for an office printer, order processing for e-tickets, or to create algorithms for breadth-first seach in graphs.

### Queue Implementation using Arrays

- you can use both linked lists and arrays to implement and create queues.
- an array based queue will look like this - [2, 3, 4, 5, 9]

- reasons to implement queues using arrays - 
    - Memory Efficient - array elements do not hold the next elements address like linked lists do.
    - Easier to Implement and understand - using arrays to implement queues require less code than using linked lists, and for this reason, it is typically easier to understand as well.

- reasons for NOT using arrays to implement queues -
    - Fixed size - an array occupies a fixed part of the memory. This means that it could take up more memory than needed, or if the array fills up, it cant hold more elements. And resizing an array can be costly - both in space and time-wise.
    - SHifting cost - dequeue causes the first element in a queue to be removed, and the other elements must be shifted to take the removed elements' place. This is  inefficient and can cause problems, especially if the queue is long.
    - Alternatives - some programming languages have built-in data structures optimized for queue operations that are better than using arrays.

- note that, when using arrays in python, we are using lists instead of arrays - because there's no arrays in python, just lists - which works similar to arrays.

- and since python's lists have good support for functionality needed to implement queues, we start with creating a queue and do queue operations with just a few lines of code -
- eg. - creating a queue using python -
`
queue = []

#enqueue
queue.append('X')
queue.append('Y')
queue.append('Z')
print('Queue: ', queue)

#dequeue
element = queue.pop(1)
print('Dequeued element: ', element)

#peek
frontElement = queue[0]
print('Peek result: ', frontElement)

#isEmpty
isEmpty = not bool(queue)
print('isEmpty result: ', isEmpty)

#size
print('Queue's Size: ', len(queue))
`

- however, but to explicitly create a data structure for queue, with basic operations, we should create a queue class instead. This way of creating queue in python is also more similar to how queues can be created in other programming languages like C and Java -
- eg. - creating queue using python class-
`
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if self.isEmpty():
            return 'Queue is empty'
        return self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            return 'Queue is empty'
        return self.queue[0]

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

#creating a new queue
newqueue = Queue()

newqueue.enqueue('o')
newqueue.enqueue('p')
newqueue.enqueue('q')
print('Queue enqueued: ', newqueue.queue)

print("Queue dequeued: ", newqueue.dequeue())

print("Queue peeked: ", newqueue.peek())

print("Queue isEmpty: ", newqueue.isEmpty())

print("Queue size: ", newqueue.size())
`

### Queue Implementation using Linked Lists

reasons for using Linked lists to implement queues -
    - Dynamic Size - the queue can grow and shrink dynamically, unlike with arrays.
    - No Shifting - the front element of the queue can be removed(enqueue) without having to shift other elements in the memory.

Reasons for NOT using linked lists to implement queue -
    - Extra Memory - each queue element must contain the address to the next element (the next linked list node).
    - Readability - the code might be harder to read and write for some because it is longeer and more complex.

- implementing a queue using a linked list in py-
`
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.back = None
        self.length = 0

    def enqueue (self, element);
        newNode = Node(element)
        if self.back is None:
            self.front = self.back = newNode
            self.length += 1
            return

        self.back.next = newNode
        self.back = newNode
        self.length += 1

    def dequeue(self):
        if self.isEmpty():
            return 'Queue is empty'
        temp = self.front
        self.front = temp.next
        self.length -= 1
        if self.front is None:
            self.back = None
        return temp.data

    def peek(self):
        if self.isEmpty():
            return 'Queue is empty'
        return self.front.data

    def isEmpty(self):
        return self.length == 0

    def size(self):
        return self.length

    def printQueue(self):
        temp = self.front
        while temp:
            print(temp.data, end='')
            temp = temp.next
        print()

#creating a queue
myQueue = Queue()

myQueue.enqueue('X')
myQueue.enqueue('Y')
myQueue.enqueue('Z')
print("Queue: ", end="")

print("Dequeue: ", myQueue.dequeue())

print("Peek: ", myQueue.peek())

print("isEmpty: ", myQueue.isEmpty())

print("Size: ", myQueue.size())

`

## Hash Tables

- a hash table is a data structure designed to be fast to work with.
- the reason hash tables are sometimes preferred instead of arrays of linked lists is because searching for, adding, and deleting data can be done really quickly, even for large amounts of data.
- in a linked list, finding a person named 'Bob' takes time because we would have to go from one node to the next, checking each node, until the node with 'Bob' is found.
- and finding 'Bob' in an Array could be fast if we knew the index, but when we only know the name Bob, we need to compare each element (like with Linked List), and that takes time.

- however, with hash table, finding 'Bob' is done really fast because there is a way to go directly to where 'Bob' is stored, using something called a hash function.

### Building a Hash Table from Scratch

here, we are building a hash table from scratch, and storing unique first names inside it -
we are building hash set in 5 steps - 
    1. start with an array
    2. store names using a hash function
    3. look up an element using a hash function
    4. handle collisions
    5. the basic hash set code example and simulation.

#### 1.Starting with an Array

using an array, we can store names like this -
`
myArray = ['Pete', 'Jones', 'Lisa', 'Bob', 'Siri']
`

- to find 'bob' in the array above, we need to compare each name, element by element, until we find 'bob'.
- if the array was sorted alphabetically, we could use Binary Search to find the name quickly, but inserting or deleting names in the array would mean a big operation of shifting elements in memory.
- to make interacting with the list of names really fast, we will use a hash table for this instead, or a Hash set, which is a simplified version of a Hash Table.
- to keep it simple, we will assume there is at most 10 names in the list, so the array must be a fixed size of 10 elements. When talking about hash tables, each of these elements is called a bucket.

`
myHashSet = [None,None,None,None,None,None,None,None,None,None]
`

#### 2. Storing names using a hash function

- now, comes the special way we interact with the Hash Set we are making.
- we want to store a name directly into its right place in the array, and this is where the `hash function` comes in.
- a hash function can be made in many ways, it is up to the creator of the Hash Table(you). A common way is to find a way to convert the value into a number that equals one of the Hash Set's index numbers, in this case a number from 0 to 9. In our example, we will use the Unicode number of each character, summarize them and do a modulo 10 operation to get index numbers 0-9.

- example -
`
def hashFunc(value):
    sumOfChars = 0
    for char in value:
        sumOfChars += ord(value) #ord() func returns the number representing the unicode code of a specified character - here, Bob

    return sumOfChars % 10

print('Bob has hash code: ', hashFunc('Bob'))
`

- the character 'B' has Unicode code point 66, 'o' has 111, 'b' has 98. Adding all of those numbers, we get 275. Modulo 275 is 5 - `275%10`. So, 'Bob', should be stored as an array element at index 5.
- the number returned by the hash function is called the hash code.

- after storing 'Bob' where the hash code tells us (index 5), our array looks like this -
`
myHashSet = [None,None,None,None,None,'Bob',None,None,None,None]
`

- we can now use the hash function to find out where to store the other names like - Pete, Jones, Lisa and Siri.
- after using the hash function to store the other names in the correct position, our array looks something like this -
`
myHashSet = [None,'Jones',None,'Lisa',None,'Bob',None,'Siri','Pete',None]
`

**Unicode Number**

- everything in our computers are stored as numbers, and the UNICODE code point is a unique number that exists for every character.
- For example, the character 'A' has a UNICODE number (also called as Unicode Code Point) of `65`.

**Modulo Operator**

- a mathematical operation, written as `%` in most programming languages (or `mod` in maths). A modulo operation divides a number with another number, and gives us the resulting remainder. 
- So, for example, `7 % 3` will give us the remainder `1`. (In other words, dividing 7 apples between 3 people means, that each person gets 2 apples, with 1 apple to spare - so modulo gives you the spare value.)

#### 3. Looking up a name using a Hash Function

- we now have established a super basic Hash Set, because we do not have to check the array element anymore to find out if 'Pete' is in there, we can just use the hash function to go straight to the right answer.
- to find out if 'Pete' is stored in the array, we give the name 'Pete' to our hash function, we get back the hash code 8, we go directly to the element at index 8, and we find our value. This way, we found our value - 'Pete' without checking any other elements.

- eg. -
`
myHashSet = [None,'Jones',None,'Lisa',None,'Bob',None,'Siri','Pete',None]

def hashFunc(value):
    sumOfChars = 0
    for char in value:
        sumOfChars += ord(value)

    return sumOfChars % 10

def containsValue(name):
    index = hashFunc(name)
    return myHashSet[index] == name

print("'Pete' is in Hash Set: ', contains('Pete'))
`

- when deleting a name from our Hash Set, we can also use the hash function to go straight to where the name is, and set that elements value to `None`.

#### Handling Collisions

- now, we're adding 'Stuart' to our Hash Set.
- we give, 'Stuart' to our hash function, and we get the hash code 3, meaning, 'Stuart' should be stored at index 3.
- trying to store 'Stuart' creates a whats called `collision` because 'Lisa' is already stored at index 3.
- to fix this collision, we can make room for more elements in the same bucket, and solving the collision problem in this way is called `chaining`. We can give room for more elements in the same bucket by implementing each bucket as a linked list, or as an array.
- after implementing each bucket as an array, to give room for potentially more than one name in each bucket. 'Stuart' can also be stored at index 3, and our Hash Set now looks like this -
`
my_hash_set = [
    [None],
    ['Jones'],
    [None],
    ['Lisa', 'Stuart'],
    [None],
    ['Bob'],
    [None],
    ['Siri'],
    ['Pete'],
    [None]
]
`

- searching for 'Stuart' in our Hash Set now means that using the hash function we end up directly in bucket 3, but then, we must first check 'Lisa' in that bucket, before we find 'Stuart' as the second element in bucket 3.

#### Hash Set Code example and simulation

- to complete our very basic Hash Set code, lets have functions for adding and searching for names in the Hash Set, which is now a two dimensional array.
`
myHashNewSet = [
    [None],
    ['Jones'],
    [None],
    ['Lisa'],
    [None],
    ['Bob'],
    [None],
    ['Siri'],
    ['Pete'],
    [None]
]

def hashFunction(value):
    return sum(ord(char) for char in value) % 10

def add(value):
    index = hashFunction(value)
    bucket = myHashNewSet[index]
    if value not in bucket:
        bucket.append(value)

def contains(value):
    index = hashFunction(value)
    bucket = myHashNewSet[index]
    return value in bucket

add('Stuart')

print(myHashNewSet)
print('Contains Stuart: ', contains('Stuart'))

`

### Use of Hash Tables

hash tables are great for -
    - checking if something is in a collection(like finding a book in a library)
    - storing unique items and quickly finding them (like storing phone numbers)
    - connecting values to keys (like linking names to phone numbers)

- the most important reason why Hash Tables are great for these things is that Hash Tables are very fast compared to Arrays and Linked Lists, especially for large sets. Arrays and Linked Lists have time complexity of `BigO(n)` for search and delete, while Hash Tables have the Time Complexity for the same functions - `Big O(1)` on average.

### Hash Set vs Hash Map

a hash table can be a Hash Set or a Hash Map. we will learn more about them in the upcoming sections.
here's a how hash sets and hash maps are different and similar - 

| Features | Hash Sets | Hash Maps |
| -------- | ------- | ------------ |
| Uniqueness and Storage | Every element is a unique key | every entry is a key-value-pair, with a key that is unique, and a value connected to it. |
| Use Cases | Checking if an element is in the set, like checking if a name is on a guest list. | finding information based on a key, like looking up who owns a certain telephone number. |
| Is it fast to search, add, and delete elements? | yes, average time complexity - Big O(1) | yes, average time complexity - Big O(1) |
| Is there a hash function that takes the key, generates a hash code, and that is the bucket where the element is stored? | Yes | Yes |

### Hash Tables Summarized

- Hash Table elements are stored in storage containers called **buckets**.
- every Hash Table element has a part that is unique thatr is called the **key**.
- a **Hash Function** takes the key of an element to generate a **hash code**.
- the hash code says what bucket the element belongs to, so now we can go directly to that hash table element - to modify it, or to delete it, or just to check if it exists.
- a **collision** happens when two hash table elements have the same hash code, because that means that they belong to the same **bucket**. A collision can be solved in two ways.
    - **Chaining** is the way collisions are solved, by using arrays or linked lists to allow more than one element in the same bucket.
    - **Open Addressing** is another way to solve collissions. with open addressing, if we want to store an element but there is already an elelment in that bucket, the element is then stored in the next available bucket. this can be done in many different ways.

**So, what are hash tables good for?**
- hash tables are powerful tools in programming, they help manage and access data efficiently.
- whether you use hash set or hash map, depends on what you need - just to know if something is there, or to find detailed information about it.


## Hash Sets

- a Hash Set is a form of hash table data structure that usually holds a large number of elements.
- using a Hash Set, we can search, add, and remove elements really fast.
- Hash Sets are used for lookup (search), to check if an element is part of a set or not.

- a hash set stores unique elements in buckets according to the element's hash code.
    
    - Hash Code - a number generated from an element's unique value (key), to determine what bucket that hash set element belongs to.
    - Unique Elements - a hash set cannot have more than one element with the same value.
    - Bucket - a Hash Set consists of many such buckets, or containers, to store elements. If two elements have the same hash code, they belong to the same bucket. The buckets are therefore often implemented as arrays or linked lists, because a bucket needs to be able to hold more than one element.


### Finding the Hash Code

- a hash code is generated by a **hash function**.
- the hash function takes the name written in the input, and sums up the Unicode code points for every character in that name.
- after that, the hash function does a modulo 10 operation (% 10) on the sum of characters to get the hash code as a number from 0 to 9.
- this means that a name is put into one of the ten possible buckets in the hash set, according to the hash code of that name. the same hash code is generated and used when we want to search for or remove a name from the hash set.
- the hash code gives us instant access as long as there is just one name in the corresponding bucket.

- Unicode code point - everything in our computers are stored as numbners, and the Unicode code point is a unique number that exist for every character. For example, the character `A` has Unicode code point `65`.
- Modulo - a mathematical operation, written as `%` in most programming languages (or mod in maths). A modulo operation divides a number with another number, and gives us the resulting remainder. So, for example, `7 % 3` will give us the remainder 1. (Dividing 7 apples between 3 people, means that each person gets 2 apples, with 1 apple remaining.)

### Direct Access in Hash Sets

- searching for `Peter` in a hash set in the above example means that the hash code `2` is generated (512 % 10), and that directs us right to the bucket `Peter` is in. If that is the only name in that bucket, we will find `Peter` right away.
- in cases like this, we say that the hash set has constant time Big O(1) for Searching, Adding, and Removing elements, which is really fast.
- But, if we search for `Jens`, we need to search through the other names in that bucket before we find `Jens`. Inn a worst case scenario, all the names end up in the same bucket, and the name we are searching for is the last one. IN such a worst case scenario the Hash Set has time Complexity of Big O (n), which is the same time complexity as arrays and linked lists.
- to keep Hash Sets fast, it is therefore important to have a hash function that will distribute the elements evenly between the buckets, and to have around as many buckets as Hash Set elements.
- having a lot more buckets than Hash Set eklements is a waste of memory, and having a lot less buckets than Hash Set elements is a waste of time.

### Hash Set Implementation

- Hash Sets in python are typically done by using Python's own - `Set` data type, but to get a better understanding of how Hash Sets work we will not use that here.
- to implement a Hash Set in python, we create a class `SimpleHashSet`.
- inside the `SimpleHashSet` class, we have a method called - `__init__` to initialize the hash set, a method `hash_function` for the hash function, and methods for the basic Hash Set operations - `add`, `contains` and `remove`.
- we also create a method `print_set` to better see how the Hash Set looks like -

- example - 
`
class SimpleHashSet:
    def __init__(self, size=100):
        self.size = size
        self.buckets = [[] for _ in range(size)] # a list of buckets, each is a list (to handle collisions)

    def hash_function(self, value):
        #add a value if its not already present
        index = self.hash_function(value)
        bucket = self.buckets[index]
        if value not in bucket:
            bucket.append(value)

    def contains(self, value)
        #check if a value exists in the set
        index = self.hash_function(value)
        bucket = self.buckets[index]
        return value in bucket

    def remove(self, value):
        #remove a value
        index = self.hash_function(value)
        bucket = self.buckets[index]
        if value in bucket:
            bucket.remove(value)

    def print_set(self):
        #prints all elements in the hash set
        print('Hash Set Contains: ')
        for index, bucket in enumerate(self.buckets):
            print(f'Bucket {index}: {bucket}')
`

- using the `SimpleHashSet` class, we can not create Hash Sets.

- example - 
`
class SimpleHashSet:
    def __init__(self, size=100):
        self.size = size
        self.buckets = [[] for _ in range(size)] # list of buckets, each is a list (to handle collisions)

    def hash_function(self, value):
        #simple hash function:sum of character codes modulo the number of buckets
        return sum(ord(char) for char in value) % self.size

    def add(self, value):
        #add a value if its not already present
        index = self.hash_function(value)
        bucket = self.buckets[index]
        if value not in bucket:
            bucket.append(value)

    def contains(self, value):
        #check if a value exists in the set
        index = self.hash_function(value)
        bucket = self.buckets[index]
        return value in bucket

    def remove(self, value):
        #removes a value
        index = self.hash_function(value)
        bucket = self.buckets[index]
        if value in bucket:
            bucket.remove(value)

    def print_set(self):
        #print all elements in the hash set
        print("Hash Set Contents: ")
        for index, bucket in enumerate(self.buckets):
            print(f"Bucket {index}: {bucket}")

#creaating the hash set
hash_set = SimpleHashSet(size=10)

hash_set.add("Charolette")
hash_set.add("Thomas")
hash_set.add("Jens")
hash_set.add("Peter")
hash_set.add("Lisa")
hash_set.add("Adele")
hash_set.add("Michaela")
hash_set.add("Bob")

hash_set.print_set()

print("\n'Peter' is in the set:", hash_set.contains('Peter'))
print("Removing 'Peter'")
hash_set.remove('Peter')
print("'Peter' is in the set:",hash_set.contains('Peter'))
print("'Adele' has hash code:",hash_set.hash_function('Adele'))

`

### Hash Maps

- a hash map is a form of hash table data structure that usually holds a large number of entries.
- using a hash map, we can search, add, modify, and remove entries really fast.
- hash maps are used to find detailed information about something.

- it is easier to understand how hash maps work if you first understand about hash tables and hash sets. Also, you should know the meaning of these words -
    
    - **Entry** - consists of a key and a value, forming a key-value pair.
    - **Key** - unique for each entry in the hash map. used to generate a hash code determining the entry's bucket in the hash map. This ensures that every entry can be efficiently located.
    - **Hash COde** - a number generated from an entry's key, to determine what bucket that hash map entry belongs to.
    - **Bucket** - a hash map consists of many such buckets, or containers, to store entries.
    - **Value** - can be nearly any kind of information, like name, birth date, and address of a person. the value can be many different kinds of information combined.


### Finding the Hash Code

- a hash code is generated by a **hash function**.
- the hash function in (in an example) takes the numbers in the social security number (not the dash - 111-211-2321), add them together and does a modulo 10 operation (%10) on the sum of characters to get the hash code as a number from 0 to 9.
- this means that a person is stored in one of ten possible buckets in the Hash Map, according to the hash code of that person's social security number. The same hash code is generated and used when we want to search for or remove a person from the hash map.
- the hash code gives us instant access as long as there is just one person in the corresponding bucket.

**Modulo** - is a mathematical operation, written as `%` in most programming languages (or mod in maths). a modulo operation divides a number with another number, and gives us the resulting remainder. So, for example, `7 % 3` will give us the remainder `1`. Dividing 7 apples between 3 people, means that each person gets 2 apples, with 1 apple remaining.


### Direct Access in Hash Maps

- Searching for `Charolotte`, or any item in Hash Map, we must use the social security number, 123-4567 (in context of the example), - the hash map key, which generates the hash code 8, as explained before.
- this means we can go straight to bucket `8` to get her name (the Hash Map value), without searching through other entries in the Hash Map.
- in cases like this, we say that the Hash Map has constant time O(1) for searching, adding and removing entries, which is really fast compared to using an array or a linked list.
- But in the worst case scenario, all the people are stored in the same bucket, and if the person we're trying to find is the last person in this bucket, we need to compare with all the other social security numbers in that bucket before we find the person we are looking for.
- in such a worst case scenario, the Hash Map has time complexity of O(n) which is the same time complexity as arrays and linked lists.
- to keep the Hash Maps fast, it is therefore important to have a hash function that will distribute the entries evenly between the buckets, and to have around as many buckets as Hash Map entries.
- Having a lot more buckets than Hash Map entries is a waste of memory, and having a lot less buckets than Hash Map entries is a waste of time - so you have to compromise here, between space and time.

**Note:**
- A social security number can be really long, like 11 digits, which means it is possible to store 100 billion people with unique social security numbners. this is a lot more than in any country's population, and even a lot more than there are people on Earth.
- Using an array, where each person's social security number is the index in the array where this person is stored, is therefore a huge waste of space(mostly empty buckets.)
- using a Hash Map(or a database with similar properties), makes more sense as the number of buckets can be adjusted to the number of people.

### Hash Map Implementation

- Hash Maps in python are typically done by using Python's own `dictionary` data type, but to get a better understanding of how Hash Maps work, we will not use that.
- To implement a Hash Map in Python, we create a class `SimpleHashMap`.
- Inside the SimpleHashMap class, we have a method called `__init__`, to initialize the Hash Map, a method `hash_function` for the hash function, and methods for the basic Hash Map operations: put, get, and remove.
- We also create a method print_map, to better see how the Hash Map looks like - 

- example, in code - 
`
class SimpleHashMap:
    def __init__(self, size=100):
        self.size = size
        self.buckets = [[] for _ in range(size)] # a list of buckets, each is a list (to handle collissions.)


    def hash_function(self, key):
        #sum only the numerical values of the key, ignoring the non-numeric characters
        numeric_sum = sum(int(char) for char in key if char.isdigit())
        return numeric_sum % 10 #perform modulo 10 on the sum

    def put(self, key, value):
        #add or update a key-value pair
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value) # update the existing key
                return
        bucket.append((key, value)) #add new key, value pair if not found

    def get(self, key):
        #retrive a value by key
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        return None #key not found

    def remove(self, key):
        #remove a key-value pair
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i] # remove the key-value pair
                return

    def print_map(self):
        #print all key-value pairs in the hash map
        print("Hash Map Contents: ")
        for index, bucket in enumerate(self.buckets):
            print(f"Bucket {index} : {bucket}")

#creating the hash map from the example
hash_map = SimpleHashMap(size = 10)

#adding the entries
hash_map.put("123-4567", "Charlotte")
hash_map.put("123-4568", "Thomas")
hash_map.put("123-4569", "Jens")
hash_map.put("123-4570", "Peter")
hash_map.put("123-4571", "Lisa")
hash_map.put("123-4672", "Adele")
hash_map.put("123-4573", "Michaela")
hash_map.put("123-6574", "Bob")

hash_map.print_map()

#demonstrating retrieval
print("\nName associated with '123-4570' ", hash_map.get("123-4570"))

print("Updating the name for '123-4567' to 'Charizard'")
hash_map.put("123-4567", "Charizard")

#checking if Peter is still there
print("Name associated with '123-4570': ", hash_map.get("123-4570"))
            
`

- using the `SimpleHashMap` class, now we can create the same Hash Map as in the example above.


## Trees

- The tree data structure is similar to Linked Lists, in that each node contains data and can be linked to other nodes.
- Data structures like Arrays, Linked Lists, Stacks and Queues, are all linear structures, which means that each element follows directly after another in a sequence. Trees however, are different.
- In a Tree, a single element can have multiple 'next' elements, allowing the data structure to branch out in various directions.
- the data structure is called a 'tree' because it looks like a tree, only upside down, like a family tree.

- The tree data structure can be useful in many cases - 
    - **Hierarchical Data** - file systems, organizational models, etc.
    - **Databases** - used for quick data retrieval.
    - **Routing Tables** - USed for routing data in network algorithms.
    - **Sorting/Searching** - used for sorting data and searching for data.
    - **Priority Queues** - priority queue data structure are commonly implemented using trees, such as binary heaps.

### Tree Terminology and Rules

- **The Whole Tree** - represents the entire tree.
- **Root Node** - represents the main/first root at the top from which all other branches branch out - the root of the tree.
- **Edges** - are all the branches connecting to and from root to nodes - just the branches/arrows/pointers. A link connecting one node to another node.
- **Nodes** - are all the nodes containing values - even the root is a node - the root node. A node can have zero, one, two or many child nodes. But a node can have only one parent node.
- **Leaf Nodes** - nodes without links to other child nodes are leaf nodes or leaves.
- **Child Nodes** - a parent node has links to its child nodes - child nodes are basically all the nodes that branch out of a parent node.
- **Parent Nodes** - a parent node has links to its child nodes. In other words, all parent nodes have child nodes, if a node doesnt have children/leaves, they are not parent nodes - a root node is also a parent node.
- **Tree Height (h = 2)** - a tree height is the maximum number of edges/vertices/pointers from the root node to a leaf node.
- **Tree Size(n = 10)** - is the number of nodes in the tree - all the nodes - from the root to last child nodes.
- **Height of a Node** - a node's height is the maximum number of edges between the nodes and a leaf node.


### Types of Trees

- trees are a fundamental data structure in computer science, used to represent hierarchical relationships. Here, we'll learn about several key types of trees - 

    - Binary Trees: Each node in this tree has up to two children, the left child node and the right child node. This structure is the foundation for more complex trees types like Binary Search Trees and AVL trees.
    
    - Binary Search Trees(BSTs): A type of Binary Tree where for each node, the left child node has a lower value, and the right child node has a higher value.
    
    - AVL Trees: A type of Binary Search Tree that self-balances so that for every node, the difference in height between the left and right subtrees is at most one. This balance is maintained through rotations when nodes are inserted or deleted.


## Binary Trees

- A binary tree is a type of tree data structure where each node can have a maximum of two child nodes, a left child and a right child node.
- this restriction, that a node can have a maximum of two child nodes, gives us many benefits - 
    - Algorithms like traversing, searching, insertion, and deletion becomes easier to understand, to implement and they run faster.
    - Keeping data sorted in a Binary Search Tree (BST) makes searching very efficient.
    - Balancing trees is easier to do with a limited number of child nodeds, using an AVL Binary TRee for example.
    - Binary Trees can be represented as arrays, making the tree more memory efficient.


### Binary Tree Terminology and Rules

- The Binary Tree - the entire binary tree.
- Root Node -  the main node, parent node of the tree from which all child nodes originate.
- A's Left Child - A is a child of the parent node, and C is A's left child.
- A's Right Child - A is a child of the parent node, and D is A's right child.
- B's subtree -  B is a child of the parent node, from B another sub-tree emerges, which goes till a height of 2.
- Tree Size(n = n) - represents the number of all children nodes present in the tree, including the parent node.
- Tree height(n = n) - the tallest/longest height of the tree, the maximum number of edges from the root node to a leaf node.
- Child Nodes - all nodes that emerge from the parent/root node and its sub nodes.
- Parent/Internal Nodes - represents the parent/root node, or internal node, in a Binary Tree is a node with one or two child nodes.


### Binary Trees vs Arrays and Linked Lists

Benefits of Binary Trees over arrays and linked lists - 
    - Arrays are fast when you want to access an element directly, like element number 700 in an array of 1000 elements for example. But inserting and deleting elements require other elements to shift in memory to make place for the new element, or to take the deleted elements place, and that is time consuming.
    - Linked Lists are fast when inserting or deleting nodes, no memory shifting is needed, but to access an element inside the list, the list must be traversed, and that takes time.
    - Binary Trees, such as Binary Search Trees and AVL Trees, are great compared to Arrays and Linked Lists because they're BOTH fast at accessing a node, AND fast when it comes to deleting or inserting a node, with no shifts in memory needed.


### Types of Binary Trees

-
 
