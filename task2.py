'''
В фермерском хозяйстве в Карелии выращивают чернику.
Она растёт на круглой грядке, причём кусты высажены только по окружности.
Таким образом, у каждого куста есть ровно два соседних.
Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью,
поэтому ко времени сбора на них выросло различное число ягод —
на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход,
находясь непосредственно перед некоторым кустом,
собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод,
которое может собрать за один заход собирающий модуль,
находясь перед некоторым кустом заданной во входном файле грядки.
'''
def max_collected_berries(N, berries):
    max_collected = 0

    for i in range(N):
        # Calculate the number of berries collected when the picking module is in front of the i-th bush
        collected = berries[i] + berries[(i-1)%N] + berries[(i+1)%N]
        max_collected = max(max_collected, collected)

    return max_collected

# Read the input
N = int(input("Enter the number of bushes: "))
berries = []
for i in range(N):
    berries.append(int(input("Enter the number of berries on bush " + str(i+1) + ": ")))

# Call the function and print the result
result = max_collected_berries(N, berries)
print("Maximum number of berries that can be collected in one run:", result)
