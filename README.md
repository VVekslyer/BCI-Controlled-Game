# Brain Controlled Pong Game using OpenBCI

Using OpenBCI's 16-Channel Cyton headset and machine learning to control games created in Unity and PyGame.


![helmet](https://user-images.githubusercontent.com/69658141/186826678-aac05fa4-972d-4054-ac93-d170ae0f7736.jpg)


In this repositry you will find the following main files:
 *  print_raw_data.py: Allows you to test printing all 8 or 16 channels of the headset.
 *  openbci_neuromore.py: Requires the OpenBCI GUI app and neuromore, allows the OpenBCI to send EEG data to neuromore via LSL.
 *  calculate_threshold.py: Allows you to find the threshold of a user's concentration; used for neuromore.
 *  game.py: The pong made in pygame.
 *  model.py: The TensorFlow model, training to understand whether the user wishes to go up or down in the game.

## Demo
Watch a live demo on https://streamable.com/j884vb

![image](https://user-images.githubusercontent.com/69658141/186840231-7761da8e-14bf-4594-8466-7feef80a604d.png)


## Pong Game
![image](https://user-images.githubusercontent.com/69658141/186831818-2e9eb98c-05eb-484a-bdb7-04bdf76ceef8.png)

## Acknowledgments
This project would've been impossible without all the help I recieved from peers in the Douglas College HiPE Lab, as well as all the wonderful professors in the engineering department who had helped assemble the helmet. Thank you all very much.

![cyton](https://user-images.githubusercontent.com/69658141/186837860-84206118-317c-4a2a-974a-d17bd697242b.jpg)
