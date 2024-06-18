from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys

from us_visa.pipeline.training_pipeline import TrainPipeline

pipeline = TrainPipeline()
pipeline.run_pipeline()