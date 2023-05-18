# start "" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" https://www.bing.com/search?q=hello  --profile-directory="Profile 1"

"""
    The function opens Microsoft Edge browser with different profiles and searches for a decreasing
    substring in Bing search engine.
"""
import subprocess
import time
# from jax import jit
import numba
import psutil

RandomText30 = "abcdefghijklmnopqrstuvwxyz123456"
RandomText10 = "uhbueehjwhgwr"
ProfileIDs = ["Default","1","2","3","4","5","7","8","9","10","11","12","13","14","15"]



def close_edge_browser():
    subprocess.run(["taskkill", "/im", "msedge.exe", "/f"])



def terminate_edge_tabs(profile_name):
    browser_processes = ["msedge.exe"]

    for proc in psutil.process_iter():
        try:
            process_name = proc.name()
            cmdline = proc.cmdline()
            if process_name.lower() in browser_processes and any(profile_name.lower() in arg.lower() for arg in cmdline):
                proc.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ProcessLookupError):
            pass



# @jit(nopython=True)
def run_command(command):
    try:
        # Open command prompt and run the command
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")

# @jit(nopython=True)
def main():
    # start = time.now
    # for each profile it will search the string 
    for i in range(len(ProfileIDs)):
        profile = ProfileIDs[i]
        if i != 0 :
            profile = "Profile " + ProfileIDs[i]
        
        print(profile)
            
        for j in range(len(RandomText30)-1,-1,-1):
            query = RandomText30[0:j]
            print(j,"   ", query)

            command = f'start "" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" https://www.bing.com/search?q={query}  --profile-directory="{profile}"'  
            run_command(command)
            time.sleep(1)
            if (j % 7 == 0):
                close_edge_browser()


if __name__ == "__main__":
    main()
