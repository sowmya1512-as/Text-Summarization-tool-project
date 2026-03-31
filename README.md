# Text-Summarization-tool-project

Company name: CodeTech IT solutions

Name: Sowmya G S

Domain : Artificial Intelligence

Duration : 4 weeks

Intern ID : CTIS7569

Mentor : Neela Santosh

Descrpition of the task :

This project focuses on developing a simple tool that summarizes lengthy articles using basic Natural Language Processing (NLP) techniques. In today’s digital world, large volumes of textual information are generated every day in the form of articles, blogs, reports, and research papers. Reading and understanding all this information can be time-consuming and inefficient. Therefore, text summarization plays a crucial role in extracting the most important information from a large body of text and presenting it in a concise and meaningful way.

The main objective of this project is to design and implement a Python-based system that takes a long piece of text as input and generates a short summary as output. The system uses basic NLP techniques without relying on internet-based APIs or pre-trained models. This makes the solution simple, efficient, and suitable for offline usage. The approach used in this project is extractive summarization, where key sentences are selected from the original text based on their importance rather than generating new sentences.

The working of the system involves several steps. First, the input text is processed and divided into individual sentences using simple string manipulation and regular expressions. This helps in analyzing the structure of the text. Next, the text is tokenized into words, and a frequency table is created to count how often each word appears. Common words that occur more frequently are considered more important in determining the relevance of sentences.

After calculating word frequencies, each sentence is scored based on the presence of important words. Sentences that contain more high-frequency words are given higher scores, as they are likely to represent key ideas of the text. Once all sentences are scored, the system selects the top-ranked sentences to form the final summary. The number of sentences in the summary can be adjusted based on the desired level of brevity.

This project demonstrates how fundamental NLP techniques such as tokenization, frequency analysis, and sentence scoring can be used to build a functional summarization tool. Although the system is basic, it effectively reduces the length of the input text while retaining its core meaning. The simplicity of the implementation makes it easy to understand and suitable for beginners learning about natural language processing.

There are several advantages to this approach. It does not require any external libraries beyond standard Python modules, making it lightweight and easy to deploy. It also works without an internet connection, ensuring privacy and reliability. However, since it is based on simple heuristics, the quality of the summary may not always match that of advanced AI models.

In conclusion, this project successfully implements a basic text summarization tool using offline NLP techniques. It highlights the importance of summarization in handling large textual data and provides a strong foundation for exploring more advanced methods such as abstractive summarization and deep learning-based models in the future.
outpiut of the task:
<img width="1282" height="373" alt="Image" src="https://github.com/user-attachments/assets/52918145-e2dc-4e62-895b-71e4d344a5eb" />
