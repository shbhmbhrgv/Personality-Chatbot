# Personality ChatBot: Chat with Joey!

## Introduction
Chat with Joey is a TensorFlow Implementation of a Neural Conversational Model with the Help of DeepQA Repo.It makes use of a SEQ2SEQ Model RNN for Sentence Predictions.
The Chatbot is Designed to Mimic the Personality of Joey, a Character from the Popular TV-Show "F.R.I.E.N.D.S".

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


## Dataset
For this project we used the [Friends TV Corpus](https://sites.google.com/site/friendstvcorpus/), which was currated by David Ayliffe for his masters thesis to study inter-gender and intra-gender conversation. We formatted the data to get conversation between Joey(a character) and several other characters. There are two reasons for this: 
  
  * We were targeting sentences with 5 words. 

  * Joey has the highest number of conversations in the dataset.

## Hyperparameters
Some of the hyperparameter we played with are sentence-length, number of hidden-layers, word embedding-size, batch-size and number of iterations. One thing to note here is that there is no logic behind these values, it was purely based on a trial and error approach.

  * We started training with sentences containing more than 20 words, It took more than 16 hours to train and still it was giving gibberish output. Then we reduced it to 10 words, although it was comparitively better we were not happy with the result. Finally we tried with 5 words and we got good outputs.
  
  * There are 2 RNN layers(encoder and decoder) and for each layer we put the number of hidden layers to 2048.
  * Changed the word embedding size to 256.
  * Batch size to 512.
  * Number of iteration to 200,000.

## Deep Q&A - Model explanations
The model is a standard seq2seq RNN with two LSTM cells one for the encoder and another for the decoder, and 256 hidden units in each RNN cell. For the purpose of our project, we changed the number of hidden layers to 2048. Basically, tensorflow processes the data inside the encoder cell during training by applying three operations that compute the state of the cell. First is forget which determines what info to throw away from the previous cell state. For example, data that is not necessary to compute the current cell state. Second is input that determines what information is to let in from the new state. Finally, output that produces the final output from the cell. The encoder converts the input into vector representation and sends it to the decoder. Then the decoder is trained on both the output sequence as well as the input representation from the encoder. Since the model works on two sequences, it can predict new elements of a sequence given prior elements of the sequence. Deep Q&A model is trained on conversational corpus to predict sentences in response to users’ queries. There are different modules for the purpose of training the model and for the evaluation of the model. The main module is chabot that contains most of the sub-modules for training and testing functionalities. This module reads the user prompt and runs the training or testing mode and eventually returns a trained model for the training mode or starts a chatbot session for the testing mode. A brief explanation is provided below for the main modules. 

## Main modules
* chatbot (module)
Training mode: The training mode generates a graph for the model and starts a tensorflow session. The tensorflow session reads a batch of data and runs the training process to periodically minimize the loss function.  

Testing mode: reads the user’s query and feeds the query to the encoder as a sequence of word ids. Then it runs the model with the batch of word ids to get a predicted sequence of word ids. The decoder then converts the predicted sequence into user readable string and returns it as an answer. 
* Model (module)
It contains the implementation of the model. It builds the model network and the computational graph with specified parameters. It basically creates two RNN cells using tensorflow, each of which with 2048 hidden layers. We increased the number of hidden layers from 256, and as mentioned above, it was purely based on a trial and error approach. There are also four defined tensorflow placeholders for the network inputs: encoder Inputs, decoder Inputs, decoder Targets same as decoder Inputs, and decoder Weights to adjust the learning to the target sentence size. The loss function is also defined using tensorflow seq2seq.sequence_loss call. 
* Trainer (module)
The Model module does not perform run on itself but just return the operators to do so. It’s actually the trainer module that launches the training with different parameters. 
* Textdata (module) 
This module loads the dialogue corpus and builds the vocabulary. It also performs all the processing of the dataset. Some of these operations include extractConversation, extractText

## Results

Below are some screenshots of our chat with the chatbot. It gives preety good results for standard questions as well as some character specific questions. 

Good Results

<img src="https://github.com/shbhmbhrgv/Personality-Chatbot/Results/good.JPG" alt="alt text" width="850" height="500">

Random 

It fails to respond appropriately to some questions.
Q: What's up?
A: Kidney Stones!

<img src="https://github.com/shbhmbhrgv/Personality-Chatbot/Results/random.JPG" alt="alt text" width="850" height="500">
