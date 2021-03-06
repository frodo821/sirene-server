/**
 * ピン3-13を使用中
 * 
 * ピン3は空気量の調節用ピン(PWM)です。
 * ピン4-13は指制御です。
 * ピン2はサミング制御です。
 */

#include <math.h>
#define _USE_ALTO_RECODER_FINGER
#include "finger.h"
// typedef unsigned long long size_t;

#define CMD_GET_SIGNATURE 0
#define CMD_PLAY_NOTE 1

static inline void play(char note)
{
  switch (note)
  {
  case 0:
  case 1:
  case 2:
  case 3:
  case 4:
  case 5:
  case 6:
  case 7:
  case 8:
  case 9:
  case 10:
  case 11:
  case 12:
  case 13:
  case 14:
  case 15:
  case 16:
  case 17:
  case 18:
  case 19:
  case 20:
  case 21:
  case 22:
  case 23:
  case 24:
  case 25:
  case 26:

    analogWrite(3, GET_FINGER(note, 11));
    for (short i = 0; i < 11; i++)
    {
      if (i == 0)
      {
        digitalWrite(2, GET_FINGER(note, 0));
      }
      else
      {
        digitalWrite(i + 3, GET_FINGER(note, i));
      }
    }
    break;

  case 27:
    analogWrite(3, 255);
    break;

  case 28:
    for (short i = 0; i < 14; i++)
    {
      if (i == 0)
      {
        digitalWrite(2, 0);
        continue;
      }
      digitalWrite(i + 3, 0);
    }
    analogWrite(3, 255);
    break;

  default:
    break;
  }
}

void setup()
{
  TCCR2B &= B11111000;
  TCCR2B |= B00000010;
  Serial.begin(19200);
  Serial.setTimeout(600000UL);
  for (int i = 2; i < 14; i++)
  {
    if (i == 3)
      continue;
    pinMode(i, OUTPUT);
  }
  analogWrite(3, 255);
}

void loop()
{
  uint8_t buffer[2];
  if (Serial.available() < 2)
    return;
  size_t read_len = Serial.readBytes(buffer, 2);

  if (read_len != 2)
  {
    return;
  }

  switch (buffer[0])
  {
  case CMD_GET_SIGNATURE:
    Serial.write(SIRENE_TYPE_SIGNATURE);
    return;

  case CMD_PLAY_NOTE:
    play(buffer[1]);
    return;

  default:
    return;
  }
}
