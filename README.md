# long-siteswaps
Extend siteswaps you already know to make them even more fun!
For example, let's say you and your passing partner can run 6-club why-not (pass self pass heff zip) but want to make the pattern longer.
You are looking for a siteswap of the form [7,8,6,2,7,7,8,6,2,7,?,?,?,?]. This project will help you find siteswaps of this form!
I call the [?, ?, ?, ?] at the end a "block" which can be used to extend why not.

## finding blocks
In the `genertor.py` file there is code which will help you find blocks to extend why-not with (or any other siteswap).
You will need to specify how long you want the blocks to be and which throws the blocks can contain.
One possible block is [7, 7, 8, 2]. This means [7,8,6,2,7,7,8,6,2,7,7,7, 8, 2] is a valid pattern.
The two locals are pass self pass heff zip pass heff and heff zip pass self pass pass zip. I.e. the two jugglers are now juggling a period 7, but the first 5 throws are why-not, which they already know!.
Once they have mastered the period 7 then they can add another block and learn a period 9 (which they already know the first 7 throws of).

## FAQS
**why are you starting with why-not as a period 10 rather than a period 5?**

Good question. Let's extend why-not as a period 5. [7, 8, 6, 2, 7, 5, 7] is a period 7 with why-not as the first five throws of the **global**.
But why about the locals? Juggler A is doing pass self pass pass heff zip zap! The five throws of why-not are no longer next to each other!
Writing out two rounds of why-not guarantees that the two jugglers still have the why-not sequence of five throws in their local.

## theory
If you like theory then here are some thoughts: A valid siteswap is a path in a state diagram which starts and finishes in the same state.
The 4-long blocks for why-not are then just paths of length 4 which start and finish in why-not's state. Some blocks will be prime and some won't.
There will be a finite number of prime blocks from which all other blocks are composed. 