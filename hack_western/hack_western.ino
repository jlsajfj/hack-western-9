#include <Stepper.h>
#include <Filters.h>
#include <Filters/MedianFilter.hpp>

//motor variables
const int h_stepsPerRevolution = 1000;
const int v_stepsPerRevolution = 1000;
int h_dir = -1;
int v_dir = -1;

// initialize the vertical stepper library on pins 8 through 11:
Stepper hStepper(h_stepsPerRevolution, 8, 10, 9, 11);
// initialize the vertical stepper library on pins 4 through 7:
// Stepper vStepper(v_stepsPerRevolution, 4, 6, 5, 7);

int speed = 30;

const int threshold = 12; // distance sensor is to ground at an angle

// imaging variables 
const int echoPin_1 = 8; // attach pin D2 Arduino to pin Echo of HC-SR04
const int trigPin_1 = 9; //attach pin D3 Arduino to pin Trig of HC-SR04
const int echoPin_2 = 2;
const int trigPin_2 = 3;

void setup() {
  pinMode(trigPin_1, OUTPUT); // Sets the trigPin as an OUTPUT
  pinMode(echoPin_1, INPUT); // Sets the echoPin as an INPUT
  pinMode(trigPin_2, OUTPUT);
  pinMode(echoPin_2, INPUT);

  //hStepper.setSpeed(speed);
  //vStepper.setSpeed(speed);
  Serial.begin(9600); // // Serial Communication is starting with 9600 of baudrate speed

}

MedianFilter<10, uint16_t> medfilt_1 = {512};
MedianFilter<10, uint16_t> medfilt_2 = {512};

void loop() {
  int sensor1 = ultrasonic(trigPin_1, echoPin_1, medfilt_1);
  int sensor2 = ultrasonic(trigPin_2, echoPin_2, medfilt_2);

  if(sensor1 <= threshold) {
    Serial.write(1);
  }
  if(sensor2 <= threshold) {
    Serial.write(2);
  }

  Serial.print(sensor1);
  Serial.print(" ");
  Serial.println(sensor2);
  
  //hStepper.step(h_dir*h_stepsPerRevolution);
}

int ultrasonic(int trigpin, int echopin, MedianFilter<10, uint16_t> &filt) {
  digitalWrite(trigpin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin HIGH (ACTIVE) for 10 microseconds
  digitalWrite(trigpin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigpin, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  long duration = pulseIn(echopin, HIGH);
  // Calculating the distance
  int distance = duration * 0.034 / 2; // Speed of sound wave divided by 2 (go and back)
  return filt(distance);
}
