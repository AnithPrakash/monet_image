import gradio as gr 
import tensorflow as tf 
import keras 
import os 


#loading model 
cycleGen=tf.keras.models.load_model('cycle-gen-models/model')
cycleGen.load_weights('cycle-gen-models/weights')

def imageProcessing(photo):
    img=tf.image.decode_jpeg(photo,channels=3)
    img=tf.image.resize(img,[256,256])
    img=(img/127.5)-1
    img=tf.expand_dims(img,axis=0)
    
    return img

def image_change(inputs):
    img=imageProcessing(inputs)
    fake_monet,_,_,_=cycleGen((img,img),training=False)
    prediction=(prediction * 127.5 + 127.5).astype(np.uint8)
    img=(img[0] * 127.5 + 127.5).numpy().astype(np.uint8)
    fig=plt.figure()
    plt.title("Monet-esque Paintings")
    plt.imshow(prediction)
    plt.axis("off")

plt.show()

Title="Monet Mimic image 🖌️🎨"

demo=gr.Interface(
    fn=predict,
    inputs=gr.Image(type="jpg"),
    output=image_change(inputs),
    title=title
)

demo.launch()