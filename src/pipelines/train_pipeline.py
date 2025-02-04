import sys,os
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer


if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))


'''class TraininingPipeline:

    
    def start_data_ingestion(self):
        try:
            data_ingestion = DataIngestion()
            feature_store_file_path = data_ingestion.initiate_data_ingestion()
            return feature_store_file_path
            
        except Exception as e:
            raise CustomException(e,sys)
        


        
    
    def start_data_transformation(self, feature_store_file_path):
        try:
            data_transformation = DataTransformation(feature_store_file_path= feature_store_file_path)
            train_arr, test_arr,preprocessor_path = data_transformation.initiate_data_transformation()
            return train_arr, test_arr,preprocessor_path
            
        except Exception as e:
            raise CustomException(e,sys)


    def start_model_training(self, train_arr, test_arr):
        try:
            model_trainer = ModelTrainer()
            model_score = model_trainer.initiate_model_trainer(
                train_arr, test_arr
            )
            return model_score
            
        except Exception as e:
            raise CustomException(e,sys)
        

    def run_pipeline(self):
        try:
            feature_store_file_path = self.start_data_ingestion()
            train_arr, test_arr,preprocessor_path = self.start_data_transformation(feature_store_file_path)
            r2_square = self.start_model_training(train_arr, test_arr)
            
            
            print("training completed. Trained model score : ", r2_square)

        except Exception as e:
            raise CustomException(e, sys)


if __name__=="__main__":
    obj=TraininingPipeline()
    obj.run_pipeline()'''