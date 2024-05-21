from intent.config.configuration import *
from intent.components.model_evaluation import *

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation = ModelEvaluation(config = model_evaluation_config) 
            model_evaluation.evaluate()
        except Exception as e:
            raise e