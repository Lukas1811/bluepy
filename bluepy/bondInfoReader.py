
def getBondInfo(interface: str, device: str) -> dict:
    ret = {}
    
    try:
        with open("/var/lib/bluetooth/%s/%s/info"%(interface, device), "r") as file:
            data = file.readlines() 
    except:
        return None
    
    top = ""
    
    for line in data:
        line = line.replace("\n", "")
        line = line.split("=")
        if line[0] == "":
            pass
        elif line[0][0] == "[":
            top = line[0].replace("[", "").replace("]","") 
            ret.update({top :{}})
        else:

            ret[top].update({line[0] : line[1]})
    
    return ret

if __name__ == "__main__":
    data =getBondInfo("00:1B:DC:08:E2:68", "EC:8B:17:64:7A:CD")
    print(data)