from keras.layers import Input, Dense, concatenate, Activation
from keras.models import Model
tweet_input = Input(shape=(45,), dtype='int32')
tweet_encoder = Embedding(100000, 200, weights=[embedding_matrix],
input_length=45, trainable=True)(tweet_input)
bigram_branch = Conv1D(filters=100, kernel_size=2, padding='valid',
activation='relu', strides=1)(tweet_encoder)
bigram_branch = GlobalMaxPooling1D()(bigram_branch)
trigram_branch = Conv1D(filters=100, kernel_size=3, padding='valid',
activation='relu', strides=1)(tweet_encoder)
trigram_branch = GlobalMaxPooling1D()(trigram_branch)
fourgram_branch = Conv1D(filters=100, kernel_size=4, padding='valid',
activation='relu', strides=1)(tweet_encoder)
fourgram_branch = GlobalMaxPooling1D()(fourgram_branch)

merged = concatenate([bigram_branch, trigram_branch, fourgram_branch], axis=1)
merged = Dense(256, activation='relu')(merged)
merged = Dropout(0.2)(merged)
merged = Dense(1)(merged)
output = Activation('sigmoid')(merged)
model = Model(inputs=[tweet_input], outputs=[output])
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

from keras.callbacks import ModelCheckpoint
filepath="CNN_best_weights.{epoch:02d}-{val_acc:.4f}.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='val_acc', verbose=1,
save_best_only=True, mode='max')
model.fit(x_train_seq, y_train, batch_size=32, epochs=5,
validation_data=(x_val_seq, y_validation)


from keras.models import load_model
loaded_CNN_model = load_model('CNN_best_weights.hdf5')
def predict_sentiment(tweet):
  tweet = tokenizer.texts_to_sequnces(tweet_cleaner(tweet))
  return loaded_CNN_model.predict(tweet)
  Senti = predict_sentiment(tweet)
