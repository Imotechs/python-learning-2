import random
import files
#making random fake names
Surnames = ['Muhamed','Musa','Abayo','Adole','Hungwati','Chia','Selu','Jubrin','Achi']
midlenames = ['joy', 'micheal','Senater','Joshua','keneth','Jessy','Ambros','Loveth']
lastnames = ['T','B','G','C','J','I','S','L','p']
Emails = ['Yahoo','gmail','outlook','hotmail']
values =random.randint(100,900)
mainvar = (7,8,9)
nexttomain = (0,1)
nexttofinal = (34,54,67,89,99,10,12,31,32,45,67,90,17,18,15,13,19,11,22,33,44,55,66,78)
finals = (123,879,674,546,123,213,343,564,678,676)
#print(values)

with open('Names.txt','w') as f:  
    f.write(f'Names\t\t Phone Numbers\t\t Mails\n')  
    for x in range(1,200):

        phone = (f'0')+ (f'{random.choice(mainvar)}')+ (f'{random.choice(nexttomain)}')+(f'{random.choice(nexttofinal)}')+(f'{values}')+(f'{random.choice(finals)}')
        Name = f"{random.choice(Surnames)} {random.choice(midlenames)} {random.choice(lastnames)}"
        Mail = Name.lower().strip()[:-2]
        choicemail= random.choice(Emails)
        candidate = f'{Name}  {phone}'
        val = list(candidate)
        
            #for x in range(len(val)):
        f.write(f'{Name}\t {phone}\t\t\t{Mail}@{choicemail}.com\n')

        print(Mail)
