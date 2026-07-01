[app]
title = Slingshot Empire
package.name = slingshotempire
package.domain = com.slingshotempire.game
source.dir = src
source.include_exts = py,png,jpg,kv,atlas,ttf,ogg,wav,json
version.regex = __version__ = ['\"](.*)['\"]
version.filename = src/config.py
requirements = python3,pygame
orientation = landscape
fullscreen = 1
android.api = 34
android.minapi = 21
android.ndk = 25b
android.sdk = 34
android.arch = arm64-v8a, armeabi-v7a
android.permissions = INTERNET, WAKE_LOCK, VIBRATE

# AdMob configuration: replace these with your real AdMob App ID before release.
# The value is read from the environment; set ADMOB_APP_ID in your build environment.
android.meta_data = com.google.android.gms.ads.APPLICATION_ID=${ADMOB_APP_ID}

android.min_sdk_version = 21
android.target_sdk_version = 34
android.accept_sdk_license = True
android.entrypoint = org.kivy.android.PythonActivity
android.apptheme = @android:style/Theme.NoTitleBar.Fullscreen
p4a.local_recipes =

# Optional: add a python-for-android AdMob recipe (e.g. kivmob/kivads) here.
# For example, if you have a local recipe folder:
# p4a.local_recipes = ./recipes

[buildozer]
log_level = 2
warn_on_root = 1
