from pyspark.sql import SparkSession
from logutil import *


def create_spark_session():
    """Creates Spark session."""
    spark_session = SparkSession.builder.master("local[*]")\
        .appName("lakehouse")\
        .config("spark.executor.memory", "3g")\
        .config("spark.executor.instances", 1)\
        .config("spark.executor.cores", 4)\
        .config("spark.driver.memory", "2g")\
        .config("spark.files.maxPartitionBytes", 33554432)\
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
        .getOrCreate()
    return spark_session
