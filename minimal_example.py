import gymnasium as gym 
import numpy as np 
#from gymnasium.wrappers.time_limit import TimeLimit 
import retro 
import time
import cv2 

# define the variables
GAME_NAME = 'DonkeyKongCountry-Snes'



for game in retro.data.list_games():
   print(game, retro.data.list_states(game))
# make the retro env
env = retro.make(
    game=GAME_NAME,
    state=retro.State.DEFAULT,
    scenario=None,
)


done = False
obs = env.reset()
while not done:
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
    print(np.min(observation))
    print(np.max(observation))
    input()
    #env.render()
    # render the observation
    cv2.imshow('observation', observation)
    cv2.waitKey(1)
    time.sleep(0.01)
