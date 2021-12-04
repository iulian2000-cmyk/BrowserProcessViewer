from subprocess import Popen, PIPE
import os, psutil
import sys




def mainApp():
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
