#Linux #Basics

> The **first** running process in old Linux is **init** in newer systems it is **systemd**. It is created by the kernel itself.

### Forking
New process is created by **fork()** system call.
It forks parent process by cloning it and changing needed parts.

### Process Lifecycle
Process is forked from a parent process and put into running state then it may go into code path where it waits for some resource or signal, while waiting process may fall into two of sleep states and give up a few cpu cycles. Also a process might be suspended by sending SIGSTOP signal. Process in this state will continue to exist until it is killed or resumed with SIGCONT. Finally the process completes its lifecycle when it is terminated and placed into zombie state until its parent process clears it off the process table.

### Process states
- Running or Runnable (R)
- Uninterruptible sleep (D) - Waiting for resources (hdd, network, io, ...) can't be interrupted by signals
- Interruptible sleep (S) - Waiting for resources like user input () can be interrupted by signals
- Stopped (T)
- Zombie (Z)

### Stopping process 
**SIGSTOP** -  put a process into stop state. Process can't catch or ignore it.
**SIGSTP** - put a process into stop state. Process can ignore the signal. The signal is send when we press **ctrl + Z** short cut. 

**SIGCONT** - bring back process to running state 

### Zombie state
When a process has completed its execution or is terminated, it will send the **SIGHLD** signal to the parent process and go into **Zombie state**. 
Zombie process will remain in this state until the parent process clears it off from the process table. To clear the process, the parent process must read the **exit value** of child using **wait()** or **waitpid()** system calls.  