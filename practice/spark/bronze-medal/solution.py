from pyspark.sql import functions as F
from pyspark.sql.window import Window

window_spec = Window.orderBy(F.col("amount").desc())

df = cloud_costs.withColumn(
    "dense_rank",
    F.dense_rank().over(window_spec)
)

final_df = df.select(col('amount')).filter(col('dense_rank')<=3).distinct()
return final_df
