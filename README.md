# DISCORD BOT: Price is Right, powered by Amazon
Play Price is Right on Discord!
This bot uses Beautiful Soup to scrape product information from a given Amazon product page, and use that to play Price is Right.
We don't quite follow Price is Right rules -- whoever guesses closest, wins. Though admittedly functionality to submit guesses and get the winner hasn't been implemented yet... But the web scraping works!
## What it does
Start your message with $pir or @<the bot> to call it, continued with the following commands:
<pre>
* '... start [Amazon url]': Start a round. The sender of this message will be the quizmaster, and won't be allowed to submit a guess. 
</pre>
The quizmaster can do the following: 
<pre>
* '... listName'    : See the Amazon listing title
* '... listImg'     : See the Amazon listing featured image
* '... listFeatures': See the Amazon listing features in a list... Sometimes junk entries come through, just ignore those >.<
</pre>
The players can do the following:
<pre>
* '... guess [guess price]': Submit a guess. Please, numbers only for now. Don't put the $, we'll add handling for that later
</pre>
And everyone can:
<pre>
* '... help' : does not actually do anything yet, sorry
</pre>
## Run your own
1. Clone this repo and install everything in requirements.txt
2. Set up a new application with a bot on Discord Developer 
3. Add your bot to your desired server, giving it 'Send Messages' permissions
4. Create a file .env in the project's root directory:
<pre>
DISCORD_TOKEN=<your token here, as a string>
</pre>
5. Run 'bot.py'
## To-do
* Put Game in a separate class
    * Track scores across multiple rounds
    * (Add currency conversion for guesses)
    * Each Discord server has own instance of Game
* Amazon scraper improvements
    * Add more measures to fool Amazon bot detection
    * Handle case when Amazon catches the bot
    * Other link error handling
    * (Add support for Amazon book listings (they're formatted differently so the existing scraper won't work, sadly))
* Fix the async logic to follow whatever best practices I'm not aware of yet