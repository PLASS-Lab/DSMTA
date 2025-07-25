import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import (Input, Conv3D, BatchNormalization, ELU, add, MaxPooling3D, Flatten, Dense, Dropout, concatenate)
from tensorflow.keras.regularizers import l2 as L2

def regression_hinge(y_true, y_pred):
    epsilon = 2
    return tf.keras.backend.mean(tf.keras.backend.maximum(tf.keras.backend.abs(y_true - y_pred) - epsilon, 0.), axis=-1)

def generateAgeGenderPredictionResNet(inputShape, paddingType='same', initType='he_uniform', regAmount=0.00005, dropRate=0.2):
    t1Input = Input(shape=inputShape + (1,), name='T1_Img')

    # Common Encoder
    features = 8
    hidden = Conv3D(features, (3, 3, 3), padding=paddingType, kernel_regularizer=L2(regAmount), kernel_initializer=initType)(t1Input)
    hidden = BatchNormalization()(hidden)
    hidden = ELU(alpha=1.0)(hidden)
    hidden = Conv3D(features, (3, 3, 3), padding=paddingType, kernel_regularizer=L2(regAmount), kernel_initializer=initType)(hidden)
    hidden = BatchNormalization()(hidden)
    shortcut = Conv3D(features, (1, 1, 1), strides=(1, 1, 1), padding=paddingType, kernel_initializer=initType)(t1Input)
    hidden = add([shortcut, hidden])
    outputs = ELU(alpha=1.0)(hidden)

    pooling = MaxPooling3D(pool_size=(2, 2, 2), strides=(2, 2, 2), padding=paddingType)(outputs)

    features = 16
    hidden = Conv3D(features, (3, 3, 3), padding=paddingType, kernel_regularizer=L2(regAmount), kernel_initializer=initType)(pooling)
    hidden = BatchNormalization()(hidden)
    hidden = ELU(alpha=1.0)(hidden)
    hidden = Conv3D(features, (3, 3, 3), padding=paddingType, kernel_regularizer=L2(regAmount), kernel_initializer=initType)(hidden)
    hidden = BatchNormalization()(hidden)
    shortcut = Conv3D(features, (1, 1, 1), strides=(1, 1, 1), padding=paddingType, kernel_initializer=initType)(pooling)
    hidden = add([shortcut, hidden])
    outputs = ELU(alpha=1.0)(hidden)

    pooling = MaxPooling3D(pool_size=(2, 2, 2), strides=(2, 2, 2), padding=paddingType)(outputs)

    features = 32
    hidden = Conv3D(features, (3, 3, 3), padding=paddingType, kernel_regularizer=L2(regAmount), kernel_initializer=initType)(pooling)
    hidden = BatchNormalization()(hidden)
    hidden = ELU(alpha=1.0)(hidden)
    hidden = Conv3D(features, (3, 3, 3), padding=paddingType, kernel_regularizer=L2(regAmount), kernel_initializer=initType)(hidden)
    hidden = BatchNormalization()(hidden)
    shortcut = Conv3D(features, (1, 1, 1), strides=(1, 1, 1), padding=paddingType, kernel_initializer=initType)(pooling)
    hidden = add([shortcut, hidden])
    outputs = ELU(alpha=1.0)(hidden)

    pooling = MaxPooling3D(pool_size=(2, 2, 2), strides=(2, 2, 2), padding=paddingType)(outputs)

    features = 64
    hidden = Conv3D(features, (3, 3, 3), padding=paddingType, kernel_regularizer=L2(regAmount), kernel_initializer=initType)(pooling)
    hidden = BatchNormalization()(hidden)
    hidden = ELU(alpha=1.0)(hidden)
    hidden = Conv3D(features, (3, 3, 3), padding=paddingType, kernel_regularizer=L2(regAmount), kernel_initializer=initType)(hidden)
    hidden = BatchNormalization()(hidden)
    shortcut = Conv3D(features, (1, 1, 1), strides=(1, 1, 1), padding=paddingType, kernel_initializer=initType)(pooling)
    hidden = add([shortcut, hidden])
    outputs = ELU(alpha=1.0)(hidden)

    pooling = MaxPooling3D(pool_size=(2, 2, 2), strides=(2, 2, 2), padding=paddingType)(outputs)

    # Age Prediction Branch
    age_features = 128
    age_hidden = Conv3D(age_features, (3, 3, 3), padding=paddingType, kernel_regularizer=L2(regAmount), kernel_initializer=initType)(pooling)
    age_hidden = BatchNormalization()(age_hidden)
    age_hidden = ELU(alpha=1.0)(age_hidden)
    age_hidden = Conv3D(age_features, (3, 3, 3), padding=paddingType, kernel_regularizer=L2(regAmount), kernel_initializer=initType)(age_hidden)
    age_hidden = BatchNormalization()(age_hidden)
    age_shortcut = Conv3D(age_features, (1, 1, 1), strides=(1, 1, 1), padding=paddingType, kernel_initializer=initType)(pooling)
    age_hidden = add([age_shortcut, age_hidden])
    age_outputs = ELU(alpha=1.0)(age_hidden)

    age_pooling = MaxPooling3D(pool_size=(2, 2, 2), strides=(2, 2, 2), padding=paddingType)(age_outputs)

    age_hidden = Flatten()(age_pooling)
    age_hidden = Dense(128, kernel_regularizer=L2(regAmount), kernel_initializer=initType, name='FullyConnectedLayer_Age')(age_hidden)
    age_hidden = ELU(alpha=1.0)(age_hidden)
    age_hidden = Dropout(dropRate)(age_hidden)
    age_prediction = Dense(1, kernel_regularizer=L2(regAmount), name='AgePrediction')(age_hidden)

    # Gender Classification Branch
    gender_features = 128
    gender_hidden = Conv3D(gender_features, (3, 3, 3), padding=paddingType, kernel_regularizer=L2(regAmount), kernel_initializer=initType)(pooling)
    gender_hidden = BatchNormalization()(gender_hidden)
    gender_hidden = ELU(alpha=1.0)(gender_hidden)
    gender_hidden = Conv3D(gender_features, (3, 3, 3), padding=paddingType, kernel_regularizer=L2(regAmount), kernel_initializer=initType)(gender_hidden)
    gender_hidden = BatchNormalization()(gender_hidden)
    gender_shortcut = Conv3D(gender_features, (1, 1, 1), strides=(1, 1, 1), padding=paddingType, kernel_initializer=initType)(pooling)
    gender_hidden = add([gender_shortcut, gender_hidden])
    gender_outputs = ELU(alpha=1.0)(gender_hidden)

    gender_pooling = MaxPooling3D(pool_size=(2, 2, 2), strides=(2, 2, 2), padding=paddingType)(gender_outputs)

    gender_hidden = Flatten()(gender_pooling)
    gender_hidden = Dense(128, kernel_regularizer=L2(regAmount), kernel_initializer=initType, name='FullyConnectedLayer_Gender')(gender_hidden)
    gender_hidden = ELU(alpha=1.0)(gender_hidden)
    gender_hidden = Dropout(dropRate)(gender_hidden)
    gender_prediction = Dense(1, activation='sigmoid', kernel_regularizer=L2(regAmount), name='GenderPrediction')(gender_hidden)

    # Model
    model = Model(inputs=t1Input, outputs=[age_prediction, gender_prediction])
    
    return model

