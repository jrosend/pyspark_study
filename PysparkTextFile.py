from pyspark import SparkContext

sparkContext = SparkContext('local[*]')

text = sparkContext.textFile('file:////usr/share/doc/python3.8/copyright')
print('Lines {}'.format(text.count()))

result = text.filter(lambda line: 'python' in line.lower())

print('Lines with python {}'.format(result.count()) )

print('End of process')
