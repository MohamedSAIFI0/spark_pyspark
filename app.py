from pyspark import SparkContext


def main():
		# Crée un SparkContext local nommé 'tp1'
		sc = SparkContext("local", "tp1")

		try:
				# Données 
				ma_liste = [1, 2, 3, 4, 5, 6, 7]

				# Création du RDD
				rdd1 = sc.parallelize(ma_liste)

				# Actions et transformations 
				print("collect:", rdd1.collect())
				print("count:", rdd1.count())
				print("sum:", rdd1.sum())

				moyenne = rdd1.mean()
				print("mean:", moyenne)

				paires = rdd1.map(lambda x: x % 2 == 0)
				print("pairs (is even):", paires.collect())

				impaires = rdd1.map(lambda x: x % 2 != 0)
				# appeler collect()
				print("impairs (is odd):", impaires.collect())

				carres = rdd1.map(lambda x: x ** 2)
				print("squares:", carres.collect())

				sup_10 = rdd1.map(lambda x: x > 10)
				print(">10:", sup_10.collect())

				print("max:", rdd1.max())
				print("min:", rdd1.min())

				print(">10 count:", rdd1.filter(lambda x: x > 10).count())

				mult_2 = rdd1.map(lambda x: x * 2)
				print("times 2:", mult_2.collect())

				print("take(3):", rdd1.take(3))

		finally:
				# Toujours arrêter le contexte Spark proprement
				sc.stop()


if __name__ == "__main__":
		main()

