# Packing List Generator

Using the responses received in a survey (Google forms/Microsoft forms, etc), generate a packing list for every respondent. 

It will also generate a grocery list with an item-wise breakdown of the quantity to be purchased

## Requirements

1. Python 3.11 or higher

## Usage instructions

1. `git clone <this-repository-url>`

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install Node.js dependencies and build CSS:
   ```bash
   npm install
   npm run build:css
   ```

5. Modify filename and column locations corresponding to individual items in `generate_labels.py`

6. Run the script:
   ```bash
   python generate_labels.py <path-to-excel-file>
   ```

   Example:
   ```bash
   python generate_labels.py demo_list.xlsx
   ```