import pickle
from tensorflow import keras
from keras.preprocessing.sequence import pad_sequences
import numpy as np


MODEL = keras.models.load_model('kaggle_model_63')
with open('tokenizer.pickle', 'rb') as f:
    TOKENIZER = pickle.load(f)

with open('labels.pickle', 'rb') as f:
    LABELS = pickle.load(f)

MAX_SEQUENCE_LENGTH = 100


def text_to_emoji(model, tokenizer, text: str):
    sequences = tokenizer.texts_to_sequences([text])
    query = pad_sequences(sequences, maxlen=MAX_SEQUENCE_LENGTH)
    output = model.predict(query)
    label_id = np.argmax(output)
    for e, v in LABELS.items():
        if v == label_id:
            return e

def get_emoji(text: str) -> str:
    return text_to_emoji(MODEL, TOKENIZER, text)
