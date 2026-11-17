from pyspark.sql import SparkSession 
from pyspark.sql import functions as F

condition = users["user_id"] == ad_impressions["user_id"]

inner_df = users.join(ad_impressions,condition,'inner').count()
left_df = users.join(ad_impressions,condition,'left').count()
full_outer_df = users.join(ad_impressions,condition,'full').count()

comb_df = [('inner_join',inner_df),
           ('left_join',left_df),
           ('full_outer_join',full_outer_df)]

final_df = spark.createDataFrame(comb_df,['join_type','row_count'])
final_df.show()
