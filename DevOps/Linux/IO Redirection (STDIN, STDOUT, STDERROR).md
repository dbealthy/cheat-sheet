# I/O Redirection
### Streams
- *STDIN (0)* -Standart input
- *STDOUT(1)*-Standart output
- *STDERR(2)* -Standart error

By default (Without redirection):
*STDIN* is going from user to programm, by means of keyboard and termial
*STDOUT* outputs its content to the termial
*STDERR* prints error to the terminal


### Stream Redirection to a file
>**When redirecting stram to a file, the file is created/overridden first of all, then command has executed and its output redirected to the file.**

Overwrite
- *>* - standart output
- *<* - standart input
- *2>* - standart error

Append
- *>>* - standart output
- *<<* - standart input
- *2>>* - standart error

Example:
- `echo "Text to trash" > /dev/null` - redirects output to trash (removes) 
- `echo "text" > write_me.txt` - overrides a file with "text"

	
### Redirect stream of one command into another (Pipes)
Symbol - **|**
`ls -al | less` - redirects ouput of ls command into less
`grep git ./Documents/NerdIT/Git.md | wc -l` - prints number of lines that contain 'git' word
	
