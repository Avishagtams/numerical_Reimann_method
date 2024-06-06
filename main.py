def riemann_method(function, a, b, n):
  """
  Calculates an approximation to the integral of a function f in a section [a, b] using the Riemann method with n subsections.

  Arguments:
    f: continuous function derivable.
    A: The beginning of the integration section.
    B: End of the integration section.
    n: number of subsections.

  Returns:
    Approximation to the integral.
  """

  if n <= 0:
    raise ValueError("The number of subsections n should be positive")

  # Calculate the size of each subsection.
  dx = (b - a) / n

  # Sum of the areas of the rectangles.
  sum_areas = 0
  for i in range(n):
    x_i = a + i * dx
    sum_areas += function(x_i) * dx

  return sum_areas

#example

def function(x):
  return x**2

a = 0
b = 1
n = 4

integral_sulotion = riemann_method(function, a, b, n)
print("Approximation to the integral of x^2 in the section [0, 1] using the Reimann method with 4 subsections:", integral_sulotion)
