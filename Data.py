f1=open("deceptive.txt",'w')
f2=open("truthful.txt",'w')
s1= 'F:/ML-Programming/op_spam_v1.4/negative_polarity/deceptive_from_MTurk/Masterfold/d_'
s2= 'F:/ML-Programming/op_spam_v1.4/positive_polarity/deceptive_from_MTurk/Masterfold/d_'
n1= ('hilton_','james_','monaco_','sofitel_')
n2= ('affinia_','ambassador_','hardrock_','talbott_')
n3= ('conrad_','fairmont_','hyatt_','omni_')
n4= ('homewood_','knickerbocker_','sheraton_','swissotel_')
n5= ('allegro_','amalfi_','intercontinental_','palmer_')
n=n1+n2+n3+n4+n5
for name in n:
    for i in range(1,21):
        f1.write(s1+name+str(i)+'.txt'+'\n')
        f1.write(s2 + name + str(i) + '.txt' + '\n')
f1.close()
s3= 'F:/ML-Programming/op_spam_v1.4/negative_polarity/truthful_from_Web/Masterfold/t_'
s4= 'F:/ML-Programming/op_spam_v1.4/positive_polarity/truthful_from_TripAdvisor/Masterfold/t_'
for name in n:
    for i in range(1,21):
        f2.write(s3+name+str(i)+'.txt'+'\n')
        f2.write(s4 + name + str(i) + '.txt' + '\n')
f2.close()