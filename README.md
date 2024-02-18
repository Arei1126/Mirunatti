# Mirunatti
Digital pet living in your smartphone case, Screen Time Reducer made of microbit.

![miruatti_ss](https://github.com/Arei1126/Mirunatti/assets/103196861/4cf92760-fdbe-4db8-a461-37a2062e0fcb)

## Description
- Mirunatti is mini electronic pet inside your smartphone case.
- Mirunatti is too shy to been watched, so you might not watch it (and your phone) too much or it will die. 

## How to play
1. Don't watch Mirunatti.
1. Watching Mirunatti more than 15 mininute at once makes Mirunatti die.
1. More thant 30 min for 60 min, or more than 1h 30 min for 8h does too.
1. <b>So, you have to close this case if you want Mirunatti to live longer. Turn off your smartphone and </b>

## Operation
- Press a, you can check Mirunatti's emotion.
- Press b, you can check Mirunatti's survival time 
- Press both a and b, reset.
- Press both a, b and lid swith, load status
- Auto save in 10 miniute

## Growth (good condition|bad condition)
- Left side faces are good conditions and others are bad one. 
- If your Mitrunatti stay bad condition, it means Mirunatti will die whithin 5 min if you continue to use your smartphone.

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

