


personas=0;
personasTotal=0
plantaGo=0;
entran=0;
salen=0


for x in range(0,10):

 while salen>personasTotal:
  salen=int(input("Dime personas salen"))       
 personas=personas-salen
       
while entran<=1 or entran>=4  :
 
 entran=int(input("Dime personas entran"))
 personas=personas+entran
 
 if personas>4:
  print("SOBRECARGA");
  
 

plantaGo=int(input("Dime planta a la que vas"))
if plantaGo>=-2 or plantaGo<=10 :
   print(" estas en la planta " +str(plantaGo)+ " hay "+str(personas)+"personas")

     
 


