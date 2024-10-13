# Smart Budget Bot 

## Overview

Smart Budget Bot is a tool that leverages the power of Google's Gemini AI to make US federal spending data more accessible and understandable to the public. It analyzes data from USAspending.gov and provides users with clear, concise answers to their questions about how the government spends money.

## Features

* *AI-Powered Search:* Ask questions about federal spending in natural language (e.g., "How much did the Department of Defense spend on AI in 2023?")
* *Spending Summaries:* Get easy-to-understand summaries of complex spending data.
* *Data Verification:* Cross-reference information with USAspending.gov to ensure accuracy.
* *Interactive UI:*  Explore data with an intuitive interface built with Streamlit.

## Technologies Used

* *Google Gemini:* Advanced language model for analyzing and summarizing spending data.
* *USAspending.gov:*  Source of US federal spending data.
* *Streamlit:*  Python framework for building the interactive web application.
* *Python Libraries:*  google.generativeai, requests, pandas, etc. (list the specific libraries you used)

## Getting Started

1. *Clone the repository:* git clone https://github.com/akshitha1103/smartbot.git
2. *Install dependencies:* pip install -r requirements.txt
3. *Obtain a Gemini API key:*  [Apply for access to the Gemini API](link to Gemini API access)
4. *Set your API key:*  Replace "GEMINI_API_KEY" in app.py with your actual API key.
5. *Run the Streamlit app:* streamlit run app.py

## Project Structure

* app.py:  Main Streamlit application code.
* utils.py:  Helper functions for data processing, API interaction, etc. (if applicable)
* requirements.txt:  List of project dependencies.
* data/:  Directory to store downloaded or processed data (if applicable).

## Future Development

* *Enhanced visualizations:*  Incorporate charts and graphs to display spending patterns.
* *Agency-specific analysis:*  Provide deeper insights into individual agencies' spending.
* *Comparative analysis:*  Allow users to compare spending across different agencies or years.
* *Data updates:*  Implement automatic data updates from USAspending.gov.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## Acknowledgments

* Google AI for providing the Gemini API.
* USAspending.gov for making federal spending data publicly available.
* The Streamlit community for creating a fantastic framework.
