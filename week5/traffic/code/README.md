# README

## Convolutional Neural Network

1. create a model
   - convolution
     - I chose the 32 filters (3, 3) with activation `relu`
   - max-pooling
     - I chose 2 $\times$ 2 pool size
   - flatten
   - hidden layer
     - 256 units in dense layer
     - dropout rate is set to 0.5 to prevent overfitting
   - output layer
     - 43 units for output
     - activation is set to `softmax`
2. compile model
   - optimizer: `adam`
   - loss : `categorical_crossentropy`
   - metrics: `accuracy`

## result

1. First, I tried the 128 units of dense layer. The accuracy is around 5-6 %, not very accurate. 

2. However, when I changed the dense layer units to 256, the accuracy upsurged.

   this is the result

   ```python
   Epoch 1/10
   500/500 ━━━━━━━━━━━━━━━━━━━━ 4s 6ms/step - accuracy: 0.1656 - loss: 22.0304     
   Epoch 2/10
   500/500 ━━━━━━━━━━━━━━━━━━━━ 3s 6ms/step - accuracy: 0.5865 - loss: 1.5401
   Epoch 3/10
   500/500 ━━━━━━━━━━━━━━━━━━━━ 3s 6ms/step - accuracy: 0.7256 - loss: 0.9414
   Epoch 4/10
   500/500 ━━━━━━━━━━━━━━━━━━━━ 3s 6ms/step - accuracy: 0.7933 - loss: 0.7153
   Epoch 5/10
   500/500 ━━━━━━━━━━━━━━━━━━━━ 3s 6ms/step - accuracy: 0.8293 - loss: 0.5876
   Epoch 6/10
   500/500 ━━━━━━━━━━━━━━━━━━━━ 3s 6ms/step - accuracy: 0.8512 - loss: 0.4988
   Epoch 7/10
   500/500 ━━━━━━━━━━━━━━━━━━━━ 3s 6ms/step - accuracy: 0.8684 - loss: 0.4500
   Epoch 8/10
   500/500 ━━━━━━━━━━━━━━━━━━━━ 3s 7ms/step - accuracy: 0.8750 - loss: 0.4452
   Epoch 9/10
   500/500 ━━━━━━━━━━━━━━━━━━━━ 3s 7ms/step - accuracy: 0.8895 - loss: 0.3961
   Epoch 10/10
   500/500 ━━━━━━━━━━━━━━━━━━━━ 3s 6ms/step - accuracy: 0.8950 - loss: 0.3622
   333/333 - 1s - 2ms/step - accuracy: 0.9123 - loss: 0.3864
   ```

3. When I set the dropout rate to 0.5, the accuracy declined. When I set it to 0.15, here is the result

   ```python
   Epoch 1/10
   500/500 ━━━━━━━━━━━━━━━━━━━━ 4s 7ms/step - accuracy: 0.3528 - loss: 19.9866     
   Epoch 2/10
   500/500 ━━━━━━━━━━━━━━━━━━━━ 4s 9ms/step - accuracy: 0.8429 - loss: 0.5924  
   Epoch 3/10
   500/500 ━━━━━━━━━━━━━━━━━━━━ 4s 9ms/step - accuracy: 0.9090 - loss: 0.3447  
   Epoch 4/10
   500/500 ━━━━━━━━━━━━━━━━━━━━ 5s 9ms/step - accuracy: 0.9369 - loss: 0.2460  
   Epoch 5/10
   500/500 ━━━━━━━━━━━━━━━━━━━━ 4s 9ms/step - accuracy: 0.9453 - loss: 0.2179  
   Epoch 6/10
   500/500 ━━━━━━━━━━━━━━━━━━━━ 4s 8ms/step - accuracy: 0.9512 - loss: 0.1833  
   Epoch 7/10
   500/500 ━━━━━━━━━━━━━━━━━━━━ 3s 7ms/step - accuracy: 0.9519 - loss: 0.2071  
   Epoch 8/10
   500/500 ━━━━━━━━━━━━━━━━━━━━ 3s 7ms/step - accuracy: 0.9489 - loss: 0.2330  
   Epoch 9/10
   500/500 ━━━━━━━━━━━━━━━━━━━━ 3s 7ms/step - accuracy: 0.9579 - loss: 0.1770  
   Epoch 10/10
   500/500 ━━━━━━━━━━━━━━━━━━━━ 3s 7ms/step - accuracy: 0.9675 - loss: 0.1392  
   333/333 - 1s - 3ms/step - accuracy: 0.9337 - loss: 0.3804
   ```

   





