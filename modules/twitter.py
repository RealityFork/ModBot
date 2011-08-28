from constants import *
import twitterhandler

class Module():

	depends = ['logger']
	commands = {'tweet': 'tweet'}
	help = {
		'desc': 'tweets things from chan to the ChaosTheory twitter account - ChaosTheoryServ',
		'tweet': {
			'desc': 'Tweets the supplied message.',
			'params': {
				'message': 'String to tweet. Must be 140 characters or less.'
			}
		}
	}

	def tweet(self, user, channel, args):
		tweet = " ".join(args)
		if user in self.main.channels[channel]['admins']:
			if len(tweet) > 140:
				self.main.say(channel, "Tweet too long, please shorten it by %s characters." % (len(tweet) - 140), MSG_MAX)
			else:	
				if twitterhandler.tweet(tweet):
					self.main.say(channel, "Sent tweet.", MSG_MAX)
				else:
					self.main.say(channel, "Sending tweet failed. Check logs for details.", MSG_MAX)
			
	def tweetQuote(self, quote):
		if len(quote) > 140:
			self.main.say(self.main.channel, "Couldn't tweet that quote - it's too long. You need to shorten it by %s characters." % (len(quote) - 140), MSG_MAX)
		elif not twitterhandler.tweet(quote):
			self.main.say(self.main.channel, "Sending quote tweet failed. Check logs for details.", MSG_MAX)

