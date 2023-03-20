# DISCORD BOT: Price is Right, powered by Amazon
Play Price is Right on Discord!

This bot will _eventually_ use Beautiful Soup to scrape product information from a given Amazon product page, and use that to play Price is Right, once I find a way to more consistently fool Amazon's anti-bot measures... But in the meantime!

The bot allows you to have a game of multiple rounds of guessing. To start a round, the quizmaster gives the bot a number for everyone else to guess. Everyone then submits their guesses, and whoever is closest wins the round (yeah, not quite actual Price is Right rules). You can do this for as many rounds as you like! Once you tell the bot to end the game, it will announce the overall winners.
## How to play
Start your message with ```$pir``` or mention/ @ the bot to call it, then continue with the following commands:
|Command|What it does|
|---|---|
| ```help```|Display available commands|
|```testGame```|Start a game!|
|```testRound <number>```|Start a round, with the given number as the 'secret' number to be guessed. (Mainly for testing purposes. To keep your secret number secret, use ```startRound``` instead!)|
|```startRound```|Start a round. The bot will DM the user who gave this command to ask for a secret number for the others to guess.|
|```guess <number>```|Saves that number as your guess. (For now, everyone can guess, but in the future, the quizmaster for that round will not be able to guess. TODO)|
|```endRound```|End the round, and display who guessed the closest|
|```endGame```|End the game, and display who won the most rounds|
<!-- <pre>
* '... start [Amazon url]': Start a round. The sender of this message will be the quizmaster, and won't be allowed to submit a guess. 
* '... test [a number]': Start a round with the price to be guessed set as the given number. For testing purposes
</pre>
The quizmaster can do the following: 
<pre>
* '... listName'    : See the Amazon listing title
* '... listImg'     : See the Amazon listing featured image
* '... listFeatures': See the Amazon listing features in a list... Sometimes junk entries come through, just ignore those >.<
</pre>
The players (and, temporarily, the quizmaster) can do the following:
<pre>
* '... guess [guess price]': Submit a guess. Please, numbers only for now. Don't put the $, we'll add handling for that later
</pre>
And everyone can:
<pre>
* '... help' : does not actually do anything yet, sorry
</pre> -->
## Run your own
1. Clone this repo and install everything in requirements.txt
2. Set up a new application with a bot on Discord Developer 
3. Add your bot to your desired server, giving it 'Send Messages' permissions
4. Create a file .env in the project's root directory:
```bash
DISCORD_TOKEN=<your token here, as a string>
```
5. Run 'bot.py'
## To-do
* Amazon scraper improvements
    * Add more measures to fool Amazon bot detection
    * Handle case when Amazon catches the bot
    * Other link error handling
    * (Add support for Amazon book listings (they're formatted differently so the existing scraper won't work, sadly))
* Refactor the bot to use discord.py's bot extension 
* Error handling
    * endRound when there hasn't been any guesses yet
    * given not numbers when I'm expecting numbers