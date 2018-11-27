# Personality ChatBot: Say Hi to Joey!

## Introduction
A personality chatbot aimed to mimic the characteristics of popular TV series characters such as Joey(from Friends) and Sheldon(from Big Bang Theory). This project is implemented as a Sequence to Sequence conversation model in Python using Tensorflow.

#### Table of Contents

* [Installation](#installation)
* [Running](#running)
* [Dataset](#dataset)
* [Hyperparameters](#hyperparameter)
* [Results](#results)


## Installation

To Run the Project you require::
 * python 3.5 and above
 * redis
 * pip3 install tensorflow
 * pip3 install django==1.10.7
 * pip3 install channels==1.1.6
 * pip3 install asgi_redis
 * pip3 install tqdm
 * pip3 install nltk
 * python3 -m nltk.downloader punkt

## Dataset
For this project we used the [Friends TV Corpus](https://fangj.github.io/friends/) and [Big Bang Theory](https://bigbangtrans.wordpress.com/about/). We preprocessed the data to get conversations between main character and other characters.

## Hyperparameters
Some of the hyperparameter we played with are sentence-length, number of hidden-layers, word embedding-size, batch-size and number of epochs.
  
  * 2 RNN layers(encoder and decoder) and for each layer we put the number of hidden layers to 2048.
  * Changed the word embedding size to 256.
  * Batch size to 512.
  * Number of epochs: 200,000.

## Training the Model:
To create dataset:

```bash
python main.py --createDataset --corpus lightweight --datasetTag <dataset file name>
```

Train the model:

```bash
python main.py --reset --corpus lightweight --device gpu --datasetTag <dataset file name> --hiddenSize <hidden size> --embeddingSize <embedding size> --batchSize <batch size> --maxLength <max length> --numEpochs <number of epochs>
```

## Running
Once you have all the depenedencies ready, do the folowing:

To Configure the Web App

```bash
cd chatbot_website/
python manage.py makemigrations
python manage.py migrate
```

Then, to Launch the Server Locally, Use the Following Commands:

```bash
redis-server &  # Launch Redis in Background
python manage.py runserver 127.0.0.1:8000
```
Then, Go to the Browser: http://127.0.0.1:8000/ 




## Results
Below are some screenshots of our chat with the chatbot tested with Joey. It gives preety good results for standard questions as well as some character specific questions. 

Good Results

<img src="https://github.com/shbhmbhrgv/Personality-Chatbot/blob/master/Results/good.JPG" alt="alt text" width="850" height="500">

Random Results

<img src="https://github.com/shbhmbhrgv/Personality-Chatbot/blob/master/Results/random.JPG" alt="alt text" width="850" height="500">
