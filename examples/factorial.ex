defmodule Factorial do
  def factorial(0) do
    1
  end
  def factorial(n) do 
    n * factorial(n-1)
  end

  def factorial_tail(0, res) do
    res
  end
  def factorial_tail(n, res) do
    factorial_tail(n-1, n*res)
  end
end