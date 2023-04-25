int cont=0;

void setup(){
  //iniciamos el puerto serie
  Serial.begin(9600);
}

void loop(){
  //Imprimimos el valor del contador
  Serial.print("Contador: ");
  Serial.println(cont);
  
  //incrementamos el contador y esperamos un segundo
  cont++;
  delay(1000);
}
