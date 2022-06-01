import pandas as pd
from pandas import ExcelWriter
import openpyxl
import os
print("¿Que movimiento quieres hacer?")
print("\nPuedes ver la informacion de un cliente o ingresar a un cliente")
ya=input("¿Que deseas hacer?")
quiero=list(ya)
terminar=quiero[2]
este=ord(terminar)
if este==70 or este==102:#informacion del cliente 
    print("\nno olvides escribir el nombre de tu archivo .xlsx")
    archivo=input("\n¿que archivo quieres?")
    doc=pd.ExcelFile(archivo)
    data=pd.read_excel(archivo)
    print(data)
else:
    nombre=input("Nombre completo del cliente")
    telefono=int(input("Numero de telefono"))
    clave=input("CURP del cliente")
    pregunta2=input("¿credito o de contado?")
    a1=list(pregunta2)
    b1=a1[1]
    c1=ord(b1) 
    class datosdelcliente:
        def __init__(self):
            self.nombreM=nombre
            self.telefonoM=telefono
            self.claveM=clave
        def datoscompletos(self):
            datos={"Nombre del cliente":[nombre],
                   "Telefono":[telefono],
                   "Clave":[clave]}
            df=pd.DataFrame(datos)
            df=df[["Nombre del cliente","Telefono","Clave"]]
            writer=ExcelWriter("datosdelcliente.xlsx")
            df.to_excel(writer,"Hoja de datos", index=False)
            writer.save()
            return(df)
        def nombre(self):
            return(self.nombreM)
        def telefono(self):
            return(self.telefonoM)
        def clave(self):
            return(self.claveM)
    datos1=datosdelcliente()
    if c1==79 or c1==111:##comprar a contado
        pregunta3=input("¿quieres ver la lista de autos?\n si o no")
        #ver la lista, columna o fila
        a2=list(pregunta3)
        b2=a2[0]
        c2=ord(b2)
        if c2==83 or c2==115:#si quiero ver la lista de autos
            pregunta4=input("¿quieres ver la lista de autos,una columan o un auto?")
            #quieres ver lista, columna o auto
            print("lista, columna o auto")
            doc=pd.ExcelFile("autos.xlsx")
            df=doc.parse("Hoja1")
            data=pd.read_excel('autos.xlsx')
            data2=pd.read_excel('autos2.xlsx')
            a3=list(pregunta4)
            b3=a3[0]
            c3=ord(b3)
            if c3==76 or c3==108:##lista
                print(df)
                g=input('\nDame el codigo del auto')
                h=int(input('Dame el indice del auto'))
                data2=pd.read_excel('codigos.xlsx')
                df=pd.DataFrame(data2,columns=[g])
                datos={'PASE A PAGAR':['',"NOMBRE DEL CLIENTE:",nombre,df.loc[0],df.loc[1],'PASAR A PAGAR:',df.loc[2],'','GRACIAS POR LA COMPRA']}
                dg=pd.DataFrame(datos)
                dg=dg[["PASE A PAGAR"]]
                writer2=ExcelWriter("Ticket.xlsx")
                dg.to_excel(writer2,"Hoja1",index=False)
                writer2.save()
                data2.drop([g],axis=1,inplace=True)
                os.remove('codigos.xlsx')
                writer3=ExcelWriter("codigos.xlsx")
                data2.to_excel(writer3,"Hoja1",index=False)
                writer3.save()
                data3=pd.read_excel('autos.xlsx')
                data3.drop([h],axis=0,inplace=True)
                data3=pd.read_excel('autos.xlsx')
                os.remove('autos.xlsx')
                writer4=ExcelWriter('autos.xlsx')
                data3.to_excel(writer4,"Hoja1",index=False)
                writer4.save()
                data3=pd.read_excel('autos.xlsx')
                print(datos1.datoscompletos())
                print("NO ponerle nombre al archivo")
            elif c3==67 or c3==99:#columna
                e=input('¿que columna deseas?')
                df=pd.DataFrame(data,columns=[e])
                print(df)
                g=input('\nDame el codigo del auto')
                h=int(input('Dame el indice del auto'))
                data2=pd.read_excel('codigos.xlsx')
                df=pd.DataFrame(data2,columns=[g])
                datos={'PASE A PAGAR':['',"NOMBRE DEL CLIENTE:",nombre,df.loc[0],df.loc[1],'PASAR A PAGAR:',df.loc[2],'','GRACIAS POR LA COMPRA']}
                dg=pd.DataFrame(datos)
                dg=dg[["PASE A PAGAR"]]
                writer2=ExcelWriter("Ticket.xlsx")
                dg.to_excel(writer2,"Hoja1",index=False)
                writer2.save()
                data2.drop([g],axis=1,inplace=True)
                os.remove('codigos.xlsx')
                writer3=ExcelWriter("codigos.xlsx")
                data2.to_excel(writer3,"Hoja1",index=False)
                writer3.save()
                data3=pd.read_excel('autos.xlsx')
                data3.drop([h],axis=0,inplace=True)
                os.remove('autos.xlsx')
                writer4=ExcelWriter('autos.xlsx')
                data3.to_excel(writer4,"Hoja1",index=False)
                writer4.save()   
                print(datos.datoscompletos())  
                print("NO ponerle nombre al archivo")
            else:##auto
                f=input('¿que auto quieres ver?')
                df=pd.DataFrame(data2,columns=["Auto",f])
                print(df)
                g=input('\nDame el codigo del auto')
                h=int(input('Dame el indice del auto'))
                data2=pd.read_excel('codigos.xlsx')
                df=pd.DataFrame(data2,columns=[g])
                datos={'PASE A PAGAR':['',"NOMBRE DEL CLIENTE:",nombre,df.loc[0],df.loc[1],'PASAR A PAGAR:',df.loc[2],'','GRACIAS POR LA COMPRA']}
                dg=pd.DataFrame(datos)
                dg=dg[["PASE A PAGAR"]]
                writer2=ExcelWriter("Ticket.xlsx")
                dg.to_excel(writer2,"Hoja1",index=False)
                writer2.save()
                data2.drop([g],axis=1,inplace=True)
                os.remove('codigos.xlsx')
                writer3=ExcelWriter("codigos.xlsx")
                data2.to_excel(writer3,"Hoja1",index=False)
                writer3.save()
                data3=pd.read_excel('autos.xlsx')
                data3.drop([h],axis=0,inplace=True)
                os.remove('autos.xlsx')
                writer4=ExcelWriter('autos.xlsx')
                data3.to_excel(writer4,"Hoja1",index=False)
                writer4.save()
                print(datos.datoscompletos())
                print("NO ponerle nombre al archivo")
        else:##iprimir ticket directo
            g=input('Dame el codigo del auto')
            h=int(input('Dame el indice del auto'))
            data2=pd.read_excel('codigos.xlsx')
            df=pd.DataFrame(data2,columns=[g])
            datos={'PASE A PAGAR':['',"NOMBRE DEL CLIENTE:",nombre,df.loc[0],df.loc[1],'PASAR A PAGAR:',df.loc[2],'','GRACIAS POR LA COMPRA']}
            dg=pd.DataFrame(datos)
            dg=dg[["PASE A PAGAR"]]
            writer2=ExcelWriter("Tickets.xlsx")
            dg.to_excel(writer2,clave,index=False)
            writer2.save()
            data2.drop([g],axis=1,inplace=True)
            os.remove('codigos.xlsx')
            writer3=ExcelWriter("codigos.xlsx")
            data2.to_excel(writer3,"Hoja1",index=False)
            writer3.save()
            data3=pd.read_excel('autos.xlsx')
            data3.drop([h],axis=0,inplace=True)
            os.remove('autos.xlsx')
            writer4=ExcelWriter('autos.xlsx')
            data3.to_excel(writer4,"Hoja1",index=False)
            writer4.save()
            print(datos.datoscompletos())
            print("NO ponerle nombre al archivo")
    else:#comprar a credito
        RFC=input('Dame tu RFC')
        codigopostal=input('dame tu codigo postal')
        calle=input('dame tu calle')
        numero=input('numero interior y exterior')
        ingresos=input('tiene el requisito de ingresos')
        historialcrediticio=input('historial crediticio')
        referenciascrediticias=input('referencias crediticias')
        referenciaspersonales=input('referencias personales')
        cuentabancaria=input('dame tu numero de cuenta bancaria')
        z=referenciascrediticias
        y=list(z)
        x=y[0]
        w=ord(x)
        pregunta3=input("¿quieres ver la lista de autos?\n si o no")#ver la lista, columna o fila
        a2=list(pregunta3)
        b2=a2[0]
        c2=ord(b2)
        class compracredito(datosdelcliente):
            def __init__(self):
                datosdelcliente. __init__(self)
                self.RFCs=RFC
                self.codigopostals=codigopostal
                self.calles=calle
                self.numeros=numero
                self.ingresoss=ingresos
                self.historialcrediticios=historialcrediticio
                self.referenciascrediticiass=referenciascrediticias
                self.referenciaspersonaless=referenciaspersonales
                self.cuentabancarias=cuentabancaria
            def datoscompletoscredito(self):
                datos={"Nombre del cliente":[nombre], "Telefono":[telefono],
                       "Clave":[clave],"RFC":[RFC],
                       "direccion":[codigopostal],"cumpleconingresos":[ingresos],
                       "historialcrediticio":[historialcrediticio],
                       "referenciascrediticias":[referenciascrediticias],
                       "referenciaspersonales":[referenciaspersonales],"cuentabancaria":[cuentabancaria]}
                df=pd.DataFrame(datos)
                df=df[["Nombre del cliente","Telefono","Clave","RFC","direccion",
                       "cumpleconingresos","historialcrediticio","referenciascrediticias",
                       "referenciaspersonales","cuentabancaria"]]
                writer=ExcelWriter("DATOS DEL CLIENTE.xlsx")
                df.to_excel(writer,"Hoja de datos crediticias", index=False)
                writer.save()
                return(df)
            def RFC(self):
                return(self.RFCs)
            def CODIGOPOSTAL(self):
                return(self.codigopostals)
            def CALLE(self):
                return(self.calles)
            def NUMERO(self):
                return(self.numeros)
            def INGRESOS(self):
                return(self.ingresoss)
            def HISTORIALCREDITICIO(self):
                return(self.historialcrediticios)
            def REFERENCIASCREDITICIAS(self):
                return(self.referenciascrediticiass)
            def REFERENCIASPERSONALES(self):
                return(self.referenciaspersonaless)
            def CUENTABANCARIA(self):
                return(self.cuentabancarias)
        datoscredito=compracredito()    
        if c2==83 or c2==115:#si quiero ver la lista de autos
            print("lista, columna o auto")
            pregunta4=input("¿quieres ver la lista de autos,una columan o un auto?")
            #quieres ver lista, columna o auto
            doc=pd.ExcelFile("autos.xlsx")
            df=doc.parse("Hoja1")
            data=pd.read_excel('autos.xlsx')
            data2=pd.read_excel('autos2.xlsx')
            a3=list(pregunta4)
            b3=a3[0]
            c3=ord(b3)
            if c3==76 or c3==108:##lista
                print(df)
                if w==77 or w==109:#muy buenas referencias crediticias
                    print('no necesita dar pago inicial')
                    a=input('¿desea dar pago inicial?')
                    b=list(a)
                    c=b[0]
                    d=ord(c)
                    if d==83 or d==115:#si dara pago inicial
                        g1=input('Dame el codigo del auto')
                        h1=int(input('Dame el indice del auto'))
                        data10=pd.read_excel('codigos.xlsx')
                        df=pd.DataFrame(data10,columns=[g1])
                        print(df)
                        costo=int(input('cuanto costo el auto'))
                        pagoinicial=int(input('Cuanto va a ser de pago inicial'))
                        tiempo=int(input('a cuantos meses se pagara el auto'))
                        subtotal=costo-pagoinicial
                        subtotal2=subtotal*(.3)
                        subtotalfinal=subtotal+subtotal2
                        meses=subtotalfinal/tiempo
                        mesesfinal=round(meses)
                        print("se pagara",mesesfinal,"por",tiempo)
                        data2=pd.read_excel('codigos.xlsx')
                        datos={'PASE A PAGAR':['',"NOMBRE DEL CLIENTE:",nombre,df.loc[0],df.loc[1],'PASAR A PAGAR:',pagoinicial,'','GRACIAS POR LA COMPRA']}
                        dg=pd.DataFrame(datos)
                        dg=dg[["PASE A PAGAR"]]
                        writer2=ExcelWriter("Ticketcredito.xlsx")
                        dg.to_excel(writer2,"Hoja1",index=False)
                        writer2.save()
                        data2.drop([g1],axis=1,inplace=True)
                        os.remove('codigos.xlsx')
                        writer3=ExcelWriter("codigos.xlsx")
                        data2.to_excel(writer3,"Hoja1",index=False)
                        writer3.save()
                        data3=pd.read_excel('autos.xlsx')
                        data3.drop([h1],axis=0,inplace=True)
                        os.remove('autos.xlsx')
                        writer4=ExcelWriter('autos.xlsx')
                        data3.to_excel(writer4,"Hoja1",index=False)
                        writer4.save()
                        print(datoscredito.datoscompletoscredito())
                        print("NO ponerle nombre al archivo")
                    else:#No dara pago inicial
                        g1=input('Dame el codigo del auto')
                        h1=int(input('Dame el indice del auto'))
                        data10=pd.read_excel('codigos.xlsx')
                        df=pd.DataFrame(data10,columns=[g1])
                        print(df)
                        costo=int(input('cuanto costo el auto'))
                        tiempo=int(input('a cuantos meses se pagara el auto'))
                        total=costo*(.35)
                        meses=total/tiempo
                        mesesfinal=round(meses)
                        print("se pagara",mesesfinal,"por",tiempo)
                        data2=pd.read_excel('codigos.xlsx')
                        datos={'PASE A PAGAR':['',"NOMBRE DEL CLIENTE:",nombre,df.loc[0],df.loc[1],'PASAR A PAGAR:',pagoinicial,'','GRACIAS POR LA COMPRA']}
                        dg=pd.DataFrame(datos)
                        dg=dg[["PASE A PAGAR"]]
                        writer2=ExcelWriter("Ticketcredito1.xlsx")
                        dg.to_excel(writer2,"Hoja1",index=False)
                        writer2.save()
                        data2.drop([g1],axis=1,inplace=True)
                        os.remove('codigos.xlsx')
                        writer3=ExcelWriter("codigos.xlsx")
                        data2.to_excel(writer3,"Hoja1",index=False)
                        writer3.save()
                        data3=pd.read_excel('autos.xlsx')
                        data3.drop([h1],axis=0,inplace=True)
                        os.remove('autos.xlsx')
                        writer4=ExcelWriter('autos.xlsx')
                        data3.to_excel(writer4,"Hoja1",index=False)
                        writer4.save()
                        compra=input("codigo del auto comprado")
                        print(datoscredito.datoscompletoscredito())
                        print("NO ponerle nombre al archivo")
                elif w==66 or w==98:#buenas referencias crediticias
                    g1=input('Dame el codigo del auto')
                    h1=int(input('Dame el indice del auto'))
                    data10=pd.read_excel('codigos.xlsx')
                    df=pd.DataFrame(data10,columns=[g1])
                    print(df)
                    costo=int(input('cuanto costo el auto'))
                    print("\npor las referencias se debe de dar el 15% de pago inicial forzoso")
                    pagoinicial=round(costo*(.15))
                    print("el minimo de pago inicial es",pagoinicial)
                    pagoinicial=int(input('Cuanto va a ser de pago inicial'))
                    tiempo=int(input('a cuantos meses se pagara el auto'))
                    subtotal=costo-pagoinicial
                    subtotal2=subtotal*(.35)
                    subtotalfinal=subtotal+subtotal2
                    meses=subtotalfinal/tiempo
                    mesesfinal=round(meses)
                    print("se pagara",mesesfinal,"por",tiempo)
                    data2=pd.read_excel('codigos.xlsx')
                    datos={'PASE A PAGAR':['',"NOMBRE DEL CLIENTE:",nombre,df.loc[0],df.loc[1],'PASAR A PAGAR:',pagoinicial,'','GRACIAS POR LA COMPRA']}
                    dg=pd.DataFrame(datos)
                    dg=dg[["PASE A PAGAR"]]
                    writer2=ExcelWriter("Ticketcredito2.xlsx")
                    dg.to_excel(writer2,"Hoja1",index=False)
                    writer2.save()
                    data2.drop([g1],axis=1,inplace=True)
                    os.remove('codigos.xlsx')
                    writer3=ExcelWriter("codigos.xlsx")
                    data2.to_excel(writer3,"Hoja1",index=False)
                    writer3.save()
                    data3=pd.read_excel('autos.xlsx')
                    data3.drop([h1],axis=0,inplace=True)
                    os.remove('autos.xlsx')
                    writer4=ExcelWriter('autos.xlsx')
                    data3.to_excel(writer4,"Hoja1",index=False)
                    writer4.save()
                    print(datoscredito.datoscompletoscredito())
                    print("NO ponerle nombre al archivo")
                else:#malas referencias crediticias
                    g1=input('Dame el codigo del auto')
                    h1=int(input('Dame el indice del auto'))
                    data10=pd.read_excel('codigos.xlsx')
                    df=pd.DataFrame(data10,columns=[g1])
                    print(df)
                    costo=int(input('cuanto costo el auto'))
                    print("\npor las referencias se debe de dar el 15% de pago inicial forzoso")
                    pagoinicial=round(costo*(.30))
                    print("el minimo de pago inicial es",pagoinicial)
                    pagoinicial=int(input('Cuanto va a ser de pago inicial'))
                    tiempo=int(input('a cuantos meses se pagara el auto'))
                    subtotal=costo-pagoinicial
                    subtotal2=subtotal*(.45)
                    subtotalfinal=subtotal+subtotal2
                    meses=subtotalfinal/tiempo
                    mesesfinal=round(meses)
                    print("se pagara",mesesfinal,"por",tiempo)
                    data2=pd.read_excel('codigos.xlsx')
                    datos={'PASE A PAGAR':['',"NOMBRE DEL CLIENTE:",nombre,df.loc[0],df.loc[1],'PASAR A PAGAR:',pagoinicial,'','GRACIAS POR LA COMPRA']}
                    dg=pd.DataFrame(datos)
                    dg=dg[["PASE A PAGAR"]]
                    writer2=ExcelWriter("Ticketcredito3.xlsx")
                    dg.to_excel(writer2,"Hoja1",index=False)
                    writer2.save()
                    data2.drop([g1],axis=1,inplace=True)
                    os.remove('codigos.xlsx')
                    writer3=ExcelWriter("codigos.xlsx")
                    data2.to_excel(writer3,"Hoja1",index=False)
                    writer3.save()
                    data3=pd.read_excel('autos.xlsx')
                    data3.drop([h1],axis=0,inplace=True)
                    os.remove('autos.xlsx')
                    writer4=ExcelWriter('autos.xlsx')
                    data3.to_excel(writer4,"Hoja1",index=False)
                    writer4.save()
                    print(datoscredito.datoscompletoscredito())
                    print("NO ponerle nombre al archivo")
            elif c3==67 or c3==99:#columna
                e=input('¿que columna deseas?')
                df=pd.DataFrame(data,columns=[e])
                print(df)
                if w==77 or w==109:#muy buenas referencias crediticias
                    print('no necesita dar pago inicial')
                    a=input('¿desea dar pago inicial?')
                    b=list(a)
                    c=b[0]
                    d=ord(c)
                    if d==83 or d==115:#si dara pago inicial
                        g1=input('Dame el codigo del auto')
                        h1=int(input('Dame el indice del auto'))
                        data10=pd.read_excel('codigos.xlsx')
                        df=pd.DataFrame(data10,columns=[g1])
                        print(df)
                        costo=int(input('cuanto costo el auto'))
                        pagoinicial=int(input('Cuanto va a ser de pago inicial'))
                        tiempo=int(input('a cuantos meses se pagara el auto'))
                        subtotal=costo-pagoinicial
                        subtotal2=subtotal*(.3)
                        subtotalfinal=subtotal+subtotal2
                        meses=subtotalfinal/tiempo
                        mesesfinal=round(meses)
                        print("se pagara",mesesfinal,"por",tiempo)
                        data2=pd.read_excel('codigos.xlsx')
                        datos={'PASE A PAGAR':['',"NOMBRE DEL CLIENTE:",nombre,df.loc[0],df.loc[1],'PASAR A PAGAR:',pagoinicial,'','GRACIAS POR LA COMPRA']}
                        dg=pd.DataFrame(datos)
                        dg=dg[["PASE A PAGAR"]]
                        writer2=ExcelWriter("Ticketcredito3.xlsx")
                        dg.to_excel(writer2,"Hoja1",index=False)
                        writer2.save()
                        data2.drop([g1],axis=1,inplace=True)
                        os.remove('codigos.xlsx')
                        writer3=ExcelWriter("codigos.xlsx")
                        data2.to_excel(writer3,"Hoja1",index=False)
                        writer3.save()
                        data3=pd.read_excel('autos.xlsx')
                        data3.drop([h1],axis=0,inplace=True)
                        os.remove('autos.xlsx')
                        writer4=ExcelWriter('autos.xlsx')
                        data3.to_excel(writer4,"Hoja1",index=False)
                        writer4.save()
                        compra=input("codigo del auto comprado")
                        print(datoscredito.datoscompletoscredito())
                    else:#No dara pago inicial
                        g1=input('Dame el codigo del auto')
                        h1=int(input('Dame el indice del auto'))
                        data10=pd.read_excel('codigos.xlsx')
                        df=pd.DataFrame(data10,columns=[g1])
                        print(df)
                        costo=int(input('cuanto costo el auto'))
                        tiempo=int(input('a cuantos meses se pagara el auto'))
                        total=costo*(.35)
                        meses=total/tiempo
                        mesesfinal=round(meses)
                        print("se pagara",mesesfinal,"por",tiempo)
                        data2=pd.read_excel('codigos.xlsx')
                        datos={'PASE A PAGAR':['',"NOMBRE DEL CLIENTE:",nombre,df.loc[0],df.loc[1],'PASAR A PAGAR:',pagoinicial,'','GRACIAS POR LA COMPRA']}
                        dg=pd.DataFrame(datos)
                        dg=dg[["PASE A PAGAR"]]
                        writer2=ExcelWriter("Ticketcredito4.xlsx")
                        dg.to_excel(writer2,"Hoja1",index=False)
                        writer2.save()
                        data2.drop([g1],axis=1,inplace=True)
                        os.remove('codigos.xlsx')
                        writer3=ExcelWriter("codigos.xlsx")
                        data2.to_excel(writer3,"Hoja1",index=False)
                        writer3.save()
                        data3=pd.read_excel('autos.xlsx')
                        data3.drop([h1],axis=0,inplace=True)
                        os.remove('autos.xlsx')
                        writer4=ExcelWriter('autos.xlsx')
                        data3.to_excel(writer4,"Hoja1",index=False)
                        writer4.save()
                        compra=input("codigo del auto comprado")
                        print(datoscredito.datoscompletoscredito())
                elif w==66 or w==98:#buenas referencias crediticias
                    g1=input('Dame el codigo del auto')
                    h1=int(input('Dame el indice del auto'))
                    data10=pd.read_excel('codigos.xlsx')
                    df=pd.DataFrame(data10,columns=[g1])
                    print(df)
                    costo=int(input('cuanto costo el auto'))
                    print("\npor las referencias se debe de dar el 15% de pago inicial forzoso")
                    pagoinicial=round(costo*(.15))
                    print("el minimo de pago inicial es",pagoinicial)
                    pagoinicial=int(input('Cuanto va a ser de pago inicial'))
                    tiempo=int(input('a cuantos meses se pagara el auto'))
                    subtotal=costo-pagoinicial
                    subtotal2=subtotal*(.35)
                    subtotalfinal=subtotal+subtotal2
                    meses=subtotalfinal/tiempo
                    mesesfinal=round(meses)
                    print("se pagara",mesesfinal,"por",tiempo)
                    data2=pd.read_excel('codigos.xlsx')
                    datos={'PASE A PAGAR':['',"NOMBRE DEL CLIENTE:",nombre,df.loc[0],df.loc[1],'PASAR A PAGAR:',pagoinicial,'','GRACIAS POR LA COMPRA']}
                    dg=pd.DataFrame(datos)
                    dg=dg[["PASE A PAGAR"]]
                    writer2=ExcelWriter("Ticketcredit0.xlsx")
                    dg.to_excel(writer2,"Hoja1",index=False)
                    writer2.save()
                    data2.drop([g1],axis=1,inplace=True)
                    os.remove('codigos.xlsx')
                    writer3=ExcelWriter("codigos.xlsx")
                    data2.to_excel(writer3,"Hoja1",index=False)
                    writer3.save()
                    data3=pd.read_excel('autos.xlsx')
                    data3.drop([h1],axis=0,inplace=True)
                    os.remove('autos.xlsx')
                    writer4=ExcelWriter('autos.xlsx')
                    data3.to_excel(writer4,"Hoja1",index=False)
                    writer4.save()
                    compra=input("codigo del auto comprado")
                    print(datoscredito.datoscompletoscredito())
                else:#malas referencias crediticias
                    g1=input('Dame el codigo del auto')
                    h1=int(input('Dame el indice del auto'))
                    data10=pd.read_excel('codigos.xlsx')
                    df=pd.DataFrame(data10,columns=[g1])
                    print(df)
                    costo=int(input('cuanto costo el auto'))
                    print("\npor las referencias se debe de dar el 15% de pago inicial forzoso")
                    pagoinicial=round(costo*(.30))
                    print("el minimo de pago inicial es",pagoinicial)
                    pagoinicial=int(input('Cuanto va a ser de pago inicial'))
                    tiempo=int(input('a cuantos meses se pagara el auto'))
                    subtotal=costo-pagoinicial
                    subtotal2=subtotal*(.45)
                    subtotalfinal=subtotal+subtotal2
                    meses=subtotalfinal/tiempo
                    mesesfinal=round(meses)
                    print("se pagara",mesesfinal,"por",tiempo)
                    data2=pd.read_excel('codigos.xlsx')
                    datos={'PASE A PAGAR':['',"NOMBRE DEL CLIENTE:",nombre,df.loc[0],df.loc[1],'PASAR A PAGAR:',pagoinicial,'','GRACIAS POR LA COMPRA']}
                    dg=pd.DataFrame(datos)
                    dg=dg[["PASE A PAGAR"]]
                    writer2=ExcelWriter("Ticketcredito8.xlsx")
                    dg.to_excel(writer2,"Hoja1",index=False)
                    writer2.save()
                    data2.drop([g1],axis=1,inplace=True)
                    os.remove('codigos.xlsx')
                    writer3=ExcelWriter("codigos.xlsx")
                    data2.to_excel(writer3,"Hoja1",index=False)
                    writer3.save()
                    data3=pd.read_excel('autos.xlsx')
                    data3.drop([h1],axis=0,inplace=True)
                    os.remove('autos.xlsx')
                    writer4=ExcelWriter('autos.xlsx')
                    data3.to_excel(writer4,"Hoja1",index=False)
                    writer4.save()
                    compra=input("codigo del auto comprado")
                    print(datoscredito.datoscompletoscredito())
            else:##auto
                f=input('¿que auto quieres ver?')
                df=pd.DataFrame(data2,columns=["Auto",f])
                print(df)
                if w==77 or w==109:#muy buenas referencias crediticias
                    print('no necesita dar pago inicial')
                    a=input('¿desea dar pago inicial?')
                    b=list(a)
                    c=b[0]
                    d=ord(c)
                    if d==83 or d==115:#si dara pago inicial
                        g1=input('Dame el codigo del auto')
                        h1=int(input('Dame el indice del auto'))
                        data10=pd.read_excel('codigos.xlsx')
                        df=pd.DataFrame(data10,columns=[g1])
                        print(df)
                        costo=int(input('cuanto costo el auto'))
                        pagoinicial=int(input('Cuanto va a ser de pago inicial'))
                        tiempo=int(input('a cuantos meses se pagara el auto'))
                        subtotal=costo-pagoinicial
                        subtotal2=subtotal*(.3)
                        subtotalfinal=subtotal+subtotal2
                        meses=subtotalfinal/tiempo
                        mesesfinal=round(meses)
                        print("se pagara",mesesfinal,"por",tiempo)
                        data2=pd.read_excel('codigos.xlsx')
                        datos={'PASE A PAGAR':['',"NOMBRE DEL CLIENTE:",nombre,df.loc[0],df.loc[1],'PASAR A PAGAR:',pagoinicial,'','GRACIAS POR LA COMPRA']}
                        dg=pd.DataFrame(datos)
                        dg=dg[["PASE A PAGAR"]]
                        writer2=ExcelWriter("Ticketcredito7.xlsx")
                        dg.to_excel(writer2,"hoja1",index=False)
                        writer2.save()
                        data2.drop([g1],axis=1,inplace=True)
                        os.remove('codigos.xlsx')
                        writer3=ExcelWriter("codigos.xlsx")
                        data2.to_excel(writer3,"hoja1",index=False)
                        writer3.save()
                        data3=pd.read_excel('autos.xlsx')
                        data3.drop([h1],axis=0,inplace=True)
                        os.remove('autos.xlsx')
                        writer4=ExcelWriter('autos.xlsx')
                        data3.to_excel(writer4,"hoja1",index=False)
                        writer4.save()
                        compra=input("codigo del auto comprado")
                        print(datoscredito.datoscompletoscredito())
                    else:#No dara pago inicial
                        g1=input('Dame el codigo del auto')
                        h1=int(input('Dame el indice del auto'))
                        data10=pd.read_excel('codigos.xlsx')
                        df=pd.DataFrame(data10,columns=[g1])
                        print(df)
                        costo=int(input('cuanto costo el auto'))
                        tiempo=int(input('a cuantos meses se pagara el auto'))
                        total=costo*(.35)
                        meses=total/tiempo
                        mesesfinal=round(meses)
                        print("se pagara",mesesfinal,"por",tiempo)
                        data2=pd.read_excel('codigos.xlsx')
                        datos={'PASE A PAGAR':['',"NOMBRE DEL CLIENTE:",nombre,df.loc[0],df.loc[1],'PASAR A PAGAR:',pagoinicial,'','GRACIAS POR LA COMPRA']}
                        dg=pd.DataFrame(datos)
                        dg=dg[["PASE A PAGAR"]]
                        writer2=ExcelWriter("Ticketcredito6.xlsx")
                        dg.to_excel(writer2,"hoja1",index=False)
                        writer2.save()
                        data2.drop([g1],axis=1,inplace=True)
                        os.remove('codigos.xlsx')
                        writer3=ExcelWriter("codigos.xlsx")
                        data2.to_excel(writer3,"hoja1",index=False)
                        writer3.save()
                        data3=pd.read_excel('autos.xlsx')
                        data3.drop([h1],axis=0,inplace=True)
                        os.remove('autos.xlsx')
                        writer4=ExcelWriter('autos.xlsx')
                        data3.to_excel(writer4,"hoja1",index=False)
                        writer4.save()
                        compra=input("codigo del auto comprado")
                        print(datoscredito.datoscompletoscredito())
                elif w==66 or w==98:#buenas referencias crediticias
                    g1=input('Dame el codigo del auto')
                    h1=int(input('Dame el indice del auto'))
                    data10=pd.read_excel('codigos.xlsx')
                    df=pd.DataFrame(data10,columns=[g1])
                    print(df)
                    costo=int(input('cuanto costo el auto'))
                    print("\npor las referencias se debe de dar el 15% de pago inicial forzoso")
                    pagoinicial=round(costo*(.15))
                    print("el minimo de pago inicial es",pagoinicial)
                    pagoinicial=int(input('Cuanto va a ser de pago inicial'))
                    tiempo=int(input('a cuantos meses se pagara el auto'))
                    subtotal=costo-pagoinicial
                    subtotal2=subtotal*(.35)
                    subtotalfinal=subtotal+subtotal2
                    meses=subtotalfinal/tiempo
                    mesesfinal=round(meses)
                    print("se pagara",mesesfinal,"por",tiempo)
                    data2=pd.read_excel('codigos.xlsx')
                    datos={'PASE A PAGAR':['',"NOMBRE DEL CLIENTE:",nombre,df.loc[0],df.loc[1],'PASAR A PAGAR:',pagoinicial,'','GRACIAS POR LA COMPRA']}
                    dg=pd.DataFrame(datos)
                    dg=dg[["PASE A PAGAR"]]
                    writer2=ExcelWriter("Ticketcredito5.xlsx")
                    dg.to_excel(writer2,"hoja1",index=False)
                    writer2.save()
                    data2.drop([g1],axis=1,inplace=True)
                    os.remove('codigos.xlsx')
                    writer3=ExcelWriter("codigos.xlsx")
                    data2.to_excel(writer3,"hoja1",index=False)
                    writer3.save()
                    data3=pd.read_excel('autos.xlsx')
                    data3.drop([h1],axis=0,inplace=True)
                    os.remove('autos.xlsx')
                    writer4=ExcelWriter('autos.xlsx')
                    data3.to_excel(writer4,"hoja1",index=False)
                    writer4.save()
                    compra=input("codigo del auto comprado")
                    print(datoscredito.datoscompletoscredito())
                else:#malas referencias crediticias
                    g1=input('Dame el codigo del auto')
                    h1=int(input('Dame el indice del auto'))
                    data10=pd.read_excel('codigos.xlsx')
                    df=pd.DataFrame(data10,columns=[g1])
                    print(df)
                    costo=int(input('cuanto costo el auto'))
                    print("\npor las referencias se debe de dar el 15% de pago inicial forzoso")
                    pagoinicial=round(costo*(.30))
                    print("el minimo de pago inicial es",pagoinicial)
                    pagoinicial=int(input('Cuanto va a ser de pago inicial'))
                    tiempo=int(input('a cuantos meses se pagara el auto'))
                    subtotal=costo-pagoinicial
                    subtotal2=subtotal*(.45)
                    subtotalfinal=subtotal+subtotal2
                    meses=subtotalfinal/tiempo
                    mesesfinal=round(meses)
                    print("se pagara",mesesfinal,"por",tiempo)
                    data2=pd.read_excel('codigos.xlsx')
                    datos={'PASE A PAGAR':['',"NOMBRE DEL CLIENTE:",nombre,df.loc[0],df.loc[1],'PASAR A PAGAR:',pagoinicial,'','GRACIAS POR LA COMPRA']}
                    dg=pd.DataFrame(datos)
                    dg=dg[["PASE A PAGAR"]]
                    writer2=ExcelWriter("Ticketcredito01.xlsx")
                    dg.to_excel(writer2,"hoja1",index=False)
                    writer2.save()
                    data2.drop([g1],axis=1,inplace=True)
                    os.remove('codigos.xlsx')
                    writer3=ExcelWriter("codigos.xlsx")
                    data2.to_excel(writer3,"hoja1",index=False)
                    writer3.save()
                    data3=pd.read_excel('autos.xlsx')
                    data3.drop([h1],axis=0,inplace=True)
                    os.remove('autos.xlsx')
                    writer4=ExcelWriter('autos.xlsx')
                    data3.to_excel(writer4,"hoja1",index=False)
                    writer4.save()
                    compra=input("codigo del auto comprado")
                    print(datoscredito.datoscompletoscredito())
        else:##iprimir ticket directo
            z=referenciascrediticias
            y=list(z)
            x=y[0]
            w=ord(x)
            if w==77 or w==109:#muy buenas referencias crediticias
                print('no necesita dar pago inicial')
                a=input('¿desea dar pago inicial?')
                b=list(a)
                c=b[0]
                d=ord(c)
                if d==83 or d==115:#si dara pago inicial
                    g1=input('Dame el codigo del auto')
                    h1=int(input('Dame el indice del auto'))
                    data10=pd.read_excel('codigos.xlsx')
                    df=pd.DataFrame(data10,columns=[g1])
                    print(df)
                    costo=int(input('cuanto costo el auto'))
                    pagoinicial=int(input('Cuanto va a ser de pago inicial'))
                    tiempo=int(input('a cuantos meses se pagara el auto'))
                    subtotal=costo-pagoinicial
                    subtotal2=subtotal*(.3)
                    subtotalfinal=subtotal+subtotal2
                    meses=subtotalfinal/tiempo
                    mesesfinal=round(meses)
                    print("se pagara",mesesfinal,"por",tiempo)
                    data2=pd.read_excel('codigos.xlsx')
                    datos={'PASE A PAGAR':['',"NOMBRE DEL CLIENTE:",nombre,df.loc[0],df.loc[1],'PASAR A PAGAR:',pagoinicial,'','GRACIAS POR LA COMPRA']}
                    dg=pd.DataFrame(datos)
                    dg=dg[["PASE A PAGAR"]]
                    writer2=ExcelWriter("Ticketcredito02.xlsx")
                    dg.to_excel(writer2,"hoja1",index=False)
                    writer2.save()
                    data2.drop([g1],axis=1,inplace=True)
                    os.remove('codigos.xlsx')
                    writer3=ExcelWriter("codigos.xlsx")
                    data2.to_excel(writer3,"hoja1",index=False)
                    writer3.save()
                    data3=pd.read_excel('autos.xlsx')
                    data3.drop([h1],axis=0,inplace=True)
                    os.remove('autos.xlsx')
                    writer4=ExcelWriter('autos.xlsx')
                    data3.to_excel(writer4,"hoja1",index=False)
                    writer4.save()
                    compra=input("codigo del auto comprado")
                    print(datoscredito.datoscompletoscredito())
                else:#No dara pago inicial
                    g1=input('Dame el codigo del auto')
                    h1=int(input('Dame el indice del auto'))
                    data10=pd.read_excel('codigos.xlsx')
                    df=pd.DataFrame(data10,columns=[g1])
                    print(df)
                    costo=int(input('cuanto costo el auto'))
                    tiempo=int(input('a cuantos meses se pagara el auto'))
                    total=costo*(.35)
                    meses=total/tiempo
                    mesesfinal=round(meses)
                    print("se pagara",mesesfinal,"por",tiempo)
                    data2=pd.read_excel('codigos.xlsx')
                    datos={'PASE A PAGAR':['',"NOMBRE DEL CLIENTE:",nombre,df.loc[0],df.loc[1],'PASAR A PAGAR:',pagoinicial,'','GRACIAS POR LA COMPRA']}
                    dg=pd.DataFrame(datos)
                    dg=dg[["PASE A PAGAR"]]
                    writer2=ExcelWriter("Ticketcredito02.xlsx")
                    dg.to_excel(writer2,"hoja1",index=False)
                    writer2.save()
                    data2.drop([g1],axis=1,inplace=True)
                    os.remove('codigos.xlsx')
                    writer3=ExcelWriter("codigos.xlsx")
                    data2.to_excel(writer3,"hoja1",index=False)
                    writer3.save()
                    data3=pd.read_excel('autos.xlsx')
                    data3.drop([h1],axis=0,inplace=True)
                    os.remove('autos.xlsx')
                    writer4=ExcelWriter('autos.xlsx')
                    data3.to_excel(writer4,"hoja1",index=False)
                    writer4.save()
                    compra=input("codigo del auto comprado")
                    print(datoscredito.datoscompletoscredito())
            elif w==66 or w==98:#buenas referencias crediticias
                g1=input('Dame el codigo del auto')
                h1=int(input('Dame el indice del auto'))
                data10=pd.read_excel('codigos.xlsx')
                df=pd.DataFrame(data10,columns=[g1])
                print(df)
                costo=int(input('cuanto costo el auto'))
                print("\npor las referencias se debe de dar el 15% de pago inicial forzoso")
                pagoinicial=round(costo*(.15))
                print("el minimo de pago inicial es",pagoinicial)
                pagoinicial=int(input('Cuanto va a ser de pago inicial'))
                tiempo=int(input('a cuantos meses se pagara el auto'))
                subtotal=costo-pagoinicial
                subtotal2=subtotal*(.35)
                subtotalfinal=subtotal+subtotal2
                meses=subtotalfinal/tiempo
                mesesfinal=round(meses)
                print("se pagara",mesesfinal,"por",tiempo)
                data2=pd.read_excel('codigos.xlsx')
                datos={'PASE A PAGAR':['',"NOMBRE DEL CLIENTE:",nombre,df.loc[0],df.loc[1],'PASAR A PAGAR:',pagoinicial,'','GRACIAS POR LA COMPRA']}
                dg=pd.DataFrame(datos)
                dg=dg[["PASE A PAGAR"]]
                writer2=ExcelWriter("Ticketcredito03.xlsx")
                dg.to_excel(writer2,"hoja1",index=False)
                writer2.save()
                data2.drop([g1],axis=1,inplace=True)
                os.remove('codigos.xlsx')
                writer3=ExcelWriter("codigos.xlsx")
                data2.to_excel(writer3,"hoja1",index=False)
                writer3.save()
                data3=pd.read_excel('autos.xlsx')
                data3.drop([h1],axis=0,inplace=True)
                os.remove('autos.xlsx')
                writer4=ExcelWriter('autos.xlsx')
                data3.to_excel(writer4,"hoja1",index=False)
                writer4.save()
                compra=input("codigo del auto comprado")
                print(datoscredito.datoscompletoscredito())
            else:#malas referencias crediticias
                g1=input('Dame el codigo del auto')
                h1=int(input('Dame el indice del auto'))
                data10=pd.read_excel('codigos.xlsx')
                df=pd.DataFrame(data10,columns=[g1])
                print(df)
                costo=int(input('cuanto costo el auto'))
                print("\npor las referencias se debe de dar el 15% de pago inicial forzoso")
                pagoinicial=round(costo*(.30))
                print("el minimo de pago inicial es",pagoinicial)
                pagoinicial=int(input('Cuanto va a ser de pago inicial'))
                tiempo=int(input('a cuantos meses se pagara el auto'))
                subtotal=costo-pagoinicial
                subtotal2=subtotal*(.45)
                subtotalfinal=subtotal+subtotal2
                meses=subtotalfinal/tiempo
                mesesfinal=round(meses)
                print("se pagara",mesesfinal,"por",tiempo)
                data2=pd.read_excel('codigos.xlsx')
                datos={'PASE A PAGAR':['',"NOMBRE DEL CLIENTE:",nombre,df.loc[0],df.loc[1],'PASAR A PAGAR:',pagoinicial,'','GRACIAS POR LA COMPRA']}
                dg=pd.DataFrame(datos)
                dg=dg[["PASE A PAGAR"]]
                writer2=ExcelWriter("Ticketcredito04.xlsx")
                dg.to_excel(writer2,"hoja1",index=False)
                writer2.save()
                data2.drop([g1],axis=1,inplace=True)
                os.remove('codigos.xlsx')
                writer3=ExcelWriter("codigos.xlsx")
                data2.to_excel(writer3,"hoja1",index=False)
                writer3.save()
                data3=pd.read_excel('autos.xlsx')
                data3.drop([h1],axis=0,inplace=True)
                os.remove('autos.xlsx')
                writer4=ExcelWriter('autos.xlsx')
                data3.to_excel(writer4,"hoja1",index=False)
                writer4.save()
                compra=input("codigo del auto comprado")
                print(datoscredito.datoscompletoscredito())
