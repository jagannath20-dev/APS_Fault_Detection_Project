from sensor.entity import artifact_entity ,config_entity
from sensor.logger import logging
from sensor.exception import SensorException
from typing import Optional
import os, sys
from sklearn.preprocessing import Pipeline
from sensor import utils
import numpy as np
import pandas as pd
from sensor.config import TARGET_COLUMN
from sklearn.preprocessing import RobustScaler
from sklearn.impute import simple_imputer
from sklearn.combine import SMOTETomek
from sklearn.preprocessing import LabelEncoder


class DataTransfoormation:


    def __init__(self,data_transformation_config:config_entity.DataTransformationConfig,
                 data_ingestion_artifact:artifact_entity.DataIngestionArtifact):


        try:

            self.data_transformation_config = data_transformation_config
            self.data_ingestion_artifact = data_ingestion_artifact

        except Exception as e:
            raise SensorException(e,sys)


    @classmethod
    def get_data_transformer_object(cls) ->Pipeline:

        try:
            simpleImputer = SimpleImputer(strategy='constant',fill_value = 0)
            robust_scaler = RobustScaler()
            pipeline = Pipeline(steps=[
                ('Imputer',simple_imputer),
                ('RobustScaler',robust_scaler)
            ])

            return  pipeline
        except Exception as e:
            raise SensorException(e, sys)

    def  initiate_data_transformation(self,) -> artifact_entity.DataTransformationArtifact:

        try:
            #reading training and test file
            train_df = pd.read_csv(self.data_ingestion_artifact.train_file_path)
            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)


            input_feature_train_df=train_df.drop(TARGET_COLUMN,axis = 1)
            input_feature_test_df=test_df.drop(TARGET_COLUMN,axis=1)

            target_feature_train_df = train_df[TARGET_COLUMN]
            target_feature_test_df = test_df[TARGET_COLUMN]

            
            label_encoder = LabelEncoder()
            label_encoder.fit(target_feature_train_df)
            #Transformation on target columns
            target_feature_train_arr = label_encoder.transform(target_feature_train_df)
            target_feature_test_arr = label_encoder.transform(target_feature_test_df)
             
            #transforming input features
            transformation_pipeline = DataTransformation.get_data_transformer_object()
            transformation_pipeline.fit(input_feature_train_df)


            #transforming input features
            input_feature_train_arr = transformation_pipeline.transform(input_feature_train_df)
            input_feature_test_arr = transformation_pipeline.transform(input_feature_test_df)



            smt = SMOTETomek(sampling_strategy = "minority")

            






        except Exception as e:
            raise SensorException(e, sys)





        






