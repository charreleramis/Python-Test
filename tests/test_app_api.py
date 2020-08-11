import pytest
import os
import subprocess
import inspect
import requests
import platform
import signal

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)

def start_app():

    comand = "python %s runserver" % os.path.join(parent_dir,"manage.py")
    cmd = comand.split(" ")
    print(cmd)
    proc = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    res = requests.get("http://127.0.0.1:8000")
    return proc.pid


class TempSingleton(object):
    __instance = None

    def __init__(self):
        self.app_pid = None
        self.server_id = None
        self.fqfp = None
        self.fid = None
        self.key_id = None

    def get_instance(self):
        if not TempSingleton.__instance:
            TempSingleton.__instance = self

        return TempSingleton.__instance

def kill_process(pid):
    operating_system = platform.system()

    if operating_system == "Windows":
        print("> KILL PROCESS %s - WINDOWS DETECTED" % pid)
        os.kill(pid, signal.SIGTERM)
    elif operating_system == "Linux":
        print("> KILL PROCESS %s - LINUX DETECTED" % pid)
        os.kill(pid, signal.SIGTERM)
    else:
        print("> KILL PROCESS %s - UNSUPPORTED OS DETECTED" % pid)


def test_create_record():
    start_app()
    params = {"context":"DUMMY PRINCIPLE","context_type":"P","context_id":13}
    res1 = requests.post("http://127.0.0.1:8000/create_data",data=params)

    params = {"context": "DUMMY VALUES", "context_type": "V", "context_id": 5}
    res2 = requests.post("http://127.0.0.1:8000/create_data", data=params)

    assert res1.status_code == res2.status_code


def test_read_data():
    id = 1

    url = "http://127.0.0.1:8000/read_data/values/%s"%id
    res1 = requests.post(url)

    url = "http://127.0.0.1:8000/read_data/principle/%s" % id
    res2 = requests.post(url)

    assert res1.status_code == res2.status_code


def test_read_all():
    url = "http://127.0.0.1:8000/read_all_data"
    res = requests.post(url)
    assert res.status_code == 200


def test_update_data():
    new_str = "Individuals and Interactions Over Processes and Tools | CHECK DB"
    params = {"id": 1, "context": new_str}
    res = requests.post("http://127.0.0.1:8000/update_data", data=params)
    assert res.status_code == 200


def test_delete_data():
    params = { "id":1}
    print("DELETE ID: 1")
    res = requests.post("http://127.0.0.1:8000/delete_data",data=params)
    assert res.status_code == 200


def test_teardown():
    s = TempSingleton().get_instance()
    if s.app_pid:
        print("> KILLING CLIENT PROCESS %s" % s.app_pid)
        kill_process(s.app_pid)
