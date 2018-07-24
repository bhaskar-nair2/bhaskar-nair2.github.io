from flask_mail import Mail, Message


class Mailer:
    def __init__(self, app):
        self.mailer = Mail(app)

    def sendThanks(self, form):
        msg = Message("Hello",
                      [form['email']],
                      """
                      Thank you for contacting me,

                       I'll reply as soon as possible.


                            ~Bhaskar Nair



                    This is a system generated reply. 
                    Please do not reply to this mail as it goes to an unchecked mail box.



                     """, sender='noreply@bhaskarnair.me')
        self.mailer.send(msg)
        del form
        del msg

    def sendMe(self, form):
        msg = Message(form['email']+"::"+form['subject'],
                      ["bhaskar@optimuscp.io"],
                      form['content'],
                      sender='noreply@bhaskarnair.me')
        self.mailer.send(msg)
