# Autonomous Robot Command Language Client

This project is an Autonomous Robot Command Language (ARCL) client designed to enable communications with an Omron robot.

## Overview

The ARCL client provides a simple and effective way to control and monitor Omron robots. It allows for direct communication with the robot, enabling tasks such as sending commands, receiving status updates, and more.

## Installation

To install the ARCL client, follow these steps:

1. Clone the repository: `git clone https://github.com/nwtaf/arcl-driver.git`
2. Navigate to the project directory: `cd arcl-driver`
3. Install the required packages: `pip install -r requirements.txt` (still working on minimizing requirements.txt)

## Usage

Within the src folder, there are a few files:
* arcl-telnet-client.py: automatically starts a telnet client where the user can enter commands
* arcl-tcp-client.py: not recommended, depreciated

## Contributing

Contributions are welcome! Please read the contributing guidelines before getting started.

## License

This project should licensed under the terms of the MIT license. I am not liable, but feel free to use the code!