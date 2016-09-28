# Sticks-Stones
Rock Paper Scissors Robot

Very simple AI that uses  a basic HMM model to predict the moves its opponent will throw next.

At the moment this project is very basic. It uses a unigram HMM model, but I have no reason to believe that a unigram will most accurately model the way that a human plays (or any n-gram HMM will model a human's play well). I'd like to add use of n-grams (not sure how large n should be yet), but at the moment I'd need to find a way for the program to deal with playing while it collects enough data to make meaningful predictions (larger n is, more data needed until meaningful predictions). For the next implementation, I think I will simultaneously build unigram bigram and trigram models and have the computer play based on whichever has the strongest prediction.

The decision algorithm that the computer player uses is make its move is also fairly arbitrary at the moment. It picks the move it thinks is likely to win with higher probability instead of deterministically. The thinking behind this being that a human player will adjust less readily to this than to a deterministic algorithm, and the computer will be more able to pick up on basic paterns before its human opponent adjust strategies. It also uses data from the entirety of the game session weighted equally, which is very unlikely to be a good strategy in the long term. I would love to do some sort of  data collection, and perhaps implement a model that would learn how to best play given the data. Right now the program is also not robust against failure, so any sort of data collection method (presumably sending it out for many people to play against it) would need to happen after this is fixed.

Enjoy playing! :]