[app]

# (str) Title of your application
title = Slingshot Empire

# (str) Package name
package.name = slingshotempire

# (str) Package domain (needed for android packaging)
package.domain = org.umeshpawade

# (str) Source code directory
source.dir = .

version = 1.0.0

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,jpeg,ttf,json,txt,bmp

# (list) Application requirements
# Pygame-bootstrap standard requires specific sequence to build correctly
requirements = python3, pygame==2.1.0, kivy==2.2.1, hostpython3

# (str) Supported orientations (one of landscape, sensorLandscape, portrait or all)
orientation = landscape

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (int) Android API to use (API 33 is standard and highly stable for pygame)
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Explicitly force accept licenses inside buildozer engine
android.accept_sdk_license = True

# (list) Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE

# (str) Core bootstrap layer for Python/Pygame apps
p4a.bootstrap = sdl2

android.archs = arm64-v8a
requirements = python3,pygame==2.5.2,kivy
