# These and other macros are documented in ../droid-configs-device/droid-configs.inc

%define device ara
%define vendor nokia

%define vendor_pretty nokia
%define device_pretty ara

%define dcd_path ./

# Adjust this for your device
%define pixel_ratio 0.89

# We assume most devices will
%define have_modem 1

%include droid-configs-device/droid-configs.inc

