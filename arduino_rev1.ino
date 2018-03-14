

/*Arduino code for the 2017/18 Lunabot. Takes input
  from the RasPi serial commands and converts to actions.
  Makes use of Servo Library.
  
  Created by Alfred Odierno 3/13/18
 */


include <Servo.h>

//------------------------- Actions ----------------------------------------
// Change the Hex to match the controller actions (buttons etc..)
#define LEFT_FWD x##
#define LEFT_REV x##
#define RIGHT_FWD x##
#define RIGHT_REV x##
#define FRAME_UP x##
#define FRAME_DOWN x##
#define CBELT_ON x##
#define CBELT_REV x##
#define AUG_ON x##
#define AUG_REV x##
#define AUG_UP x##
#define AUG_DOWN x##
#define AUTO_MINE x##
#define E_STOP x##

//------------------------------Pins---------------------------------
//Motors
#define LDRIVE_PIN #
#define RDRIVE_PIN #
#define LACT_PIN #
#define RACT_PIN #
#define CBELT_PIN #
#define AUGPWR_PIN #
#define AUGDIR_PIN #
#define LBSCR_PIN #
#define RBSCR_PIN #
#define BSDIR_PIN #

//Limit Switches     I hope we have have enough pins left for these. 
#define A_up #
#define A_down #
             //In reality, I don't think we'll need these...
#define F_up #
#define F_down #


//-----------------------Servos-----------------
//Defining the VEX Motor controllers as Servos
Servo Ldrive;
Servo Rdrive;
Servo Lact;
Servo Ract;
Servo Cbelt;

//-------------------------MISC---------------------------------------
// The numbers are based on servo angles 0'-180'. For our case, 90' is null. Some buffer is given on either side.  
#define POS 170 //FULL Forward
#define NULL 90 //STOP on VICTOR this number may have to be calibrated...
#define NEG 10 //FULL Reverse
#define P_MOD 160 //Allows matching of actuator speeds.
#define N_MOD 20 
#define OFF LOW
#define ON HIGH
#define wait 500


void setup( )
{
  //Initialize Ldrive
  Ldrive.attach(LDRIVE_PIN);
  Ldrive.write(NULL);
    
  //Initialize Rdrive
  Rdrive.attach(RDRIVE_PIN);
  Rdrive.write(NULL);
  
  //Initialize Lact;
  Lact.attach(LACT_PIN);
  Lact.write(NULL);
  
  //Initialize Ract;
  Ract.attach(RACT_PIN);
  Ract.write(NULL);
  
  //Initialize Cbelt
  Cbelt.attach(CBELT_PIN);
  Cbelt.write(NULL);    
  
  //Initialize AugPwr
  pinMode(AUGPWR_PIN, OUTPUT);
  digitalWrite(AUGPWR_PIN, OFF);
  
   //Initialize AugDir
  pinMode(AUGDIR_PIN, OUTPUT);
  digitalWrite(AUGDIR_PIN, OFF);
  
  //Initialize Lbscr
  pinMode(LBSCR_PIN, OUTPUT);
  digitalWrite(LBSCR_PIN, OFF);
  
  //Initialize Rbscr
  pinMode(RBSCR_PIN, OUTPUT);
  digitalWrite(RBSCR_PIN, OFF);
  
  //Initialize BscrDir
  pinMode(BSDIR_PIN, OUTPUT);
  digitalWrite(BSDIR_PIN, OFF);
  
  Serial.begin( 9600 );
}


void loop( )
{
    if(Serial.available() > 0)
    {
        prevData = curData;
  //    Serial.print("prevData = ");
  //    Serial.println(prevData);
      
        curData = Serial.read();
//      Serial.print("Byte read. Now curData = ");
//      Serial.println(curData);
      
      //Commands start with the header 0xFF 0xEE at the moment
        if( prevData == 0xFF && curData == 0xEE )
        {
//        Serial.println( "VALID COMMAND Executing" );
        }
    }  
  }



//====================== readCommand( Serial ser )==============
//Read a command from the given Serial connection 

void readCommand( )
{
  byte action = Serial.read( );

  if( action == LEFT_FWD ) //See Actions section for assignments
  {
    Serial.println("Reading Action LEFT_FWD");
    Ldrive.write(POS);
    delay(wait);
    Ldrive.write(NULL);
  }
  
  if( action == RIGHT_FWD ) //See Actions section for assignments
  {
    Serial.println("Reading Action RIGHT_FWD");
    Rdrive.write(POS);
    delay(wait);
    Rdrive.write(NULL);    
  }
  
  if( action == LEFT_REV ) //See Actions section for assignments
  {
    Serial.println("Reading Action LEFT_REV");
    Ldrive.write(NEG);
    delay(wait);
    Ldrive.write(NULL);    
  }

  if( action == RIGHT_REV ) //See Actions section for assignments
  {
    Serial.println("Reading Action RIGHT_REV");
    Rdrive.write(NEG);
    delay(wait);
    Rdrive.write(NULL);    
  }  
  
  if( action == FRAME_UP ) //See Actions section for assignments
  {
    //while(digitalRead(F_up, LOW)){
    Serial.println("Reading Action FRAME_UP");
    Lact.write(POS);
    Ract.write(P_MOD); //One of the actual actuators moves at a slower rate, so PWM is modified to match speeeds.
    delay(wait);
    Lact.write(NULL);  
    Ract.write(NULL); 
  }
  
  if( action == FRAME_DOWN ) //See Actions section for assignments
  {
    //while(digitalRead(F_down, LOW)){
    Serial.println("Reading Action FRAME_DOWN");
    Lact.write(NEG);
    Ract.write(N_MOD); //One of the actual actuators moves at a slower rate, so PWM is modified to match speeeds.
    delay(wait);
    Lact.write(NULL);  
    Ract.write(NULL); 
  }
  
  if( action == CBELT_ON ) //See Actions section for assignments
  {
    Serial.println("Reading Action CBELT_ON");
    Cbelt.write(POS);
    delay(wait);
    Rdrive.write(NULL);    
  }  
  
  if( action == CBELT_OFF) //See Actions section for assignments
  {
    Serial.println("Reading Action CBELT_OFF");
    Cbelt.write(NEG);
    delay(wait);
    Rdrive.write(NULL);    
  }  
  
  if( action == AUG_ON ) //See Actions section for assignments
  {
    Serial.println("Reading Action AUG_ON");
    digitalWrite(AUGPWR_PIN, ON);
    delay(wait);
    digitalWrite(AUGPWR_PIN, OFF); 
  }
  
  if( action == AUG_REV ) //See Actions section for assignments
  {
    Serial.println("Reading Action AUG_REV");
    digitalWrite(AUGPWR_PIN, ON);
    digitalWrite(AUGDIR_PIN, ON);
    delay(wait);
    digitalWrite(AUGPWR_PIN, OFF);
    digitalWrite(AUGDIR_PIN,OFF);
  }
  
  if( action == AUG_UP ) //See Actions section for assignments
  {
    Serial.println("Reading Action AUG_UP");
    //while(digitalRead(A_up, LOW)){
    digitalWrite(BSDIR_PIN, HIGH); // Enables the motor to move in a particular direction
    for(int x = 0; x < 200; x++)   // Makes 200 pulses for making one full cycle rotation
    {
      digitalWrite(LBSCR_PIN, HIGH); 
      digitalWrite(RBSCR_PIN, HIGH); //If on of the ballscrews turn at a slower rate it will need its own delay
      delayMicroseconds(500); 
      digitalWrite(LBSCR_PIN,LOW);
      digitalWrite(RBSCR_PIN, LOW);
      delayMicroseconds(500); 
    }
  }
    
  if( action == AUG_DOWN ) //See Actions section for assignments
  {
    Serial.println("Reading Action AUG_DOWN"); 
    //while(digitalRead(A_down, LOW)){
    digitalWrite(BSDIR_PIN, LOW); // Enables the motor to move in a particular direction
    for(int x = 0; x < 200; x++)   // Makes 200 pulses for making one full cycle rotation
    {
      digitalWrite(LBSCR_PIN, HIGH); 
      digitalWrite(RBSCR_PIN, HIGH); //If on of the ballscrews turn at a slower rate it will need its own delay
      delayMicroseconds(500); 
      digitalWrite(LBSCR_PIN,LOW);
      digitalWrite(RBSCR_PIN, LOW);
      delayMicroseconds(500); 
    }
  }  
  
/*if( action == AUTO_MINE ) //See Actions section for assignments
  {
    Serial.println("Reading Action AUTO_MINE"); 
*/}
  
  if( action == E_STOP ) //See Actions section for assignments
  {
    Serial.println("Reading Action E_STOP"); 
    Ldrive.write(NULL);
    Rdrive.write(NULL);
    Lact.write(NULL);
    Ract.write(NULL);
    Cbelt.write(NULL);    
    digitalWrite(AUGPWR_PIN, OFF);
    digitalWrite(AUGDIR_PIN, OFF);
    digitalWrite(LBSCR_PIN, OFF);
    digitalWrite(RBSCR_PIN, OFF);
    digitalWrite(BSDIR_PIN, OFF);
  }
}



