## Analysing XKCD comics with LDA


Just a small repo that details my attempts in natural language processing. I attempt to perform latent ditrecht allocation to identify common topics
within XKCD comics and their explanations.

This repo mainly houses code that:

1. Scrapes data from XKCD website, and also their explanations.

2. Clean up and organize this text information.

3. Create an LDA model that annotates all comics according to their topics.

4. Create a really bare-bones web application that can allow users to search for comics according to each of these topics
using Flask and deployed to heroku.

One weird aspect about this whole thing was that in deploying this to flask, I had to create a separate repo / submodule for it, so its technically a submodule not just
a subfolder.

