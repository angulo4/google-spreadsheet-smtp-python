# google-spreadsheet-smtp-python
Sending due date email remainders from a Google Spreadsheet using Python and SMTP

How to send email remainders when a domain(hosting) is about to expire, using Google SpreadSheet and Python.

Scenery:
Web design Agency with customers that have domains + hosting to renew each year.
Information is recorded on a Google SpreadSheet and has to be review on a monthly basis, to contact customer and remind him about renewal fees.
Looking for an easy way of doing it using Python with some cron monthly schedule.

This code has three parts:
1st part (connecting with Google SpreadSheet via Google APIs console) thanks to Greg Baugues from Twilio (https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html)
2nd part (how to send emails using SMTP with Python)
3rd part (using datetime to know when to send email notifications).

This is a basic Python code, has "A LOT" to improve, but it's working for me.

