import copy
print ("\033c\033[40;37m\n")

ss="""8086 X86
80186 X86
80286 X86
80386 X86
80486 X86
ARM7 ARM
ARM8 ARM"""

def chrarray(s):
    ss=[]
    for a in s:
       ss.append(copy.copy(a))           
    return ss
l=chrarray(ss)
print(l)