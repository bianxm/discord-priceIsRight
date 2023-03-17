from amazon import AmazonInfo
import discord
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# global variables
is_round_running = False
challenger = ''
listing = ''
listPrice = ''
guesses = {} #price: [list of guessers]

# def getClosest(guesses, listPrice):

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    global is_round_running
    global challenger
    global listing
    global listPrice
    global guesses

    if message.author == client.user:
        return

    # get message tokens
    startToken, *tokens = message.content.split() 

    if startToken == '$pir' or client.user.mentioned_in(message):
        if not is_round_running:
            if not tokens:
                await message.channel.send(f"""Welcome to Discord The Price is Right, featuring Amazon!
            Start a round, or $pir help""")
                return
            
            if tokens[0] == 'start':
                listing = AmazonInfo(tokens[1])
                listPrice = listing.get_price()
                is_round_running = True
                challenger = message.author
                messageToSend = f"Round starts!"
                messageToSend += f"\n{challenger.mention} is the quizmaster for this round"
                # print(listing.soup)
                await message.channel.send(messageToSend) # see who challenger is and save and mention
                return
            
            if tokens[0] == 'test':
                listing = AmazonInfo('https://www.york.ac.uk/teaching/cws/wws/webpage1.html')
                listPrice = tokens[1]
                is_round_running = True
                challenger = message.author
                messageToSend = f"Round starts!"
                messageToSend += f"\n{challenger.mention} is the quizmaster for this round"
                await message.channel.send(messageToSend) # see who challenger is and save and mention
                return

        
        if is_round_running:
            # round playing logic 
            if tokens[0] == 'start':
                await message.channel.send("Sorry, a round is already running!")
                return
            
            if message.author == challenger:
                if tokens[0] == 'listName':
                    await message.channel.send(listing.get_title())
                    return
                
                if tokens[0] == 'listImg':
                    await message.channel.send(listing.get_img())
                    return
                
                if tokens[0] == 'listFeatures':
                    messageToSend = '\n\n'.join(['   - '+i for i in listing.get_features() if i is not None])
                    await message.channel.send(messageToSend)
                    return
                
                if tokens[0] == 'reveal':
                    await message.channel.send(listPrice)
                    return
                    # reveal price

                if tokens[0] == 'endRound':
                    # get current winner and announce!!
                    winners = guesses[min(guesses.keys())]
                    messageToSend = f"The price listed on Amazon is **{listPrice}**"
                    messageToSend += f"\n\n{' '.join([winner.mention for winner in winners])}"
                    messageToSend += f"\nCongrats! You guys won <3"
                    messageToSend += f"\n\n Ending round now"
                    is_round_running = False
                    guesses = {}
                    await message.channel.send(messageToSend)
                    return
                    # reveal price
                    # reset global variables
            # else:
                if tokens[0] == 'guess':
                    difference = abs(float(tokens[1]) - float(listPrice[1:]))
                    guesses[difference] = guesses.get(difference,[]) + [message.author]
                    print(guesses)
                    return
                    
    

client.run(os.environ['DISCORD_TOKEN'])