WifiManager wifiManager = (WifiManager) context.getSystemService(Context.WIFI_SERVICE);
int numberOfLevels = 5;
WifiInfo wifiInfo = wifiManager.getConnectionInfo();
int level = WifiManager.calculateSignalLevel(wifiInfo.getRssi(), numberOfLevels);
