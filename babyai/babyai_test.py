import babyai
from gym_minigrid.wrappers import *
env = gym.make('BabyAI-GoToRedBall-v0')
env = RGBImgPartialObsWrapper(env)