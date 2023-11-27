import matplotlib.pyplot as plt
import random

plt.figure(figsize=(10,10))

time = [x for x in range(0, 24)]
temperature = [-11.0, -11.2, -11.3, -11.5, -10.9, -10.7,
               -10.7, -10.6, -10.4, -10.2, -10.1, -10.0,
               -9.8, -9.7, -9.8, -9.7, -10.0, -10.1,
               -10.4, -10.5, -10.7, -10.7, -10.9, -11.3]

plt.subplot(221)
plt.plot(time, temperature)
plt.title("график температуры")
plt.xlabel("время, ч")
plt.ylabel("тепература, градусы цельсия")
plt.ylim(-13, -8)


categories = ["бакалея", "молочка", "мясо", "напитки", "рыба"]
total = [random.randint(100, 500) for y in range(5)]

plt.subplot(222)
plt.bar(categories, total)
plt.title("продажи")
plt.xlabel("категория")
plt.ylabel("количество, шт")


weight = []
height = [random.randint(150, 200) for y in range(100)]
for i in range(100):
    weight.append(height[i] + random.randint(-30, 30))

plt.subplot(223)
plt.scatter(height, weight)
plt.title("зависимость роста от веса")
plt.xlabel("вес, кг")
plt.ylabel("рост, см")


marks = [random.randint(1, 10) for y in range(1000)]

plt.subplot(224)
plt.hist(marks)
plt.title("распределение оценок")
plt.xlabel("оценка")
plt.ylabel("количесво учеников")

plt.show()
