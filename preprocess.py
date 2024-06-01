from sklearn.preprocessing import LabelEncoder
ln=LabelEncoder()
train["label"]=ln.fit_transform(train["label"])
def newdataset(row):
    if row["is_tma"]:
        return f"{test_path}/{row['image_id']}_thumbnail.png"
    else:
        return f"{path}/{row['image_id']}_thumbnail.png"
train["image_path"]=train.apply(newdataset,axis=1)
print(train.head())

from sklearn.preprocessing import LabelEncoder
def getter(dataframe, path,augmenter_function=None):
    classes = []
    images = []
    for row in dataframe.iterrows():
        img_path = os.path.join(path,f"{str(row[1][0])}_thumbnail.png")
        
        classes.append(row[1][1])
        images.append(preprocessing(img_path))
       
    
    encoder = LabelEncoder()
    label = encoder.fit_transform(classes)
    labels_list = list(encoder.classes_)
        
    return images, label, labels_list

