import odrive
import time

odrv0 = odrive.find_any()
Xaxis = odrv0.axis0
Xmotor = Xaxis.motor
Xenc = Xaxis.encoder
Yaxis = odrv0.axis1
Ymotor = Yaxis.motor
Yenc = Yaxis.encoder


steps = 1000
ticks = 0

endstopMaxAmps = ((steps / 100) * 2.4)
odriveMaxAmps = Xmotor.config.current_lim

xRange = 0
yRange = 0
xMaximum = 0
yMax = 0
xMin = 0
yMin = 0
xRatio = 0
yRatio = 0
stepsForX = 0
stepsForY = 0

def gotoPos(xpos, ypos):
    xpos = ypos
    Xaxis.controller.pos_setpoint = (xpos/1024)*(xRange)+xMin
    Yaxis.controller.pos_setpoint = (ypos/1024)*(yRange)+yMin

def initialize(xmax, ymax):
    home()

def home():
    initialXEncoderPos = int(Xenc.pos_estimate)
    initialYEncoderPos = int(Yenc.pos_estimate)

    startTime = time.monotonic()
    while True:
        currentPos = int(Xaxis.encoder.pos_estimate)

        Xaxis.controller.pos_setpoint = currentPos + steps

        currentUsage = Xmotor.current_control.Iq_measured

        ticks = ticks + 1 if (currentUsage >= endstopMaxAmps) else ticks - 1
        ticks = ticks if ticks >= 0 else 0
        if ticks >= 3:
            break

        time.sleep(0.01)
    #xMax = currentPos - steps
    #Xaxis.controller.pos_setpoint = initialXEncoderPos

    startTime = time.monotonic()
    while True:
        currentPos = int(Xaxis.encoder.pos_estimate)

        Xaxis.controller.pos_setpoint = currentPos - steps

        currentUsage = Xmotor.current_control.Iq_measured

        ticks = ticks + 1 if (currentUsage >= endstopMaxAmps) else ticks - 1
        ticks = ticks if ticks >= 0 else 0
        if ticks >= 3:
            break

        time.sleep(0.01)
    xMin = currentPos + steps
    Xaxis.controller.pos_setpoint = initialXEncoderPos

    xRange = -abs(xMin) + abs(xMaximum)

    initialXEncoderPos = int(Xenc.pos_estimate)
    intialYEncoderPos = int(Yenc.pos_estimate)


    startTime = time.monotonic()
    while True:
        currentPos = int(Xaxis.encoder.pos_estimate)

        Xaxis.controller.pos_setpoint = currentPos + steps

        currentUsage = Xmotor.current_control.Iq_measured

        ticks = ticks + 1 if (currentUsage >= endstopMaxAmps) else ticks - 1
        ticks = ticks if ticks >= 0 else 0
        if ticks >= 3:
            break

        time.sleep(0.01)
    xMax = currentPos - steps
    Xaxis.controller.pos_setpoint = initialXEncoderPos

    startTime = time.monotonic()
    while True:
        currentPos = int(Xaxis.encoder.pos_estimate)

        Xaxis.controller.pos_setpoint = currentPos - steps

        currentUsage = Xmotor.current_control.Iq_measured

        ticks = ticks + 1 if (currentUsage >= endstopMaxAmps) else ticks - 1
        ticks = ticks if ticks >= 0 else 0
        if ticks >= 3:
            break

        time.sleep(0.01)
    yMin = currentPos + steps
    Yaxis.controller.pos_setpoint = initialYEncoderPos

    yRange = -abs(yMin) + abs(yMax)