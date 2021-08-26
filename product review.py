header=['product id','product name','categories','MRP','price','discount']
categories_=['books','cloths','toys','shoes']
book_=['Rich dad Poor dad','The intelligent investor','Twelth fail','Alchemist',
       'outliers','sapiens']
cloth_=['T-shirt','shirt','Jeans','Jogger','Trouser']
toys_=['Nerf fortnite','Wooden cooking set','Hydraulic plane launcher',
      'Musical fishing game','Tumbling tower']
shoe_=['Adidas','Nike','puma','sparx','Red tape']
#entries=int(input('enter'))
import random
def pdetail(a,b,c):
    pid=a
    pname=random.choice(b)
    cat=c
    mrp_=random.randint(250,650)
    price_=random.randint(150,mrp_)
    dis=((mrp_-price_)*100)//mrp_
    details=str(pid)+','+pname+','+cat+','+str(mrp_)+','+str(price_)+','+str(dis)+'%'
    return details
with open('preview.csv','w') as f:
    data=','.join(header)
    f.write(data)
    f.write('\n')
    for i in range(1,1001):
        list=['d1','d2','d3','d4']
        a=random.choice(list)
        if a=='d1':
            d1=pdetail(i,book_,categories_[0])
            f.write(d1+'\n')
        elif a=='d2':    
            d2=pdetail(i,cloth_,categories_[1])
            f.write(d2+'\n')
        elif a=='d3':
            d3=pdetail(i,toys_,categories_[2])
            
            f.write(d3+'\n')
        elif a=='d4':
            d4=pdetail(i,shoe_,categories_[3])
            f.write(d4+'\n')
         
        

print('1-product of x category\n'+'2-product with price range from x and y\n'+
      '3-product of more than x% discount\n'+'4-product of x categories with y% discoutnt\n'
      +'5-exit')
for i in range(1,6):
    choice=int(input('enter your choice'))
    if choice==1:
        x=str(input('enter your category'))
        with open('1.txt','w') as f:
            with open('preview.csv',encoding='utf-8') as f1:
                for line in f1:
                    line=line.replace('\n','')
                    line1=line.split(',')
                    if line1[2]==x:
                        f.write(line+'\n')
    elif choice==2:
        x=str(input('enter intial price'))
        y=str(input('enter final price'))
        with open('2.txt','w') as f:
            with open('preview.csv',encoding='utf-8') as f1:
             
                for line in f1:
                    line=line.replace('\n','')
                    line1=line.split(',')
                    if line1[4]>'150' and line1[4]<'250':
                        f.write(line+'\n')
           
    elif choice==3:
        x=str(input('enter your discount'))
        with open('3.txt','w') as f:
            with open('preview.csv',encoding='utf-8') as f1:
                for line in f1:
                    line=line.replace('\n','')
                    line1=line.split(',')
                    if line1[5]>'45%':
                        f.write(line+'\n')
    elif choice==4:
        x=str(input('enter your category'))
        y=str(input('enter your discount'))
        with open('4.txt','w') as f:
            with open('preview.csv',encoding='utf-8') as f1:
                for line in f1:
                    line=line.replace('\n','')
                    line1=line.split(',')
                    if line1[2]==x and line[5]>y:
                        f.write(line+'\n')
                        
    else :
        break

















        
            
            
            
