#include <math.h>
#define _USE_ALTO_RECODER_FINGER
#include "finger.h"
#define DEBUG 1
/**
 * ピン3-13を使用中
 * 
 * ピン3は空気量の調節用ピン(PWM)です。
 * ピン5-13は通常指制御です。
 * ピン2はサミング制御で、ピン4はサミングによってできる隙間の制御です。
 * 00→○,10→⌀,11→●
 */

void setup()
{
  TCCR2B &= B11111000;
  TCCR2B |= B00000010;
  Serial.begin(9600);
  Serial.setTimeout(600000UL);
  for(int i = 2; i < 14; i++)
  {
    if(i==3)
      continue;
    pinMode(i , OUTPUT);
  }
  analogWrite(3, 255);
}

void loop()
{
  char buf[3];
  String readed = Serial.readStringUntil('.');
  if(!isNumber(readed))
  {
#ifdef DEBUG
    Serial.print("'");
    Serial.print(readed.c_str());
    Serial.println("' is not a valid number.");
#endif
    return;
  }
  int val = atoi(readed.c_str());
  if(0 <= val && val <= 26)
  {
    Play(val);
  } else if(val == 28) {
    for(short i = 0; i < 14; i++) {
      if(i==0) {
        digitalWrite(2, 0);
        continue;
      }
      digitalWrite(i+3, 0);
    }
    analogWrite(3, 255);
  } else if(val == 27) {
    analogWrite(3, 255);
  }
}

void Play(short num)
{
  analogWrite(3, FING_STEP[num][11]);
  //Serial.println(FING_STEP[num][11]);
  for(short i = 0; i < 11; i++)
  {
    if(i==0) {
      digitalWrite(2, FING_STEP[num][0]);
    } else {
      digitalWrite(i+3, FING_STEP[num][i]);
    }
#if DEBUG
    Serial.print(FING_STEP[num][i], DEC);
    Serial.print(" ");
  }
  Serial.print("\n");
#else
  }
#endif
}

bool isNumber(String str)
{
  int len = str.length();
  if(0 >= len)
    return false;
  int nlen = len;
  for(int i = 0; i < nlen; i++)
  {
    if(isSpace(str.charAt(i)))
    {
      len--;
      continue;
    }
    if(!isDigit(str.charAt(i)))
      return false;
  }
  return 0 < len;
}
