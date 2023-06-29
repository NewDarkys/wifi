import subprocess

def get_wifi_networks():
    cmd = ['iwlist', 'wlan0', 'scan'] # замените 'wlan0' на интерфейс Wi-Fi вашего устройства
    output = subprocess.check_output(cmd).decode('utf-8')
    networks = []
    network = {}

    for line in output.split('\n'):
        if 'Cell' in line:
            if network:
                networks.append(network)
            network = {}
        elif 'ESSID' in line:
            network['ssid'] = line.split(':')[1].strip().strip('"')
        elif 'Quality' in line:
            quality = line.split('=')[1].split()[0].split('/')
            network['signal_level'] = round((int(quality[0]) / int(quality[1])) * 100, 2)
    
    if network:
        networks.append(network)
    
    return networks

def display_wifi_networks(networks):
    for network in networks:
        print(f"Network: {network['ssid']}")
        print(f"Signal Level: {network['signal_level']} dBm")
        print()

# Получение списка сетей Wi-Fi
wifi_networks = get_wifi_networks()

# Отображение списка сетей Wi-Fi
display_wifi_networks(wifi_networks)
