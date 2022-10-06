import cv2

capture = cv2.VideoCapture('assets/video.mp4')
#METHOD 1
def rescaleFrame(frame, scale):
    #Best to use for resizing already existing videos
    '''Making a rescaling function to resize the image by taking the frame and the scale '''
    width = int(frame.shape[1] * scale)
    '''the value of width is convereted to an integer multiplied by the scale (number of pixels x scale)
    also frame.shape[1] is the width of image ''' 
    height = int(frame.shape[0] * scale)
    ''' frame.shape[0] is the height of the original image times the scale '''
    dimensions = (width,height)
    ''' the dimensions of the new image formed here'''

    return cv2.resize(frame, dimensions, interpolation = cv2.INTER_AREA)
    # ''' the function resizes the image/video by first taking in the original frame
    # then the dimensions for the new image and then the interpolation which means _______
    # (not found yet)'''

#METHOD 2

def changeRes(width,height):
    #Only works with live video 
    capture.set(3,width)#3 stand for hte class properties which means it refers to width of the image/video
    capture.set(4,height)#4 stands for the class properties which means it refers to the height of the image
    #There is also a option to change the brightness of the image by changing 4 to 10

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(
        frame = frame,
        scale = 0.55
    )
    cv2.imshow('Video resized', frame_resized)
    ''' Reads the video frame by frame each time and tells us true or false 
    if it worked or not. '''

    if cv2.waitKey(20) & 0xFF==ord('d'):#here if the letter d is pressed the video ends itself immediatly, ord means the ordinal number of that character in the ASCII table.
        break
    # ''' -215:Assertion failed error implies that either the frames left weere not enough
    # for cv2 to show more so it break it itself but for a longer video there might be enough
    # frames to show
    
    # This also happens when a wrong directory is specified or the object mentioned is not found'''

capture.release()
cv2.destroyAllWindows()