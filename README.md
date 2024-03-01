# Description
The project consists on three scripts which iterate over a list of PDF paths. For each PDF, the processes the article, extract the abstract, generate a word cloud, count figures, and extracts links. The results are printed to the console.

For a detailed code explanation consult the release section.

# Requirements
Python 3.10

Grobid 1.0.0

Conda  23.11.0

matplotlib 3.4.3

wordcloud 1.8.1

beautifulsoup4 4.10.0


# Installation and execution instructions
## 1. Install Python
$ sudo apt update

$ sudo apt install python3

## 2. Create a safe environment to install packages without affecting the system-wide Python installation
Link for conda installation: https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html

Commands to create and activate the environment

$ conda activate

$ conda create -n <choose_name> python=3.10

$ conda activate <choose_name>

## 3. Make sure you have the following Python libraries installed. You can install them with the commands:
$ pip install wordcloud

$ pip install matplotlib

$ pip install beautifulsoup4

## 4. Install grobid_client_python
Link to the GitHub repository: https://github.com/kermitt2/grobid_client_python/blob/master/Readme.md

## 5. Download the code
You can find it in the release section or in the code file. 

## 6. Run the code
Run Grobid (if the following command does not work, see other options in Grobid's GitHub repository).

$ ./gradlew run

You can check if it is working by accessing http://localhost:8070/

In another window, while running grobid in the first one, change your directory to grobid_client_python

$ cd grobid_client_python

And then, run the your chosen script

$ pyhton /path/of/the/script

# Running examples
Consult the repository's test file

# Citation
Consult the repository's citation file.

# Where to get help 
Grobid's GitHub repository: https://github.com/kermitt2/grobid/

Conda's web installation page: https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html

# DOI
https://doi.org/10.5281/zenodo.10732799

