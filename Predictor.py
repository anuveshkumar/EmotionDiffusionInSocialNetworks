# Time dependent analysis

dataset_size = 1000  
tweet_matrix = np.zeros((len(screen_names), dataset_size))  
ouput_vector = np.zeros(dataset_size)  
for i in range(len(dataset_size)):  
  tweet = user_tweet[i]  
   output_vector[i] = predict_sentiment(tweet.text)  
   time = tweet.timestamp  timebuffer = range(time - 12, time)  
   for j in range(len(screen_names)):  
      tweet_list = []  
      try:  
        for tweet in screen_name:  
          if tweet in timebuffer:  
            tweet_list.append(predict_sentiment(tweet.text)  
            avg_sentiment = tweet_list.avg  
            tweet_matrix[i][j] = avg_sentiment  
      except:  tweet_matrix[i][j] = 0.5   

Dataset = pd.DataFrame(data=tweet_matrix[:,:],columns=screen_names)  
Dataset[‘output_sentiment’] = output_vector

from keras.models import Sequential  
from keras.layers import Dense    
model = Sequential  
model.add(Dense(len(screen_names))  
model.add(Dense(1, activation=’sigmoid’))  
model.compile(loss=’binary_crossentropy’,  optimizer=’adam’,metrics=[‘accuracy’])    
model.fit(X_train1, y_train1, validation_data=(X_valid, y_valid),  batch_size=batch_size, epochs=1)    
model.evaluate(X_test, Y_test)  
