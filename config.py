import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

MODULE_PATH = os.path.join(BASE_DIR,"clinicalai")
DATASET_NAME = "MedicalData.json"
RAW_DATA_DIR = os.path.join(MODULE_PATH,"datasets","raw")

PROCESSES_DATA_DIR = os.path.join(MODULE_PATH,"datasets","processed")
