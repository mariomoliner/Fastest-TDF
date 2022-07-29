# Was the 2022 TDF the best ever?

"C'est le tour de france" 

The goal of this article is to analyze wether the hardest multi-stage cycling race of the world was also this year the hardest in modern era. We are going to analyze hardness in regards to athletic performance. Ofcourse it would be interesting to compare it with older tour de france editions however the different technological advances and lack of statistical data make this not possible. Older tdf (tour de france) were usually harder in the pure meaning of the word:

*hard: with great exertion; with vigor or violence; strenuously*

Nevertheless in this article we will focus in the sense of hardness from a purely athletic point of view. 



![images](./img/tour2022_image.jfif)


## What is hardness in cycling?

Concretely in a multistage race such as the tour de france we usually understand hardness as the concatenation of hard stages, a stage can be said that it was tough/hard when some of the following criteria apply:
1. The longer a stage is the harder it is
2. The more elevation gain the harder
3. Extreme weather conditions make for a harder stage, whether cold or hot, around 20 degrees is perfect for cycling practice
4. The faster a stage it has been the harder it was
5. The more crosswind/headwind the harder, on the other hand tailwind makes it easier
6. The higher altitude the harder it is to ride a bike because of the lack of oxygen

## Criterias we are going to follow

Given the nature of the tour de france, ie. a 20 day stage race. We are going to focus in the criteria 1, 2, 3, 4. As the grand Boucle is several days long the rest of the criteria may be considered not as important and additionally they are much harder to quantify and to get reliable data of them.



## Comparison

We have collected data of the tdf since the year 2015, for earlier editions data was lacking, especially climbing perfomances. It would be interestin how the numbers compare to the ones of the EPO era. 

![images](./img/general_stats.PNG)

We plot the VAMS of the different climbs of the last 3 years. VAM stands for "velocità ascensionale media", translated in English means "average ascent speed". The term was coined by Italian physician and cycling coach Michele Ferrari, is the speed of elevation gain, usually stated in units of metres per hour and is very positively correlated with watts/kg a rider has to push in a climb.

![images](./img/cloud_VAMS.PNG)

We chose climbs of at least 5km as shorter tend have too high VAMS and depending the tdf edition it can vary considerably the amount of these kind of climbs

Finally we can plot the mean VAM of each tdf edition. That is a very good estimator of the climbing performance of a stage race like tour de france.

![images](./img/meanVAM.PNG)

## Putting all the ingredients together

We are going to define the the difficulty of a tour the france as a linear combination of the before mentioned metrics.

$TDF_{hardness} = \alpha \cdot normmean_{VAM} +  \beta \cdot norm_{distance} +  \gamma \cdot normmean_{Speed} + \delta \cdot normmean_{temp}$



we have chosen the following values:

 * (1) $\alpha = 0.45, \beta = 0.02, \gamma = 0.45, \delta = 0.08$
 * (2) $\alpha = 0.6, \beta = 0.02, \gamma = 0.3, \delta = 0.08$
 * (3) $\alpha = 0.3, \beta = 0.02, \gamma = 0.6, \delta = 0.08$
 
A little comment on each formula, in (1) we equate the weight of the mean VAM and distance. On the second we give more weight to the VAM whereas in the third the other way around. The scalar factor of the distance is fairly small as it is usually quite steady and we don't believe is of much importance. The temperature in contrast is a litle higher.

Also, as seen in the formula we take each metric normalized, that is divide by its mean. This way if $TDF_{hardness} = 1$ it would mean it was a pretty average tour de france version, the higher the better or harder it was racen.

### Results

The results after applying the formulas to the different editions is the following;

![images](./img/difficulties.PNG)


## Conclusions

As we see from the results, the 2022 tour de france looks like clearly is the hardest or best in terms in performance we have seen, at least in the last 7 years. It was ridden the fastest ever in history and also its mean VAM its the highest in the recent times. Good times to be a cycling fan

Author: mario.moliner@gmail.com
