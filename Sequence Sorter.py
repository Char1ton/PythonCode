def sort(Seq):
        print(Seq)
        print('Seq')
        for i in range(len(Seq)):
            start=i
            for k in range(i+1,len(Seq)):
                if Seq[k]<Seq[start]:
                    start=k
            Seq[i],Seq[start]=Seq[start],Seq[i]
        print("Sorted Seq",Seq)

def absort(Seq):
    abSeq=[abs(N) for N in Seq]
    print(abSeq)
    for j in range(len(abSeq)):
            start=j
            for z in range(j+1,len(abSeq)):
                if abSeq[z]<abSeq[start]:
                    start=z
            abSeq[j],abSeq[start]=abSeq[start],abSeq[j]
    print("Sorted Absolute Seq",abSeq)
#Main Program
Seq=[0,2,1,5,3,-1]
sort(Seq)
absort(Seq)