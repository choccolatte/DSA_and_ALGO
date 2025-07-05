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

- there are different variants, or types of Binary Trees worth discussing to get a better understanding of how Binary Trees can be structured.
- the different kinds of Binary Trees are also worth mentioning now as these words and concepts will be used later in the notes.
- Here're short explanations of different types of Binary Tree structures -
    - A **balanced Binary Tree** has at most 1 in the difference between its left and right sub-tree heights, for each node in the tree.
    - A **complete Binary Tree** has all the levels full of nodes, except the last level, which can also be full, or filled from left to right. The properties of a complete Binary Tree means it is also balanced.
    - A **full Binary Tree** is a kind of tree where each node has either 0 or 2 child nodes.
    - A **perfect Binary Tree** has all leaf nodes on the same level, which means that all levels are full of nodes, and all internal nodes have two child nodes. The properties of a perfect Binary Tree means it is also full, balanced, and complete.

 
### Binary Tree Implementation

- Here,  we are creating a Binary Tree structure where each node can be linked to both its left and right child nodes, instead of linking each node to one next node.

`
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

#Test
print("root.right.left.data:", root.right.left.data)
`


### Binary Tree Traversal

- Going through a tree by visiting every node, one at a time, is called traversal.
- Since Arrays and Linked Lists are linear data structures, there is only one obvious way to traverse these: start at the first element, or node, and continue to visit the next until you have visited them all.
- But since a tree can branch out in different directions (non-linear), there are different ways of traversing Trees.
- There are two main categories of Tree Traversal methods - 
    - Breadth First Search(BFS) - it is when the nodes on the same level are visited before going to the next level in the tree. This means that the tree is explored in a more sideways direction.
    - Depth First Search(DFS) - it is when the traversal moves down the tree all the way to the leaf nodes, exploring the tree branch by branch in a downwards direction.

- There are three different types of DFS traversals - 
    - Pre order
    - In order
    - Post order


## Pre-order Traversal

- pre-order traversal is a type of DFS, where every node is visited in a certain order.
- pre-order traversal is done by visiting the root node first, then recursively do a pre-order traversal of the left suubtree, followed by a recursive pre-order traversal of the right subtree. Its used for creating a copy of the tree, prefix notation of an expression tree, etc.
- This traversal is 'pre' because the node is visited 'before' the recursive pre-order traversal of the left and right subtrees.

- this is how the code for pre-order traversal looks like - 
- example in py
`
def preOrderTraversal(node):
    if node is None:
        return
    print(node.data, end = ", ")
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)
`

- here, the first node to be printed is node R, as the Pre-order traversal works by first visiting,  or printing, the current node (line 4 of example), before calling the left and right child nodes recursively (line 5 and 6 of example).

- the `preOrderTraversal()` function keeps traversing the left subtree recursively (line 5 of example), before going on to traversing the right subtree (line 6 of ex). So, the next nodes that are printed are 'A' and then 'C'.

- the first time the argument `node` is `None`, is when the left child of node C is given as an argument (C has no left child).

-  After `None` is returned the first time when calling C's left child, C's right child also returns `None`, and then the recursive calls continue to propogate back so that A's right child D is the next to be printed.

- The code continues to propagate back so that the rest of the nodes in the R's right subtree gets printed.


## In-Order Traversal of Binary Trees

- In-Order Traversal is a type of DFS, where each node is visited in a certain orer - basically it runs an entire line of nodes in a edge/line. Then, it'll go to the next node of the next line, and so on.

- In-Order Traversal does a recursive In-Order Traversal of the left subtree in a tree, visits the root node, and finally, does a recursive In-Order Traversal of the right subtree. This traversal is mainly used for Binary Search Trees, where it returns values in ascending order.

- What makes this traversal 'in' order, is that the node is visited in between the recursive function calls. The node is visited after the In-Order Traversal of the left subtree, and before the In-Order Traversal of the right subtree.

- example of In-Order Traversal in python
`
def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end = ",")
    inOrderTraversal(node.right)
`

### Explanation

- here, the `inOrderTraversal()` function kefeps calling itself with the current left child node as an argument (line 4 of ex) until  the argument is `None`, and the function returns (line 2-3 of ex).
- The first time the argument `node` is `None`, is when the left child of node C is given as an argument (C has no left child).
- After that, the `data` part of node C is printed (Line 5 of ex), which means that 'C' is the first thing that gets printed.
- Then, node C's right child is given as an argument (line 6 of ex), which is `None`, so the function call returns without doing anything else.
- After 'C' is printed, the previous `inOrderTraversal()` function calls continue to run, so that 'A' gets printed, then 'D' gets printed, then 'R', and so on.


## Post-Order Traversal in Binary Trees

- Post-Order Traversal is a type of DFS, where each node is visited in a certain order - basically it goes deep, and gets the last node first, then goes to the second deepest/last node, and so on.
- It works by recursively doing a Post-Order Traversal of the left subtree and the right subtree, followed by a visit to the root node. It is used for deleting a tree, post-fix notation of an expression tree, etc.
- What makes this traversal 'Post' is that visiting a node is done 'after' the left and right child nodes are called recursively.

- example of Post-Order Traversal in python 
`
def postOrderTraversal(node):
    if node is None:
        return

    postOrderTraversal(node.left)
    postOrderTraversal(node.right)
    print(node.data, end = ", ")
`

### Explanation

- the `postOrderTraversal()` function keeps traversing the left subtree recursively (line 4 of ex), until `None` is returned when C's left child node is called as the `node` argument.
- After C's left child node returns `None`, line 5 runs and C's right child node returns None, and then the letter 'C' is printed (line 6 of ex).
- This means that C is visited, or printed, 'after' its left and right child nodes are traversed, that is why it is called 'post' order traversal.
- The `postOrderTraversal()` function continues to propagate back to previous recursive function calls, so the next node to be printed is 'D', then 'A'.
- The function continues to propagate back and printing nodes until all nodes are printed, or visited.


## Array Implementation of Binary Trees

- to avoid the cost of all the shifts in memory that we get from using an Array, it is useful to implement Binary Trees with pointers from one element to the next, just like Binary Trees are implemented before this point, especially when the Binary Tree is modified often.
- But in case we read fromm the Binary Tree a lot more than we modify it, an array implementation of a Binary Tree can make sense as it needs less memory, it can be easier to implement, and it can be faster for certain operations due to cache locality.

    **Cache Locality**
    - is when the fast cache memory in the computer stores parts of memory that was recently accessed, or when the cache stores parts of memory that is close to the address that is currently accessed. This happens because it is likely that the CPU needs something in the next cycle that is close to what it used in the previous cycle, either close in time or close in space.
    - Since Array elements are stored contiguously in memory, one element right after the other, computers are sometimes faster when reading from arrays because the next element is already cached, available for fast access in case the CPU needs it in the next cycle.

- Consider a Binary tree with Root node - R
    - left child node - A
        - left child of A - C
        - right child of A - D
    - right child node - B
        - left child of B - E
        - right child of B - F
            - child of F - G

- this Binary tree can be stored in an array starting with the root node R on index 0. The rest of the tree can be built by taking a ndoe stored on index i, and storing its left child node on index 2.i + 1, and its right child node on index 2.i + 2.

- here is an array implementation of Binary tree in py - 
`
binary_tree_array = ['R', 'A', 'B', 'C', 'D', 'E', 'F', None, None, None, None, None, None, 'G']

def left_child_index(index):
    return 2 * index + 1

def right_child_index(index):
    return 2 * index + 2

def get_data(index)
    if 0 <= index < len(binary_tree_array):
        return binary_tree_array[index]
    return None

right_child = right_child_index(0)
left_child_of_right_child = left_child_index(right_child)
data = get_data(left_child_of_right_child)

print("root.right.left.data: ", data)
`

- in the array implementation, since the Binary Tree nodes are placed in an array, much of the code is about accessing nodes using indexes, and about how to find the correct indexes.

- lets say, we want to find the left and right child nodes of node B. Because B is on index 2, B's left child is on index 2.2 + 1 = 5, which is node E, right? And B's right child is on index 2.2 + 2 = 6, which is node F, adn that also fits with the code above right?

- as we can see on line 1, this implementation requires empty array elemenets where nodes have no child nodes. So, to avoid wasting space on an empty array elements, Binary Trees stored using Array implementation should be a 'perfect' Binary Tree, or a nearly perfect one.

- a perfect Binary Tree is when every internal node have exactly two child nodes, and all leaf nodes are on the same level.

- if we remove the G node in the Binary Tree we're talking about, we would get a perfectly equal branched node.

- and the first line in the code above can be written without space on empty array elements - 

`
binary_tree_array = ['R', 'A', 'B', 'C', 'D', 'E', 'F']
`

- this is how the three different DFS traversals can be done on an Array Implementation on a Binary Tree -

`
binary_tree_array = ['R', 'A', 'B', 'C', 'D', 'E', 'F', None, None, None, None, None, None, 'G']

def left_child_index(index):
    return 2 * index + 1

def right_child_index(index):
    return 2 * index + 2

def pre_order(index):
    if index >= len(binary_tree_array) or binary_tree_array[index] is None:
        return []
    return [binary_tree_array[index]] + pre_order(left_child_index(index)) + pre_order(right_child_index(index))

def in_order(index):
    if index >= len(binary_tree_array) or binary_tree_array[index] is None:
        return []
    return in_order(left_child_index(index)) + [binary_tree_array[index]] + in_order(right_child_index(index))

def post_order(index):
    if index >= len(binary_tree_array) or binary_tree_array[index] is None:
        return []
    return post_order(left_child_index(index)) + post_order(right_child_index(index)) + [binary_tree_array[index]]

print("Pre-order Traversal:", pre_order(0))
print("In-order Traversal:", in_order(0))
print("Post-order Traversal:", post_order(0))
`

- here, by comparing how these traversals are done in an array implementation to how the pointer implementation was traversed, you can see that the pre-order, in-order, and post-order traversals works in the same recursive way.



## Binary Search Trees

- A Binary Search Tree is a Binary Tree where every node's left child has a lower value, and every node's right child has a higher value.

- a clear advantage with Binary Search Trees is that operations like search, delete, and insert are fast and done without having to shift values in memory.

### Binary Search Trees

- a Binary Search Tree(BST) is a type of Binary Tree data structure, where the following properties must be true for any node "X" in the tree:
    - the X node's left child and all of its descendants (children, children's children, and so on) have lower values than X's value.
    - The right child, and all of its descendants have higher values than X's value.
    - Left and right subtrees must also be Binary Search Trees.

- these properties makes it faster to search, add, and delete values than a regular binary tree.

- to make this as easy to understand and implement as possible, lets assume that all values in a Binary Search Tree are unique.

### Binary Search Tree Concepts and Relevant Terminology

- **Binary Search Tree(BST)** - the entire BST tree.
- **Tree Size(n = n)** - the size of the BST tree. Represents the number of nodes in it (n).
- **Root Node** - represents the main/root node of the BST.
- **7's Left Child** - 7 is one of the branches of root node (13), and its left child is 3.
- **7's Right Child** - 7 is one of the branches of root node (13), and its right child is 8.
- **Tree Height(h = n)** - represents the single longest indices/path from root node to the last node possible in any left or right sides of the tree.
- **15's Height(h = n)** - represents the single longest indices/path from node 15 to the last node possible in any left or right sides of the sub-tree. A node's height is the maximum number of edges between that node and a leaf node.
- **13's Right Subtree** - represents the entire subtree available on the right side of the tree.
- **13's in-order Successor** - here will be 14. Why? Because in-order successor is the node that comes after it if we were to do in-order traversal.  In-order traversal of the BST here would result in node 13 coming before node 14, and so, the successor of node 13 is node 14.
- **Child Nodes** - represents all the child nodes present in the tree leaving the root node.
- **Parent/Internal Nodes** - represents the nodes (including the root node) which has other child nodes coming out of it.
- **Leaf Nodes** - represents the last nodes in a BST - either left or right side of the tree.


- **tree's descendants** - descendants of a node are all the child nodes of that node, and all their child nodes, and so on. Just start with a node, and the descendants will be all the nodes that are connected below that node. 

- **Subtree** - starts with one of the nodes in the tree as a local root, and consists of that node and all of its descendants.

### Traversal of Binary Search Tree

- just to confirm that we actually have a Binary Tree data structure in front of us, we can just check if the properties at the top of the notes are true. So, for every node in the code, check if all of the values to the left of the node are lower, and that all the values to the right are higher.

- another way to check if a Binary Tree is BST, is to do an in-order traversal(like we did before - Implementation section), and check if the resulting list of the values are in an increasing order.

- here's the code for an implementation of the Binary Search Tree with traversal - 

`
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end = ", ")
    inOrderTraversal(node.right)

root = TreeNode(13)
node7 = TreeNode(7)
node15 = TreeNode(15)
node3 = TreeNode(3)
node8 = TreeNode(8)
node14 = TreeNode(14)
node19 = TreeNode(19)
node18 = TreeNode(18)

root.left = node7
root.right = node15

node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node19

node19.left = node18

#Traverse
inOrderTraversal(root)
`

- as we can see by running the code example above, the in-order traversal produces a list of numbers in an increasing (ascending) order, which means that this Binary Tree is a Binary Search Tree.

### Search for a Value in a BST

- Searching for a value in a BST is very similar to how we found a value using Binary Tree on an array.

- For Binary Tree to work, the array must be sorted already, and searching for a value in an array can then be done really fast.

- Similarly, searching for a value in a BST can also be done really fast becasue of how the nodes are placed.


- **How it works?**

1. Start at the root node.
2. If this is the value we are looking for, return.
3. If the value we are looking for is higher, continue searching in the right subtree.
4. If the value we are looking for is lower, continue searching in the left subtree.
5. If the subtree we want to search does not exist, depending on the programming language, return `None` or `NULL`, or something similar, to indicate that the value is not inside the BST.

- implementation in python - 
`
def search(node, target):
    if node is None:
        return None
    elif node.data == target:
        return Node
    elif target < node.data:
        return search(node.left, target)
    else:
        return search(node.right, target)
`

- the time complexity for searching a BST for a value is Big O(h), where h is the height of the tree.
- for a BST with most nodes on the right side of example, the height of the tree becomes larger than it needs to be, and the worst case search will take longer. Such trees are called unbalanced.

- in case of looking at differences btw Balanced BST and UnBalanced BST, if both the trees have the same number of nodes, and in-order traversal of both trees gives us the same result but the height is very different. It takes longer time to search the unbalanced tree above because it is higher.

- Compared to the BST, a different type of Binary Tree called the AVL Tree - which are self balancing, which means that the height of the tree is kept to a minimum so that operations like search, insertion and deletion takes less time.


### Insert a Node in BST

- Inserting a node in BST is similar to searching for a value.

**How it works?**
1. Start at the root node.
2. Compare each node:
    - Is the value lower? Go left
    - Is the value higher? Go right.
3. Continue to compare nodes with the new value until there is no right or left to compare with. That is where the new node is inserted.

- Inserting nodes as described above means that an inserted node will always become a new leaf node.

- All nodes in the BST are unique, so in case we find the same value as the one we want to insert, we do nothing.

- implementation of inserting a node in BST - 
`
def insert(node, data):
    if node is None:
        return TreeNode(data)
    else:
        if data < node.data:
            node.left = insert(node.left, data)
        elif data > node.data:
            node.right = insert(node.right, data)
    return node
`

### Find the Lowest Value in a BST Subtree

- before we can delete a node in BST, we first need a function that finds the lowest value in a node's subtree - 

**How it works?**
1. Start at the root node of the subtree.
2. Go left as far as possible.
3. The node you end up in is the node with the lowest value in that BST subtree.

- suppose we have a BST with 13 as the root node, 7 as left node - 3 (7's left), 8(7's right), 15 as the right node - 14(15's left), 19(15's right), here, if we keep going left, we end up in node 3, which is the lowest value in the BST.

- And, if we start at node 15, and keep going left, we end up in node 14, which is the lowest value in node 15's subtree.

- in py implementation
`
def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current
`

- now, we can use the `minValueNode()` function to find a node's in-order successor, and use that to delete a node.


### Delete a Node in a BST

- to delete a node, our function must first search the BST to find it.

- after the node is found there are three different cases where deleting a node must be done differently.

**How it works?**
1. If the node is a leaf node, remove it by removing the link to it.
2. If the node only has one child node, connect the parent node of the node you want to remove to that child node.
3. If the node has both right and left child nodes: Find the node's in-order successor, change the values with that node, then delete it.

- in step 3 above, the successor we find will always be a leaf node, and because its the node that comes right after the ndoe we want to delete, we can swap values with it and delete it.

- suppose, we have a BST with 13 as its root node, 7 as its left node - 7 -> 3(left), 8(right), 15 as its right node - 15 -> 14(left), 19(right) -> 18(left).


- deleting node 8.
    - Node 8 here is a leaf node (case 1), so, after we find it, we can just delete it.

- deleting node 19.
    - Node 19 has only one child node (case 2). To delete node 19, the parent node 15 is connected directly to node 18, and then node 19 can be removed.

- deleting node 13.
    - Node 13 has two child nodes (case 3). We find the successor, the node that comes right after during in-order traversal, by finding the lowest node in node 13's right subtree, which is node 14. Value 14 is then put into node 13, and then we can delete node 14.

- this is how a BST can be implemented with functionality for deleting a node - implementing in py - 

`
def delete(node, data):
    if not node:
        return None

    if data < node.data:
        node.left = delete(node.left, data)
    elif data > node.data:
        node.right = delete(node.right, data)
    else:
        #Node with only one child or no child
        if not node.left:
            temp = node.right
            node = None
            return temp
        elif not node.right:
            temp = node.left
            node = None
            return temp

        #Node with two children, get the in-order successor
        node.data = minValueNode(node.right).data
        node.right = delete(node.right, node.data)
    return node
`

- line 1 of ex - the `node` argument here makes it possible for the function to call itself recursively on smalller and smaller subtrees in the search for the node with the `data` we want to delete.

- line 2-8 of ex - this is searching for the node with the correct `data` that we want to delete.

- line 9-22 of ex - the node we want to delete has been found. There are three such cases - 
    - Case 1: Node with no child nodes (leaf node). `None` is returned, and that becomes the parent node's new left or right value by recursion (Line 6 or 8).
    - Case 2: Node with either left or right child node. That left or right child node becomes the parent's new left or right child through recursion(line 7 or 9).
    - Case 3: Node has both left and right child nodes. The in-order successor is found using the `minValueNode()` function.  We keep the successor's value by setting it as the value of the node we want to delete, and then, we can delete the successor node.

- Line 24 of ex - `node` is returned to maintain the recursive functionality.


### BST Compared to Other Data Structures

- Binary Search Tree takes the best from two other data structures - Arrays andn Linked Lists.

| Data Structure | Searching for a value | Delete/ Insert leads to shifting in memory |
---------------------------------------------------------
| Sorted Array | Big O(log n) | Yes |
| Linked Lists | Big O (n) | No |
| BST | Big O (log n) | No |


- Searching a BST is just as fast as Binary Search on an array, with the same time complexity - Big O(log n).

- And deleting and inserting new values can be done without shifting elements in memory, just like with Linked Lists. So, BST gets the best of both data structures.


### BST Balance and Time Complexity

- On a Binary Search Tree, operations like inserting a new node, deleting a node, or searching for a node are actually Big O(h). That means that the higher the tree is (h), the longer the operation will take.

- The reason why we wrote that searching for a value is Big O(log n) in the table above is because that is true if the tree is 'balanced' - Balanced BST - where the left and right branches are almost the same numbers and spread.

- A balanced BST is called so because there are approximately the same number of nodes on the left and right sides of the tree.

- the exact way to tell that a Binary Tree is balanced is that the height of the left and right subtrees of any node only differs by one. For example, if in a BST, the left subtree of the root node has a height of h = 2, and the right subtree has a height of h = 3.

- For a balanced BST, with a large number of nodes (big n), we get height h ~ log 2 n, and therefore the time complexity for searching, deleting, or inserting a node can be written as Big O(h) = Big O(log n).

- But, in case the BST is completely unbalanced, for example, lets assume the height of the tree is approximately the same as the number of nodes, h ~ n, and we get time complexity Big O(h) = Big O(n), searching, deleting, or inserting a node.

- So,, to optimize operations on a BST, the height must be minimized, and to do that, the tree must be balanced.

- And keeping a Binary Search Tree balanced is exactly what AVL Trees do.


## AVL Trees

- The AVL Tree is a type of Binary Search Tree named after two Soviet inventors Georgy Adelson- Velsky and Evegenii Landis, who invented the AVL tree in 1962.
- AVL Trees are self-balancing, which means that the tree height is kept to a minimum so that a very fast runtime is guarnteed for searching, inserting, and deleting nodes, with time complexity - Big O(log n).

- The only difference between a regular BST and an AVL tree is that AVL trees do rotation operations in addition, to keep the tree balance.
- a BST is in balance when the difference in height between the left and right subtrees is less than 2.
- by keeping balance, the AVL Tree ensures a minimum tree height, which means that search, insert, and delete operations can be done really fast.

- lets say for example, we have a BST (unbalanced) of height 6, and an AVL Tree (self-balancing) of height 3. The two trees are both Binary Search Trees, they have the same nodes, and the same in-order traversal (alphabetical), but the height is very different because the AVL Tree has balanced itself.

### Workings of an AVL Tree

- an AVL tree works by inserting values to the nodes, then using a condition, if the root node is greater than a value, it will rotate left or right and self balance the tree.

#### Left and Right Rotations

- to restore balance in an AVL tree, left or right rotations are done, or a combination of left and right rotations.
- if any left or right rotation happens in the tree, the subtree changes its parent. Subtrees change parent in this way during rotation to maintain the correct in-order traversal, and to maintain the BST property that the left child is less than the right child, for all the nodes in the tree.
- Also, keep in mind that it is not always the root node that becomes unbalanced and need rotation.

### The Balance Factor

- A node's balance factor is the difference in subtree heights.
- The subtree heights are stored at each node for all the nodes in an AVL Tree, and the balance factor is calculated based on its subtree heights to check if the tree has become out of balance.
- The height of a subtree is the number of the edges between the root node of the subtree and the leaf node farthest down in that subtree.

    - The Balance Factor (BF) for a node (X) is the difference in the height between its right and left subtrees.

    - BF(X) = height(rightSubtree(X) - height(leftSubtree(X)))

    - Balance factor values : 
        - 0 - the node is in balance
        - more than 0 - the node is 'right heavy'
        - less than 0 - the node is 'left heavy'

    - If the balance factor is less than -1, or more than 1, for one or more nodes in the tree, the tree is considered not in balance, and a rotation operation is needed to restore balance.

- Now, we'll see the different rotation operations that an AVL tree can do to regain balance.

#### The Four 'out-of-balance" Cases

- when the balance factor of just one node is less than -1, or more than 1, the tree is regarded as out of balance, and a restoration is needed to restore balance.

- There are four different ways an AVL Tree can be out of balance, and each of these cases require a different rotation operations.

| Case | Description | Rotation to Restore Balance |
-------------------------------------------------
| Left-Left (LL) | The unbalanced node and its left child node are both left-heavy. | A single right rotation. |

| Right-Right (RR) | The unbalanced node and its right child node are bnoth right heavy. | A single left rotation. |

| Left-Right (LR) | The unbalanced node is left heavy, and its left child node is right heavy. | First, do a left rotation on the left child node, then do a right rotation on the unbalanced node. |

| Right-Left (RL) | The unbalanced node is right heavy, and its right child node is left heavy. | First, do a right rotation on the right child node, then do a left rotation on the unbalanced node. |


#### The Left-Left (LL) Case

- the node where the unbalance is discovered is left heavy, and the node's left child node is also left heavy.

- When this LL case happens, a single right rotation on the unbalanced node is enough to resotre balance.

- In a LL case, two LL cases happen - 
    1. When D is added to a tree of P(left) and Q (root), the balance factor of Q becomes -2, which means the tree is unbalanced. This is an LL case because both the unbalance node Q and its left child node P are left heavy (negative balalce factors). A single right rotation at node Q restores the tree balance.
    2. After nodes L, C, and B are added, P's balance factor is -2, which means the tree is out of balance. This is also an LL case because both the unbalanced node P and its left child node D are left heavy. A singel right rotation restores the balance.

    - Note: The second time the LL case happens in the above case, a right rotation is done, and L goes from being the right child of D to being the left child of P. Rotations are done like that to keep the correct in-order traversal ('B, C, D, L, P, Q' in the case above). ANother reason for changing the parent when a rotation is done is to keep the BST property, that the left child is always lower than the node, and that the right child is always higher.

#### The Right-Right (RR) Case

- a right-right case happens when a node is unbalanced and right heavy, and the right child node is also right heavy.

- A single left rotation at the unbalanced node is enough to restore balance in the RR case.

- lets take an exaple of a root node - A, and a right node B, here, we see how the RR case happens and when - 
    
    1. When node D is inserted, A becomes unbalanced, and bot A and B are right heavy. A left rotation at node A restores the tree balance.

    2. After ndoes E, C, and F are inserted, node B becomes unbalanced. This is an RR case because both node B and its right child node D are right heavy. A left notation restores the tree balance.


#### The Left-Right (LR) Case

- the left-right case is when the unbalanced node is left heavy, but its child node is right heavy.

- In this LR case, a left rotation is first done on the left child node, and then a right rotation is done on the original unbalanced node.

- in an example of root node - Q, and left node E, we will see the LR case happen 2 times, and rotation operations are required and done to restore balance - 

    1. When K is inserted at left, node Q (root) gets unbalanced with a balance factor of -2, so it is left heavy, and its left child E is right heavy, so this is a left-right case.

    2. After nodes C, F, and G are inserted, node K becomes unbalanced and left heavy, with its left child node E right heavy, so its a left-right case.


#### The Right-Left (RL) Case

- the right-left case is when the unbalanced node is right heavy, and its right child node is left heavy.

- in this case, we first do a right rotation on the unbalanced node's right child, adn then we do a left rotation on the unbalanced node itself.

- lets take an example of an AVL - root node - A, and right node - F, and see where and when the righ-left case happens - 

    1. After inserting node B at E's left node, we get a right-left case because node A becomes unbalanced and right heavy, and its right child is left heavy. TO restore balance, a right rotation is first done on node F, and then a left rotation is done on node A.

    2. the next right-left case occurs after nodes G, (inserted at right of node F), E (inserted at left of node F), and D, (inserted at left of node E), are added. This is a right-left case because node B is unbalanced and right heavy, and its right child F is left heavy. TO restore balance, a right rotation is first done on node F, and then a left rotation is done on node B.


### Retracing in AVL Trees

- after inserting or deleting a node in an AVL tree, the tree may become unbalanced. To find out if the tree is unbalancecd, we need to update the heights and recalcualte the balance factors of all ancestor nodes.

- This process, known as retracing, is handled through recursion. As the recursive calls propagate back to the root after an insertion or deletion, each ancestor node's height is updated and the balance factor is recalculated. If any ancestor node is found to have a balance factor outside the range of -1 to 1, a rotation is performed at that node to restore the tree's balance.

    - suppose we take an example tree where node C is the root node, E is right node, and B is left node. If we add node F at the end of the right node (at the final right node), the nodes C, E, and H (all child nodes of node E), are all unbalanced, but sincec retracing works through recursion, the unbalance at node H is discovered and fixed first, which in this case also fixes the unbalance in nodes E and C.

    - after node F is inserted, the code will retrace, calculating balancing factors as it propagates back up towards the root node. When node H is reached, and the balancing factor -2 is calculated, a right rotation is done. Only after this rotation is done, the code will continue to retrace, calculating balancing factors further up on ancestor nodes E and C.

    - Because of the rotation, balancing factors for nodes E and C stay the same as before node F was inserted.


### AVL Insert Node Implementation

- this code below is based on the BST implementation on the previous topic, for inserting nodes.

- there is only one new attribute for each node in the AVL tree compared to the BST, and that is height, but there are many new functions and extra code lines needed for the AVL tree implementation because of how the AVL tree rebalances itself.

- the implementation below builds an AVL tree based on a list of characters. The last node inserted here will be 'F', also triggers a right rotation - 

- code in py
`
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

def getHeight(node):
    if not node:
        return 0
    return node.height

def getBalance(node):
    if not node:
        return 0
    return getHeight(node.left) - getHeight(node.right)

def rightRotate(y):
    print('Rotate right on node', y.data)
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))
    x.height = 1 + max(getHeight(x.left), getHeight(x.right))
    return x

def leftRotate(x):
    print('Rotate left on node', x.data)
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    x.height = 1 + max(getHeight(x.left), getHeight(x.right))
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))
    return y

def insert(node, data):
    if not node:
        return TreeNode(data)

    if data < node.data:
        node.left = insert(node.left, data)
    elif data > node.data:
        node.right = insert(node.right, data)

    # Update the balance factor and balance the tree
    node.height = 1 + max(getHeight(node.left), getHeight(node.right))
    balance = getBalance(node)

    # Balancing the tree
    #LEFT LEFT
    if balance > 1 and getBalance(node.left) >= 0:
        return rightRotate(node)

    # LEFT RIGHT
    if balance > 1 and getBalance(node.left) < 0:
        node.left = leftRotate(node.left)
        return rightRotate(node)

    # RIGHT RIGHT
    if balance < -1 and getBalance(node.right) <= 0:
        return leftRotate(node)

    # RIGHT LEFT
    if balance < -1 and getBalance(node.right) > 0:
        node.right = rightRotate(node.right)
        return leftRotate(node)

    return node

def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end = ", ")
    inOrderTraversal(node.right)

# inserting nodes
root = None
letters = ['C', 'B', 'E', 'A', 'D', 'H', 'G', 'F']
for letter in letters:
    root = insert(root, letter)

inOrderTraversal(root)

`

### AVL Delete Node Implementation

- when deleting a node that is not a leaf node, the AVL tree requires the `minValueNode()` function to find a node's next node in the in-order traversal. This is the same as when deleting a node in a binary search tree, as explained in the prev main topic.

- to delete a node in an AVL tree, the same code to restore balance is needed as for the code to insert a node - 

- code in py
`
del minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def delete(node, data):
    if not node:
        return node

    if data < node.data:
        node.left = delete(node.left, data)
    elif data > node.data:
        node.right = delete(node.right, data)
    else:
        if node.left is None:
            temp = node.right
            node = None
            return temp
        elif node.right is None:
            temp = node.left
            node = None
            return temp

        temp = minValueNode(node.right)
        node.data = temp.data
        node.right = delete(node.right, temp.data)

    if node is None:
        return node

    # Update the balance factor and balance the tree
    node.height = 1 + max(getHeight(node.left), getHeight(node.right))
    balance = getBalance(node)

    # Balancing the tree
    #Left Left
    if balance > 1 and getBalance(node.left) >= 0:
        return rightRotate(node)

    #Left Right
    if balance > 1 and getBalance(node.left) < 0:
        node.left = leftRotate(node.left)
        return rightRotate(node)
    
    #Right Right
    if balance < -1 and getBalance(node.right) <= 0:
        return leftRotate(node)
    
    #Right Left
    if balance < -1 and getBalance(node.right) > 0:
        node.right = rightRotate(node.right)
        return leftRotate(node)
    
    return node
`

### Time Complexity for AVL Trees

- comparing two trees - BST(unbalanced) and AVL. If we want to search for the last node in both the trees, in BST, it would mean all nodes except the node we're searchinf for much be compared. But searching for the same node in an AVL tree only requires us to visit 'h' nodes (depending on the height of the tree.)

- So, in worst case, algorithms like search, insert, and delete must run through the whole height of the tree. This means that keeping the height (h) of the tree low, like we do using AVL trees, gives us a lower runtime.

- See the comparison of the time complexities between BST and AVL Trees below, and how the time complexities relate to the height (h) of the tree, and the number of nodes (n) in the tree - 
    
    - The BST is not self-balancing. This means that a BST can be very unbalanced, almost like a long chain, where the height is nearly the same as the number of nodes. This makes the operations like searching, deleting and inserting the nodes slow, with time complexity Big O(h) = Big O(n).

    - the AVL Tree however, is self balancing. That means that the height of the tree is kept to a minimum so that operations like searching, deleting and inserting nodes are much faster, with time complexity Big O(h) = Big O(log n).

### Big O(log n) explained

- the fact that the time complexity is Big O(h) = Big O(log n) for search, insert and delete on an AVL Tree with height h and nodes can be explained like this - 

    - imagine a perfect Binary Tree where all nodes have two child nodes except on the lowest level.
    - Then, the number of nodes on each level in such an AVL tree are - 1, 2, 4, 8, 16, 32,...
    - which is the same as - 2(pow0), 2(pow1), 2(pow2), 2(pow3), 2(pow4), 2(pow5),...
    - to get the number of nodes n in a perfect Binary Tree with height h = 3, we can add the number of nodes on each level together:
        - n3 = (pow0), 2(pow1), 2(pow2), 2(pow3) = 15
    - which is actually the same as - n3 = s(pow4 - 1) = 15
    - and this is actually the case for larger trees as well! If we want to get the number of nodes n in a tree with height h = 5 for example, we find the number of nodes like this - n5 = 2(pow6 - 1) = 63
    - so, in general, the relationship between the height h of a perfect Binary Tree and the number of nodes in it n, can be expressed as - 
        - nh = 2(pow h + 1) - 1
    
    - Note: the formula above can also be found by calculating the sum of the geometric series 2(pow0) + 2(pow1) + 2(pow2) + 2(pow3) + .... + 2(pown)

    - we know that the time complexity for searching, deleting or inserting a node in an AVL tree is Big O(h), but we want to argue that the time complexity is actually Big O(log (n)), so we need to find the height h described by the number of ndoes n:
        - n = 2(pow h + 1) - 1
        - n + 1 = 2(pow h + 1)
        - log2(n+1) = log2(2(pow h + 1))
        - h = log2(n + 1) - 1
         
        - Big O(h) = Big O(log n)

    - How the last line above is derived might not be obvious, but for a Binary Tree with a lot of nodes (big n), the "+1" and "-1" terms are not important when we consider time complexity.

    - the math above shows that the time complexity for search, delete and insert operations on an AVL Tree Big O(h), can actually be expressed as Big O(log n), which is fast, a lot faster than the time complexity for BST which is Big O(n).


## Graphs

- a graph is a non-linear data structure that consists of vertices(nodes) and edges.
- a vertex, also called a node, is a point or an object in the Graph, and an edge is used to connect two vertices with each other.
- Graphs are non-linear because the data structure allows us to have different paths to get from one vertex to another, unlike with linear data structures like arrays or linked lists.
- Graphs are used to represent and solve problems where the data consists of objects and relationships between them, such as - 
    - Social Networks - each person is a vertex, and relationships(like friendships) are the edges. Algorithms can suggest potential friends.
    - Maps and Navigation - locations, like a town or bus stops, are stored as vertices, and roads are stored as edges. Algorithms can find the shortest route between the two locations when stored as a Graph.
    - Internet - Can be represented as a Graph, with web pages as vertices and hyperlinks as edges.
    - Biology - Graphs can model systems like neural networks or the spread of diseases.


### Graph Properties

- Here are the properties and terms linked with Graphs, to help you understand it better - 

    - Weighted - a weighted graph is a graph where the edges have values. Meaning, the edges have numbers, these numbers can be anything. The weight value of an edge can represent things like distance, capacity, time, or probability.

    - Connected - a connected graph is when all the vertices are connected through edges somehow. A graph that is not connected, is a Graph with isolated (disjoint) subgraphs, or single isolated vertices.

    - Directed - also known as a digraph, is when the edges between the vertex pairs have a direction (A -> B). The direction of an edge can represent things like hierarchy or flow.

    - Cyclic - A cyclic graph is defined differently depending on whether it is directed or not - 
        - a Directed cyclic graph is when you can follow a path along the directed edges that goes in circle. Removing the directed edge from one node(vertices) to another makes the directed Graph not cyclic anymore.
        - An undirected cyclic graph is when you can come back to the same vertex you started at without using the same edge more than once. The undirected Graph is cyclic because we can start and end up in another vertes without using the same edge twice.

    - Loop - also called a self-loop, is an edge that begins and ends on the same vertex. A loop is a cycle that only consists of one edge. By adding the loop on any vertex in a Graph, it becomes cyclic.


### Graph Representations

- a graph representation tells us how a graph is stored in memory.
- different graph representations can:

    - take up more or less space.
    - be faster or slower to search or manipulate.
    - be better suited depending on what type of graph we have (weighted, directed, etc.) and what we want to do with the graph.
    - be easier to understand and implement than others.

- There are many different graph representations, but here, we'll be using Adjacency Matrix moving forward, as its easy to understand and implement, and it also works in all cases relevant.
- Graph representations store information about which vertices are adjacent, and how the edges between the vertices are. Graph representations are slightly different if the edges are directed or weighted.
- Two vertices are adjacent, or neighbors, if there is an edge between them.


### Adjacency Matrix Graph Representation

- Adjacency Matrix is the Graph representation (structure) here.
- the Adjacency Matrix is a 2D array (matrix) where each cell on index `(i, j)` stores information about the edge from vertex `i` to vertex `j`.

- for example, lets say we have a graph of A-D, where each of them are connected to each other, except D, which is only connected to A. Here's what its adjacency matrix representation will look like - 

        A B C D
    A     1 1 1
    B   1   1 
    C   1 1
    D   1

- the adjacency matrix above represents an undirected Graph, so the values '1' only tells us where the edges are. Also, the values in the adjacency matrix is symmetrical because the edges go both ways (undirected graph).
- To create a directed Graph with an adjacency matrix, we must decide which vertices the edges go from and to, by inserting the value at the correct indexes `(i, j)`. To represent a weighted Graph, we can put other values than '1' inside the adjacency matrix.

- if we decide to create a directed and weighted Graph with the adjacency matrix representation, it will look like this.

        A B C D
    A     3 2 
    B    
    C     1
    D   4

- in the adjacency matrix above, the value `3` on index `(0, 1)` tells us that there is an edge from vertex A to vertex B, and the weight for that edge is `3`.

- as you can see, the weights are placed directly into the adjacency matrix for the correct edge, and for a directed Graph, the adjacency matrix does not have to be symmetric.


### Adjacency List Graph Representation

- in case we have a 'sparse' Graph with many vertices, we can save space by using an Adjacency List compared to using an Adjacency Matrix, because an Adjacency Matrix would reserve a lot of memory on empty Array elements for edges that dont exist.
- A 'sparse' graph is a Graph where each vertex only has edges to a small portion of the other vertices in the Graph.
- An Adjacency List has an array that contains all the vertices in the Graph, and each vertex has a Linked List (or Array) with the vertex's edges.

- eg. of an Adjacency List 
      A -> 3 -> 1 -> 2 -> null
      B -> 0 -> 2 -> null
      C -> 1 -> 0 -> null
      D -> 0 -> null

- in the adjacency list above, the vertices A to D are placed in an array, and each vertex in the array has its index written right next to it.
- each vertex in the array has a pointer to a linked list that represents that vertex's edges. More specifically, the linked list contains the indexes to adjacent (neighbor) vertices.
- So, for example, vertex A has a link to a Linked List with values 3, 1, and 2. These values are the indexes to A's adjacent vertices D, B and C.

- an adjacency list can also represent a directed and weighted graph, like this - 
- eg. of an Adjacency List representing a directed and weighted graph
      A -> 1,3 -> 2,2 -> null
      B -> null
      C -> 1,1 -> null
      D -> 0,4 -> null

- in the Adjacency List above, the vertices are stored in an array, each vertex has a pointer to a Linked List with edges stored as `i,w`, where `i` is the index of the vertex the edge goes to, and `w` is the weight of that edge.
- Node D for example, has a poitner to a Linked List with an edge to vertex A. The values `0,4` means that vertex D has an edge to vertex on index `0` (vertex A), and the weight of that edge is `4`.


## Graphs Implementation

### A basic graph implementation

- before we can run algorithms on a Graph, we must first implement it somehow.

- to implement a graph, we will use an Adjacency matrix, like the one below - 
        A B C D
    A     1 1 1
    B   1   1
    C   1 1
    D   1

- to store data for each vortex, in this case the letters A, B, C and D, the data is put in a seperate array that matches the indexes in the adjacency matrix, like this - 
- vertexData = ['A', 'B', 'C', 'D']

- For an undirected and not weighted Graph, like in the graph above, an edge between vertices `i` and `j` is stored with value `1`. It is stored as `1` on both places `(j, i)` and `(i, j)` because the edge goes in both directions. As you can see, the matrix becomes diagonally symmetric for such undirected Graphs.
- Lets look at somethiong more specific. In the adjacency matrix above, vertex A is on index `0`, and vertex D is on index `3`, so we get the edge between A and D stored as value `1` in position `(0, 3)` and `(3, 0)`, because the edge goes in both directions.

- here's an implementation of the undirected Graph from the image above in py - 

`
vertexData = ['A", 'B', 'C', 'D']

adjacency_matrix = [
    [0, 1, 1, 1], # edges for A
    [1, 0, 1, 0], # edges for B
    [1, 1, 0, 0], # edges for C
    [1, 0, 0, 0] # edges for D
]

def print_adjacency_matrix(matrix):
    print("\nAdjacency Matrix: ")
    for row in matrix:
        print(row)

print('vertexData:', vertexData)
print_adjacency_matrix(adjacency_matrix)
`

- this implementation is basically just a two dimensional array, but to get a better sense of how the vertices are connected by edges in the Graph we have just implemented, we can run this function - 

`
def print_connections(matrix, vertices):
    print("\nConnections for each vertex:")
    for i in range(len(vertices)):
        print(f"{vertices[i]}:", end="")
        for j in range(len(vertices)):
            if matrix[i][j]:  # if there is a connection
                print(vertices[j], end=" ")
        print() # prints new line
`

### GRaph Implementation using Classes

- a more proper way to store a graph is to add an abstraction layer using classes so that a Graph's vertices, edges, and relevant methods, like algorithms that we will implement later, are contained in one place.

- Programming languages with built-in object-oriented functionality like Python and Java, make implementation of Graphs using classes much easier than languages like C, without this built-in functionality.

- an undirected Graph's adjacency Matrix

    -   A B C D
      A   1 1 1
      B 1   1
      C 1 1
      D 1

- here's how the undirected Graph above can be implemented using classes in python - 

`
class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def print_graph(self):
        print("Adjacency Matrix:)
        for row in self.adj_matrix:
            print(' '.join(map(str, row)))
        print("\nVertex Data:")

        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex {vertex} : {data}")

g = Graph(4)
g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_edge(0, 1) # A - B
g.add_edge(0, 2) # A - C
g.add_edge(0, 3) # A - D
g.add_edge(1, 2) # B - C

g.print_graph()
`

- in the code above, the matrix symmetry we get for undirected Graphs is provided for on lines - '            self.adj_matrix[u][v] = 1
self.adj_matrix[v][u] = 1' - and this saves us some code when initializing the edges in the Graph on lines - 
g.add_edge(0, 1) # A - B
g.add_edge(0, 2) # A - C
g.add_edge(0, 3) # A - D
g.add_edge(1, 2) # B - C.

### Implementation of Directed and Weighted Graphs

- to implement a Graph that is directed and weighted, we just need to do a few changes to previous implementation of the undirected Graph.

- to create directed Graphs, we just need to remove line 10 in the previous example code above - self.adj_matrix[v][u] = 1, so that the matrix is not automatically symmetric anymore.

- the second change we need to do is to add a `weight` argument to the `add_edge()` method, so that instead of just having value `1` to indicate that there is an edge between two vertices, we use the actual weight value to define the edge.

- implementation of a directed and weighted graph - 
-     A B C D
    A   3 2
    B
    C   1
    D 4

- in python using Class- 
`
class Graph:
    def __init__(self, size):
        self.adj_matrix = [[None] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self,  u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            # self.adj_matrix[v][u] = weight

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def print_graph(self):
        print("Adjacency Matrix: ")
        for row in self.adj_matrix:
            print(' '.join(map(lambda x: str(x) if x is not None else '0', row)))
        print("\nVertex Data:")
        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex{vertex} : {data}")

g = Graph(4)
g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_edge(0, 1, 3)  # A -> B with weight 3
g.add_edge(0, 2, 2)  # A -> C with weight 2
g.add_edge(3, 0, 4)  # D -> A with weight 4
g.add_edge(2, 1, 1)  # C -> B with weight 1

g.print_graph()
`

- here, this line - self.adj_matrix = [[None] * size for _ in range(size)] - represents, all edges are set to `None` initially.

- on line - def add_edge(self,  u, v, weight):
 - the weight can now be added to an edge with additional `weight` argument.

- on line - # self.adj_matrix[v][u] = weight - by removing this line (commenting), the Graph can now be set up as being directed.


## Graphs Traversal

- to traverse a Graph means to start in one vertex, and go along the edges to visit other vertices untl all vertices, or as many as possible, have been visited.

- Understanding how a graph can be traversed is important for understanding how algorithms that run on Graphs work.

- The two most common ways a Graph can be traersed are - 
    - Depth First Search (DFS)
    - Breadth First Search (BFS)

- DFS is usually implemented using a Stack, or by the use of recursion (which utilizes the call stack), while BFS is usually implemented using a Queue.

- **Note:**
    - the `call stack` keeps functions running in the correct order.
    - if for example, FunctionA calls FunctionB, FunctionB is placed on top of the call stack and starts running. Once FunctionB is finished, it is then removed from the stack, and then FunctionA resumes its work.


### Depth First Search Traversal (DFS)

- DFS is said to go 'deep' because it visits a vertex, then an adjacent vertex, and then that vertex' adjacent vertex, and so on, and in this way, the distance from the starting vertex increases for each recursive iteration.

- **How it works?**

    1. Start DFS traversal on a vertex.
    2. Do a recursive DFS traversal on each of the adjacent vertices as long as they are not already visited.

- if we use this traversal pattern on a graph, we see that DFS traversal starts in vertex D(lets say x), marks D as visited. Then, for every new vertex visited, the traversal method is called recursively on all adjacent vertices that have not been visited yet. So, when vertex A is visited (parernt node of D), vertex C or vertex E(depending on the implementation - C is adjacent to A, E is adjacent to D), is the next vertex where the traversal continues.

- Example in code - in py - 
`
class Graph:
    def __init__(self, size):
        self.adj_matrix = [[10] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def print_graph(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(' '.join(map(str, row)))
        print("\nVertex Data:")
        
        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex {vertex}: {data}")

    def dfs_util(self, v, visited):
        visited[v] = True
        print(self.vertex_data[v], end=' ')

        for i in range(self.size):
            if self.adj_matrix[v][i] == 1 and not visited[i]:
                self.dfs_util(i, visited)

    def dfs(self, start_vertex_data):
        visited = [False] * self.size
        start_vertex = self.vertex_data.index(start_vertex_data)
        self.dfs_util(start_vertex, visited)

g = Graph(7)

g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')
# <!-- g.add_vertex_data(7, 'H')
# g.add_vertex_data(8, 'I')
# g.add_vertex_data(9, 'J') -->

g.add_edge(3, 0) # D - A
g.add_edge(0, 2)  # A - C
g.add_edge(0, 3)  # A - D
g.add_edge(0, 4)  # A - E
g.add_edge(4, 2)  # E - C
g.add_edge(2, 5)  # C - F
g.add_edge(2, 1)  # C - B
g.add_edge(2, 6)  # C - G
g.add_edge(1, 5)  # B - F

g.print_graph()

print("\nDFS starting from vertex D: ")
g.dfs('D')
`

- line g.dfs('D') - 
    - the DFS traversal starts when the `dfs()` method is called.

- line visited = [False] * self.size - 
    - the `visited` array is first set to `false` for all vertices, because no vertices are visited yet at this point.

- line self.dfs_util(start_vertex, visited) -
    - the `visited` array is sent as an argument to the `dfs_util()` method. When the `visited` array is sent as an argument like this, it is usually just a reference to the `visited` array thjat is sent to the `dfs_util()` method, and not the actual array with the values inside. So, there is always just one `visited` array in our program, and the `dfs_util()` method can make changes to it as nodes are visited (line - visited[v] = True)

- line for i in range(self.size):
            if self.adj_matrix[v][i] == 1 and not visited[i]:
                self.dfs_util(i, visited) - 
    
    - for the current vertex `v`, all adjacent nodes are called recursively if they are not already visited.


### Breadth First Search (BFS) Traversal

- BFS visits all adjacent vertices of a vertex before visiting the neighboring vertices to the adjacent vertices. This means that vertices with the same distance from the starting vertex are visited before vertices further away from the starting vertex are visited.

- **How it works?**
    
    1. Put the starting vertex into the queue.
    2. For each vertex taken from the queue, visit the vertex, then put all unvisited adjacent vertices into the queue.
    3. Continue as long as there are vertices in the queue.

- BFS traversal visits vertices the same distance from the starting vertex, before visiting vertices further away. So, for example, after visiting verte A, vertex E and C are visited before visiting vertex B, F, and G because those vertices are further away(they have more distance count from the original vertex).

- BFS traversal works this way by putting all adjacent vertices in a queue (if they are not already visited), and then using the queue to visit the next vertex.

- here's the example in python code - 

`
def bfs(self, start_vertex_data):
    queue = [self.vertex_data.index(start_vertex_data)]
    visited = [False] * self.size
    visited[queue[0]] = True

    while queue:
        current_vertex = queue.pop(0)
        print(self.vertex_data[current_vertex], end = ' ')

        for i in range(self.size):
            if self.adj_matrix[current_vertex][i] == 1 and not visited[i]:
                visited[i] = True
`

- line - queue = [self.vertex_data.index(start_vertex_data)]
    visited = [False] * self.size
    visited[queue[0]] = True -

    - `bfs()` method starts by creating a queue with the start vertex inside, creating a `visited` array, and setting the start vertex as visited.

- line - while queue:
        current_vertex = queue.pop(0)
        print(self.vertex_data[current_vertex], end=' ')
      
        for i in range(self.size):
            if self.adj_matrix[current_vertex][i] == 1 and not visited[i]:
                queue.append(i)
                visited[i] = True
    
    - the bfs traversal works by taking a vertex from the queue, printing it, and adding adjacent vertices to the queue if they are not visited yet, and then continue to take vertices from the queue in this way. The traversal finishes when the last element in the queue has no unvisited adjacent vertices.


### DFS and BFS Traversal of a Directed Graph

- DFS and BFS traversals can actually be implemented to work on directed Graphs (instead of undirected) with just very few changes.

- to go from traversing a directed Graph instead of an undirected Graph, we just need to remove the last line in the `add_edge()` method we created earlier.

- `
def add_edge(self, u, v):
    if 0 <= u < self.size and 0 <= v < self.size:
        self.adj_matrix[u][v] = 1
`

- we must also take care when we build our Graph because the edges are now directed.

- the code example below contains both BFS and DFS traversal of the directed Graph in python - 

`
class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v):
        if 0 <= u <self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = 1

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def print_graph(self):
        print("Adjacency matrix: ")
        for row in self.adj_matrix:
            print(' '.join(map(str, row)))
        print("\nVertex Data: ")

        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex {vertex} : {data}")

    def dfs_util(self, v, visited):
        visited[v] = True
        print(self.vertex_data[v], end = ' ')

        for i in range(self.size):
            if self.adj_matrix[v][i] == 1 and not visited[i]:
                self.dfs_util(i, visited)

    def dfs(self, start_vertex_data):
        visited = [False] * self.size

        start_vertex = self.vertex_data.index(start_vertex_data)
        self.dfs_util(start_vertex, visited)

    def bfs(self, start_vertex_data):
        queue = [self.vertex_data.index(start_vertex_data)]
        visited = [False] * self.size
        visited[queue[0]] = True

        while queue:
            current_vertex = queue.pop(0)
            print(self.vertex_data[current_vertex], end = ' ')

        for i in range(self.size):
            if self.adj_matrix[current_vertex][i] == 1 and not visited[i]:
                visited[i] = True

g = Graph(7)

g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')

g.add_edge(3, 0)  # D -> A
g.add_edge(3, 4)  # D -> E
g.add_edge(4, 0)  # E -> A
g.add_edge(0, 2)  # A -> C
g.add_edge(2, 5)  # C -> F
g.add_edge(2, 6)  # C -> G
g.add_edge(5, 1)  # F -> B
g.add_edge(1, 2)  # B -> C

g.print_graph()

print("\nDFS starting from vertex D:")
g.dfs('D')

print("\BFS starting from vertex D:")
g.bfs('D')

`


## Graphs Cycle Detection

### Cycles in Graphs

- A cycle in a Graph is a path that starts and ends at the same vertex, where no edges are repeated. It is similar to walking through a maze and ending up exactly where you started.

- A cycle can be defined slightly different depending on the situation. A self-loop for example, where an edge goes from and to the same vertex, might or might not be considered a cycle, depending on the problem you are trying to solve.

### Cycle Detection

- It is important to be able to detect cycles in Graphs because the cycles can indicate problems or special conditions in many applications like networking, scheduling, and circuit design.

- The two most common ways to detect cycles are - 
    1. DFS - Depth First Search traversal explores the Graph and marks the vertices as visited. A cycle is detected when the current vertex has an adjacent vertex that has already been visited.
    2. Union-Find - This works by initially defining each vertex as a group, or a subset. Then these groups are joined for every edge. Whenever a new edge is explored, a cycle is detected if two vertices already belong to the same group.


### DFS Cycle Detection for Undirected Graphs

- to detect cycles in an undirected Graph using Depth First Search (DFS), we use a code very similar to the DFS Trraversal code with just a few changes.

- **How it works?**
    1. Start DFS Traversal on each unvisited vertex (in case the Graph is not connected).
    2. During DFS, mark vertices as visited, and run DFS on the adjacent vertices (recursively).
    3. If an adjacent vertex is already visited and is not the parent of the current vertex, a cycle is detected, and `True` is returned.
    4. If DFS Traversal is done on all vertices and no cycles are detected, `False` is returned.

- the DFS Traversal starts in vertex A, because that is the first vertex in the adjacency matrix. Then, for every new vertex visited, the traversal method is called recursively on all adjacent vertices that have not been visited yet. The cycle is detected when vertex F(last) is visited, adn it is discovered that the adjacent vertex C(middle node connected to A and F - both main nodes) has already been visited.

- code example in python -
`
class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v):
        if 0 <= u self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex <self.size:
            self.vertex_data[vertex] = data

    def print_graph(self):
        print("Adjacency Matrix: ")
        for row in self.adj_matrix:
            print(' '.join(map(str, row)))
        print("\nVertex Data: ")

        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex {vertex} : {data}")

    def dfs_util(self, v, visited, parent):
        visited[v] = True

        for i in range(self.size):
            if self.adj_matrix[v][i] == 1:
                if not visited[i]:
                    if self.dfs_util(i, visited, v):
                        return True
                    elif parent != 1:
                        return True
        return False

    def is_cyclic(self):
        visited = [False] * self.size
        for i in range(self.size):
            if not visited[i]:
                if self.dfs_util(i, visited, -1):
                    return True
        return False

g = Graph(7)

g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')

g.add_edge(3, 0)  # D - A
g.add_edge(0, 2)  # A - C
g.add_edge(0, 3)  # A - D
g.add_edge(0, 4)  # A - E
g.add_edge(4, 2)  # E - C
g.add_edge(2, 5)  # C - F
g.add_edge(2, 1)  # C - B
g.add_edge(2, 6)  # C - G
g.add_edge(1, 5)  # B - F

g.print_graph()

print("\nGraph has cycle:", g.is_cyclic())
`

- here, line print("\nGraph has cycle:", g.is_cyclic()) - 
    - the DFS cycle detection starts when the `is_cyclic()` method is called.

- line visited = [False] * self.size - 
    - the `visited` array is first set to `false` for all vertices, because no vertices are visited yet at this point.

- lines - for i in range(self.size):
            if not visited[i]:
                if self.dfs_util(i, visited, -1):
                    return True
          return False
    - DFS cycle detection is run on all vertices in the Graph. This is to make sure all vertices in case the Graph is not connected. If a node is already visited, there must be a cycle, and `True` is returned. If all nodes are visited just once, which means no cycles are detected, `False` is returned.

- liens - def dfs_util(self, v, visited, parent):
        visited[v] = True

        for i in range(self.size):
            if self.adj_matrix[v][i] == 1:
                if not visited[i]:
                    if self.dfs_util(i, visited, v):
                        return True
                elif parent != i:
                    return True
        return False
    - this is the part of the DFS cycle detection that visits a vertex, and then visits adjacent vertices recursively. A cycle is detected and `True` is returned if an adjacent vertex has already been visited, and it is not the parent node.


### DFS Cycle Detection for Directed Graphs

- To detect cycles in Graphs that are directed, the algorithm is still very similar as for undirected Graphs, but the code must be modified a little bit because for a directed Graph, if we come to an adjacent node that has already been visited, it does not necessarily mean that there is a cycle.

- to implement DFS cycle detection on a directed Graph, we need to remove the symmetery we have in the adjacency matrix for undirected Graphs. We also need to use `recStack` array to keep track of visited vertices in the current recursive path.

- example in python - 
`
class Graph:
    # ...
    def add_edge(self, u, v):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = 1
            # self.adj_matrix[v][u] = 1

    # ...
    def dfs_util(self, v, visited, recStack):
        visited[v] = True
        recStack[v] = True
        print("Current vertex: ", self.vertex_data[v])

        for i in range(self.size):
            if self.adj_matrix[v][i] == 1:
                if not visited[i]:
                    if self.dfs_util(i, visited, recStack):
                        return True
                elif recStack[i]:
                    return True

        recStack[v] = False
        return False

    def is_cyclic(self):
        visited = [False] * self.size
        recStack = [False] * self.size

        for i in range(self.size):
            if not visited[i]:
                print() # new line
                if self.dfs_util(i, visited, recStack):
                    return True
        return False

g = Graph(7)

# ...
g.add_edge(3, 0)  # D -> A
g.add_edge(0, 2)  # A -> C
g.add_edge(2, 1)  # C -> B
g.add_edge(2, 4)  # C -> E
g.add_edge(1, 5)  # B -> F
g.add_edge(4, 0)  # E -> A
g.add_edge(2, 6)  # C -> G

g.print_graph()

print("Graph has cycle: ", g.is_cyclic())
`

- here, line - # self.adj_matrix[v][u] = 1 - omitted
    - this line is removed because it is only applicable for undirected graphs.

- line - recStack = [False] * self.size - 
    - the `recStack` array keeps an overview over which vertices have been visited during a recursive exploration of a path.

- line - if self.adj_matrix[v][i] == 1:
                if not visited[i]:
                    if self.dfs_util(i, visited, recStack):
                        return True
                elif recStack[i]:
                    return True
    - for every adjacent vertex not visited before, do a recursive DFS cycle detection. If an adjacent vertex has been visited before, also in the same recursive path (for i in range(self.size):), a cycle has been found, and `True` is returned.


### Union-Find Cycle Detection

- Detecting cycles using Union-Find is very different from using DFS.

- Union-Find Cycle detection works by first putting each node in its own subset (like a bag or a container). Then, for every edge, the subsets belonging to each vertex are merged. For an edge, if the vertices already belong to the same subset, it means that we have found a cycle.

- Union Find Cycle detection is only applicable for Graphs that are undirected.
- Union Find cycle detection is implemented using the adjacency matrix representation, so setting up the Graph structure with vertices and edges is basically the same as in previous examples.

- example in python -
`
class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size
        self.parent = [i for i in range(size)] # union-find array

    def add_edge(self, u, v):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def find(self, i):
        if self.parent[i] == i:
            return i
        return self.find(self.parent[i])

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        print('Union:', self.vertex_data[x], '+' , self.vertex_data[y])
        print(self.parent, '\n')

    def is_cyclic(self):
        for i in range(self.size):
            for j in range(i + 1, self.size):
                if self.adj_matrix[i][j]:
                    x = self.find(i)
                    y = self.find(j)
                    if x == y:
                        retrurn True
                    self.union(x, y)
        return False

g = Graph(7)

g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')

g.add_edge(1, 0)  # B - A
g.add_edge(0, 3)  # A - D
g.add_edge(0, 2)  # A - C
g.add_edge(2, 3)  # C - D
g.add_edge(3, 4)  # D - E
g.add_edge(3, 5)  # D - F
g.add_edge(3, 6)  # D - G
g.add_edge(4, 5)  # E - F

print("Graph has cycle: ", g.is_cyclic())

`

- here, in line - self.parent = [i for i in range(size)]  # Union-Find array
    - the `parent` array contains the root vertex for every subset. This is used to detect a cycle by checking if two vertices on either side of an edge already belongs to the same subset.

- line - def find(self, i):
    - the `find` method finds the root of the set that the given vertex belongs to.

- line - def union(self, x, y):
    - the `union` method combines two subsets.

- line - def is_cyclic(self):
    - the `is-cyclic` method uses the `find` method to detect a cycle if two vertices `x` and `y` are already in the same subset. If a cycle is not detected, the `union` method is used to combine the subsets.


## Shortest Path

### The Shortest Path Problem

- the shortest path problem is famous in the field of computer science.
- To solve the shortest path problem means to find the shortest possible route or path between two vertices(or nodes) in a Graph.
- In the shortest path problem, a Graph can represent anything from a road network to a communication network, where the vertices can be intersections, cities, or routers, and the edges can be roads, flight paths, or data links.

- lets say we have an example graph, in that graph, the shortest path from vertex D(bottomost left) to vertex F(topmost right) in the graph is D -> E -> C -> F, with a total path weight of 2 + 4 + 4 = 10. Other paths from D to F are also possible, but they have a heigher total weight, so they can not be considered to be the shortest path.

### Solutions to the Shortest Path Problem

- Dijkstrea's algorithm and the Bellman-Ford algorithm find the shortest path from one start vertex, to all other vertices.
- To solve the shortest path problem means to check the edges inside the Graph until we find a path where we can move from one vertex to another using the lowest possible combined weight along the edges.
- this sum of weights along the edges that mke up a path is called a **path cost** or a **path weight**.
- algorithms that find the shortest paths, like the Dijkstra's algorithm or the Bellman-Ford algorithm, find the shortest paths from one start vertex to all the other vertices.
- To begin with, the algorithms set the distance from the start vertex to all vertices to be infinitely long. And as the algorithms run, edges between the vertices are checked over and over, and shorter paths might be found many times until the shortest paths are found at the end.
- Every time an edge is checked and it leads to a shorter distance to a vertex being found and updated, it is called a **relaxation** or **relaxing an edge**.

### Positive and Negative Edge Weights

- Some algorithms that find the shortest paths, like the Dijkstra's algorithm, cna only find the shortest paths in graphs where all the edges are positive. Such graphs with positive distances are also the easiest to understand because we can think of the edges between the vertices as distances between locations.
- if we interpret the edge weighs as money lost by going down one vertex to another, a positive edge weight of 4 from vertex A to C in a graph means that we must spend $4 to go from A to C.
- But graphs can also have negative edges, and for such the Bellman-Ford algorithm can be used to find the shortest paths.
- and similarly, if the edge weights represent money lost, the negative edge weight -3 from vertex C to A in a graph can be understood as an edge where there is more money to be made than money lost by going from C to A. So, if for example, the cost of fuel is $5 going from C to A, and we get paid $8 for picking up packages in C and delivering them in A, money lost is -3, meaning we are actually earning $3 in total.


### Negative Cycles in Shortest Path Problems

- FInding the shortest paths becomes impossible if a graph has negative cycles.
- Having a negative cycle means that there is a path where you can go in circles, and the edges that make up this circle have a total path weight that is negative.
- Lets say, in an example graph, the path A -> E -> B -> C -> A is a negative cycle because the total path weight is 5 + 2 - 4 - 4 = 1.
- the reason why it is impossible to find the shortest paths in a graphs with negative cycles is that it will always be possible to continue running an algorithms to find even shorter paths.
- Lets say for example that we are looking for the shortest distance from vertex D in a graph, to all other vertices. At first, we find the distance from D to E to be 3, by just walking the edge D -> E. But after this, if we talk one round in the negative cycle E -> B -> C -> A -> E, then the distance to E becomes 2. After walking one more round the distance becomes 1, which is even shorter, and so on. We can always walk one more round in the negative cycle to find the shorter distance to E, which means the shortest distance cna never be found.
- Luckily, the Bellman-Ford algorithm, that runs on graphs with negative edges, can be implemented with detection for negative cycles.


## Dijkstra's Algorithm

- Dijkstra's shortest path algorithm was invented in 1956 by the Dutch computer scientist Edsger W. Dijkstra's during a twenty minutes coffee break, while out shopping with his fiancee in Amsterdam.
- The reason for inventing the algorithm was to test a new computer called ARMAC.

- Dijkstra's Algorithm finds the shortest path from one vertex to all other vertices.
- It does so by repeatedly selecting the nearest unvisited vertex and calculating the distance to all the unvisited neighboring vertices.

- Dijkstra's Algorithm is often considered to be the most straightforward algorithm for solving the shortest path problem.
- Dijkstra's Algorithm is used for solving single-source shortest path problems for directed or undirected paths. Single-source means that one vertex is chosen to be the start, and the algorithm mwill find the shortest path from that vertex to all other vertices.
- Dijkstra's Algorithm does not work for graphs with negative edges. For graphs with negative edges, the Bellman-Ford algorithm that can be used instead.
- To find the shortest path, Dijkstra's Algorithm needs to know which vertex is the source, it needs a way to mark vertices as visited, and it needs an overview of the current shortest distance to each vertex as it works its way through the graph, updating these distances when a shorter distance is found.

**How it works?**

1. Set initial distances for all vertices: 0 for the source vertex, and infinity for all the other.
2. Choose the unvisited vertex with the shortest distance from the start to be the current vertex. So the algorithm will always start with the source as the current vertex.
3. FOr each of the current vertex's unvisited neighbor vertices, calculate the distance from the source and update the distance if the new, calculated, distance is lower.
4. We are now done with the current vertex, so we mark it as visited. A visited vertex is not checked again.
5. GO back to step 2 to choose a new current vertex, and keep repeating these steps until all vertices are visited.
6. In the end, we are left with the shortest path from the source vertex to every other vertex in the graph.

**Note:**
- the basic version of Dijkstra's Algorithm gives us the value of the shortest path cost to every vertex, but not what the actual path is. So, for example, if we get the shortest path cost value 10 to vertex F in a graph, but the algorithm does not give us which vertices (D -> E -> C -> D -> F) that make up this shortest path. We will add this functionality later.


### A Detailed Dijkstra's Simulation

- If you run through a specific graph using Dijkstra Algorithm, you'll see that the distances calculated from vertex D to all other vertices, by always choosing the next vertex to be the closest unvisited vertex from the starting point.

### Manual Run Through of Dijkstra Algorithm

- Lets take an example graph, where we want to find the shortest path from the source vertex D to all other vertices, so that for example, the shortest path to C is D -> E -> C, with path weight 2 + 4 = 6.
- to find the shortest path, Dijkstra Algorithm uses an array with the distances to all other vertices, and initially sets these distances to infinite, or a very big number. And distance to the vertex we start from (the source) is set to 0.

- `distances = [inf, inf, inf, 0, inf, inf, inf]
    #vertices [A ,  B ,  C , D,  E ,  F ,  G]
`

- now, if we portray the above code in a graph, we see the initial infinite distances to other vertices from the starting vertex D. The distance value for vertex D is 0 because that is the starting point.

- Dijkstra Algorithm then sets the vertex D as the current vertex, and looks at the distance to the adjacent vertices. Since the initial distance to vertices A and E is infinite, the new distance to these are updated with the edge weights. So, vertex A gets the distance changed from infinite to 4, and vertex E gets the distance changed to 2. Note that, updating the distance values in this way is called 'relaxing'.

- After relaxing vertices A and E, vertex D is considered visited,and will not be visited again.
- The next vertex to be chosen as the current verrtex must the vertex with the shortest distances to the source vertex (vertex D), among the previously unvisited vertices. Vertex E is therefore chosen as the current vertex after vertex D.

- the distance to all adjacent and not previously visited vertices from vertex E must not be calculated, and updated if needed.
- the calculated distance from D to vertex A, via E, is 2 + 4 = 6. But the current distance to vertex A is already 4, which is lower, so the distance to vertex A is not updated.
- The distance to vertex C is calculated to be 2 + 4 = 6, which is less than infinity, so the distance to vertex C is updated.
- Similarly, the distance to node G is calculated and updated to be 2 + 5 = 7.
- the next vertex to be visited is vertex A because it has the shortest distance from D of all the unvisited vertices.

- the calculated distance to vertex C, via A, is 4 + 3 = 7, which is higher than the already set distance to vertex C, so the distance to vertex C is not updated.
- Vertex A is now marked as visited, and the next current vertex is vertex C because that has the lowest distance from vertex D between the remaining unvisited vertices.

- Vertex F gets updated distance 6 + 5 = 11, and vertex B gets updated distance 6 + 2 = 8.
- calculated distance to vertex G via vertex C is 6 + 5 = 11 which is higher than the already set distance of 7, so distance to vertex G isnot updated.
- vertex C is marked as visitedd, and the next vertex to be visited is G because it has the lowest distance between the remaining unvisited vertices.

- vertex F already has a distance of 11. This is lower than the calculated distance from G, which is 7 + 5 = 12, so the distance to vertex F is not updated.
- vertex G is marked as visited, and B becomes the current vertex because it has the lowest distance of the remaining unvisited vertices.

- the new distance to F via B is 8 + 2 = 10, because it is lower than F's existing distance of 11.
- vertex B is marked as visited, and there is nothing to check for the last unvisited vertex F, so Dijkstra's algorithm is finished.
- every vertrex has been visited only once, and the result is the lowest distance from the source vertex D to every other vertex in the graph.


### Implementation of Dijkstra's Algorithm

- To implement Dijkstra's algorithm, we create a `Graph` class. The `Graph` class represents the graph with its vertices and edges.
- example in Python -

`
class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight # for undirected graph

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data
`

- here, in line - self.adj_matrix = [[0] * size for _ in range(size)]
    - we create the `adj_matrix` to hold all the edges and edge weights. Initial values are set to `0`.

- in line - self.size = size
    - `size` is the number of vertices in the graph.

- in line - self.vertex_data = [''] * size
    - the `vertex_data` holds the names of all the vertices.

- in line - def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight  # For undirected graph
    - the `add_edge` method is used to add an edge from vertex `u` to vertex `v`, with edge weight `weight`.

- in line - def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data
    - the `add_vertex_data` method is used to add a vertex to the graph. The index where the vertex should belong is given with the `vertex` argument, and the `data` is the name of the vertex.

- the `Graph` class also contains the method that runs the Dijkstra's algorithm:
`
def dijkstra(self, start_vertex_data):
    start_vertex = self.vertex_data.index(start_vertex_data)
    distances = [float('inf')] * self.size
    distances [start_vertex] = 0
    visited = [False] * self.size

    for _ in range(self.size):
        min_distance = float('inf')
        u = None
        for i in range(self.size):
            if not visited[i] and distances[i] < min_distance:
                min_distance = distances[i]
                u = i

            if u is None:
                break

            visited[u] = True

            for v in range(self.size):
                if self.adj_matrix[u][v] != 0 and not visited[v]:
                    alt = distances[u] + self.adj_matrix[u][v]
                    if alt <distances[v]:
                        distances[v] = alt
    
    return distances
`

- here, in line distances = [float('inf')] * self.size
        distances[start_vertex] = 0
    - the initial distance is set to infinity for all the vertices in the `distances` array, except for the start vertex, where the distance is 0.

- in line - visited = [False] * self.size
    - all vertices are initially set to `False` to mark them as not visited in the `visited` array.

- in line - min_distance = float('inf')
            u = None
            for i in range(self.size):
                if not visited[i] and distances[i] < min_distance:
                    min_distance = distances[i]
                    u = i
    - the next current vertex is found. Outgoing edges from this vertex will be checked to see if shorter distances can be found. It is the unvisited vertex with the lowest distance from the start.

- in line - if u is None:
                break
    - here, if the next current vertex has not been found, the algorithm is finished. This means that all vertices that are reachable from the source have been visited.

- in line - visited[u] = True
    - here, the current vertex is set as visited before relaxing adjacent vertices. This is more effective because we avoid checking the distance to the current vertex itself.

- in line - for v in range(self.size):
                if self.adj_matrix[u][v] != 0 and not visited[v]:
                    alt = distances[u] + self.adj_matrix[u][v]
                    if alt < distances[v]:
                        distances[v] = alt
    - here, distances are calculated for not visited adjacent vertices, and updated if the new calculated distance is lower.

- After defining the `Graph` class, the vertices and edges must be defined to initialize the specific graph, and the complete code for this Dijkstra's algorithm example looks like this - 
`
class Graph:
    def __init__(self, size):
        self.adj_matrix=[[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight # for undirected graph

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex <self.size:
            self.vertex_data[vertex] = data

    def dijkstra(self, start_vertex_data):
        start_vertex = self.vertex_data.index(start_vertex_data)
        distance = [float('inf')] * self.size
        distances[start_vertex] = 0
        visited = [False] * self.size

        for _ in range(self.size):
            min_distance = float('inf')
            u = None
            for i in range(self.size):
                if not visited[i] and distances[i] < min_distance:
                    min_distance = distances[i]
                    u = i

            if u is None:
                break

            visited[u] = True

            for v in range(self.size):
                if self.adj_matrix[u][v] != 0 and not visited[v]:
                    alt = distances[u] + self.adj_matrix[u][v]
                    if alt < distances[v]:
                        distances[v] = alt

        return distances

g = Graph(7)

g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')

g.add_edge(3, 0, 4)  # D - A, weight 5
g.add_edge(3, 4, 2)  # D - E, weight 2
g.add_edge(0, 2, 3)  # A - C, weight 3
g.add_edge(0, 4, 4)  # A - E, weight 4
g.add_edge(4, 2, 4)  # E - C, weight 4
g.add_edge(4, 6, 5)  # E - G, weight 5
g.add_edge(2, 5, 5)  # C - F, weight 5
g.add_edge(2, 1, 2)  # C - B, weight 2
g.add_edge(1, 5, 2)  # B - F, weight 2
g.add_edge(6, 5, 5)  # G - F, weight 5

#Dijkstra's algorithm from D to all vertices
print("\nDijkstra's Algorithm starting from vertex D:")
distances = g.dijkstra('D')
for i, d in enumerate(distances):
    print(f"Distance from D to {g.vertex_data[i]}: {d}")
`


### Dijkstra's Algorithm on Directed Graphs

- to run Dijkstra's algorithm on directed graphs, very few changes are needed.
- similarly to the change we needed for cycle detection for directed graphs, we just need to remove one line of code so that the adjacency matrix is not symmetric anymore.
- lets implement this directed graph and run Dijkstra's algorithm from vertex D.

- Here's the implementation of Dijkstra's algorithm on the directed graph, with vertex D as the source vertex:
`
class Graph:
    def __init__(self, size):
        self.adj_matrix=[[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            # self.adj_matrix[v][u] = weight # for undirected graph

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex <self.size:
            self.vertex_data[vertex] = data

    def dijkstra(self, start_vertex_data):
        start_vertex = self.vertex_data.index(start_vertex_data)
        distance = [float('inf')] * self.size
        distances[start_vertex] = 0
        visited = [False] * self.size

        for _ in range(self.size):
            min_distance = float('inf')
            u = None
            for i in range(self.size):
                if not visited[i] and distances[i] < min_distance:
                    min_distance = distances[i]
                    u = i

            if u is None:
                break

            visited[u] = True

            for v in range(self.size):
                if self.adj_matrix[u][v] != 0 and not visited[v]:
                    alt = distances[u] + self.adj_matrix[u][v]
                    if alt < distances[v]:
                        distances[v] = alt

        return distances

g = Graph(7)

g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')

g.add_edge(3, 0, 4)  # D - A, weight 5
g.add_edge(3, 4, 2)  # D - E, weight 2
g.add_edge(0, 2, 3)  # A - C, weight 3
g.add_edge(0, 4, 4)  # A - E, weight 4
g.add_edge(4, 2, 4)  # E - C, weight 4
g.add_edge(4, 6, 5)  # E - G, weight 5
g.add_edge(2, 5, 5)  # C - F, weight 5
g.add_edge(2, 1, 2)  # C - B, weight 2
g.add_edge(1, 5, 2)  # B - F, weight 2
g.add_edge(6, 5, 5)  # G - F, weight 5

#Dijkstra's algorithm from D to all vertices

print("\nDijkstra's Algorithm starting from vertex D:")
distances = g.dijkstra('D')
for i, d in enumerate(distances):
    print(f"Distance from D to {g.vertex_data[i]}: {d}")
`

- by removing/omitting just this line -  #self.adj_matrix[v][u] = weight   For undirected graph - we are able to convert a directed graph into an indirected graph.

- the key difference between a directed and undirected graph traversal using Dijkstra's algorithm is that - in this case, vertex B cannot be visited from D, and this means that the shortest distance from D to F is now 11, and not 10, because the path can no longer go through vertex B.


### Returning The Paths from Dijkstra's Algorithm

- With a few adjustments, the actual shortest paths can also be returned by Dijkstra's algorithm, in addition to the shortest path values. So for example, instead of just returning that the shortest path value is 10 from vertex D to F, the algorithm can also return that the shortest path is "D -> E -> C -> B -> F".

- to return the path, we create a `predecessors` array to keep the previous vertex in the shortest path for each vertex. The `predecessors` array can be used to backtrack to find the shortest path for every vertex.

- example in py - 
`
class Graph:
    def __init__(self, size):
        self.adj_matrix=[[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight # for undirected graph

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex <self.size:
            self.vertex_data[vertex] = data

    def dijkstra(self, start_vertex_data):
        start_vertex = self.vertex_data.index(start_vertex_data)
        distance = [float('inf')] * self.size
        predecessors = [None] * self.size #adding predecessors here for returning paths
        distances[start_vertex] = 0
        visited = [False] * self.size

        for _ in range(self.size):
            min_distance = float('inf')
            u = None
            for i in range(self.size):
                if not visited[i] and distances[i] < min_distance:
                    min_distance = distances[i]
                    u = i

            if u is None:
                break

            visited[u] = True

            for v in range(self.size):
                if self.adj_matrix[u][v] != 0 and not visited[v]:
                    alt = distances[u] + self.adj_matrix[u][v]
                    if alt < distances[v]:
                        distances[v] = alt
                        predecessors[v] = u #another predecessors added

        return distances, predecessors #returning both - distance and predecessor

    def get_path(self, predecessors, start_vertex, end_vertex):
        path = []
        current = self.vertex_data.index(end_vertex)
        while current is not None:
            path.insert(0, self.vertex_data[current])
            current = predecessors[current]
            if current == self.vertex_data.index(start_vertex):
                path.insert(0, start_vertex)
                break
        return '->'.join(path) # join the vertices with '->'

g = Graph(7)

g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')

g.add_edge(3, 0, 4)  # D - A, weight 5
g.add_edge(3, 4, 2)  # D - E, weight 2
g.add_edge(0, 2, 3)  # A - C, weight 3
g.add_edge(0, 4, 4)  # A - E, weight 4
g.add_edge(4, 2, 4)  # E - C, weight 4
g.add_edge(4, 6, 5)  # E - G, weight 5
g.add_edge(2, 5, 5)  # C - F, weight 5
g.add_edge(2, 1, 2)  # C - B, weight 2
g.add_edge(1, 5, 2)  # B - F, weight 2
g.add_edge(6, 5, 5)  # G - F, weight 5

#Dijkstra's algorithm from D to all vertices
print("\nDijkstra's Algorithm starting from vertex D:")
distances, predecessors = g.dijkstra('D')
for i, d in enumerate(distances):
    path = g.get_path(predecessors, 'D', g.vertex_data[i])
    print(f"{path}, Distance: {d}")
`

- here, in line - predecessors = [None] * self.size
                - predecessors[v] = u
    - the `predecessors` array is first initialized with `None` values, then it is updated with the correct predecessor for each vertex as the shortest path values are updated.

- in line - def get_path(self, predecessors, start_vertex, end_vertex):
        path = []
        current = self.vertex_data.index(end_vertex)
        while current is not None:
            path.insert(0, self.vertex_data[current])
            current = predecessors[current]
            if current == self.vertex_data.index(start_vertex):
                path.insert(0, start_vertex)
                break
        return '->'.join(path)  # Join the vertices with '->'
    - the `get_path` method uses the `predecessors` array and returns a string with the shortest path from start to end vertex


### Dijkstra's Algorithm with a Single Destination Vertex

- Lets say we are only interested in finding the shortest path between two vertices, like finding the shortest distance between vertex D(midpoint) and vertex F(fatherest) in a graph.

- Dijkstra's algorithm is normally used for finding the shortest path from one source vertex to all other vertices in the graph, but it can also be modified to only find the shortest path from the source to a single destination vertex, by just stopping the algorithm when the destination is reached (visited).
- this means that for the specific graph we're talking about, Dijkstra's algorithm will stop after visiting F(the destination vertex), before visiting vertices H, I, and J because they are farther away from D than F is.
- Lets say, vertex F got visited and just got updated with distance 10 from vertex B(adjacent to it). Since F is the unvisited vertex with the lowest distance from D, it would normally be the next current vertex, but since it is the destination, the algorithm stops. If the algorithm did not stop, J(last node) would be the next vertex to get an updated distance 11 + 2 = 13, from vertex I(second last).
- the code below is Dijkstra's algorithm implemented to find the shortest path to a single destination vertex - 
`
class Graph:
        def __init__(self, size):
        self.adj_matrix=[[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight # for undirected graph

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex <self.size:
            self.vertex_data[vertex] = data

    def dijkstra(self, start_vertex_data, end_vertex_data):
        start_vertex = self.vertex_data.index(start_vertex_data)
        end_vertex = self.vertex_data.index(end_vertex_data)
        distances = [float('inf')] * self.size
        predecessors = [None] * self.size
        distances[start_vertex] = 0
        visited = [False] * self.size

        for _ in range(self.size):
            min_distance = float('inf')
            u = None
            for i in range(self.size):
                if not visited[i] and distances[i] < min_distance:
                    min_distance = distances[i]
                    u = i

            if u is None or u == end_vertex:
                print(f"Breaking out of loop. Current Vertex: {self.vertex_data[u]}")
                print(f"Distances: {distances}")
                break

            visited[u] = True
            print(f"Visited vertex: {self.vertex_data[u]}")

            for v in range(*self.size):
                if self.adj_matrix[u][v] != 0 and not visited[v]:
                    alt = distances[u] + self.adj_matrix[u][v]
                    if alt < distances[v]:
                        distances[v] = alt
                        predecessors[v] = u

        return distances[end_vertex], self.get_path(predecessors, start_vertex_data, end_vertex_data)

    def get_path(self, predecessors, start_vertex, end_vertex):
        path = []
        current = self.vertex_data.index(end_vertex)
        while current is not None:
            path.insert(0, self.vertex_data[current])
            current = predecessors[current]
            if current == self.vertex_data.index(start_vertex):
                path.insert(0, start_vertex)
                break
        return '->'.join(path) # join the vertices with '->'

#example usage
g = Graph(7)

#rest of the graph setup
g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')

g.add_edge(3, 0, 4)  # D - A, weight 5
g.add_edge(3, 4, 2)  # D - E, weight 2
g.add_edge(0, 2, 3)  # A - C, weight 3
g.add_edge(0, 4, 4)  # A - E, weight 4
g.add_edge(4, 2, 4)  # E - C, weight 4
g.add_edge(4, 6, 5)  # E - G, weight 5
g.add_edge(2, 5, 5)  # C - F, weight 5
g.add_edge(2, 1, 2)  # C - B, weight 2
g.add_edge(1, 5, 2)  # B - F, weight 2
g.add_edge(6, 5, 5)  # G - F, weight 5

distance, path = g.dijkstra('D', 'F')
print(f"Path: {path}, Distance: {distance}")

`

- here, in line -if u is None or u == end_vertex:
                    print(f"Breaking out of loop. Current vertex: {self.vertex_data[u]}")
                    print(f"Distances: {distances}")
                    break
    - if we are about to choose the destination vertex as the current vertex adn mark it as visited, it means we have already calculated the shortest distance to be the destination vertex, and the Dijkstra's algorithm can be stopped in this single destination case.


### Time Complexity for Dijkstra's algorithm

- with V as the number of vertices in our graph, the time complexity for Dijkstra's algorithm is - 
    - Big O(V * V) #V squared basically

- the reason why we get this time complexity is that the vertex with the lowest distance must be search for the next current vertex, and that takes Big O(V) time. And since this must be done for every vertex connected to the source, we need to factor that in, and so we get the time complexity - Big O(V * V) for Dijkstra's algorithm.
- By using a Min-heap or Fibonacci-heap data structure for the distances instead, the time needed to search for the minimum distance vertex is reduced from Big O(V) to Big O(log V), which results in an improved time complexity for Dijkstra's algorithm -

    - Big O(V.logV + E)

        - here, V is the number of vertices in the graph, and E is the number of edges.
    
- the improvement we get from using a Min-heap data structure for Dijkstra's algorithm is especially good if we have a large and sparse graph, which means a graph with a large number of vertices, but not as many edges.
- the implementation of Dijkstra's algorithm with the Fibonacci-heap data structure is better for dense graphs, where each vertex has an edge to almost every other vertex.


## Bellman-Ford Algorithm

- the Bellman-Ford algorithm is best suited to find the shortest paths in a directed graph, with one or more negative edge weights, from the source vertex to all other vertices.
- It does so by repeatedly checking all the edges in the graph for shorter paths, as many as there are vertices in the graph(minus 1).

- the Bellman-Ford algorithm can also be used for graphs with positive edges(both directed and undirected), like we can with Dijkstra's algorithm, but Dijkstra's algorithm is preferred in such cases because it is faster.
- Using the Bellman-Ford algorithm on a graph with negative cycles will not produce a result of shortest paths because in a negative cycle, we can always go one more round and get a shorter path.
- A negative cycle is a path we can follow in circles, where the sum of the edge weights is negative.
- Luckily, the Bellman-Ford algorithm can be implemented to safely detect and report the presence of negative cycles.

**How it works?**
1. Set initial distance to zero for the source vertex, and set initial distances to infinity for all other vertices.
2. For each edge, check if a shorter distance can be calculated, and update the distance if the calculated distance is shorter.
3. Check all edges(step 2) V - 1 times. This is as many times as there are vertices (V), minus one.
4. Optional: Check for negative cycles. (will be explained better later).


### Manual Run Through

- the Bellman-Ford algorithm is actually quite straight forward, because it checks all the edges, using the adjacency matrix. Each check is to see if a shorter distance can be made by going from the vertex on one side of the edge, via the edge, to the vertex on the other side of the edge.
- And this check of all edges is done V - 1 times, with V being the number of vertices in the graph.
- In an example graph, our Bellman-Ford algorithm checks all the edges in the adjacency matrix in our graph - 5 - 1 = 4 times.

        A B C D E
    A       4   5
    B       -4 
    C   -3
    D   4    7  3
    E     2 3

- the first four edges that are checked in our graph are A -> C, A -> E, B -> C, and C -> A. These first four edge checks do not lead to any updates of the shortest distances because the starting vertex of all these edges has an infinite distance.
- AFter the edges from vertices A, B, C are checked, the edges from D are checked. Since the starting point (vertex D) has distance 0, the updated distances for A, B, and C are the edge weights going out from vertex D.
- the next edges to be checked are the edges going from vertex E, which leads to updated distances for vertices B and C.
- the Bellman-Ford algorithm have now checked all edges 1 time. the algorithm will check all edegs 3 more times before it is finished, because the Bellman-Ford algorithm will check all edges as many times as there are vertices in the graph, minus 1.
- the algorithm starts checking all edges a second time, starting with checking the edges going out from vertex A. Checking the edges A -> C and A -> E do not lead to updated distances.
- the next edge to be checked is B -> C, going out from vertex B. this leads to an updated distance from vertex D to C of 5 - 4 = 1.
- Checking the next edge C -> A, leads to an updated distance 1 - 3 = -2 for vertex A.
- the check of edge C -> A in round 2 of the Bellman-Ford algorithm is actually the last check that leads to an updated distance for this specific graph. the algorithm will continue to check all edges 2 more times without updating any distances.
- Checking all edges V - 1 times in the Bellman-Ford algorithm may seem like a lot, but it is done this many times to make sure that the shortest distances will always be found.


### Implementation of the Bellman-Ford Algorithm

- implementing the Bellman-Ford algorithm is very similar to how we implemented the Dijkstra's algorithm.
- We start by creating the `Graph` class, where the methods `__init`, `add_edge`, and `add_vertex` will be used to create the specific graph we want to run the Bellman-Ford algorithm on to find the shortest paths.

`
class Graph:
    def __init__(self, size):
        self.adj_matrix = [[10] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            #self.adj_matrix[v][u] = weight # For undirected graph

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def bellman_ford(self, start_vertex_data):
        start_vertex = self.vertex_data.index(start_vertex_data)
        distances = [float('inf')] * self.size
        distances[start_vertex] = 0

        for i in range(self.size - 1):
            for u in range(self.size):
                for v in range(self.size):
                    if self.adj_matrix[u][v] != 0:
                        if distances[u] + self.adj_matrix[u][v] < distances[v]:
                            distances[v] = distances[u] + self.adj_matrix[u][v]
                            print(f"Relaxingg edge {self.vertex_data[u]} - {self.vertex_data[v]}, Updated distances to {self.vertex_data[v]}: {distances[v]}")
        return distances
`

- notice that, the `bellman_ford` method is also placed inside the `Graph` class. It is this method that runs the Bellman-Ford algorithm.

- here, line - distances = [float('inf')] * self.size
            distances[start_vertex] = 0
    - at the beginning, all vertices are set to have an infinite long distance from the starting vertex, except for the starting vertex itself, where the distance is set to 0.
- line - for i in range(self.size - 1):
    - here, all edges are checked V - 1 times using for loop.
- line - for u in range(self.size):
                for v in range(self.size):
    - a double for-loop checks all the edges in the adjacency matrix. For every vertex `u`, check edges going to vertices `v`.
- line - if self.adj_matrix[u][v] != 0:
                        if distances[u] + self.adj_matrix[u][v] < distances[v]:
                            distances[v] = distances[u] + self.adj_matrix[u][v]
    - if the edge exist, and if the calculated distance si shorter than the existing distance, update the distance to that vertex `v`.
    
    - The complete code, including the initialization of our specific graph and code for running the Bellman-Ford algorithm, looks like this -

`
class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            #self.adj_matrix[v][u] = weight # for undirected graph
    
    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def bellman_ford(self, start_vertex_data):
        start_vertex = self.vertex_data.index(start_vertex_data)
        distances = [float('inf')] * self.size
        distances[start_vertex] = 0

        for i in range(self.size - 1):
            for u in range(self.size):
                for v in range(self.size):
                    if self.adj_matrix[u][v] != 0:
                        if distances[u] + self.adj_matrix[u][v] < distances[v]:
                            distances[v] = distances[u] + self.adj_matrix[u][v]
                            print(f"Relaxing edge {self.vertex_data[u]} - {self.vertex_data[v]}, Updated distance to {self.vertex_data[v]}: {distances[v]}")
        return distances

g = Graph(5)

g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')

g.add_edge(3, 0, 4)  # D -> A, weight 4
g.add_edge(3, 2, 7)  # D -> C, weight 7
g.add_edge(3, 4, 3)  # D -> E, weight 3
g.add_edge(0, 2, 4)  # A -> C, weight 4
g.add_edge(2, 0, -3) # C -> A, weight -3
g.add_edge(0, 4, 5)  # A -> E, weight 5
g.add_edge(4, 2, 3)  # E -> C, weight 3
g.add_edge(1, 2, -4) # B -> C, weight -4
g.add_edge(4, 1, 2)  # E -> B, weight 2

#Running the bellman-ford algorithm from D to all vertices
print("\nThe Bellman-Ford Algorithm starting from vertex D:")

distances = g.bellman_ford('D')

for i, d in enumerate(distances):
    print(f"Distance from D to {g.vertex_data[i]} : {d}")
`

### Negative Edges in the Bellman-Ford Algorithm

- to say that the Bellman-Ford algorithm finds the "shortest paths" is not intuitive, because how can we draw or imagine distances that are negative? So, to make it easier to understand we could isntead say that it is the "cheapest paths" that are found with Bellman-Ford.
- In practise, the Bellman-Ford Algorithm could for example help us to find delivering routes where the edges weights represent the cost of fuel and other things, minus the money to be made by driving that edge between those two vertices.
- With this implementation in mind, the -3 weight on edge C -> A could mean that the fuel cost is $5 driving from C to A, and that we get paid $8 for picking up packages in C and delivering them in A. So, we end up earning $3 more than we spend. therefore, a total of $2 can be made by driving the delivery route D -> E -> B -> C -> A in our graph.


### Negative Cycles in the Bellman-Ford Algorithm

- if we can go in circles in a graph, and the sum of edges in that circle is negative, we have a negative circle.
- By changing the weight on edge C -> A from -3 to -9, we get two negative cycles: A -> C -> A and A -> E -> C -> A. And every time we check these edges with the Bellman-Ford algorithm, the distances we calculate and update just become lower and lower.
- The problem with negative cycles is that a shortest path does not exist, because we can always go one more round to get a path that is shorter.
- That is why, it is useful to implement the Bellman-Ford algorithm with detection for negative cycles.


### Detection of Negative Cycles in the Bellman-Ford Algorithm

- after running the Bellman-Ford algorithm, checking all edges in a graph V -1 times, all the shortest distances are found.
- but, if the graph continues negative cycles, and we go one more round checking all edges, we will find at least one shorter distance in this last round, right?
- so, to detect negative cycles in the Bellman-Ford algorithm, after checking all edges V -1 times, we just need to check all edges one more time, and if we find a shorter distance this last time, we can conclude that a negative cycle must exist.
- Below is the `bellman-ford` method, with negative cycle detection included, running on the graph example above with negative cycles due to the C -> A edge weight of -9.
- example in py - 

`
def bellman-ford(self, start_vertex_data):
    start_vertex = self.vertex_data.index(start_vertex_data)
    distances = [float('inf')] * self.size
    distances[start_vertex] = 0

    for i in range(self.size - 1):
        for u in range(self.size):
            for v in range(self.size):
                if self.adj_matrix[u][v] != 0:
                    if distances[u] + self.adj_matrix[u][v] < distances[v]:
                        distances[v] = distances[u] + self.adj_matrix[u][v]
                        print(f"Relaxing edeg {self.vertex_data[u]} -> {self.vertex_data[v]}, Updated distance to {self.vertex_data[v]}: {distances[v]}")

    #negative cycle detection
    for u in range(self.size):
        for v in range(self.size):
            if self.adj_matrix[u][v] != 0:
                if distances[u] + self.adj_matrix[u][v] < distances[v]:
                    return (True, None) #Indicate a negative cycle was found
    
    return (False, distances) #indicate no negative cycle and return distances
`

- here, in line -         for u in range(self.size):
            for v in range(self.size):
                if self.adj_matrix[u][v] != 0:
                    if distances[u] + self.adj_matrix[u][v] < distances[v]:
    - all edges are checked one more time to see if there are negative cycles.

- in line - return (True, None)  # Indicate a negative cycle was found
    - returning `True` indicates that a negative cycle exists, and `None` is returned instead of the shortest distances, because finding the shortest distances in a graph with negative cycles does not make sense (because a shorter distance can always be found by checking all edges one more time).

- in line - return (False, distances)  # Indicate no negative cycle and return distances
    - returning `False` means that there is no negative cycles, and the `distances` can be returned.


### Returning the Paths from the Bellman-Ford Algorithm

- we are currently finding the total weight of the shortest paths, so that for example, 'distance from D to A: -2' is a result from running the Bellman-Ford algorithm.
- but, by recording the predecessor of each vertex whenever an edeg is relaxed, we can use that later in our code to print the result including the actual shortest paths. This means we can give more information in our result, with the actual path in addition to the path weight: 'D -> E -> B -> C -> A, Dstance: -2'.
- this last code example is the complte code for the Bellman-Ford algorithm, with everything we have discussed up until now: finding the weights of shortest paths, detecting negative cycles, and finding the actual shortest paths:
- code in py- 
`
class Graph:
	def __init__(self, size):
		self.adj_matrix = [[0] * size for _ in range(size)]
		self.size = size
		self.vertex_data = [''] * size

	def add_edge(self, u, v, weight):
		if 0 <= u < self.size and 0 <= v < self.size:
			self.adj_matrix[u][v] = weight
			#self.adj_matrix[v][u] = weight # for undirected graph
	
	def add_vertex_data(self, vertex, data):
		if 0 <= vertex < self.size:
			self.vertex_data[vertex] = data

	def bellman_ford(self, start_vertex_data):
		start_vertex = self.vertex_data.index(start_vertex_data)
		distances = [float('inf')] * self.size
        predecessors = [None] * self.size
		distances[start_vertex] = 0

		for i in range(self.size - 1):
			for u in range(self.size):
				for v in range(self.size):
					if self.adj_matrix[u][v] != 0:
						if distances[u] + self.adj_matrix[u][v] < distances[v]:
							distances[v] = distances[u] + self.adj_matrix[u][v]
                            predecessors[v] = u
							print(f"Relaxing edge {self.vertex_data[u]} - {self.vertex_data[v]}, Updated distance to {self.vertex_data[v]}: {distances[v]}")
	
	#return distances

		#negative cycle detection
		for u in range(self.size):
			for v in range(self.size):
				if self.adj_matrix[u][v] != 0:
					if distances[u] + self.adj_matrix[u][v] < distances[v]:
						return (True, None) #Indicate a negative cycle was found
    
		return (False, distances) #indicate no negative cycle and return distances

    def get_path(self, predecessors, startg_vertex, end_vertex):
        path=[]
        current = self.vertex_data.index(end_vertex)
        while current is not None:
            path.insert(0, self.vertex_data[current])
            current = predecessors[current]
            if current == self.vertex_data.index(start_vertex):
                path.insert(0, start_vertex)
                break
        return '->'.join(path)

g = Graph(5)

g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')

g.add_edge(3, 0, 4)  # D -> A, weight 4
g.add_edge(3, 2, 7)  # D -> C, weight 7
g.add_edge(3, 4, 3)  # D -> E, weight 3
g.add_edge(0, 2, 4)  # A -> C, weight 4
g.add_edge(2, 0, -3) # C -> A, weight -3
g.add_edge(0, 4, 5)  # A -> E, weight 5
g.add_edge(4, 2, 3)  # E -> C, weight 3
g.add_edge(1, 2, -4) # B -> C, weight -4
g.add_edge(4, 1, 2)  # E -> B, weight 2

#Running the bellman-ford algo from D to all vertices
print("\nThe Bellman-Ford Algorithm starting from vertex D:")
negative_cycle, distances, predecessors = g.bellman_ford('D')
if not negative_cycle:
    for i, d in enumerate(distances):
        if d != float('inf'):
            path = g.get_path(predecessors, 'D', g.vertex_data[i])
            print(f"{path}, Distance: {d}")
        else:
            print(f"No path from D to {g.vertex_data[i]}, Distance: Infinity")
else:
    print("Negative weight cycle detected. Cannot compute shortest paths.")
`

- here, in line - predecessors = [None] * self.size
    - the `predecessors` array holds each vertex' predecessor vertex in the shortest path.

-in line - predecessors[v] = u
    - the `predecessors` array gets updated with the new predecessor vertex every time an edge is relaxed.

- line - def get_path(self, predecessors, start_vertex, end_vertex):
        path = []
        current = self.vertex_data.index(end_vertex)
        while current is not None:
            path.insert(0, self.vertex_data[current])
            current = predecessors[current]
            if current == self.vertex_data.index(start_vertex):
                path.insert(0, start_vertex)
                break
        return '->'.join(path)
    - the `get_path` method uses the `predecessors` array to generate the shortest path string for each vertex.


### Time Complexity for the Bellman-Ford Algorithm

- the time complexity for the Bellman-Ford Algorithm mostly depends on the nested loops.
- the **outer for-loop** runs V - 1 times, or V times in case we also have negative cycle detection. For graphs with many vertices, checking all edegs one less time than there are vertices makes little difference, so we can say that the outer loop contributes with big O(V) to the time compexity.
- the **two inner for-loops** checks all edges in the graph. If we assume a worst case scenario in terms of time complexity, then, we have a very dense graph where every vertex has an edge to every other vertex, so for all vertex V, the edge to all other vertices V must be checked, which contributes with Big O(V * V) to the time complexity. 
- So, in total, we get the time complexity for the Bellman-Ford Algorithm:
        - Big O(V * V * V) - v cubed

- however, in practical situations and especially for sparse graphs, meaning each vertex only has edges to a small portion of the other vertices, time complexity of the two inner for-loops checking all edges can be approximated from Big O(V * V) to Big O(E), and we get the total time complexity for the Bellman-Ford:
        - Big O(V * E)

- the time complexity for the Bellman-Ford Algorithm is slower than for Dijkstra's algorithm, but the Bellman-Ford can find the shortest paths in the graphs with negative edges and it can detect negative cycles, which Dijkstra's algorithm can't do.



## Minimum Spanning Tree Problem

- the Minimum Spanning Tree(MST) is the collection of edges required to connect all vertices in an undirected graph, with the minimum total edge weight.
- One way to find MST, is to run Prim's algorithm, another way to do this which also works for unconnected graphs, is to run Kruskal's algorithm.
- It is called a Minimum Spanning Tree, because it is connected, acyclic, undirected graph, which is the definition of a tree data structure.
- in the real world, finding the Minimum Spanning Tree can help us find the most effective way to connect to the internet or to the electrical grid, or it can help us finding the fastest route to deliver packages.

### An MST Thought Experiment

- lets imagine that the circles(points) in a graph are villages that are without electrical power, and you want to connect them to the electrical grid. After one village is given electrical power, the electrical cables must then be spread out from that village to the others. The villages can then be connected in a lot of different ways, each route having a different cost.
- the electrical cables are expensive, and digging ditches for the cables, or stretching the cables in the air is expensive as well. The terrain can certainly be a challenge, and then there is perhaps a future cost for maintenance that is different depending on where the cables end up.
- all these route costs can be factored in as edge weights in a graph. Every vertex represents a village, and every edge represents a possible route for the electrical cable between two villages.
- After such a graph is created, the Minimum Spanning Tree(MST) can be found, and that will be the most effective way to connect these villages to the electrical grid.
- And this is actually what the first MST algorithm (Boruvka's algorithm) was made for in 1926: To find the best way to connect historical region of Moravia, in the Check Republic, to the electrical grid.


### MST Algorithms

- Can it find the MST (a Minimum Spanning Tree) in an unconnected graph? -> 
    - Prim's Algorithm - No 
    - Kruskal's algorithm - Yes

- How does it start?
    - Prim's Algorithm - The MST grows from a randomly chosen vertex.
    - Kruskal's algorithm - The first edge in the MST is the edge with the lowest edge weight.

- What time complexity does it have?
    - Prim's Algorithm - Big O(V * V), or Big O(E * log V)(optimized)
    - Kruskal's algorithm - Big O(E * log E)


## MST Prim's Algorithm

- Prim's algorithm was invented in 1930 by the Czech mathematician Vojtecj Jarnik.
- The algorithm was then rediscovered by Robert C. Prim in 1957, and then also rediscovered by Edgar W. Dijkstra in 1959. Therefore, the algorithm is also sometimes called "Jarnik's algorithm" or the "Prim-Jarnik algorithm."

- Prim's algorithm finds the Minimum Spanning Tree (MST) in a connected and undirected graph.
- the MST found by Prim's algorithm is the collection of edges in a graph, that connects all vertices, with a minimum sum of edge weights.
- Prim's algorithm finds the MST by first including a random vertex to the MST. The algorithm then finds the vertex with the lowest edge weight from the current MST, and includes that to the MST. Prim's algorithm keeps doing this until all nodes are included in the MST.
- Prim's algorithm is greedy, and has a straightforward way to create a minimum spanning tree.
- For Prim's algorithm to work, all the nodes must be connected. To find the MST's in an unconnected graph, Kruska;'s algorithm can be used instead.


**How it works?**
1. Choose a random vertex as the starting point, and include it as the first vertex in the MST.
2. Compare the edges going out from the MST. Choose the edge with the lowest weight that connects a vertex among the MST vertices to a vertex outside the MST.
3. Add that edge and vertex to the MST.
4. Keep doing step 2 and 3 until all vertices belong to the MST.

**Note**: Since the starting vertex is chosen at random, it is possible to have different edges included in the MST for the same graph, but the total edge weight of the MST will still have the same minimum value.


### Manual Run Through

- Lets run through Prim's algorithm manually on an example graph, so we undeerstand the detailed step-by-step operations before we try to program it.
- Prim's algorithm starts growing the Minimum Spanning Tree(MST) from a random vertex, but for this demonstration, vertex A(left-most node) is chosen as the starting vertex.
- From vertex A, the MST grows along the edge with the lowest weight. So, vertices A and D now belong to the group of vertices that belong to the Minimum Spanning Tree.
- A `parents` array is central to how Prim's algorithm grows the edges in the MST.
- at this point, the `parents` array looks like this -

`
parents = [-1, 0, -1, 0, 3, 3, -1, -1]
#vertices [A, B, C, D, E, F, G, H]
`

- vertex A, the starting vertex, has no parent, and has therefore value `-1`. Vertex D's parent is A, that is why DW's parent value is `0` (vertex A is located at index 0). B's parent is also A, and D is the parent of E and F.
- the `parents` array helps us to keep the MST tree structure (a vertex can only have one parent).
- Also, to avoid cycles and to keep track of which vertices are currently in the MST, the `in_mst` array is used.
- the `in_mst` array currently looks like this - 

`
in_mst = [true, false, false, true, false, false, false, false]
#vertices [A, B, C, D, E, F, G, H]
`

- the next step in Prim's algorithm is to include one more vertex as part of the MST, and the vertex closest to the current MST nodes A and D is chosen.
- Since both A-B and D-F have the same lowest edge weight `4`, either B or F can be chosen as the next MST vertex. We choose B as the next MST vertex here.
- as you can see, the MST edge to E came from vertex D before, now it comes from vertex B, because B-E with weight `6` is lower than D-E with weight `7`. Vertex E can only have one parent in the MST tree structure ( and in the `parents` array), so B-E and D-E can't both be MST edges to E.
- The next vertex in the MST is vertex C, because edge B-C with weight `3` is the shortest edge weight from the current MST vertices.
- As vertex C is included in the MST, edges out from C are checked to see if there are edges with a lower weight from this MST vertex to vertices outside the MST. Edge C-E has a lower weight (`3`) than the previous B-E MST edge(`6`), and the C-H edge gets included in the MST with edge weight `2`.
- Vertex H is the next to be included in the MST, as it has the lowest edge weight `6`, and vertex H becomes the parent of vertex G in the `parents` array.
- The next vertex to be included in the MST is either E or F, because they have both the lowest edge weight to them: `4`.
- we choose vertex E here as the next vertex to be included in the MST for the example.
- the next and last two vertices to be added to the MST are vertices F and G. D-F is the MST edge to F, and E-G is the MST edge to G because these edges are the edegs with the lowest weight from the current MST.


### Implementation of Prim's algorithm

- for Prim's algorithm to find a Minimum Spanning Tree (MST), we create a `Graph` class. We will use the methods inside this `Graph` class later to create the graph from the example above, and to run the Prim's algorithm on it.
- code in py -
`
class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight # For undirected graph

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data
`

- here, in line - self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size
    - at first, the adjacency matrix is empty, meaning there are no edges in the graph. Also, the vertices have no names to start with.

- in line - def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight  # For undirected graph
    - the `add_edge` method is for adding an edge, with an edge weight value, to the undirected graph.

- in line - def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data
    - the `add_vertex_data` method is used for giving names to the vertices, like for example 'A' or 'B'.

- now that the structure for creating a graph is in place, we can implement Prim's algo as a method inside the `Graph` class.
`
    def prims_algo(self):
        in_mst = [False] * self.size
        key_values = [float('inf')] * self.size
        parents = [-1] * self.size

        key_values[0] = 0 # starting vertex

        print("Edge \tWeight ")
        for _ in range(self.size):
            u = min((v for v in range(self.size) if not in_mst[v]), key = lambda v: key_values[v])

            in_mst[u] = True

            if parents[u] != -1: #skip printing for the first vertex since it has no parent 
                print(f"{self.vertex_data[parents[u]]} - {self.vertex_data[u]} \t{self.adj_matrix[u][parents[u]]}")

            for v in range(self.size):
                if 0 < self.adj_matrix[u][v] < key_values[v] and not in_mst[v]:
                    key_values[v] = self.adj_matrix[u][v]
                    parents[v] = u
`

- here, in line - in_mst = [False] * self.size
    - the `in_mst` array holds the status of which vertices are currently in the MST. Initially, none of the vertices are part of the MST.

- in line - key_values = [float('inf')] * self.size
    - the `key_values` array holds the current shortest distance from the MST vertices to each vertex outside the MST.

- in line - parents = [-1] * self.size
    - the MST edges are stored in the `parents` array. Each MST edge is stored by storing the parent index for each vertex.

- in line - key_values[0] = 0  # Starting vertex
    - to keep it simple, and to make this code run like in the "Manual Run Through" example above, the first vertex (vertex A at index `0`) is set as the starting vertex. Changing the index to `4` will run Prim's algorithm from vertex E, and that works just as well.

- in line - u = min((v for v in range(self.size) if not in_mst[v]), key=lambda v: key_values[v])
    - the index is found for the vertex with the lowest key value that is not yet part of the MST.

- in line - for v in range(self.size):
                if 0 < self.adj_matrix[u][v] < key_values[v] and not in_mst[v]:
                    key_values[v] = self.adj_matrix[u][v]
                    parents[v] = u
    - after a new vertex is added to the MST(with this line - in_mst[u] = True), this part of the code checks to see if there are now edegs from this newly added MST vertex that can lower the key values to other vertices outside the MST. If that is the case, the `key_values` and `parents` array are updated accordingly. This can be seen clearly in the example aboev when a new vertex is added to the MST and becomes the active (current) vertex.

- now, we create the graph from the "Manual Run Through" above and run Prim's algo on it:
- code in py - 
`
g = Graph(8)

g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')
g.add_vertex_data(7, 'H')

g.add_edge(0, 1, 4)  # A - B
g.add_edge(0, 3, 3)  # A - D
g.add_edge(1, 2, 3)  # B - C
g.add_edge(1, 3, 5)  # B - D
g.add_edge(1, 4, 6)  # B - E
g.add_edge(2, 4, 4)  # C - E
g.add_edge(2, 7, 2)  # C - H
g.add_edge(3, 4, 7)  # D - E
g.add_edge(3, 5, 4)  # D - F
g.add_edge(4, 5, 5)  # E - F
g.add_edge(4, 6, 3)  # E - G
g.add_edge(5, 6, 7)  # F - G
g.add_edge(6, 7, 5)  # G - H

print("Prim's Algorithm MST: ")
g.prims_algo()

`

- here, in line - for v in range(self.size):
    - we can actually avoid the last loop in Prim's algo by changing this line to for _ in range(self.size - 1):. This is because when there is just one vertex not yet in the MST, the parent vertex for that vertex is already set correctly in the `parents` array, so the MST is actually already found at this point.


### Time Complexity for Prim's Algorighm

- with V as the number of vertices in our graph, the time complexity for Prim's algorithm is 
    - Big O(V * V)

- the reason why we get this time complexity is because of the nested loops inside the Prim's algorithm (one for-loop with two other for-loops inside it).
- The first for-loop(for _ in range(self.size):) goes through all the vertices in our graph. This has time complexity of - Big O(V).
- the second for-loop(u = min((v for v in range(self.size) if not in_mst[v]), key=lambda v: key_values[v])) goes through all the adjacent vertices in the graph to find the vertex with the lowest key value that is outside the MST, so that it can be the next vertex included in the MST. This has time complexity of - Big O(V).
- after a new vertex is included in the MST, a third for-loop(for v in range(self.size):) checks all other vertices to see if there are outgoing edges from the newly added MST vertex to vertices outside the MST that can lead to lower key values and updated parent relations. This also has time complexity - Big O(V).

- Putting the time complexities together we get - 
    - Big O(V) * (Big O(V) + Big O(V)) = Big O(V) * (2 * Big O(V))
                                    = Big O(V * 2 * V)
                                    = Big O(2 * V * V)
                                    = Big O(V * V)
    
- By using a priority queue data structure to manage key values, instead of using an array like we do here, the time complexity  for Prim's algo can be reduced to - 
    - Big O(E * log V)

    - where, E is the number of edges in the graph, and V is the number of vertices.

- Such an implementation of Prim's algorithm using a priority queue is best for sparse graphs. A graph is sparse when each vertex is just connected to a few of the other vertices.


## Kruskal's Algorithm

- Kruskal's algorithm finds the Minimum Spanning Tree (MST), or the Minimum Spanning Forest, in an undirected graph.
- the MST (or MSTs) found by Kruskal's algorithm is the collection of edges that connect all vertices (or as many as possible) with the minimum total edge weight.
- Kruskal's algorithm adds edges to the MST (or Minimum Spanning Forest,) starting with the edges with the lowest edge weights.
- Edges that would create a cycle are not added to the MST.
- Kruskal's algorithm checks all edges in the graph.


### Minimum Spanning Forest
- is what it is called when a graph has more than one Minimum Spanning Tree. This happens when a graph is not connected.
- Unlike Prim's algo, Kruskal's algorithm can be used for such graphs that are not connected, which means that it can find more than one MST, and that is what we call a Minimum Spanning Forest.

- here, to find out if an edge will create a cycle, we will use the Union-Find Cycle detection inside Kruskal's algorithm.

**How it works?**
1. Sort the edges in the graph from the lowest to the highest edge weight.
2. For each edge, starting with the one with the lowest edge weight:
    a. Will this edge create a cycle in the current MST?
        - if no: Add the edge as an MST edge.


### Manual Run Through

- lets run through Kruskal's algorithm manually on an example graph, so that we understand the detailed step-by-step operations before we try to program it.
- The first three edges are added to the MST. These three edges have the lowest edge weights and do not create any cycles:
- C-E, weight 2
- D-E, weight 3
- A-B, weight 4

- after that, edge C-D cannot be added as it would lead to a cycle.
- the next four edges Kruskal's algorithm tries to add to the MST are - 
    - E-G, weight 6
    - C-G, weight 7(not added)
    - D-F, weight 7
    - B-C, weight 8

- edge C-G cannot be added to the MST because it would create a cycle.

- as you can already see the MST is already created at this point, but Kruskal's algorithm will continue to run until all the edges are tested to see if they can be added to the MST.
- The last three edges Kruskal's algorithm tries to add to the MST are the ones with the highest edge weights-
    - A-C, weight 9(not added)
    - A-G, weight 10(not added)
    - F-G, weight 11 (not added)

- each of these edges would create a cycle in the MST, so they cannot be added.
- Kruskal's algorithm is now finished.


**Note:**
- Although Kruskal's algorithm checks all the edges in the graph, the example we talked about at the top of this topic stops right after the last edge isadded to the MST or Minimum Spanning Forest so that we donthave to look at all the red edges that cant be added.
- This is possible because for a connected graph, there is just one MST, and the search can stop when the number of edges in the MST is one less than there are vertices in the graph (V - 1). For the unconnected graph, there are two MSTs in our example, and the algorithm stops when the MSTs have reached a size of V - 2 edges in total.


### Implementation of Kruskal's Algorithm

- for Kruskal's algorithm to find a Minimum Spanning Tree(MST), or a Minimum Spanning Forest, we create a `Graph` class. We will use the methods inside the `Graph` class later to create the graph from the example above, and to run the Kruskal's algorithm on it.

- code in py - 
`
class Graph:
    def __init__(self, size):
        self.size = size
        self.edges = [] # for storing edges as (weight, u, v)
        self.vertex_data = [''] * size # store vertex names

    def add_edge(self, u, v, weight):
        if 0 <= u self.size and 0 <= v < self.size:
            self.edges.append((weight, u, v)) # add edge with weight

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data
`

- here, in line - if 0 <= u < self.size and 0 <= v < self.size: 
and 
if 0 <= vertex < self.size:
    - checks if the input arguments `u`, `v`, adn `vertex` are within the possible range of index values.

- to do Union-Find Cycle detection in Kruskal's algo, these two methods `find` and `union` are also defined inside the `Graph` class.

`
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
`

- here, line - def find(self, parent, i):
                    if parent[i] == i:
                        return i
                    return self.find(parent, parent[i])
    - the `find` method uses the `parent` array to recursively find the root of a vertex. For each vertex, the `parent` array holds a pointer (index) to the parent of that vertex. The root vertex is found when the `find` method comes to a vertex in the `parent` array that points to itself. Keep reading to see how the `find` method and the `parent` array are used inside the `kruskals_algo` method.

- in line -     def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
    - when an edge is added to the MST, the `union` method uses the `parent` array to merge (union) two trees. The `rank` array holds a rough estimate of the tree height for every root vertex. When merging two trees, the root with a lesser rank becomes a child of the other tree's root vertex.


- now, here's how Kruskal's algo is implemented as a method inside the `Graph` class:

`
    def kruskals_algo(self):
        result = [] # MST
        i = 0 # edge counter

        self.edges = sorted(self.edges, key = lambda item: item[2])

        parent, rank = [], []

        for node in range(self.size):
            parent.append(node)
            rank.append(0)

        while i < len(self.edges):
            u, v, weight = self.edges[i]
            i += 1

            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                result.append((u, v, weight))
                self.union(parent, rank, x, y)

        print("Edge \tWeight")
        for u, v, weight in result:
            print(f"{self.vertex_data[u]} - {self.vertex_data[v]} \t{weight}")
`

- here, in line - self.edges = sorted(self.edges, key = lambda item: item[2])
    - the edegs must be sorted before Kruskal's algo starts trying to add the edges to the MST.

- in line - parent.append(node)
            rank.append(0)
    - the `parent` and `rank` arrays are initialized. to start with, every vertex is its own root (every element in the `parent` array points to itself), and every vertex has no height (0 values in the rank array).

- in line - u, v, weight = self.edges[i]
            i += 1
    - pick the smallest edge, and increment `i` so that the correct edge is picked in the next iteration.

- in line - x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                result.append((u, v, weight))
                self.union(parent, rank, x, y)
    - if the vertices `u` and `v` at each end of the current edge have different roots `x` and `y`, it means that there will be no cycle for the new edge and the trees are merged. To merge the trees, the current edge is added to the `result` array, and we run the `union` method to make sure the trees are merged correctly, so that there is only one root vertex in the resulting merged tree.

- now, lets create the graph from our manual run through example above and run Kruskal's algo on it - 

- `
class Graph:
    def __init__(self, size):
        self.size = size
        self.edges = [] #For storing edges as (weight, u, v)
        self.vertex_data = [''] * size # store vertex names

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.edges.append((u, v, weight)) #add edeg with weight

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
    
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskals_algo(self):
        result = [] # MST
        i = 0 #edge counter

        self.edges = sorted(self.edges, key = lambda item: item[2])

        parent, rank = [], []

        for node in range(self.size):
            parent.append(node)
            rank.append(0)

        while i < len(self.edges):
            u, v, weight = self.edges[i]
            i += 1

            x = self.find(parent, u)
            y = self.find(parent, v)
            if x!= y:
                result.apend((u, v, weight))
                self.union(parent, rank, x, y)

        print("Edge \tWeight:")
        for u, v, weight in result:
            print(f"{self.vertex_data[u]}-{self.vertex_data[v]} \t{weight}")

g = Graph(7)
g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')

g.add_edge(0, 1, 4)  #A-B,  4
g.add_edge(0, 6, 10) #A-G, 10
g.add_edge(0, 2, 9)  #A-C,  9
g.add_edge(1, 2, 8)  #B-C,  8
g.add_edge(2, 3, 5)  #C-D,  5
g.add_edge(2, 4, 2)  #C-E,  2
g.add_edge(2, 6, 7)  #C-G,  7
g.add_edge(3, 4, 3)  #D-E,  3
g.add_edge(3, 5, 7)  #D-F,  7
g.add_edge(4, 6, 6)  #E-G,  6
g.add_edge(5, 6, 11) #F-G, 11

print("Kruskal's Algorithm MST: ")
g.kruskals_algo()
`


### Time Complexity for Kruskal's Algorithm

- with \(E\) as the number of edges in our graph, the time complexity for Kruskal's algo is - 
    - \[ Big O( E \cdot log{E} ) \]

- we get this time complexity because the edges must be sorted before Kruskal's can start adding edges to the MST. Using a fast algorithm like Quick Sort or Merge Sort gives us a time complexity of \(Big O( E \cdot log{E} ) \) for this sorting alone.

- after the edges are sorted, they are all checked one by one, to see if they will create a cycle, and if not, they are added to the MST.
- although it looks like a lot of work to check if a cycle will be created using the `find` method, and then to include an edge to the MST using the `union` method, this can still be viewed as one operation. The reason we can see this as just one operation is that it takes approximately constant time. That means that the time this operation takes grows very little as the graph grows, and so it does actually not contribute to the overall time complexity.
- Since the time complexity for Kruskal's algorithm only varies with the number of edges \ (E\), it is especially fast for sparse graphs where the ratio between the number of edges \(E\) and the number of vertices \(V\) is relatively low.


## Maximum Flow

- the maximum flow problem is about finding the maximum flow through a directed graph, from one place in the graph to another.
- more specifically, the flow comes from a source vertex s, and ends up in a sink vertex t, and each edge in the graph is degined witha flow and a capacity, where the capacity is the maximum flow that edge can have.

- Finding the maximum flow can be very useful - 
    - for planning roads in a city to avoid future traffic jams.
    - to assess the effect of removing a water pipe, or electrical wire, or network cable.
    - to find out where in the flow network expanding the capacity will lead to the highest maximum flow, with the purpose of increasing for example traffic, data traffic, or water flow.


### Terminology and Concepts

-a **flow network** if often what we call a directed graph with a flow flowing through it.
- the **capacity** c of an edge tells us how much flow is allowed to flow through that edge.
- Each edge also has a **flow** value that tells how much the current flow is in that edge.
    - v1 -> 0/7 -> v2

- the edge in the equation above - v1 -> v2, going from vertex v1 to vertex v2, has its flow and capacity described as `0/7`, which means that the flow is `0`, and the capacity is `7`. So, the flow in this edge can be increased up to 7, but not more.
- in its simplest form, flow network has one `source vertex s` where the flow comes out, and one `sink vertex t` where the flow goes in. The other vertices just have flow passing through them.
- for all vertices except s and t, there is a `conservation of flow`, which means that the same amount of flow that goes into a vertex, must also come out of it.
- the maximum flow is found by algorithms such as Ford-Fulkerson, or Edmonds-Karp, by sending more and more flow through the edges in the flow network until the capacity of the edges are such that no more flow can be sent through. Such a path where more flow can be sent through is called an `augumented path`.
- the Ford-Fulkerson and Edmonds-Karp algorithms are implemented using something called a `residual network`. This will be explained in more detail later.
- the `residual network` is set up with the `residual capacities` on each edge, where the residual capacity of an edge is the capacity on that edge, minus the flow. So, when the flow is increased in a an edge, the residual capacity is decreased with the same amount.
- for each edge in the residual network, there is also a `reversed edge` that points in the opposite direction of the original edge. The residual capacity of a reversed edge is the flow of the original edge. Reversed edges are important for sending flow back on an edge as part of the maximum flow algorithms.
- when the maximum flow is found, we get a value for how much flow can be sent through the flow network in total.


### Multiple Source and Sink Vertices

- the Ford-Fulkerson and Edmonds-Karp algorithms expects one source vertex and one sink vertex to be able to find the maximum flow.
- If the graph has more than one source vertex, or more than one sink vertex, the graph should be modified to find the maximum flow.
- to modify the graph so that you can run the Ford-Fulkerson or Edmonds-Karp algorithm on it, create an extra super-source vertex if you have multiple source vertices, and create an extra super-sink vertex if you have multiple sink-vertices.
- From the super-source vertex, create edges to the original source vertices, with infinite capacities. And create edges from the sink vertices to the super-sink vertex similarly, with infinite capacities.
- To run the Ford-Fulkerson or Edmonds-Karp on an example graph where s1 and s2 are two sources, and t1, t2, t3 are three sinks, a super source S is created with edges with infinite capacities to the original source nodes, and a super sink T is created with edges infinite capacities to it from the original sinks.
- the Ford-Fulkerson or Edmonds-Karp algorithm is now able to find maximum flow in a graph with multiple source and sink vertices, by going from the super source S, to the super sink T.


### The Max-Flow Min-Cut Theorem

- to understand what this theorem says, we first need to know what a cut is.
- we create two sets of vertices: one with only the source vertex inside it called 'S' and one with all the other vertices inside it (including the sink vertex) called 'T'.
- now, starting in the source vertex, we can choose to expand set S by including adjacent vertices, and continue to include adjacent vertices as much as we want as long as we do not include the sink vertex.
- expanding set S will shrink set T, because any vertex belongs either to set S or set T.
- in such a setup, with any vertex belonging to either set S or set T, there is a 'cut' between the sets. the cut consists of all the edges stretching from set S to set T.
- if we add all the capacities from edges going from set S to set T, we get the capacity of the cut, which is the total possible flow from source to sink in this cut.
- the maximum cut is the cut we can make with the lowest total capacity, which will be the bottleneck.
- lets say, in an example graph, we make three cuts - A, B, C, all three with different total capacity and max cuts.

- Cut A - this cut has vertices s and v1 in set S, and the other vertices are set in set T. The total capacity of the edges leaving set S in this cut, from sink to source, is 3 + 4 + 7 = 14. We are not adding the capacity from edge v2 -> v1, because this edge goes in the opposite direction, from sink to source. So the maximum possible flow across cut A is 14.
- Cut B - the maximum possible flow is 3 + 4 + 3 = 10 across cut B.
- cut C - the maximum possible flow is 2 + 6 = 8 across cut C. If we checked all other cuts in the graph, we would not find a cut with a lower total capacity. THis is the minimum cut. In our example above, 8 is the maximum flow, which is what the max-flow min-cut theorem says.
- The max-flo min-cut theorem says that finding the minimum cut in a graph, is the same as finding the maximum flow, because the value of the minimum cut will be the same value as the maximum flow.


### Pracical Implications of the Max-Flow Min-Cut Theorem

- finding the maximum flow in a graph using an algorithm like Ford-Fulkerson also helps us understand where the minimum cut is: The minimum cut will be where the edges have reached full capacity.
- The minimum cut will be where the bottleneck is, so if we want to increase flow beyond the maximum limit, which is often the case in practical solutions, we now know which edges in the graph that needs to be modified to increase the overall flow.
- Modifying edges in the minimum cut to allow more flow can be very sueful in many situations:
    
    - Better traffic flow can be achieved because city planners now know where to create extra lanes, where to re-route traffic, or where to optimize traffic signals.
    - in manufacturing, a higher production output can be reached by targeting improvements where the bottleneck is, by upgrading equipment or reallocating resources for example.
    - in logistics, knowing where the bottleneck is, the supply chain can be optimized by changing the routes, or increase the capacity at critical points, ensuring that goods are moved more effectively from warehouses to consumers.

- So, using maximum flow algorithms to find the minimum cut, helps us to understand where the system can be modified to allow an even higher throughput.


### The Maximum Flow Problem Described Mathematically

- the maximum flow problem is not just a topic in Computer science, it is also a type of mathematical optimization, that belongs to the field of mathematics.


## DS Ford-Fulkerson Algorithm

- the Ford-Fulkerson Algorithm solves the maximum flow problem.
- finding the maximum flow can be helpful in many areas: for optimizing network traffic, for manufacturing, for supply chain and logistics, or for airline scheduling.

- the Ford-Fulkerson Algorithm solves the maximum flow problem for a directed graph.
- the flow comes from a source vertrex(s), and ends up in a sink vertex(t), and each edge in the graph allow a flow, limited by a capacity.
- the Ford-Fulkerson Algorithm works by looking for a path with available capacity from the source to the sink (called an augumented path), and then sends as much flow as possible through that path.
- the Ford-Fulkerson Algorithm continues to find new paths to send more flow through until the maximum flow is reached.
- if we take an example, the Ford-Fulkerson Algorithm solves the maximum flow problem: it finds out how much flow can be sent from the source vertex, s, to the sink vertex, t, and that maximum flow is 8.
- the numbers in the example graph are fractions, where the first number is the flow, and the second number is the capacity (maximum possible flow in that edge). So, for example, `0/7` on edge s -> v2, means there is `0` flow, with a capacity of `7` on that edge.

- **Note**
- the Ford-Fulkerson Algorithm is often described as a method of as an algorithm, because it does not specify how to find a path where flow can be increased. This means it can be implemented in different ways, resulting in different time complexities. But here, we will call it an algorithm, and use DFS to find the paths.


- **How it works?**
1. Start with zero flow on all edges.
2. Find an augumented path where more flow can be sent.
3. Do a bottleneck calculation to find out how much flow can be sent through that augumented path.
4. Increase the flow found from the bottleneck calculation for each edge in the augumented path.
5. Repeat steps 2-4, until max flow is found. This happens when a new augumented path can no longer be found.


### Residual Network in Ford-Fulkerson Algorithm

- the Ford-Fulkerson Algorithm actually works by creating and using something called a residual network, which is a representation of the original path.
- in this residual network, every edge has a residual capacity, which is the original capacity of the edge, minus the flow in that edge. The residual capacity can be seen as the leftover in an edge with some flow.
- For example, if there is a flow of 2 in the v3 -> v4 edge, and the capacity is 3, the residual flow is 1 in that edge, because there is no room for sending 1 more unit of flow through that edge.


### Reversed Edges in Ford-Fulkerson Algorithm

- the Ford-Fulkerson Algorithm also uses something called reversed edegs to send flow back. This is useful to increase the total flow.
- for example, the last augumented path s -> v2 -> v4 -> v3 -> t in the example above and the manual run through below shows how the total flow is increased by one more unit, by actually sending flow back on edge v4 -> v3, sending the flow in the reverse direction.
- sending flow back in the reverse direction on edge v3 -> v4 in our example means that this 1 unit of flow going out of vertex v3, now leaves v3 on edge v3 -> t instead of v3 -> v4.
- to send the flow back, in the opposite direction of the edge, a reverse edge is created for each original edge in the netwkr. The Ford-Fulkerson Algorithm can then use these reverse edges to send flow in the reverse direction.
- a reversed edge has no flow or capacity, just residual capacity. The residual capacity for a reversed edge is always the same as the flow in the corresponding original edge. In our example, the edge v3 -> v4 has a flow of 2, which means there is a residual capacity of 2 on the corresponding reversed edge v4 -> v3.
- this just means that when there is a flow of 2 on the original edge v3 -> v4, there is a possibility of sending that same amount of flow back on that edge, but in the reversed direction. Using a reversed edge to push back flow can also be seen as undoing a part of the flow that is already created.
- the idea of a residual network with residual capacity on edges, and the idea of reversed edges, are central to how the Ford-Fulkerson Algorithm works, and we will go into more detail about this when we implement the algorithm.


### Manual Run Through

- there is no flow in the graph to start with.
- to find the maximum flow, the Ford-Fulkerson Algorithm must increase flow, but first, it needs to find out where the flow can be increased: it must find an augumented path.
- the Ford-Fulkerson Algorithm actually does not specify how such an augumented path is found (that is why it is often described as a method instead of an algorithm), but we will use DFS to find the augumented paths for the Ford-Fulkerson Algorithm here.
- the first augumented path Ford-Fulkerson finds using DFS is s -> v1 -> v3 -> v4 -> t.
- and using the bottleneck calculation, Ford-Fulkerson finds that 3 is the highest flow that can be sent through the augumented path, so the flow is increased by 3 for all the edges in this path.

- the next iteration of the Ford-Fulkerson algorithm is to do these steps again:
    2. Find a new augumented path.
    3. Find how much the flow in that path can be increased.
    4. Increase the flow along the edges in that path accordingly.

- the next augumented path is found to be s -> v2 -> v1 -> v4 -> v3 -> t, which includes the reversed edge v4 -> v3, where the flow is sent back.
- the Ford-Fulkerson concept of reversed edegs comes in handy because it allows the path finding part of the algorithm to find an augumented path where reversed edges can also be included.
- in this specific case, that means that a flow of 2 can be sent back on edge v3 -> v4, going into v3 -> t instead.
- the flow can only be increased by 2 in this path because that is the capacity in the v3 -> t edge.

- the next augumented path is found to be 2 -> v2 -> v1 -> v4 -> t.
- the flow can be increased by 2 in this path. The bottleneck (limiting edge) is v1 -> v4 because there is only room for sending two more units of flow in that edge.

- the next and last augumented path is s -> v2 -> v4 -> t.
- the flow can only be increased by 1 in this path because of edge v4 -> t being the bottleneck in this path with only space for one more unit of flow (capacity - flow = 1).

- at this point, a new augumenting path cannot be found (it is not possible to find a path where more flow can be sent through from s to t), which means the max flow has been found, and the Ford-Fulkerson algo is finished.
- the maximim flow is 8. As you can see now, the flow (8) is the same going out to the source vertex s, as the flow going into the sink vertex t.
- also, if you take any other vertex than s or t, you can see that the amount of flow going into a vertex, is the same as the flow going out of it. This is what we call conservation of flow, and this must hold for all such flow networks (directed graphs where each edge has a flow and a capacity).


### Implementation of the Ford-Fulkerson Algorithm

- to implement the Ford-Fulkerson Algorithm, we create a `Graph` class, the `Graph` represents the graph with its vertices and edges - 
`
class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v, c):
        self.adj_matrix[u][v] = c

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data
`

- here, in line - self.adj_matrix = [[0] * size for _ in range(size)]
    - we create the `adj_matrix` to hold all the edges and edge capacities. Initial values set to `0`.
- in line - self.size = size
    - `size` is the number of vertices in the graph.
- in line - self.vertex_data = [''] * size
    - the `vertex_data` holds the names of all the vertices.
- in line - def add_edge(self, u, v, c):
        self.adj_matrix[u][v] = c
    - the `add_edge` method is used to add an edge from vertex `u` to vertex `v`, with capacity `c`.
- in line - def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data
    - here, the `add_vertex_data` method is used to add a vertex name to the graph. The index of the vertex is given with the `vertex` argument, and `data` is the name of the vertex.

- the `Graph` class also contains the `dfs` method to find augumented paths, using DFS:
`
    def dfs(self, s, t, visited=None, path=None):
        if visited is None:
            visited = [False] * self.size
        if path is None:
            path = []

        visited[s] = True
        path.append(s)

        if s == t
            return path

        for ind, val in enumerate(self.adj_matrix[s]):
            if not visited[ind] and val > 0:
                result_path = self.dfs(ind, t, visited, path.copy())
                if result_path:
                    return result_path
        
        return None
`