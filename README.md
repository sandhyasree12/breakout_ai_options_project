# Options Trading Data Analysis

## Overview

This project aims to analyze options trading data using the Quotient API. It retrieves options chain data for specified financial instruments and performs calculations related to margin and premium for options trading.

## Features

- Fetches option chain data for a specified symbol using the Quotient API.
- Filters data based on option type (Call/Put), expiration date, and strike price.
- Calculates the margin and premium required for purchasing options.
- Handles API response messages and potential errors gracefully.

## Technologies Used

- Python 3.x
- Pandas
- Requests
- Quotient API

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/sandhyasree12/breakout_ai_options_project
Navigate to the project directory:

bash
Copy code
cd options-trading
Create a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
Activate the virtual environment:

On Windows:
bash
Copy code
venv\Scripts\activate
On macOS/Linux:
bash
Copy code
source venv/bin/activate
Install the required packages:

bash
Copy code
pip install -r requirements.txt
Usage
Update the config.py file (or equivalent) with your API key and any other necessary configurations.

Run the main script:

bash
Copy code
python main.py
Follow the prompts or modify the script to analyze different symbols and expiration dates.

Sample Output
Refer to the sample_output.csv file for examples of the output generated by the script.

Testing
To run the tests, execute:

bash
Copy code
python -m unittest test_data.py
This will run all unit tests defined in test_data.py.

Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
Thanks to the developers of the Quotient API for providing access to trading data.

