# Weather App

This simple Python script allows you to get the current weather conditions for a specified city using the OpenWeatherMap API.

## Prerequisites

- Python 3.x
- Required Python packages (`requests`, `python-dotenv`) also check requirements.txt file

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/mradegboyega/pip-venv.git
    cd your-repo
    ```

2. Install the required packages:

    ```bash
    pip install requests python-dotenv
    ```

3. Create a `.env` file in the project root and add your OpenWeatherMap API key:

    ```plaintext
    API_KEY=your_openweathermap_api_key
    ```

4. Run the script:

    ```bash
    python weather_app.py
    ```

## Usage

1. Run the script as described in the "Getting Started" section.
2. Enter the name of the city when prompted.

## Features

- Get current weather conditions for a specified city.
- Display temperature, feels-like temperature, and weather description.

## Configuration

Update the `.env` file with your OpenWeatherMap API key.


## Acknowledgments

- [OpenWeatherMap API](https://openweathermap.org/api) for providing weather data.


NOTE: I used this simple project to learn pip and venv in python

