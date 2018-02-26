from os import path

FULL_LABEL_SIZE = 8922
FULL_LABEL_SIZE_II = 5031

PAD_CHAR = "**PAD**"
EMBEDDING_SIZE = 100
MAX_LENGTH = 2500

#where you want to save any models you may train
MODEL_DIR = path.join(path.dirname(__file__), 'saved_models')

DATA_DIR = path.join(path.dirname(__file__), 'mimicdata/')
MIMIC_3_DIR = path.join(path.dirname(__file__), 'mimicdata/mimic3')
MIMIC_2_DIR = path.join(path.diranem(__file__), 'mimicdata/mimic2')
