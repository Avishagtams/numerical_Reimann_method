def riemann_integral_approximation(f, start, end, num_subsections):
  """
  Calculates an approximation to the integral of a function f over the interval [start, end] using the Riemann method with num_subsections subsections.

  Arguments:
    f: The function to integrate. It should be a continuous and differentiable function.
    start: The start point of the integration interval.
    end: The end point of the integration interval.
    num_subsections: The number of subsections to divide the interval into.

  Returns:
    Approximation to the integral.
  """

  if num_subsections <= 0:
    raise ValueError("The number of subsections should be positive")

  # Calculate the width of each subsection.
  delta_x = (end - start) / num_subsections

  # Sum of the areas of the rectangles.
  sum_areas = 0
  for i in range(num_subsections):
    x_i = start + i * delta_x
    sum_areas += f(x_i) * delta_x

  return sum_areas

# Example

def square_function(x):
  """Defines the function f(x) = x^2."""
  return x**2

start_point = 0
end_point = 1
num_subsections = 4000

integral_approximation = riemann_integral_approximation(square_function, start_point, end_point, num_subsections)
print("Approximation to the integral of x^2 over the interval [0, 1] using the Riemann method with 4000 subsections:", integral_approximation)
