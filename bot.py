# from amazon import AmazonInfo
import discord
import os
from dotenv import load_dotenv
from game import Game, Round

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

currGame = None

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    global currGame

    if message.author == client.user:
        return

    # get message tokens
    startToken, *tokens = message.content.split() 

    if startToken == '$pir' or client.user.mentioned_in(message):
        if not currGame:
            if not tokens:
                messageToSend = "Welcome to Discord The Price is Right, featuring Amazon!"
                messageToSend += "\nStart a round, or $pir help"
                await message.channel.send(messageToSend)
                return
            
            #if tokens[0] == 'start':
                #listing = AmazonInfo(tokens[1])
                #listPrice = listing.get_price()
                #is_round_running = True
                #challenger = message.author
                #messageToSend = f"Round starts!"
                #messageToSend += f"\n{challenger.mention} is the quizmaster for this round"
                ## print(listing.soup)
                #await message.channel.send(messageToSend) # see who challenger is and save and mention
                #return
            
            if tokens[0] == 'testGame':
                #listing = AmazonInfo('https://www.york.ac.uk/teaching/cws/wws/webpage1.html')
                #listPrice = tokens[1]
                #is_round_running = True
                #challenger = message.author
                currGame = Game()
                messageToSend = f"Game starts!"
                await message.channel.send(messageToSend)
                return
            
        if currGame:
            if currGame.round:
                if tokens[0] == 'endGame' or tokens[0] == 'testRound':
                    messageToSend = f"Sorry, there is a round running! '$pir endRound' first!"
                    await message.channel.send(messageToSend)
                    return

                if tokens[0] == 'start':
                    await message.channel.send("Sorry, a round is already running!")
                    return
                
                #if message.author == currGame.round.challenger:
                    #if tokens[0] == 'listName':
                        #await message.channel.send(listing.get_title())
                        #return
                    
                    #if tokens[0] == 'listImg':
                        #await message.channel.send(listing.get_img())
                        #return
                    
                    #if tokens[0] == 'listFeatures':
                        #messageToSend = '\n\n'.join(['   - '+i for i in listing.get_features() if i is not None])
                        #await message.channel.send(messageToSend)
                        #return
                    
                    #if tokens[0] == 'reveal':
                        #await message.channel.send(listPrice)
                        #return
                        ## reveal price

                if tokens[0] == 'endRound':
                    # get current winner and announce!!
                    messageToSend = f"The price to guess was**{currGame.round.listPrice}**"
                    winners = currGame.end_round()
                    #messageToSend = f"The price listed on Amazon is **{listPrice}**"
                    messageToSend += f"\n\n{' '.join([winner.mention for winner in winners])}"
                    messageToSend += f"\nCongrats! You guys won this round<3"
                    messageToSend += f"\n\n Ending round now"
                    messageToSend += f"\n'$pir testRound [price]' for new round"
                    messageToSend += f"\n'$pir endGame' to end game and announce winners!"
                    await message.channel.send(messageToSend)
                    return
                # else:
                if tokens[0] == 'guess':
                    guesser = message.author
                    guess = currGame.round.submit_guess(guesser, float(tokens[1]))
                    messageToSend = f"Thanks {guesser.mention}, your guess is now {guess}"
                    await message.channel.send(messageToSend)
                    return
            else:
                if tokens[0] == 'endGame':
                    winners, highScore = currGame.end_game()
                    currGame = None
                    messageToSend = f"With {highScore} points, our winners are..."
                    messageToSend += '\n' + ''.join([winner.mention for winner in winners])
                    await message.channel.send(messageToSend)
                    return

                if tokens[0] == 'testRound':
                    challenger = currGame.start_round(message.author, float(tokens[1]))
                    messageToSend = f"Round starts!"
                    messageToSend += f"\n{challenger.mention} is the quizmaster for this round"
                    await message.channel.send(messageToSend) # see who challenger is and save and mention
                    return
                    

client.run(os.environ['DISCORD_TOKEN'])