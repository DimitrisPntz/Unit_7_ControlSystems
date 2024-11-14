# Unit_7_ControlSystems
My Unit 7 Control Systems project.

# Project Overview
My Unit 7 Control Systems project is an Hand Written Digit Prediction. It uses Pygame for the user interface and the user draws a digit in the 800x800 window.
Then The pretrained AI makes a guess to what digit it is. The `ArduinoScript.py` is the master controller for the entrire project. It launches two threads,
the Master Thread and the Arduino Thread: These Threads serve distinct functions.
 # Thread Responsibilities

## Master Thread
The Master Thread serves as the backbone of the operation, sending commands to the Arduino.

### Commands:
- **`ON`**: Turns on all lights on the Arduino.
- **`OFF`**: Turns off all lights on the Arduino.
- **`EXIT`**: Gracefully exits all threads with the help of the Arduino.

## Arduino Thread
The Arduino Thread handles most of the work and runs the Paint2D clone used to replicate the MNIST data.

### Responsibilities:
- Handles drawing, input, and sensor data from the user.
- Runs the neural network on the user's input data.
- Manages communication with the Arduino, delivering commands (e.g., the `OPEN LIGHT` command) to control which light (LED) class to turn on.


## The Neural Network
The Neural Network is made in Pytorch and has 2 Hidden Layers. It is a very simple Neural Network and doesn't use Convolution layers as this is a very simple classification task.
But despite that it has over 95% accuracy. This is the models architecture by torchsummary.

### Model Summary
| Layer (Type)    | Output Shape | Parameters |
|-----------------|--------------|------------|
| **Linear-1**    | [-1, 256]    | 200,960    |
| **ReLU-2**      | [-1, 256]    | 0          |
| **Linear-3**    | [-1, 128]    | 32,896     |
| **ReLU-4**      | [-1, 128]    | 0          |
| **Linear-5**    | [-1, 64]     | 8,256      |
| **ReLU-6**      | [-1, 64]     | 0          |
| **Linear-7**    | [-1, 10]     | 650        |

---

**Total parameters**: 242,762  
**Trainable parameters**: 242,762  
**Non-trainable parameters**: 0  

---

### Memory Usage

- **Input size**: 0.00 MB
- **Forward/backward pass size**: 0.01 MB
- **Parameters size**: 0.93 MB
- **Estimated Total Size**: 0.94 MB

## Pygame
Using Pygame I have made a simple drawing program which simulates the training data by MNIST so it can be used with the Neural Network.
To draw just click to draw. To reset the canvas press `SPACE`

## How to use the software
### Requirements
- Arduino
- Breadboard
- 10 LEDs
- 12 wires
- 10 resistors

### Setup Instructions
1. **Power Connections**:
   - Connect the Arduino’s 5V pin to the **+** power rail on the breadboard.
   - Connect the Arduino’s GND pin to the **-** power rail on the breadboard.

2. **LED Connections**:
   - Set up each LED with a resistor, connecting them to Digital Pins 4 through 13 on the Arduino.

3. **Upload the Code**:
   - Upload the `ARDUINOCODE.ino` file to your Arduino.

4. **Testing**:
   - Run the `ArduinoScript.py` script.
   - When prompted, enter the communication port your Arduino is using.
   - Type `ON` in the terminal; this should turn on all the LEDs.

5. **Draw and Test the Neural Network**:
   - If the LEDs light up as expected, you’re ready to draw and have the neural network identify your digits.

## Example Usage of the System:
![image](https://github.com/user-attachments/assets/3a56bdcb-6470-4b07-a89a-04ccbafac6ab)
![image](https://github.com/user-attachments/assets/1a4e005e-531a-4bc1-9987-059e5aed1d76)
