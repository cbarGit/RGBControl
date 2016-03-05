int colorRGB[3];
int redPin = 11;
int greenPin = 10;
int bluePin = 9;

int delayVal = 50;
int blnFade = 0;
int h_int;
float h;
int r=0, g=0, b=0;

void h2rgb(float h, int &R, int &G, int &B);
void colorFade();

void setup() {
 
 Serial.begin(57600); 
 pinMode(redPin, OUTPUT);
 pinMode(greenPin, OUTPUT);
 pinMode(bluePin, OUTPUT);

}

void loop() {
 
 if(Serial.available() >= 2){
   
   switch( byte( Serial.read() )) {
     case 'r':
       colorRGB[0] = Serial.read();
       blnFade = 0;
       break;
     case 'g':
       colorRGB[1] = Serial.read();
       blnFade = 0;
       break;   
     case 'b':
       colorRGB[2] = Serial.read();
       blnFade = 0;
       break;
     case 'c':
       Serial.flush();
       blnFade = 0;
       break;
     case 'f':
       delayVal = Serial.read();
       Serial.flush();
       colorFade();
       blnFade = 1;
     }
  }
  analogWrite(redPin, colorRGB[0]); 
  analogWrite(greenPin, colorRGB[1]);
  analogWrite(bluePin, colorRGB[2]);
  delay(20);
}

void colorFade() {

while (blnFade == 1) {
if(Serial.available() ){
  blnFade = 0;
  break; 
}   
for(int fadeValue = 0 ; fadeValue <= 1024; fadeValue +=5) {
   h = ((float)fadeValue)/1024;
   h_int = (int) 360*h;
   h2rgb(h,r,g,b);
   if(Serial.available() ){
     blnFade = 0;
     break; 
   } 
   analogWrite(redPin, r);
   analogWrite(greenPin, g);
   analogWrite(bluePin, b);
   delay(delayVal);
 }
}
}

void h2rgb(float H, int& R, int& G, int& B) {
 int var_i;
 float S=1, V=1, var_1, var_2, var_3, var_h, var_r, var_g, var_b;
 if ( S == 0 ) {
   R = V * 255;
   G = V * 255;
   B = V * 255;
 } else {
   var_h = H * 6;
   if ( var_h == 6 ) var_h = 0;
   var_i = int( var_h ) ;
   var_1 = V * ( 1 - S );
   var_2 = V * ( 1 - S * ( var_h - var_i ) );
   var_3 = V * ( 1 - S * ( 1 - ( var_h - var_i ) ) );

   if ( var_i == 0 ) {
     var_r = V     ;
     var_g = var_3 ;
     var_b = var_1 ;
   } else if ( var_i == 1 ) {
     var_r = var_2 ;
     var_g = V     ;
     var_b = var_1 ;
   } else if ( var_i == 2 ) {
     var_r = var_1 ;
     var_g = V     ;
     var_b = var_3 ;
   } else if ( var_i == 3 ) {
     var_r = var_1 ;
     var_g = var_2 ;
     var_b = V     ;
   } else if ( var_i == 4 ) {
     var_r = var_3 ;
     var_g = var_1 ;
     var_b = V     ;
   } else {
     var_r = V     ;
     var_g = var_1 ;
     var_b = var_2 ;
   }
   R = (1-var_r) * 255;
   G = (1-var_g) * 255;
   B = (1-var_b) * 255;
 }
}
