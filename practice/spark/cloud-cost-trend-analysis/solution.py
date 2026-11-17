from pyspark.sql import SparkSession 
from pyspark.sql import functions as F

window_spec = Window.partitionBy("svc_name").orderBy("bill_date").asc()

prev_amt = cloud_costs.withColumn("previous_amount", F.lag('amount').over(window_spec))

result_df = prev_amt .withColumn("price_change", F.col("amount")-F.col("previous_amount"))

result_df = result_df.select(
    "svc_name",
    "bill_date",
    "amount",
    "price_change"
)

result_df.show()
