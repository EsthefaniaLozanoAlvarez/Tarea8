def chi(a,b,c):
    dis=(b*b)-(4*a*c)
    if(dis>0):
        x1=(-b+((dis)**(1/2)))/(2*a)
        x2=(-b-((dis)**(1/2)))/(2*a)
        print("X1= ",x1,"X2= ",x2)
    if(dis==0):
        x1=x2=(-b)/(2*a)
        print("X1 = "+str(x1)+" X2 = "+str(x2))
    if(dis<0):
        xr=(-b)/(2*a)
        x1=((-dis)**(1/2))/(2*a)
        x2=-(-dis)**(1/2)/(2*a)
        print("X1 parte real=",xr,"parte imaginaria= j",x1,"X2 parte real=",xr,"parte imaginaria= j",x2)
a=float(input('Valor de coeficiente cudrático: '))
b=float(input('Valor de coeficiente lineal: '))
c=float(input('Valor de término independiente: '))
chi(a,b,c)
   
