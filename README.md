# Script Queue Manager

A small suite of simple CLI tools to queue up scripts to be executed. A simple use case is that of having to repeatedly execute the same scripts with different parameters and each script takes hours to execute. (eg - I personally use it to queue my deep learning training tasks)

## Installing from pip

### Stable release
```shell script
pip install script-queue-manager
```

### Development release
```shell script
pip install -i https://test.pypi.org/simple/ script-queue-manager
```

## Getting Started
I highly recommend that you fork the project by clicking on the ``Fork`` button and then cloning your fork using the command mentioned below.

``
git clone <your fork URL>
`` 

### Prerequisites
- Python 3.5+
- A code editor or IDE(preferable PyCharm)

### Setting up for Development
Follow the steps mentioned below to get your dev instance running.

1) After cloning your fork, open the project in an IDE or code editor of you choice.

1) It is highly advisable that you create a new Python environment for the project. Follow the instructions given [here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands).

1) Navigate to the project directory and install the `requirement.txt` packages.
    ```
    cd <project-directory>
    pip install -r requirements.txt
    ```
1) Build the project:

    ``` 
    python setup.py install 
    ```

1) Use the `pusher` to push a script to the task queue.
   ```
   sqm-pusher -s "cat x.txt"
   ``` 
1) Start the `executor` tool.
   ```
   sqm-executor
   ```
   If you want to start it as a background process, in Ubuntu run 
   ```
   sqm-executor &
   ```
   
## Execution Model
The executor fetches an object from the front of the queue and prepares a script as `PRE_SCRIPT + QUEUE_SCRIPT`. Here, `PRE_SCRIPT` can be given as input to the executor using the flag `-p` as shown below:
```shell script
sqm-executor -p "path-to-the-file-containing-the-prescripts"
```
The sleeping interval for the executor to sleep in between tasks can be provided using the flag `-s`. By default it is 15s.
The executor produces logs for every task it executes. The file path for this log file can be provided using the `-l` flag. By default it is located at `$HOME/sqm/logs.txt`.

## Tests
Not yet implemented

## Built With

* [Persistqueue](https://pypi.org/project/persist-queue/) - File based queue.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Mayank Vaidya** - *Initial work*

See also the list of [contributors](contributors.md) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details
