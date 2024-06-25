1. Умение писать работающий код
2. Умение тестировать свой код
3. Умение писать эффективный код

# Сложность, тестирование и особые случаи
## Сложность алгоритмов
Сложность алгоритма - порядок количества действий, которые выполняет алгоритм.

https://en.wikipedia.org/wiki/Time_complexity

In theoretical computer science, the time complexity is the computational complexity that describes the amount of computer time it takes to run an algorithm. Time complexity is commonly estimated by counting the number of elementary operations performed by the algorithm, supposing that each elementary operation takes a fixed amount of time to perform. 
the time complexity is generally expressed as a function of the size of the input. Since this function is generally difficult to compute exactly, and the running time for small inputs is usually not consequential, one commonly focuses on the behavior of the complexity when the input size increases—that is, the asymptotic behavior of the complexity. Therefore, the time complexity is commonly expressed using big O notation.

Example of big O notation:
f(x) = O(g(x)) as x->inf since there exists M>0 and x_0 such that 0<=f(x)<=M*g(x) whenever x>=x_0

Также существует "пространственная" сложность

Если никак не удается найти ошибку в прогремме, то можно применить стресс-тестирование. Для этого пишется еще одно максимально простое решение задачи и создается генератор тестов. Затем прогоняем обе программы (написанную, с ошибкой и максимально простую) на каждом тесте. И если мы нашли тест, на котором ответы различны - то его и нужно использовать для отладки изначального решения. Однако стоит помнить, что вообще говоря и в максимально простом решении может быть ошибки...