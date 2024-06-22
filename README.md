# Key-Splasher

Key-Splasher is a simple keylogger tool designed to log keystrokes and display them with colored output in the terminal using Colorama.

## Table of Contents

- [Key-Splasher](#key-splasher)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Basic Usage](#basic-usage)
    - [Options](#options)
    - [Example](#example)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)

## Features

- **Keystroke Logging**: Capture and log keystrokes.
- **Colorful Output**: Display status messages in color using Colorama.
- **Log to File**: Save captured keystrokes to a log file.

## Requirements

-Python 3.x
-Dependencies:
 - `argparse`
 - `pynput`
 - `colorama`

Install dependencies using `pip`:


## Installation
### Clone the repository:

```bash
 git clone https://github.com/MrAdi46/key-splasher.git
cd key-splasher

# Run the Script
python key_splasher.py -f <log_file>

# Example Usage
python key_splasher.py -f mykeylogs.txt

# Run with Specified Log File
python key_splasher.py --log_file=mylogs.txt
```
## How It Works
### Initialization: 
- Key-Splasher initializes by setting up the log file and configuring the logging system.
- Key Press Handling: Captures each key press using pynput and appends the character or key name to an internal list.
- Log Writing: Periodically writes the captured keystrokes to the specified log file.

### Threaded Execution: 
- Runs the keylogging function in a separate thread for continuous operation until manually stopped.

## Security Notice
- **Key-Splasher** is intended solely for educational purposes or for use with ***explicit permission***. 

- **Unauthorized** use of keylogging software to capture keystrokes without consent is ***illegal and unethical***. Always obtain permission from the owner of the system before using this tool.

## Contributing
- Contributions are welcome! Please fork the repository and submit a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.

## License
- This project is licensed under the MIT License.

## Contact
For questions, suggestions, or issues, please reach out via the following channels:

- **GitHub Issues**: [Create an issue](https://github.com/MrAdi46/key-splasher/issues)
- **GitHub Discussions**: [Join the discussion](https://github.com/MrAdi46/key-splasher/discussions)
- **LinkedIn**: [Aditya Pachghare](https://www.linkedin.com/in/aditya-pachghare-a440a2228/)

### Feel free to contact us for:

- **Bug Reports**: If you encounter any issues while using Key-Splasher.
- **Feature Requests**: If you have ideas on how to improve Key-Splasher.
- **General Inquiries**: If you have questions or need assistance.

---
