from pyspark.sql import SparkSession 
from pyspark.sql.functions import col
from pyspark.sql.functions import F
from pyspark.sql.window import Window 


df = svc_health.groupBy("svc_name").agg(min(col("uptime")).alias("min_update")).orderBy(col("min_update").asc())

window_spec = Window.orderBy(F.col("min_update").asc())

final = df.withColumn('rnk', F.dense_rank().over(window_spec)).filter(F.col('rnk')<=10)

final.drop("rnk").show()
