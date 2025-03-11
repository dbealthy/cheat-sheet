Create venv (.venv) - dir name
``` bash
python3 -m venv .venv
``` 

Activate venv
``` bash
source .venv/bin/activate
```
Deactivate venv
``` bash
deactivate
```

alternative way to run python script using venv:
``` bash
.venv/bin/python3 main.py
```


>if Virtual environment is launched from a script, it is suggested to use *full paths* and use bash scripts and not *shell* ones.

>*Shell* scripts don't support *source* command.
>*Bash* does