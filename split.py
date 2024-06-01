x_train,x_test,y_train,y_test=train_test_split(images,label,test_size=0.2,random_state=100,shuffle=True)

datagen=ImageDataGenerator(rescale=1.0/255,
                          rotation_range=40,
                          horizontal_flip=True,
                          vertical_flip=True,
                          width_shift_range=0.2,
                          height_shift_range=0.2,
                          zoom_range=0.5,
                          
                          fill_mode="nearest",
                          shear_range=0.2)

train_gen=datagen.flow(
    x_train,
    y=y_train,
    batch_size=8)
valid_gen=datagen.flow(
    x_test,
    y=y_test,
    batch_size=8)
