import matplotlib.pyplot as plt
plt.plot(history.history["accuracy"])
plt.plot(history.history["val_accuracy"])
plt.title("training accuracy's & validation accuracy")
plt.xlabel("epoch")
plt.ylabel("accuracy")
plt.legend(["Train" ,"validation"],loc="upper left")
plt.show()

plt.plot(history.history["loss"])
plt.plot(history.history["val_loss"])
plt.title("train & validation losses curve")
plt.xlabel("epoch")
plt.ylabel("loss")
plt.legend(["train", "validation"],loc="upper right")
plt.show()



layer_names=[layer.name for layer in efficientnet.layers[:10]]
outputs=[layer.output for layer in efficientnet.layers[:10]]

activation_model=tf.keras.Model(inputs=efficientnet.input,outputs=outputs)

sample_image=images[0].reshape((1,224,224,3))

activation=activation_model.predict(sample_image)

for layer_name ,layer_activation in zip(layer_names,activation):
    n_features=layer_activation.shape[-1]
    size=layer_activation.shape[1]
    
    display_grid=np.zeros((size,size * n_features))
    
    for i in range(n_features):
        channel_image = layer_activation[0, :, :, i]
        channel_image -= channel_image.mean()
        channel_image /= channel_image.std()
        channel_image *= 64
        channel_image += 128
        channel_image = np.clip(channel_image, 0, 255).astype('uint8')
        display_grid[:, i * size : (i + 1) * size] = channel_image

    scale = 1.0 / n_features
    plt.figure(figsize=(scale * display_grid.shape[1], scale * display_grid.shape[0]))
    plt.title(layer_name)
    plt.grid(False)
    plt.imshow(display_grid, aspect='auto', cmap='viridis')

plt.show()


