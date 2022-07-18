# Databricks notebook source
import pyspark.sql.functions as F
from pyspark.sql.window import Window
from datetime import datetime, date, timedelta, time
import plotly.express as px
import sys
import os
import pandas as pd
import numpy as np

# COMMAND ----------

#SOURCE
white = spark.table("winequality_white_csv")
red = spark.table("winequality_red_1_csv")

# COMMAND ----------

display(white)

# COMMAND ----------


