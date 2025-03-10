### Mount ntfs ssd from windows with read and write permissions, also setting its owner to current user

``` bash
sudo mount -t ntfs-3g -o uid=1000,gid=1000 /dev/nvme0n1p2 /storage
```

`sudo parted -l` - show all connected stat devices