from vedo import Mesh, Plotter

# Load the avatar model
avatar = Mesh("C:/Users/STAR/Desktop/arduino/avatargirl1115.stl")
avatar.color([0.96, 0.80, 0.69])  # A soft tan/brown



# Normalize to center and scale the avatar
avatar.normalize()

# Setup plotter with no axes
plotter = Plotter(bg="white", axes=0, title="Interactive Avatar")

# Position the camera (front view, looking from -Y)
plotter.camera.SetPosition([0, -2, 1])   # x, y, z
plotter.camera.SetViewUp([0, 0, 1])      # z-axis is up

# Show the avatar
plotter.show(avatar, zoom=1.0, interactive=True)