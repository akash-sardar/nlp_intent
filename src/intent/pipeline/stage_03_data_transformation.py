from intent.config.configuration import *
from intent.components.data_transformation import *

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config = data_transformation_config) 
            data_transformation.transform_data()
        except Exception as e:
            raise e