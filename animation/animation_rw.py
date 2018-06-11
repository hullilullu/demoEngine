import os
import animation
from animation import animation

def load_animations_in_dir(d):
    return_dict = {}
    for file_name in d:
            print(os.getcwd())
            f = open(d + "/testanims.txt")
            lines = f.readlines()
            for l in lines:
                sl = l.split(";")
                frames = []
                #try:
                anData = sl[0].split(",")
                name = anData[0]
                sheet = anData[1]
                for fr in(sl[1:]):
                    frame = fr.split(",")
                    print(frame)
                    frames.append(animation.Frame(sheet, int(frame[0]), int(frame[1]), int(frame[2]), int(frame[3]), int(frame[4])))
                return_dict[name] = animation.Animation(frames)
                #except:
                print("animation load error")
    return return_dict



"""
return_dict = {}

	return_dict["GO_TEST"] = animation.Animation([animation.Frame("test_graphics.jpg", 0, 0, 70, 85), animation.Frame("test_graphics.jpg", 70, 0, 70, 85)])
	return_dict["IDLE_TEST"] = animation.Animation([animation.Frame("test_graphics.jpg", 0, 0, 70, 85), animation.Frame("test_graphics.jpg", 10, 0, 70, 85)])
	return_dict["IDLE_MAIN"] = animation.Animation([animation.Frame("generalMainSmall.jpg", 42, 42, 99, 126)])
	return_dict["JUMP_MAIN"] = animation.Animation([animation.Frame("generalMainSmall.jpg", 57, 423, 67, 134)])
	return_dict["WALK_MAIN"] = animation.Animation([animation.Frame("generalMainSmall.jpg", 45, 226, 114, 109, offset_x = -15),
		animation.Frame("generalMainSmall.jpg", 262,230, 42, 120, offset_x = 35),
		animation.Frame("generalMainSmall.jpg", 460, 230, 64, 123, offset_x = 13)], 2)

"""
#if file.endswith(".txt"):
