schu=["","UN ","DEUX ","TROIS ","QUATRE ","CINQ ","SIX ","SEPT ","HUIT ","NEUF "]
schud=["DIX ","ONZE ","DOUZE ","TREIZE ","QUATORZE ","QUINZE ","SEIZE ","DIX SEPT ","DIX HUIT ","DIX NEUF "]
schd=["","DIX ","VINGT ","TRENTE ","QUARANTE ","CINQUANTE ","SOIXANTE ","SOIXANTE ","QUATRE VINGT ","QUATRE VINGT "]
def convNombre2lettres(nombre):
    s=''
    reste=nombre
    i=1000000000
    strnombre = str(nombre)
    l = strnombre.split('.')
    reste = int(l[0])

    while i>0:
        y=reste/i
        if y!=0:
            centaine=y/100
            dizaine=(y - centaine*100)/10
            unite=y-centaine*100-dizaine*10
            if centaine==1:
                s+="CENT "
            elif centaine!=0:
                s+=schu[centaine]+"CENT "
                if dizaine==0 and unite==0: s=s[:-1]+"S "
            if dizaine not in [0,1]: s+=schd[dizaine]
            if unite==0:
                if dizaine in [1,7,9]: s+="DIX "
                elif dizaine==8: s=s[:-1]+"S "
            elif unite==1:
                if dizaine in [1,9]: s+="ONZE "
                elif dizaine==7: s+="ET ONZE "
                elif dizaine in [2,3,4,5,6]: s+="ET UN "
                elif dizaine in [0,8]: s+="UN "
            elif unite in [2,3,4,5,6,7,8,9]:
                if dizaine in [1,7,9]: s+=schud[unite]
                else: s+=schu[unite]
            if i==1000000000:
                if y>1: s+="MILLIARDS "
                else: s+="MILLIARD "
            if i==1000000:
                if y>1: s+="MILLIONS "
                else: s+="MILLIONS "
            if i==1000:
                s+="MILLE "
        #end if y!=0
        reste -= y*i
        dix=False
        i/=1000;
    #end while
    if len(s)==0: s+="ZERO "
    flag = False
    if len(l) > 1:
        if int(l[1])!=0:
            return s +"DINARS ET "+convNombre2lettres(l[1])+"CENTIMES"
    return s
#print convNombre2lettres(19220.36)
