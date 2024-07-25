## Monet Minic Image 🖌️🎨
## 1.Overview 

This is project is trying to regain the brushing stroke of Claude Monet by using CycleGen AI .
The main goal is to create a mimic of those stroke to our modern images.It took around 5 to 10 epochs to gain the little quality of those strokes to be copied.


## 2. Dataset 

To do the process we need a bunch of monet paintings so we used the dataset called as gan-getting-started. Its include a 300 of monet paintings and a lot of image captured in modern days which are similar to those paintings 

## 3.Result 

![Screenshot 2024-07-24 174024](https://github.com/user-attachments/assets/425b0efd-9cd1-4f59-9951-7e14dafa9ef9)

This is sample image that generate by the models which copy the feature of the monet paintings 


## 4. CycleGen Model Gradio Interface

This project provides a Gradio interface for the CycleGen model, allowing users to upload images and get Monet-esque paintings as outputs. The model and interface are deployed on Hugging Face Spaces.


## 5.Epochs processing 

![Screenshot 2024-07-24 220534](https://github.com/user-attachments/assets/bdf69137-94ad-4b10-b83e-fe3d7b4c58e2)
This took around 90 min to do that. 

## 6.How to use

 **Upload an Image**:
    - Use the Gradio interface to upload an image.
    - The model will process the image and return a Monet-esque painting.

 **Model Details**:
    - The CycleGen model is a neural network trained to generate images in the style of Monet paintings.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. file for details.

## Acknowledgements

- The Gradio team for the amazing interface library.
- The Hugging Face team for providing the platform to deploy machine learning models.
