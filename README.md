# Unit_7_ControlSystems
My Unit 7 Control Systems project.

# Project Overview
My Unit 7 Control Systems project is an Hand Written Digit Prediction. It uses Pygame for the user interface and the user draws a digit in the 800x800 window.
Then The pretrained AI makes a guess to what digit it is. The `ArduinoScript.py` is the master controller for the entrire project. It launches two threads,
the Master Thread and the Arduino Thread: These Threads serve distinct functions.
  * Master Thread - Master Thread serves as the backbone of operation sending commands to the arduino.
  *     * These Three Commands:
  *     *   `ON`   - Turns on all lights on Arduino.
  *     *   `OFF`  - Turns off all lights on the Arduino.
  *     *   `EXIT` - Gracefully Exits all threads with the help of Arduino.

  * Arduino Thread - Arduino Thread handles most of the work and runs the Paint2D clone used to replicate the MNIST Data.
  *     * Handles the Drawing/Inputs/Sensors by the user.
  *     * Runs the Neural Network on the data by the user.
  *     * Handles Communication to the arduino delivering commands by telling it which Light class to turn on (This is the `OPEN LIGHT ` Command).

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

## Example Usage of the System:
![image](https://github.com/user-attachments/assets/3a56bdcb-6470-4b07-a89a-04ccbafac6ab)
![image](https://github.com/user-attachments/assets/1a4e005e-531a-4bc1-9987-059e5aed1d76)
