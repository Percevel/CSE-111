from tkinter import Tk, Frame, Canvas, BOTH
import random

def main():
    width = 800
    height = 500

    # Create the root Tk object.
    root = Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = Frame()
    frame.master.title("Scene")
    frame.pack(fill=BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = Canvas(frame)
    canvas.pack(fill=BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.
    Parameters:
        scene_left - left side of the region; less than scene_right
        scene_top - top of the region; less than scene_bottom
        scene_right - right side of the region
        scene_bottom - bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """
    # Call your functions here, such as draw_sky, draw_ground,
    # draw_snowman, draw_tree, draw_shrub, etc.
    draw_sky(canvas,scene_left,scene_top,scene_right,scene_bottom)
    draw_ground(canvas, scene_left,scene_top+400,scene_right,scene_bottom )
    draw_cloud(canvas, scene_left+10,scene_top+10, scene_left+200, scene_top+100)
    draw_cloud(canvas, scene_right-400,scene_bottom-600, scene_right-50, scene_bottom-400)
    draw_grass(canvas, scene_left,scene_top+400,scene_right,scene_bottom )
    draw_trees(canvas, scene_left,scene_right, scene_top+400 )
    


# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.
def draw_sky(canvas,left_x_corner, left_y_corner, right_x_corner, right_y_corner):
    canvas.create_rectangle(left_x_corner, left_y_corner, right_x_corner, right_y_corner, fill="light blue",outline="light blue")

def draw_ground(canvas,left_x_corner, left_y_corner, right_x_corner, right_y_corner):
    canvas.create_rectangle(left_x_corner, left_y_corner, right_x_corner, right_y_corner, fill="tan4",outline="tan4")

def draw_cloud(canvas,left_x_corner, left_y_corner, right_x_corner, right_y_corner):
    canvas.create_oval(left_x_corner,left_y_corner,right_x_corner,right_y_corner, outline  ="white", fill="white")

    leng = right_x_corner-left_x_corner
    heig = right_y_corner - left_y_corner
    newstartx = left_x_corner + leng/2
    newstarty = left_y_corner + heig/2
    canvas.create_oval(newstartx, newstarty, newstartx+leng , newstarty+heig, outline  ="gray86", fill="gray86")

def draw_grass(canvas,left_x_corner,left_y_corner, right_x_corner,right_y_corner):
    for x in range(left_x_corner, right_x_corner, 6):
        for y in range(left_y_corner, right_y_corner, 6):
            c = random.randint(0,2)
            if c == 0:
                canvas.create_line(x,y,x,y-random.randint(5,15), width = 5, fill = "darkGreen")
            else:
                canvas.create_line(x,y,x,y-random.randint(5,15), width = 5, fill = "green")

def draw_trees(canvas,left_x_corner, right_x_corner, y_level):
    for x in range(0, 31):
        start = random.randint(left_x_corner, right_x_corner)

        canvas.create_line(start, y_level, start, y_level-40, width = 8, fill = "brown")

        canvas.create_polygon(start - 30, y_level-40, start, y_level-65, start + 30, y_level-40, fill = "green")
        canvas.create_polygon(start - 30, y_level-55, start, y_level-80, start + 30, y_level-55, fill = "green")
        canvas.create_polygon(start - 30, y_level-70, start, y_level-105, start + 30, y_level-70, fill = "green")
        canvas.create_polygon(start - 30, y_level-85, start, y_level-130, start + 30, y_level-85, fill = "green")
        canvas.create_polygon(start - 30, y_level-100, start, y_level-155, start + 30, y_level-100, fill = "green")


# Call the main function so that
# this program will start executing.
main()