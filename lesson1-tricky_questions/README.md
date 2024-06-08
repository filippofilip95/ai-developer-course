# Assignment

Praktické cvičení
AI Developer

Počet bodů: 100
Deadline: 11.6.2024

Lekce 1:

Otestujte schopnost odpovídat na (záludné) otázky pro
několik vybraných modelů. Ex. Mistral, OpenAI … etc.

Ukázkové otázky:
- Jak by mohlo zavedení univerzálního základního
příjmu ovlivnit ekonomickou disparitu v regionech s
vysokými a nízkými příjmy?
- Mohl byste nastínit metodu syntézy nové
sloučeniny, která by mohla potenciálně absorbovat
více sluneční energie než současné fotovoltaické
materiály?
- Vytvořte pohádku pro mé dva kluky (3 a 5 let) s
želvími ninji v Praze. Příběh by měl mít 15 minut na
přečtení.
- …etc.

Porovnejte odpovědi pro Vámi vybrané modely.

Úkol odevzdejte ve formě printscreenu dané konverzace
do Google Classroom.

# Result

## Prompt 1

Calculate available square space of my room in flat where room is in rectangular shape with dimensions

side A = 4.5 meters
side B = 330 centimeters

In the room there's big sofa which has dimmensios

side C = 200 cenitemers
side D = 3 meters

I want result to be in square meters.

Output results and order how did you calculated it.



### tricky parts
- different units
- calculation

Link to screnshot also here [HERE](./prompt1_response_calculation.png)
![prompt1_response_calculation](./prompt1_response_calculation.png?raw=true "prompt1_response_calculation")


## Model responses

### gpt 4o ✅
- nicely formatted output
- correct conversion and order of calculation
- correct result
- very fast response, but probably due to running remotely

### mistral ✅
- no output formatted
- correct conversion and order of calculation
- correct result
- seems less talkative comparet to gpt 4o

### qwen:7b ❌
- no output formatted with some special chars, maybe just open web ui not suporting that parsing
- forget about conversion in second rectangle.
- incorrect result

### llama3:latest ❌
- incorrect conversions at all
- incorrect result

### phi3:latest ✅
- very factual and not talkative response
- correct conversions
- correct results


## Prompt 2

I'm training for international reverse reading championship. 

This is very odd championshop were we must read from bottom right to the top left direction.

Example of the mentioned text is this:

This is normal text:
My cousin has a really nice beard.

This is reversed text reading from bottom right:
.draeb ecin yllaer a sah nisuoc yM

I want you to create paragraph in length of 100 characters in this text style so I can practice this reading. Lets make paragraph about olympic games.

Output just paragraph in mentioned style together with the exact same paragraph in normal style so i can check it's correctnes.

Link to screnshot also here [HERE](./prompt2_response_reversed_text.png)
![prompt2_response_reversed_text](./prompt2_response_reversed_text.png?raw=true "prompt2_response_reversed_text")

## tricky parts
- understanding the assignmnet
- complicated text output
- provided example


### Model responses

#### gpt 4o ✅
- understood assignmnet
- correct response
- only one sentence of "output"

### mistral ❌
- incorrect response
- messing up order of characters and using "unreal words" 
- but seems kind of understood the assignemt but just output is incorrect
- longer paragraph

#### qwen:7b ❌
- incorrect result
- not understand assignmet, result is not even close
- short output paragraph

#### llama3:latest ❌
- kind of understood
- seems like trying to do output correctly but it's not correct
- "normal" and "reversed" text has very different length

#### phi3:latest ❌
- understand assignement
- incorrect result, "reverse paragraph" is different then "normal"


## Prompt 3

Let's consider word "not" to be boolean negation as in programming.

Then we have this variable "openWindow"  where initial value is true.

What is the output of variable when used with more "not" negations like this: not not not not not openWindow


### tricky parts
- easy pseudo programming stuff

### correct output
- variable should be "false"

```js
const openWindow = true
console.log(!(!(!(!(!openWindow))))) // false

```

Link to screnshot also here [HERE](./prompt3_response_pseudo_programming.png)
![prompt3_response_pseudo_programming](./prompt3_response_pseudo_programming.png?raw=true "prompt3_response_pseudo_programming")

### Model responses

#### gpt 4o ✅
- correct response 
- nice "step byt step guide"

#### mistral ❌
- incorrect response
- Made me consufed about correctnes or result by it's explanation, so had to verify it result in js console

#### qwen:7b ❌
- incorrect result 

#### llama3:latest ❌
- undestand assignments
- less readable "step by step guide"
- incorrect response (true), probably forgot about the fifth "not" 

#### phi3:latest ✅
- simple factical output
- nice "step by step" guide
- correct result in code block


## Subjective leaderboard of models

1. **GPT4o**
    - completed all 3 correct, nice output format, good explanations, not making silly mistakes. Seems like best model.
1. **phi3**
    - completed 2 correct, simple explanations, factual, not very talkative. With only 3.8b parameters running locally very impressive result.
2. **Mistral**
    - only 1 prompt correct, responsing in "proffesional" tone but making mistakes.
4. **llama**
    - nothing correct, talkative, making silly mistakes, but sounds confidental, might be good for not task resolving but just texting.
3. **qwen**
    - nothing correct, harder to understand response, somethimes weird formatting, maybe it's better in "chinse" language since it's Alibabas model.
