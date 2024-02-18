# Mirunatti
Digital ped living in your smartphone case, Reducing Screen Timer for microbit
![IMG_20240218_190226](https://github.com/Arei1126/Mirunatti/assets/103196861/30062c94-e934-4931-a7ba-5ccf3c947249)

## Description
Mirunatti is mini electronic pet　inside your smartphone case. Mirunatti is too shy to been watched, so you might not watch it (and your phone) too much or it will die. 

## How to play
1. Don't watch Mirunatti.
1. Watching Mirunatti more than 15 mininute at once makes it die.
1. more thant 30 min for 60 min, or more than 1h 30 min for 8h does too.

## Operation
- Press a, you can check Mirunatti's emotion.
- Press b, you can check Mirunatti's survival time 
- Press both a and b, reset.
- Press both a, b and lid swith, load status
- Auto save in 10 miniute

## Growth (good condition|bad condition)
Egg: 0 ~ 30min after birth
<pre>
@@@  |  @
@ @  | @ @
@@@  | @@
</pre>

Child: 30min ~ 4h after birth
<pre>
 @ @  |  @ @
      |  
 @ @  |   @
  @   |  @ @
</pre>
Adult: 4h ~ after birth
<pre>
  @  @  |  @  @
        |  
  @  @  |   @@
   @@   |  @  @
</pre>

Death: exceeded limit
<pre>
  @  
 @@@
  @
@@@@@
</pre>
## Hardware
- microbit v1~
- smartphone case holding microbit and lid switch
- pin 0 pulled down, conneted to lid switch (normal open),
- When case is opened, lid switch is pushed, thus the circuit will close and pin 0 will UP.

