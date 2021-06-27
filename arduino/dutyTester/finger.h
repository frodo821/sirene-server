#ifndef __FINGER_H_INCLUDED
#define __FINGER_H_INCLUDED
#include <avr/pgmspace.h>
#ifndef USE_ALTO_RECODER_FINGER
const unsigned int FING_STEP[27][13] = {
  {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 187}, // 0 ド
  {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 187}, // 1 ド#
  {1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 187}, // 2 レ
  {1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 174}, // 3 レ#
  {1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 174}, // 4 ミ
  {1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 174}, // 5 ファ
  {1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 174}, // 6 ファ#
  {1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 172}, // 7 ソ
  {1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 172}, // 8 ソ#
  {1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 170}, // 9 ラ
  {1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 170}, //10 ラ#
  {1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 167}, //11 シ
  {1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 167}, //12 ド
  {0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 167}, //13 ド#
  {0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 165}, //14 レ
  {0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 167}, //15 レ#
  {1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 167}, //16 ミ
  {1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 165}, //17 ファ
  {1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 164}, //18 ファ#
  {1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 162}, //19 ソ
  {1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 160}, //20 ソ#
  {1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 160}, //21 ラ
  {1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 158}, //22 ラ#
  {1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 158}, //23 シ
  {1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 156}, //24 ド
  {1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 154}, //25 ド#
  {1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 152}  //26 レ
};
#else
const unsigned int FING_STEP[27][13] = {
  {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
  {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0},
  {1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0},
  {1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0},
  {1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0},
  {1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1},
  {1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0},
  {1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0},
  {1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0},
  {1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0},
  {1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0},
  {1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0},
  {1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0},
  {0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0},
  {0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0},
  {0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0},
  {1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0},
  {1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0},
  {1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0},
  {1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0},
  {1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0},
  {1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0},
  {1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0},
  {1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0},
  {1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0},
  {1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1},
  {1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0}
};
#endif
#endif
