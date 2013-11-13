#Self Driving Car Project

###Platform
The folloing sections deal with to dos and information regarding the vehicle(s) themselves, and the hardware and systems there.

####To dos
#####First Critical Path
Fix the platform

- Wheels
    -  Rubber tires
        - Bearings for connectors
        - re: website buy rubber tires
        - [Peg-perigo](http://us.pegperego.com/toys-catalog/2013/Polaris+Sportsman+850+Gold)
        - bike tire
- Steering
    - bearings on the steering linkage connecter bar so that steering is smoother.  Currentyly steering is slightly loose.
    - play with motor controller to remove the latency in the steering linkage and figure out what is going on.
    - Have the steering (teleop) code reset to a 'center' after pressure is taken of the joystick
    - Code
        - Redo some of the low level code in C instead of python?

- Sensor mounts
    - Camera remounted to reduce vibration
        - 3d print something
            - either individual pieces or a large piece to hold all of the sensors
        - actually attach things to the car body instead of having them float slightly, this will reduce jar.
    - Lidar remount
        - secure it down, still removable
    - Center phone
        - The mount needs to be removable
    - computer
        - bolts
        - new computer?
            - < 85 watts, preferably around 50 watts
            - specialized hardware?
        - best bet is to continue to use a laptop, I can ask some questions to a few places about small footprint low power devices, but I can't make any promises
    - Remount the acyrlic dragonboard covers
        - Lasercut some nice pretty fitted sheets.
    - USB hub
        - Duct tape or some security
        - Dead man 
            - Talk to Jesse
            - Continue using figits?
            - battery interrupt that needs a ping every [time period] or it shuts off the main circuit?
    - battery harness
        - One single larger battery
    - dead man switch
        - Should it stay where it is?
        Also that whole back-panel needs to be shored up, its floppya nd terrifying

- Electrical
    - rewire everything
    - 1 single power source
        - Split to rails
    - things to wire
        - terminal block that splits to
        - dragonboards
        - USB hub
        - network device
        - computer
        - lidar
        - wheels
        - linear actuator

- Who can commit time to this
    - Josh -> Mounting
    - Jesse -> Steering
    - Bill -> Tires
    - Thomas -> Electrical

