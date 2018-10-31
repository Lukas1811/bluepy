bluepy
======

This a fork from the popular [bluepy](https://github.com/IanHarvey/bluepy) API by [IanHarvey](https://github.com/IanHarvey), it adds the features:

- checking if a device is available, in one function 
- pairing (with passkey check)
- bondstore access (gives you the possibility to read the bondstore on your linux machine

Installation
------------
```
sudo python3 -m pip install git+https://github.com/Lukas1811/bluepy.git
```

New Functions
=============

- Peripheral:
  - static **getControllerAddress()** 
    Returns the address of the local bluetooth controller
  - static **getInfo(interface: str, address:str)**
    Returns bondinformation for a specific device on a specific local controller
  - static **unpair(address: str)**
    Removes bonding informations for a specific device
  - static **pair(address: str, passkey: int)**
    Bonds the local controller with a device (close your connection to the device before pairing)
  - static **isAvailable(address: str)**
    Returns if a device is currently advertising


