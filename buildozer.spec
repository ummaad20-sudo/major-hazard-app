[app]

# (str) Title of your application
title = 13 Major Hazard

# (str) Package name
package.name = majorhazard

# (str) Package domain
package.domain = com.safety.app

# (str) Source code directory
source.dir = .

# (list) Source files to include
source.include_exts = py,kv,png,jpg

# (str) Application version
version = 1.0

# (list) Application requirements
requirements = python3,kivy

# (str) Orientation
orientation = portrait

# (bool) Fullscreen
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# (int) Android API
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b

# (str) Entry point
entrypoint = main.py

# (bool) Log level
log_level = 2

# (str) Presplash
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon
# icon.filename = %(source.dir)s/data/icon.png


[buildozer]
log_level = 2
warn_on_root = 1
