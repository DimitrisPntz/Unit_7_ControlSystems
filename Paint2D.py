import pygame
import torch
import numpy as np
from PIL import Image 

from torchvision import transforms
from ModelArchitecture import NumberIdentifier

import time
def LoadTorch():
    # Define Camera transforms to be able to work with the AI
    transform = transforms.Compose([
        transforms.ToPILImage(),
        transforms.Grayscale(num_output_channels=1),
        transforms.Resize((28, 28)),
        transforms.ToTensor()
    ])
    
    # Define the Model Architecture and load the pretrained weights
    Model = NumberIdentifier()
    Model.load_state_dict(torch.load('TrainedModel/ImageClassifier_97', weights_only=True))
    Model.eval()
    
    return Model, transform

def Draw(SerialInstance):
    Model, transform = LoadTorch()

    LastGuess = -1

    WIDTH, HEIGHT = 800, 800
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Touch Screen MNIST Project")

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    BRUSHWIDTH = 30
    DRAWING = False

    screen.fill(BLACK)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                DRAWING = True
                pygame.draw.circle(screen, WHITE, (event.pos[0], event.pos[1]), BRUSHWIDTH)
            elif event.type == pygame.MOUSEMOTION and DRAWING:
                pygame.draw.circle(screen, WHITE, (event.pos[0], event.pos[1]), BRUSHWIDTH)
            elif event.type == pygame.MOUSEBUTTONUP:
                DRAWING = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    screen.fill(BLACK)

            pygame.display.flip()

        ScreenArray = pygame.surfarray.array3d(screen)
        
        # For some reason Pygame does a wierd transformation to the screen when put into a np array so we are just correcting for it here
        ScreenArray = np.rot90(ScreenArray, k=3)
        ScreenArray = np.fliplr(ScreenArray)

        # Make the prediction
        prediction = Model.predict(transform(ScreenArray)).item()

        if(LastGuess != prediction):
            print("The AI thinks it is a ", prediction)
            Command = f"OPEN LIGHT {prediction + 4}" # Error Correct for the Pins starting at 4 and not zero 
            SerialInstance.write(Command.encode('utf-8'))
            LastGuess = prediction

        if(SerialInstance.in_waiting > 0):
            ArduinoMessage = SerialInstance.readline().decode('utf-8').strip()

            if ArduinoMessage == "EXIT":
                return 0
            
            print(f"\nReceived from Arduino: {ArduinoMessage}")

def Test(SerialInstance):
    Classes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    while True:
        Command = int(input("Enter Class: "))
        print("TESTING LIGHT", Command+4)
        Command = f"OPEN LIGHT {Command+4}"
        SerialInstance.write(Command.encode('utf-8'))
        time.sleep(2)