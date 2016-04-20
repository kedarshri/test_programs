def main():
   filename = raw_input("Enter Name of the File:")
   fhandle = open (filename)
   count = 0
   for line in fhandle:
       count= count+1
   print 'Number of Lines:',count

if __name__ == "__main__":
     main()
