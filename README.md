## CSV Normalizer
This Python script takes a csv file as input and outputs some corrections on it.

### Requirements
- Python 3.x
- Virtualenv
- Pip

### Installation
Set up a virtual environment:

``
virtualenv --python=</path/to/Python3> .
``

Activate the virtual environment:

``
source /bin/activate
``

Install pytz:

``
pip install pytz
``

### Usage
Run the script with a csv file input and output on command line:

``
python normalize.py sample.csv
``

Run the script and direct the output into a new file:

``
python normalize.py sample.csv > sample2.csv
``
