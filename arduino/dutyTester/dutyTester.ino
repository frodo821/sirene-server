#include <math.h>
#define _USE_ALTO_RECODER_FINGER
#include "finger.h"

int note = 0;

void setup() {
  TCCR2B &= B11111000;
  TCCR2B |= B00000010;
  Serial.begin(9600);
  Serial.setTimeout(2000u);
  for (int i = 2; i < 14; i++)
  {
    if(i==3)
      continue;
    pinMode(i, OUTPUT);
  }
  analogWrite(3, 255);
}

void loop() {
  int val = 0;
  String str = Serial.readStringUntil('.');
  if (str.length() < 2)
    return;
  if (!isNumber(str)) {
    note++;
    if (note > 26)
      note = 0;
    Play(note);
    val = 255 - atoi(str.c_str());
    Serial.print("Air current: ");
    Serial.println(val);
    Serial.print("Note id: ");
    Serial.println(note);
    return;
  }
  Play(note);
  val = 255 - atoi(str.c_str());
  Serial.print("Air current: ");
  Serial.println(val);
  Serial.print("Note id: ");
  Serial.println(note);
  if (0 > val and 255 < val)
    return;
  analogWrite(3, val);
}

bool isNumber(String str)
{
  if (0 >= str.length())
    return false;
  int len = str.length();
  for (int i = 0; i < str.length(); i++)
  {
    if (isSpace(str.charAt(i)))
    {
      len--;
      continue;
    }
    if (!isDigit(str.charAt(i)))
      return false;
  }
  return 0 < len;
}

void Play(short num)
{
  for (short i = 0; i < 12; i++)
  {
    if(i==0) {
      digitalWrite(2, FING_STEP[num][i]);
      continue;
    }
    digitalWrite(i + 3, FING_STEP[num][i]);
#if DEBUG
    Serial.print(FING_STEP[num][i]);
  }
  Serial.print("\n");
#else
  }
#endif
}
