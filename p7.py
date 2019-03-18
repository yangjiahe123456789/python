def wordCount(data):
    re = {}
    for i in data:
        re[i] = re.get(i,0) + 1
    return re
if __name__ == "__main__":
    data =["When"," I"," do"," count"," the", "clock"," that", "tells", "the"," time"]
    print ("The result is %s" % wordCount(data))
