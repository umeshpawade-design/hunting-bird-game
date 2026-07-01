[app]

# (str) Title of your application
title = Slingshot Empire

# (str) Package name
package.name = slingshotempire

# (str) Package domain (needed for android packaging)
package.domain = org.umeshpawade

# (str) Source code directory
source.dir = .

# (str) Application version
version = 1.0.0

# (list) Source files to include
source.include_exts = py,png,jpg,jpeg,ttf,json,txt,bmp

# (list) Application requirements
requirements = python3,pygame==2.5.2,kivy

# (str) Supported orientations
orientation = landscape

# (bool) Indicate if the application should be fullscreen
fullscreen = 1

# (int) Android API to use
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

# (list) The Android architectures to build for
android.archs = arm64-v8a

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
