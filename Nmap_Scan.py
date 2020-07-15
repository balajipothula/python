# sudo apt -y install nmap xsltproc
# pip install ushlex

import shlex, subprocess

def nmap_scan_report():
  exec_nmap("cmd -Pn -sV -A --top-ports 2000 -iL input.txt -oX  output.xml")
  exec_cmd("xsltproc output.xml -o output.html")

def exec_cmd(cmd):
  args = shlex.split(cmd)
  pipe = subprocess.Popen(args, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
  out, err = pipe.communicate()

if __name__ == "__main__":
  nmap_scan_report()
