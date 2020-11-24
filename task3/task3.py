import random
#lines = tuple(open(task1.txt, 'r'))
def generator(arrlength):
    array=[]
    i=0
    while i<arrlength:
        a=random.randint(0, 1000)
        array.append(a)
        i += 1
    return array

def success(volume,a):
    i=0
    vol=0
    success=0
    i = 1
    while i<len(a):
        if 0<=(vol+a[i])<volume:
            vol=vol+a[i]
            success=success+1
        i += 1
    emptyVol=volume-vol
    return vol, success, emptyVol
    
def main():
    valume = random.randint(10, 1000)
    arrlength = random.randint(10, 1000)
    array=generator(arrlength)
    result=success(valume,array)
	noSuc=arrlength-result[1]

    print("объем бочки -", valume, "л,", "текущий объем воды в бочке -", result[0],"л,","пустой объем -", result[2],"л,","количество попыток-",arrlength,"успешных попыток -",result[1],",не успешных",noSuc)
    
main()
    

 