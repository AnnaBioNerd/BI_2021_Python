class RNA(str):
    def __init__(self,sequence):
        self._seq = sequence
    
    def gc_content(self):
        return (list(self._seq).count('C') + list(self._seq).count('G'))/len(self._seq)

    def reverse_complement(self):
        rev = self._seq[::-1]
        rev_tr = rev.maketrans('ATGC','TACG')
        rev = rev.translate(rev_tr)
        return rev
        
class DNA(RNA):
    def transcribe(self):
        return self._seq.replace('T','U')
    
#Для проверки:
#seq_RNA_1 = RNA('TACCGCCAATCG')
#seq_RNA_2 = RNA('TACCGCCAATCGC')
#seq_RNA_3 = RNA('TACCGCCAATCG')
#seq_DNA = DNA('TACGCCA')

#1. Инициализация строкой
#print(seq_RNA_1)
#2. Доля нуклеотидов
#print(seq_RNA_1.gc_content())
#3. Компл. послед.
#print(seq_RNA_1.reverse_complement())
#4. Итерация по послед.
#for i in seq_RNA_1:
#    print(i)
#5. Объекты с один. послед. должны быть равны
#равны
#print(seq_RNA_1 == seq_RNA_3)
#не равны
#print(seq_RNA_1 == seq_RNA_2)
#6. Добавлевлние в множество
#print([seq_RNA_1,seq_RNA_2])
#7. траскриб.
#print(seq_DNA.transcribe())