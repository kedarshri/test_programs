import pexpect
ip_address = '1.1.1.1'
username = 'cisco'
password = 'cisco'
# Create Pexpect telnet session
session = pexpect.spawn('telnet ' + ip_address, timeout=20)
result = session.expect(['Username:', pexpect.TIMEOUT])

# Check for error, if so then print error and exit
if result != 0:
    print ('--- FAILURE! creating session for: ', ip_address)
    exit()
    # Session expecting username, enter it here
session.sendline(username)
result = session.expect(['Password:', pexpect.TIMEOUT])

# Check for error, if so then print error and exit
if result != 0:
    print ('--- FAILURE! entering username: ', username)
    exit()

# Session expecting password, enter it here
session.sendline(password)
result = session.expect(['>', pexpect.TIMEOUT])

# Check for error, if so then print error and exit
if result != 0:
    print (' FAILURE! entering password: ', password)
    exit()

print ('--- Success! connecting to: ', ip_address)
print ('---               Username: ', username)
print ('---               Password: ', password)
print ('------------------------------------------------------\n')
# Send 'show interface' command to gather data about links
session.sendline('show interface summary')   # Send 'show interface' command
result = session.expect(['>', pexpect.TIMEOUT, pexpect.EOF])
if result == 0:    # successful reply to show interface command
    print ('Command sent successfully')
    return True
elif result == 1:  # timeout occurred
    print ('Timed out')
    return False
elif result == 2:   # EOF occurred
    print ('Received unexpected EOF response')
    return False
else:
    print ('Unexpected response')
    return False
    
    
# show_int_output = session.before
 
# int_output_lines = show_int_output.splitlines()
 
 session.close()
