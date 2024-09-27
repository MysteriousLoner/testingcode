This application aims to demonstrate key elements of our solution to gamify 
and incentivice sustainable spending.

This application has 2 parts, the front-end webapp in /client, and backend server
in /server

Tech stack:
BE framework -django
db           -sqlite3
FE framework -next.js + react.js
GameEngine   -Gdevelop
GameGraphics -piskal

-----------------------------------------------------------------------------------------------

Considering that bash script might not work on other devices and this project's simplicity, 
Manual instructions will be provided to start the prototype.

1. navigate to server/
2. run the following command
source venv/bin/activate && cd pandahack && python manage.py runserver

3. navigate to client/
4. make sure you have npm
5. run the following command
npm install
npm run dev

6. open the url given by npm and append it with /42kl-food-app
for example, if npm gives this prompt: 
> 42kl-food-app@0.1.0 dev
> next dev

  ▲ Next.js 14.2.13
  - Local:        http://localhost:3000

 ✓ Starting...
 ✓ Ready in 1523ms

 visit: http://localhost:3000/42kl-food-app

 demourl: https://ruisheng95.github.io/42kl-food-app/
 