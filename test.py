from jnius import autoclass

activity = autoclass('org.kivy.android.PythonActivity').mActivity
wifi_info = activity.getSystemService(activity.WIFI_SERVICE).getConnectionInfo()
signal_strength = wifi_info.getRssi()
print(signal_strength)
