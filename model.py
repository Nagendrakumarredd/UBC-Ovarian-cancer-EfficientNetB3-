weights_path = "/kaggle/input/efficientnetb3-weights/efficientnetb3_notop.h5"  # Replace with the path to the downloaded file
efficientnet = EfficientNetB3(
    include_top=False,
    weights=weights_path,
    input_shape=(224, 224, 3)
)

for layer in efficientnet.layers:
    layer.trainable=False
x=tf.keras.layers.Flatten()(efficientnet.output)
#x=tf.keras.layers.GlobalAveragePooling2D()(efficientnet.output)
x=tf.keras.layers.Dropout(0.5)(x)
x=tf.keras.layers.Dense(1024,activation="relu",kernel_regularizer=regularizers.l2(1e-4))(x)
x=tf.keras.layers.Dense(5,activation="softmax")(x)
model=tf.keras.Model(inputs=efficientnet.input,outputs=x)
model.summary()


model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),loss=tf.keras.losses.SparseCategoricalCrossentropy(),metrics=['accuracy'])

reduce_lr=ReduceLROnPlateau(monitor="val_loss",factor=0.1,patience=5,min_lr=1e-5)
epoch=50 
history=model.fit(
    images,label,validation_split=0.2,
    epochs=epoch,
    batch_size=8,
    callbacks=[reduce_lr]
)

