Задача: построить непрерывно-детерминированную модель системы и сформировать с ее помощью заданныого вида колебаний.
Порядок моделирования динамической системы:
1)Привести исходную систему дифференциальных уравнений к явному виду и понизить порядок до первого. 
2)Провести численное интегрирование заданным методом. 
3)Построить графики реализации динамического процесса во времени и фазовые портреты. 
4)Подстроить параметры для получения различных видов колебаний (амплитуда колебаний не должна бесконечно возрастать). 
5) Если колебание хаотическое, то построить график зависимости среднеквадратического расстояния между реализациями колебательного 
процесса от начальных условий .Если колебание регулярное, то построить график зависимости среднеквадратической ошибки от шага
интегрирования.
Динамическая система: Контур с нелинейным затуханием. Уравнение и описание системы:x" - e(1-x^2)x` + x = 0
При e->0 колебания гармонические. Нелинейные свойства проявляются при значениях e ≫ 1. 
Метод численного интегрирования: метод Адамса
Порядок: 2

Решение:
Код описания численного интегрирования уравнения методом Адамса 2 порядка представлен в файле main.py.Колебательный процесс расположен
по оси х на 14 позиций и по оси y на 100 позиций в виде 2 графиков.
Код для визуализации фазового портрета уравнения представлен в файле faza.py.Фазовый портрет представлен в различных вариациях
при некоторых условиях (без начальных параметров, с начальными параметрами х0=0 и y0=100, с изменением параметра e=0.001,
в увеличенном формате)
Код для построения графика зависимости среднеквадратической ошибки от шага интегрирования представлен в файле Graf.py