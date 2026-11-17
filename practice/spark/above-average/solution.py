from pyspark.sql import SparkSession 
from pyspark.sql import functions as F

df = products.withColumn("catalog_avg",products.agg(avg("price")))
filter_df = df.filter(col("price")>col("catalog_avg")).orderBy(col("price").desc())
filter_df.select(
"product_name",
"category",
"price",
"catalog_avg").show()
