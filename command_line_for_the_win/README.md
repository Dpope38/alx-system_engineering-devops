Project Name: **Command line for the win.**

***How to set up "sftp" on the ubuntu terminal***:

1:: Install the openSsh server and ssh on your local machine. command to use "sudo apt install openssh && sudo apt install ssh"

2:: After installing SSH server, we need to make some modifications to the SSHD configuration file located at "sudo nano /etc/ssh/sshd_config"

3:: Scroll to the end or bottom of the file and add the following lines:
    "Match Group sftp
    ChrootDirectory %h
    ForceCommand internal-sftp
    AllowTcpForwarding no"

4:: Save and close the file.

5:: Create a new user account that will be used for SFTP access. Replace <username> with the desired username. "sudo adduser <username>"

6:: Create a directory for SFTP access. Replace <username> with the username you created in the previous step. "sudo mkdir /home/<username>/sftp"

7:: Change the owner of the directory to root and the user you created. Replace <username> with the username you created. "sudo chown root:<username> /home/    <username>/sftp"

8:: Change the permissions of the directory. "sudo chmod 755 /home/<username>/sftp"

9:: To apply the changes, restart the SSH service. "sudo systemctl restart ssh"

10:: Connect to the Remote SFTP Host




