<?php
#1Write a function largestOdd(arr) that takes an array arr and returns the largest odd number in it. If there are no odd numbers, it should return a string "No odd numbers found".
function largestOdd($arr){
    return array_reduce($arr,function($prev_result,$item){
            return ($item % 2) && $item >= $prev_result ? $item : $prev_result;
        }) ?? "No odd numbers found";
}
echo largestOdd($arr);
#2Let s be a string that contains a sequence of decimal numbers separated by commas, e.g., s = '1.23,2.4,3.123'. Write a function sequenceSum(s) that prints the sum of the numbers in s.
function sequenceSum($s){
    $sum = 0;
    $sep = explode(", ",$s);
    var_dump ($sep);

    foreach($sep as $i){
        $sum = trim($i) + $sum;
    }

    return $sum;
}
echo sequenceSum('1.1, 2.1, 3.9');


#3Write a function vowelsNumber(s) that accepts string s as a parameter and counts up the number of vowels contained in the string. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
#4Write a function  contains(str1, str2) that accepts two strings str1 and str2 as arguments and returns a boolean True if either string occurs anywhere in the other, and False otherwise. Function should be case insensitive.
#5Write a function isPalindrome(s) that accepts string s as an argument and returns a boolean True if string reads the same way backwards and forwards. The function should be case and spaces insensitive.
#6Write a function findExtremeDivisors(n1, n2). n1 and n2 should be positive ints. The function should return a string “Error: n1 and n2 should be positive ints!” if either n1 or n2 <= 0.The function returns an array of two elements containing the smallest common divisor > 1 and the largest common divisor of n1 and n2.If the are no common divisors, the function should return a string "There are no common divisors".
