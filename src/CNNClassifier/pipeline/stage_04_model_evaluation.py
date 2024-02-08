from CNNClassifier.config.configuration import ConfigurationManager
from CNNClassifier.components.model_evaluation_mlflow import Evaluation
from CNNClassifier import logger

STAGE_NAME = "Evaluation Stage"

class EvaluationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            eval_config = config.get_evaluation_config()
            evaluation = Evaluation(eval_config)
            evaluation.evaluation()
            evaluation.log_into_mlflow()
        except Exception as e:
            raise e
