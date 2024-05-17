from intent.config.configuration import *
from intent.components.model_trainer import *

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer = ModelTrainer(config = model_trainer_config) 
            model_trainer.train()
        except Exception as e:
            raise e 