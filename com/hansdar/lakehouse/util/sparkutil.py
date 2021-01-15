from pyspark.sql import SparkSession
from pyspark.sql.functions import lit
from pyspark.sql.types import StringType
from logutil import *


def create_spark_session():
    """Creates Spark session."""
    spark_session = SparkSession.builder.master("local[*]")\
        .appName("ScrumAssistant")\
        .config("spark.executor.memory", "3g")\
        .config("spark.executor.instances", 1)\
        .config("spark.executor.cores", 4)\
        .config("spark.driver.memory", "2g")\
        .config("spark.files.maxPartitionBytes", 33554432)\
        .enableHiveSupport()\
        .getOrCreate()
    spark_session.conf.set("spark.sql.shuffle.partitions", 24)
    return spark_session


def cast_to_string(all_columns):
    """Casts all columns to String."""
    string_columns = []

    for each_column in all_columns:
        string_columns.append(lit(None).cast(StringType()).alias('{0}'.format(each_column)))
    return string_columns
