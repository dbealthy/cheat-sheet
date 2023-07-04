All usb devices are located in `/dev/bus/usb`


## Userful commands
- List all usb devices with their corresponding ids
> `lsusb`

- List verbose information about usb devices
> `lsusb -v`

- Check devices permissions
> `ls -l /dev/bus/usb/{bus_id}`

- Change devices permissions
>`sudo chmod a+w /dev/bus/usb/{bus_id}}/{device_id}`

- Change device owner
> `sudo chown {username}:{optional_group} /dev/bus/usb/{bus_id}{device_id}`

# Add rules for devices on system start up.
This might be useful when passing though devices to VMs and errors that happen because of permissions.

create file in `/etc/udev/rules.d` called `{devicename}.rules`
with content:
`SUBSYSTEMS=="usb", ATTRS{idVendor}=="{vendor_id}", ATTRS{idProduct}=="{product_id}", MODE="0666" OWNER="{owner_id}"`

