from pyspark import SparkContext

sc = SparkContext("local","tp1")

ma_liste = [1, 2, 3, 4, 5, 6, 7]

rdd1 = sc.parallelize(ma_liste)

print(rdd1.collect())

print(rdd1.count())

print(rdd1.sum())

moyenne = rdd1.mean()
print(moyenne)

paires = rdd1.map(lambda x : x%2 == 0)
print(paires.collect())

impaires = rdd1.map(lambda x : x%2 != 0)
print(impaires.collect)

carres = rdd1.map(lambda x : x**2)
print(carres.collect())

sup_10 = rdd1.map(lambda x : x > 10)
print(sup_10.collect())

print(rdd1.max())
print(rdd1.min())


print(rdd1.filter(lambda x : x > 10).count())


mult_2 = rdd1.map(lambda x : x * 2)
print(mult_2.collect())

print(rdd1.take(3))

