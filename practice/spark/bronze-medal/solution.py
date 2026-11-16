from pyspark.sql.functions import col

result = cloud_costs.select('amount').distinct().orderBy(col('amount').desc()).limit(3)

return result
