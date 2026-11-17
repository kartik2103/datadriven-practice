from pyspark.sql import functions as F
from pyspark.sql.window import Window

combined_df = (
    cloud_costs.select("svc_name", "region", "amount")
    .unionByName(
        cost_allocs.select("svc_name", "region", "amount")
    )
)

w_desc = Window.partitionBy("region").orderBy(
    F.col("amount").desc(),
    F.col("svc_name").asc()
)

w_asc = Window.partitionBy("region").orderBy(
    F.col("amount").asc(),
    F.col("svc_name").asc()
)

ranked_df = (
    combined_df
    .withColumn("expensive_rank", F.row_number().over(w_desc))
    .withColumn("cheap_rank", F.row_number().over(w_asc))
)

result_df = ranked_df.groupBy("region").agg(
    F.max(
        F.when(F.col("expensive_rank") == 1, F.col("svc_name"))
    ).alias("most_expensive"),

    F.max(
        F.when(F.col("cheap_rank") == 1, F.col("svc_name"))
    ).alias("cheapest")
)

result_df.orderBy("region").show()
