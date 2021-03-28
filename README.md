# Calculator

This is a calculator I developed depending on a guideline of VidMob Engineering Take Home Exercise.



## How to use

### Requirement

- Python 3.x should be installed

### Run the program

1. Store all files in calculator.zip at the same location

2. Run calculator.py

3. Working successfully, you can see the below

   > ​	Please enter a mathematical expression. Type 'exit' to leave.
   >
   >  

4. Input an expression; input 'exit' to end the program

5. Get a calculated value; an error might happen through an input validation

## Requirements to develop

- (clear) Take text or string as input
- (clear) Support positive, negative, and decimal numbers
- (clear) Support +, -, *, and / operations
- (clear) Support parentheses
- (clear) A bit of documentation or help text for how to use this program

## How to solve

- Infix -> Postfix

  > Infix Expression: A + B * C + D
  >
  > Postfix Expression: A B C * + D +
  >
  > Ways to do
  >
  > 1. Prioritize operators
  >
  > 2. Suppose parenthesis exists according to the priority of operators
  >
  > 3. Move operatros back after ")"
  >
  > 4. Remove parenthesis
  >
  >    e.g. A + B * C -> (A + ( B * C ) -> A B C * +

## Test

> \> 1 + 2
>
> 3.0
>
> \> 4*5/2
>
> 10.0
>
> \> -5+-8--11*2
>
> 9.0
>
> \> -.32    /.5
>
> -0.64
>
> \> (4-2)*3.5
>
> 7.0
>
> \> 2+-+-4
>
> Syntax Error
>
> \> 19 + cinnamon
>
> Invalid Input

## Updating

- "Stack" class will be added
- Variable names are edited to be intuitive and readable
- Unittest will be implented
- Handle various errors
- Demo will be added