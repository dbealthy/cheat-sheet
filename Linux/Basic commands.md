# Termial basics
*source*: https://www.youtube.com/watch?v=s3ii48qYBxAe
>*Commands marked with '!' may be dangerous*

### Directories
`pwd` - prints current working directory
`cd ~`, `cd` - go to home directory

`ls` - shows not hidden files
`ls -a` - shows all files
`ls -lah` - long listed files (hum read sizes, prommistions, cr dates)

`mkdir [dirname]` - make a directory
`rmdir [dirname]` - remove empty directory
`rm -rf [dirname]` - !remove all dir's contents and dir itself

### Files
`touch [filename.txt]` - create file without writing in it
`nano [filename2.txt]` - create file and write in it

`cat [filename]` - show file's contents in the termial
`less [filename]` - read file line by line
`head [filename]` - print first 10 lines of a file (default)
`tail -n 20 [filename]` - print last 20 lines of a file 


`mv [file1.txt] [newdir\/]` - moves file to new location
`cp [file1.txt] [newdir\/]` - copies file to new location
`rm [path/file1.txt]` - remove file

`chmod [int] [filename]` - sets file's promissions
### Search
`which [programm/command]` - prints binary program's location
`whereis [programm/command` - prints binary, libs, files location of the program
`locate [programm/command]` - lists all dirs/files that have [pr/co] in title
`sudo updatedb` - updates files and dirs for `locate`
`find [dirname] -iname str_search` - finds files/dirs that have str in title (any case)

---
`grep 'str_search' [path/filename]` - search specific words in a file
`sed "s/OLD/NEW/g"` - find and replace str


### Print Text
`echo "Some Text"` - prints text in termial
`printf "1\n2\n3"` - prints text with formatting

### Special characters
'**\>**' - Greater than symbol, write's command's output to a file
'**\|**' - Pipe symbol, redirects output of one command to anothe command
>`printf "1\\n2\\n3" > filename.txt` - write text to file

>`ls -l | sed "s/[aeio]/u/g"` - replace all vowels of  listed dirs to 'u'

### Kill programms
`kill programmname` - kills instance of programm
`killall programmname` - kill all instances of programm
`xkill` - turns cursor into an x, any program it is cliked exits (once)
`htop` - show all processes and allow to kill them. (install)

### Internet
`ping google.com` - check internet connection by pinging
`wget https://somelinux.com/new-release.iso` - download

### Miscellaneous
`man [command]` - open command's manual
`clear`, **ctrl + L** - clear termial screen
`history` - shows all commands history in termial
`!number` - runs command from history by number
`!!` - run last command that was used
`date` - shows current date
`cal` - shows calendar
`bc` - calculator