import pymem
import pymem.process
import ctypes


l4d2_process = "left4dead2.exe"
server_module = "server.dll"


m_iFOV = 0x1D8C
dwLocalPlayer = 0x7BACCC


def main():
    l4d2 = pymem.Pymem(l4d2_process)
    print("\n" + l4d2_process + " found.")


    server = pymem.process.module_from_name(l4d2.process_handle, server_module).lpBaseOfDll
    if server: print(server_module + " found.")


    fov_val = int(input("FOV Value: "))


    while True:
        player = l4d2.read_int(server + dwLocalPlayer)
        l4d2.write_int(player + m_iFOV, fov_val)


if __name__ == '__main__':
    ctypes.windll.kernel32.SetConsoleTitleA("[L4D2] Fov changer")
    main()
