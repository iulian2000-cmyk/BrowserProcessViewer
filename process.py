from subprocess import Popen, PIPE
import os, psutil
import sys


def view_all_processes():
    print()
    list_processes_system = psutil.process_iter()
    for process in list_processes_system:
        try:
            # Get process name & pid from process object.
            processName = proc.name()
            processID = proc.pid
            processCMD = proc.cmdline()
            processTime = proc.cpu_times()
            processPPID = proc.ppid()
            processMemory = proc.memory_percent()
            print("PROCES NAME : " ,processName)
            print("PID : ",processID)
            print("PPID :",processPPID)
            print("CMD : " ,processCMD)
            print("CPU times : ", processTime)
            print("Memory use :" , processMemory)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass


def kill_process(pid):
    os.kill(int(pid), 9)


def suspend_process(pid):
    process = psutil.Process(int(pid))
    process.suspend()


def resume_process(pid):
    process = psutil.Process(int(pid))
    process.resume()


def start_a_new_process(path_executabile, arguments):
    arguments_cmd = " "
    for arg in arguments:
        arguments_cmd = arguments_cmd + arg + " "

    print(os.popen(path_executabile + "  " + arguments_cmd).read())


def mainApp():
    if len(sys.argv) == 1:
        print("Give me some arguments !")
        exit(0)
    if sys.argv[1] == "view":
        view_all_processes()
    if sys.argv[1] == "kill":
        if len(sys.argv) < 3:
            print("\n Error : Usage : python process.py kill <PID> \n")
        else:
            kill_process(sys.argv[2])
    if sys.argv[1] == "suspend":
        if len(sys.argv) < 3:
            print("\n Error : Usage : python process.py suspend <PID>")
        else:
            suspend_process(sys.argv[2])
    if sys.argv[1] == "resume":
        if len(sys.argv) < 3:
            print("\n Error : Usage : python process.py resume <PID>")
        else:
            resume_process(sys.argv[2])
    if sys.argv[1] == "run":
        if len(sys.argv) < 3:
            print("\n Error : Usage : python process.py run <PATH_EXECUTABILE> <ARGS>")
        else:
            app_to_run = sys.argv[2]
            args_run = []
            for index in range(3, len(sys.argv)):
                args_run.append(sys.argv[index])

            print("\n Application to run :" + app_to_run + "\n")
            start_a_new_process(app_to_run, args_run)


mainApp()
