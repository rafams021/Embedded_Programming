#!/usr/bin/env python
# coding: utf-8

# # Joy Ride - Part 3: Parallel Parking
# In this section you will write a function that implements the correct sequence of steps required to parallel park a vehicle.
# 
# NOTE: for this segment the vehicle's maximum speed has been set to just over 4 mph. This should make parking a little easier.
# 
# ![](https://upload.wikimedia.org/wikipedia/commons/2/26/ParallelParkingAnimation.gif)

# If you have never heard of WASD keys, please check out this [link](https://en.wikipedia.org/wiki/Arrow_keys#WASD_keys).
# 
# ## Instructions to get started
# 
# 1. Run the `SETUP CELL` below this one by pressing `Ctrl + Enter`.
#     - If the cell does not run, delete the comment in the cell
# 1. Click the button that says "Load Car Simulator". The simulator will appear below the button.
# 1. Run the cell below the simulator, marked `CODE CELL` (hit `Ctrl + Enter`). 
# 1. Try to drive the car using WASD keys. You might notice a problem...
# 1. Press the **Reset** button in the simulator and then modify the code in the `CODE CELL` as per the instructions in TODO comments. 
# 1. When you think you've fixed the problem, run the code cell again. 
# 
# **NOTE** 
# - Depending on your computer, it may take a few minutes for the simulator to load! Please be patient.
# - Remember to re-run your `CODE CELL`:
#  - 1) Click "Restart Connection" button on the cell above and wait for a minute for the kernel to get ready.
#  - 2) Run this code cell (press Control+Enter) and as the code cell starts running,
#  - 3) Click "Reset button" on the simulator
#     (If you don't see the "Reset" button inside the simulator, please click "Load Car Simulator" button again)
# 
# ### Instructions to Reload the Simulator
# Once the simulator is loaded, the `SETUP CELL` cannot be rerun, or it will prevent the simulator from appearing. If something happens to the simulator, you can do the following:
# - Go to Jupyter’s menu: Kernel --> Restart and Clear Output
# - Reload the page (Cmd-R)
# - Run the first cell again
# - Click the Green `Load Car Simulator` button

# In[2]:


get_ipython().run_cell_magic('HTML', '', '<link rel="stylesheet" type="text/css" href="buttonStyle.css">\n<button id="launcher">Load Car Simulator </button>\n<button id="restart">Restart Connection</button>\n<script src="setupLauncher.js"></script><div id="simulator_frame"></sim>\n<script src="kernelRestart.js"></script>')


# In[ ]:


# CODE CELL

# Important notes: please do the following steps before you re-run your code on the simulator
# 1) Click "Restart Connection" button on the cell above and wait for a minute for the kernel to get ready.
# 2) Run this code cell (press Control+Enter)  and as the code cell starts running,
# 3) Click "Reset button" on the simulator
#    (If you don't see the "Reset" button inside the simulator, please click "Load Car Simulator" button again)


# Once again, the steer value can be from -25 and 25
# Your throttle and brake can be from -1 to 1
car_parameters = {"throttle": 0, "steer": 0, "brake": 0}

def control(pos_x, pos_y, time, velocity):
    """ Controls the simulated car"""
    global car_parameters
    
    
    # TODO: Use WASD keys in simulator to gain an intuitive feel of parallel parking.
    # Pay close attention to the time, position, and velocity in the simulator.
    
    # TODO: Use this information to make decisions about how to set your car parameters
    
    # In this example the car will drive forward for three seconds
    # and then backs up until its pos_y is less than 32 then comes to a stop by braking
    if(pos_y > 37.6):
        car_parameters["throttle"] = -0.2
        car_parameters["steer"] = 1
        car_parameters["brake"] = 0
    elif(pos_y > 35):
        car_parameters["throttle"] = -0.01
        car_parameters["steer"] = 0
        car_parameters["brake"] = 0
    elif(pos_y > 31.5):
        car_parameters["throttle"] = -0.01
        car_parameters["steer"] = -1
        car_parameters["brake"] = 0
    else:
        car_parameters["throttle"] = 0
        car_parameters["steer"] = 0
        car_parameters["brake"] = 1
    
    return car_parameters
    
import src.simulate as sim
sim.run(control)


# # Submitting this Project!
# Your parallel park function is correct when:
# 
# 1. Your car doesn't hit any other cars.
# 2. Your car stops completely inside of the right lane.
# 
# Once you've got it working, it's time to submit. Submit by pressing the `SUBMIT` button at the lower right corner of this page.

# In[ ]:




