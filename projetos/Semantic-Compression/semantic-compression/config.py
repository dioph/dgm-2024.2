# PATHS
PATH_TRAIN = "data/city/train" # data/city/train, data/coco/train
PATH_TEST = "data/city/val" # data/city/val, data/coco/val
PATH_MODELS = "models/"
PATH_FIGS = "figs/"

# ARCHITECTURE
C_MODE = 0 # 0=GC, 1=GC+, 2=SC
DTYPE = 32 # 32, 16
DEVICE = 'cuda'
## COMPLEXITY
FILTERS = 128 # 32, 64, 128, 240
N_BLOCKS = 5 # 3, 4, 5, 6
CHANNELS = 2 # 2, 4, 8
N_CONVS = 4
LAMBDA_D = 10
GAN_LOSS = "BCE" # BCE, MSE
## EXTRA TECHNIQUES
DROPOUT = 0.0 # 0, 0.3
REAL_LABEL = 1.0
FAKE_LABEL = 0.0
INPUT_NOISE = 0.0 # 0.0, 0.1
## QUANTIZER
SIGMA = 1000.
LEVELS = 5
L_MIN = -2
L_MAX = 2
## DATA
SHORT_SIZE = 192 # 96, 192, 384
CROP_SHAPE = (128, 256) # CITY: (64, 128, 256); COCO: (96, 192, 384)

# TRAINING
AE_LR = 3E-4 # 1E-4, 3E-4, 1E-3
DC_LR = 3E-4 # 1E-4, 3E-4, 1E-3
BATCH_SIZE = 150 # 50, 100, 150
PT_EPOCHS = 0 # 0, 50
FT_EPOCHS = 1 # 1, 10, 50

# VERBOSE
PLOT_EVERY = 1
SAVE_EVERY = 1
DISC_EVERY = 1
