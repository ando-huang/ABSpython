import traceback

try:
    raise Exception("err message")
except:
    errorFile = open('error_log.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print("Err message sent to error_log.txt")
