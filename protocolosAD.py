protocolo=input("Ingrese el nombre del protocolo en mayúscula: ")
OSPF=110
EIGRP=90
BGP=20
if protocolo=="OSPF":
    print("La distancia administrativa de OSPF es: "+ str(OSPF))
elif protocolo=="EIGRP":
    print("La distancia administrativa de EIGRP es: "+ str(EIGRP))
elif protocolo=="BGP":
    print("La distancia administrativa de BGP es: "+ str(BGP))
else:
    print("Opción Inválida.")