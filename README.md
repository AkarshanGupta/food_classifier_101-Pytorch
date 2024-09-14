## Introduction

This project is designed to create a web-based tool for predicting food categories from uploaded images. The tool leverages a pre-trained VGG model to classify images into one of 101 food categories. Users can upload an image of food, and the system will analyze the image to predict the specific food category it belongs to. This tool aims to facilitate easy and accurate food identification, which can be useful for various applications, such as dietary analysis, food recognition in mobile apps, and automated food categorization systems.

## Objective

The main objectives of this project are to:
1. Develop an intuitive web interface where users can upload images of food.
2. Utilize a pre-trained VGG model to accurately predict the food category of the uploaded image.
3. Provide immediate feedback to users with the predicted food category.

## Technology

### Gradio

Gradio is a Python library that allows for the easy creation of web-based interfaces for machine learning models. It will be used to develop the user interface for the food category prediction tool, enabling users to interact with the model by uploading images and receiving predictions.

### Python

Python is the programming language used to implement the logic of the project. It supports a wide range of libraries and tools for machine learning, data manipulation, and web development. In this project, Python will be used to integrate the VGG model, handle image processing, and manage user interactions through Gradio.

### PyTorch

PyTorch is an open-source machine learning framework used for building and training neural networks. It will be utilized to work with the pre-trained VGG model, perform inference on the uploaded images, and handle the computations required for food category classification.

# Website
![Screenshot 2024-09-07 184730](https://github.com/user-attachments/assets/9008bf5a-995b-407c-9c11-58d34839c11f)

https://github.com/user-attachments/assets/229b496a-69d9-41c1-a4c8-eafd6a324249

# Few Things 
1. This project includes two notebooks:
   - The first notebook faced challenges like low accuracy, overfitting, and underfitting.
   - I resolved these issues in the **Final_Notebook**, which successfully addresses:
     - The accuracy problem.
     - Both overfitting and underfitting issues.

2. You can approach this project in two ways:
   - **Approach 1**: Download the interface file and run it using **python interface.py**. Since we are using Gradio, it will automatically launch the interface.
     - The required models and dependencies will be downloaded from the cache on the local machine where the file is executed, and the interface will interact with these models to generate results.
   - **Approach 2**: Run the **Final_Notebook**, save the trained model, and write an interface script that includes the following logic:
     - The interface should preprocess the input image and then feed it to the saved model for prediction, returning the output.
     - I couldn't complete this approach due to hardware limitations—my machine lacks a GPU, and the free GPU runtime in Colab wasn't sufficient to train and save the entire model.

3. For the interface, I utilized a pre-trained model:
   - The pre-trained model used is **Microsoft ResNet-50**.












