## Inspiration

Discord community managers can benefit from having a direct plugin for their community members to sign up for newsletters with regular updates. We put all their needs together into a bot with easy integration for them to upload their own email templates with us. They can broadcast to their subscribers from a database that keeps getting updated in real-time with discord subscriber signups.  This saves any hassle for the subscribers having to log in somewhere specific and for the community manager to manage any databases or a place to keep their templates. We hope to make it all easier with the addition of just one bot to your server!

---

## What it does

Sign Me Up is a Discord bot that would help discord community managers easily broadcast newsletters directly from its dashboard and create an easy sign up for the server users. On the user's side, they can upload up to templates for their emails and broadcast from anywhere anytime using the dashboard. The subscribers can signup for the newsletter by simply using the smu command, more details on the commands are below.

### Available Commands:

- ping: Tells you how slow the bot is aka the bot's latency
- smu : Adds you to the mailing list IF your email ID is valid
- help: To learn about the commands offered

---

## How we built it
**Discord API:**  Using the Discord API, we authorized our bot to allow a direct login and allow users to add the bot to their servers.

**Cockroach:** We use CockroachDB and PostgreSQL, we managed the database for the application.

**SendGrid API:** With help of SendGrid, we make a feature for users to directly broadcast their email templates to their subscribers.  

More information on how we used these can be found [here](https://github.com/nandiniproothi/signmeup-bot/)

---

## Challenges we ran into

- We are all beginners in the respective parts we took up for the project and had limited to no experience in the technologies we used. 

---

## Accomplishments that we're proud of

- As beginners, we had the opportunity to learn a lot from the various elements necessary within this project in the duration of the hack, coordinated well as a team and learned the ins and outs of working on collaborative git projects. 

---

## What we learned

- We got hands-on experience in working with new technologies, solving problems and collaborating to create something new! 

---

## What's next for Sign Me up Bot

- In its current form, the bot's broadcast feature could become more helpful with a scheduling feature. Sign Me Up bot could also be expanded for subscribers to choose to sign up for multiple users administrating the same server. 

---