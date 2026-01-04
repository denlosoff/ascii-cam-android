[app]

# (str) Title of your application
title = Ascii Cam

# (str) Package name
package.name = asciicam

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (str) Version of your application
version = 0.1

# (list) Source files to include (let buildozer find them)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of modules to be packaged in the apk
requirements = python3,kivy,pillow,numpy

# (str) Presplash background color (for new android toolchain)
#android.presplash_color = #FFFFFF

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.arch = arm64-v8a

# (list) Permissions
android.permissions = CAMERA

# (int) Android API to use
android.api = 27

# (int) Minimum API required
android.minapi = 21

[buildozer]

# (int) Log level (0 = error, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
