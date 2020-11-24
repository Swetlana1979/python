import argparse
parser = argparse.ArgumentParser(description='A tutorial of argparse!')
parser.add_argument("--file",default='task.hpp')
args = parser.parse_args()
file = args.file


#print(nb)
def convert_base(nb, base):
    
    try:
        if int(base):
			base = len(base)
        strStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if strStr.count(str(nb))!=0:
            nb = strStr.find(str(nb))+9
        
        nb = int(nb)
        
        alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if nb < base:
            return alphabet[nb]
        else:
            newNum = ''
            while nb > 0:
                newNum = str(nb % base) + newNum
                nb //= base
            return newNum
                    
    except Exception as e:
        print('Неверный ввод')
        
def main (file):
    f = open(file)
	a = f.readline()
	while line:
		a = f.readline()
	f.close()
	nb=a[0]
	base=a[1]
    result = convert_base(nb, base)
    print(result)
main (nb=1, base='01')