# IP Location Finder

![Python Version](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A simple Python application that retrieves the IP address and geolocation of the user using the ipdata.co API.

## Prerequisites

Before using this application, you need to sign up for an account on [ipdata.co](https://ipdata.co/) to obtain an API key.

## Features

- Retrieves the user's public IP address.
- Provides information about the user's geographical location including country, city, latitude, and longitude.

## Installation

1. Clone the repository:

2. Install the required dependencies:
   pip install -r requirements.txt

## Configuration

Open `config.py` and replace `'YOUR_API_KEY'` with your actual ipdata.co API key.

## Usage

Run the `main.py` script:
  py main.py


The application will then fetch the IP address and location details of the user using the ipdata.co API and display them.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/improvement`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/improvement`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

