Bliq Programming Language – Overview

Purpose:
Bliq is a minimalist, beginner-friendly interpreted programming language. It has a very simple syntax and supports variables, input/output, conditions, and loops.

Core Features

Variables

set creates a variable and assigns a value (integer).

add increases the variable’s value.

sub decreases the variable’s value.

input asks the user for a value.

Variables can be inserted into text with !name!.

Examples:

set x 5
add x 3
sub x 2
input name
say Hello !name!


Output

say prints text to the console.

Variables inside ! ... ! are replaced with their values.

Example:

say The value is !x!


Input

input varname asks the user for a value.

The value is stored in a variable.

Example:

input age
say You are !age! years old


Conditions

if starts a block.

Supported comparisons: equals (equal), bigger (greater), smaller (less).

Block ends with end.

Example:

set points 10
if points bigger 5
    say High score!
end


Loops

while repeats a block as long as the condition is true.

Block ends with end.

Example:

set counter 1
while counter smaller 4
    say Counter is !counter!
    add counter 1
end

Keywords

say → print text to console

set → set a variable

add → increase a variable

sub → decrease a variable

input → ask user for input

if ... end → conditional block

while ... end → loop block

Example Program
say Welcome to Bliq
input name
say Hello !name!

set x 1
while x smaller 4
    say Counting: !x!
    add x 1
end

if x equals 4
    say Finished counting
end


Possible Output (if the user enters Emil):

Welcome to Bliq
Hello Emil
Counting: 1
Counting: 2
Counting: 3
Finished counting
