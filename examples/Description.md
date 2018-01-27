# Factorial Function:

## The Factorial Function
### Python Code
Python is a modern multi-paradigm programming language, its syntax resembles that of English language.
#### Recursive
The most basic implementation as a recursive function is almost litterally the definition from maths:
```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

```
However, this function isn't good for large numbers. After `factorial(997)` there will be an error because of the recursion depth. It is also slow.
#### For-Loop
This is way it is faster to implement a for loop.
```python
def factorial_for(n):
    if n == 0:
        return 1
    else:
        res = 1
        for e in range(1, n+1):
            res = res * e
        return res
```
### Elixir Code
Elixir is a relatively new functional programming language, its syntax is similar to ruby code and maybe even better to read than python.
#### Recursive
```elixir
  def factorial(0), do
    1
  end
  def factorial(n) do 
    n * factorial(n-1)
  end
```
This code has the same disadvantage like the python code, however there is another workaround, namely pattern matching.
```elixir
  def factorial_tail(0, res) do
    res
  end
  def factorial_tail(n, res) do
    factorial_tail(n-1, n*res)
  end
```
### C Code
C is a very old programming language its structure is more or less assembly code, with descriptive names.
#### Recursive
```C
int factorial(int n)
{
    if (n == 0)
    {
        return 1;
    } 
    else
    {
        return n * factorial(n-1);
    }
}
```
This code has several disadvantages, high numbers are not represented in an int, rather use long long int or other libraries.
Of course this will also be ineffective for large numbers, because of the method calls.

#### For Loop
```
int factorial_for(int n)
{
    if (n == 0)
    {
        return 1;
    }
    int res = 1;
    for (int i = n; i > 0; --i)
    {
        res *= i;
    }
    return res;
}
```

## The Factorial of 10
- [Bytecode](a.out)

### Assembly Code
```assembly
.LFB0:
    .cfi_startproc
    pushq   %rbp
    .cfi_def_cfa_offset 16
    .cfi_offset 6, -16
    movq    %rsp, %rbp
    .cfi_def_cfa_register 6
    movl    %edi, -20(%rbp)
    movq    %rsi, -32(%rbp)
    movl    $10, -4(%rbp)
    movl    $1, -12(%rbp)
    movl    -4(%rbp), %eax
    movl    %eax, -8(%rbp)
    jmp .L2
.L3:
    movl    -12(%rbp), %eax
    imull   -8(%rbp), %eax
    movl    %eax, -12(%rbp)
    subl    $1, -8(%rbp)
.L2:
    cmpl    $0, -8(%rbp)
    jg  .L3
    movl    -12(%rbp), %eax
    popq    %rbp
    .cfi_def_cfa 7, 8
    ret
    .cfi_endproc
```


### Corresponding C-Code

```C
    int n = 10;
    int res = 1;
    for (int i = n; i > 0; --i)
    {
        res *= i;
    }
    return res;

```














