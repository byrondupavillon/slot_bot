from pynput import mouse

# Initialize variables to store the top-left and bottom-right coordinates
top_left = None
bottom_right = None


def on_click(x, y, button, pressed):
    global top_left, bottom_right

    if pressed:
        # If top_left hasn't been set, this is the first click (top-left corner)
        if top_left is None:
            top_left = (int(x), int(y))
            print(f"Click top left of the image")
            print(f"Top-left corner set at X: {top_left[0]}, Y: {top_left[1]}")
            print("Now, click the bottom-right corner of the image...")

        # If top_left is set, this must be the second click (bottom-right corner)
        elif bottom_right is None:
            bottom_right = (int(x), int(y))
            print(f"Bottom-right corner set at X: {bottom_right[0]}, Y: {bottom_right[1]}")

            # Calculate the region dimensions
            width = bottom_right[0] - top_left[0]
            height = bottom_right[1] - top_left[1]
            print(f"Region Coords: {top_left[0]}, {top_left[1]}, {width}, {height}")

            # Stop the listener since we've got both clicks
            return False

# Set up the listener for mouse clicks
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
