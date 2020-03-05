# Work Sample Test

We have created what is known as a 'work sample test'. It is a technical test designed to
mimic the actual work you'll be doing if you should join iLiveIt instead of algorithmic tests
that you might be used to.

As we discussed in the first interview we are moving our services to Kubernetes and running everything
in containers. While the move to the new architecture will greatly simplify building services one thing 
will still be present for a long time: APIs.

In this work test you'll be required to build an API as well as a sample client that uses your API. 

Your task is to create an API that receives JSON packets to send SMS and email messages, you don't have
to actually send the messages, but rather just handle the requests.

Requirements:

1. The API must require authorization. Using Bearer tokens in the HTTP headers is how we currently handle it.
2. You must handle every error you can think of, from input errors to database errors.
3. You must design the JSON packets yourself. For SMS packets it must include a cellphone number and SMS text, for email, an email address and HTML body.
4. You must use the appropriate HTTP status codes in your responses.
5. You must use the appropriate HTTP methods for your API routes.
6. Every message request must be logged in a database table that you need to create. You don't need to log all the information you receive, but enough to be able to report on.
7. Assume that multiple clients will use your API and thus client information must be logged for every packet. Clients must also have different authorization tokens to identify them as such.
8. The API must include at least the following 2 routes:

	a. /api/submit
		You will submit the JSON packets for messages to this route

	b. /api/message/{id}
		This route will return basic information about the message that was previously sent
		to the API. For SMS you must return at least cellphone number and SMS text, for email, the email address and HTML body. 
		Note: Clients must only be able to retrieve their own messages.


Restrictions:

1. You are free to use any language you want given that your API isn't 'hosted'. By 'hosted' we mean
languages like PHP and ASP.NET. We'd like to see how you build a long running process which we can't do
with PHP and ASP.NET.

2. We use MySQL as our database. We'd prefer you use a MySQL-compatible database like MySQL itself or MariaDB. 
Both are free and open-source. 

3. You are free to use open-source frameworks to build the API. We don't expect you to write your own webserver or database layer. 
4. Timeframe. We expect the result on the 16th of March. If you need more time, let us know.
5. This must be 100% your own work. You are not allowed to have anyone else complete any part of the task for you. 
6. You are prohibited from posting the task online to any forum for any sort of help on building the API. 
7. You are free to use resources that you would in a normal programming task, like Google, documentation, etc.

Submitting your work:

We use GitHub for all code, we'd like you to create your own repository and commit your code there.