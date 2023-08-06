1. Move to applications direcotry for all users
```bash
cd /usr/share/applications
```

2. Create new or edit existing file that ends with ***.desktop***
3. Write script to 
```bash
[Desktop Entry]
Version=1.0
Type=Application
Terminal=false
Exec=/usr/bin/gedit
Name=gedit
Comment=gedit
Icon=/home/linuxconfig/Downloads/icon.png
```