# Packing List Generator

Using the responses received in a survey (Google forms/Microsoft forms, etc), generate a packing list for every respondent. 

It will also generate a grocery list with an item-wise breakdown of the quantity to be purchased

## Requirements 

1. Install [pipenv](https://pipenv.pypa.io/en/latest/installation.html)

## Usage instructions

1. `git clone <this-repository-url>`

2. `pipenv install`

3. Modify filename and column locations corresponding to individual items in `generate_labels.py`

4. `pipenv run python generate_labels.py`