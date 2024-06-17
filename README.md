# StreamlitSheetsUI

A simple web application that allows users to input data into a Google Sheet with privacy and security in mind.

## Demo

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://usefulphrases.streamlit.app/)

## Motivation

Google Sheets is a powerful tool to share data, analyzise it and provide meaningful oragnizational insights. Google Sheets allows everyone to see real-time updates.

However, sharing access to a Google Sheet can cause difficulty as you may want to limit editing access to a particular section within a sheet while still allowing individuals to be able to read all the data. Google Sheets does allow a sheet to be in "Read-Only" mode, but this prohibits them from adding any information at all. Additionally data validation can be critical. If information needs to be formatted in a particular way to be analyzed by a Google Sheets formula or Python script, you need to be sure that information is entered correctly.

To tackle the above issues and many others, creating a simple web application to read from and write to a Google Sheet can be a powerful organizational tool.

## Installation

Clone the repository.

Install the required libraries with pip:

```powershell
pip3 install -r requirements.txt
```
## Usage

To run the application, run the following command in the terminal:

```powershell
streamlit run app.py
```

## Key Features to be Implemented

- Allows users to input data only in the designated cells
- Formats the data before writing to the Google Sheet
- Analyzes the data and provides insights
- Adds an additional layer of security by password protecting access to the application that is connected to the Google Sheets

## Note
You will need to create a google service account to use this application. To do this, you will need to go to the Google Cloud Platform and create a project. Then enable the Google Sheets API and create a service account. You will need to download the JSON file that contains the credentials and place it in the root directory of the project.

## Status

This project is _complete_.
