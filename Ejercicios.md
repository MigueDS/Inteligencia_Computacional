Los ejercicios a completar están basados a partir unos ejemplo de funciones en Python para generar algoritmos evolutivos

Las preguntas, que hay que contestar implementando una modificación en el código son las siguientes:

## Exercises

1. If you have knowledge about Object-oriented Programming (OOP) implement the above
algorithm as a Python class.
2. With the current parent selection mechanism, could both parents be the same individual? If so,
how could we modify `select_parents` to avoid that behaviour?
3. Could you write a function to implement a parent selection mechanism based on a
binary tournament?
4. With the current crossover operator, what does happen if both parents are the same individual?
5. Could you write a function to implement a *Uniform Crossover*?
6. In the current version of our GA, the crossover operator is always applied, i.e. the
crossover rate is equal to 1. Sometimes, this is not suitable, so it would be great to
have a crossover rate that decides if the crossover operator is applied or not. Before
applying it, a random number in the range $[0, 1]$ must be generated. If the said random
number is lower than the crossover rate, then the crossover is applied by producing two
new children. Otherwise, both parents become the new children in the offspring population.
7. What value should we use for the mutation rate if we only want to modify one gene at maximum?
By using that value, what does happen with the GA? How could you fix it?
8. How could you use the number of function evaluations as the stopping criterion in the GA?
9. How could you incorporate elitism in the survivor selection scheme?
10. Could you write a version of the GA where a *replace-worst* survivor strategy is considered?
11. The GA works with an even population size. What set of changes would you incorporate to
also allow an odd population size?
