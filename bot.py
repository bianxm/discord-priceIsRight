import discord
import os
from dotenv import load_dotenv
from helpmessage import HELPMESSAGE
from game import Game

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

currGames = {}

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    global currGames

    if message.author == client.user or isinstance(message.channel, discord.channel.DMChannel):
        return

    # get message tokens
    startToken, *tokens = message.content.split() 
    # get guild id
    guild = message.channel.guild.id
    currGame = currGames.get(guild)

    if startToken == '$pir' or client.user.mentioned_in(message):
        if not currGame:
            if not tokens:
                messageToSend = "Welcome to Discord The Price is Right, featuring Amazon!"
                messageToSend += "\nStart a round, or $pir help"
                await message.channel.send(messageToSend)
                return
        
            if tokens[0] == 'help':
                await message.channel.send(HELPMESSAGE)
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
                currGames[guild] = Game()
                messageToSend = f"Game starts!"
                await message.channel.send(messageToSend)
                return
            
        if currGame:
            if not tokens:
                messageToSend = "Hi! Hope you're enjoying your game :)"
                await message.channel.send(messageToSend)
                return

            if tokens[0] == 'help':
                await message.channel.send(HELPMESSAGE)
                return
            
            if tokens[0] == 'testGame':
                messageToSend = f"Sorry, there is already a game running! '$pir endGame' first!"
                await message.channel.send(messageToSend)
                return
            
            if currGame.round:
                if tokens[0] == 'endGame' or tokens[0] == 'testRound':
                    messageToSend = f"Sorry, there is a round running! '$pir endRound' first!"
                    await message.channel.send(messageToSend)
                    return

                #if tokens[0] == 'start':
                    #await message.channel.send("Sorry, a round is already running!")
                    #return
                
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
                    winners = currGames[guild].end_round()
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
                    guess = currGames[guild].round.submit_guess(guesser, float(tokens[1]))
                    messageToSend = f"Thanks {guesser.mention}, your guess is now {guess}"
                    await message.channel.send(messageToSend)
                    return

            else:
                if tokens[0] == 'guess':
                    await message.channel.send("There's no round running yet! Do '$pir testRound [amount]' to start a new test round")
                    return

                if tokens[0] == 'endRound':
                    messageToSend = f"There's no round running at the moment. Did you mean to do '$pir testRound'?"
                    await message.channel.send(messageToSend)
                    return

                if tokens[0] == 'endGame':
                    if not currGame.points:
                        messageToSend = "You haven't played any rounds yet... Will go ahead and end this game though."
                        messageToSend += "\nIf you want to start a new game, please do '$pir testGame' again"
                        del currGames[guild] 
                    else:
                        winners, highScore = currGames[guild].end_game()
                        del currGames[guild]
                        messageToSend = f"With {highScore} points, our winners are..."
                        messageToSend += '\n' + ''.join([winner.mention for winner in winners])
                    await message.channel.send(messageToSend)
                    return

                if tokens[0] == 'testRound':
                    challenger = currGames[guild].start_round(message.author)
                    currGames[guild].round.listPrice = float(tokens[1])
                    messageToSend = f"Round starts!"
                    messageToSend += f"\n{challenger.mention} is the quizmaster for this round"
                    await message.channel.send(messageToSend) # see who challenger is and save and mention
                    return
                
                if tokens[0] == 'startRound':
                    # DM message.author to get the secret number
                    challenger = currGames[guild].start_round(message.author)
                    await message.channel.send("Waiting to be given secret number...")
                    currGames[guild].round.listPrice = await get_secret(challenger)
                    messageToSend = f"Secret number received!\nRound starts!"
                    messageToSend += f"\n{challenger.mention} is the quizmaster for this round"
                    await message.channel.send(messageToSend) # see who challenger is and save and mention
                    return

async def get_secret(quizmaster):
    await quizmaster.send(f"Give me your secret number")
    def check(m):
        return m.channel == quizmaster.dm_channel
    # try:
    reply = await client.wait_for('message', check=check)
    #except asyncio.TimeoutError:
        #await quizmaster.send('Took too long... Round aborted, please')
    return float(reply.content)
                    

client.run(os.environ['DISCORD_TOKEN'])