from pyspark.sql import SparkSession 
from pyspark.sql.functions import col
from pyspark.sql.functions import F
from pyspark.sql.window import Window 


df = svc_health.groupBy("svc_name").agg(min(col("uptime")).alias("min_update")).orderBy(col("min_update").asc())

df.limit(10)
