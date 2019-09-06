from flask_mail import Mail, Message


class Mailer:
    def __init__(self, app):
        self.mailer = Mail(app)

    def sendThanks(self, form):
        msg = Message("Hello",
                      [form['email']],
                      html="""
                     <h2> Thank you for contacting me,<br>

                       I'll reply as soon as possible.<br><br>


                        <i>~Bhaskar Nair</i></h2><br><br><br><br>



                    <em>This is a system generated reply. 
                    Please do not reply to this mail as it goes to an unchecked mail box.</em>



                     """, sender='noreply@bhaskarnair.me')
        self.mailer.send(msg)
        del form
        del msg

    def sendMe(self, form):
        msg = Message(form['subject'],
                      ["bhaskar@optimuscp.io"],
                      sender='noreply@bhaskarnair.me',
                      html='''
                      <h2>{}</h2><br>
                      <i>sent</i><br><br>
                      <h3>{}</h3>
                      <br><br>
                      <a href="mailto:{}">Click to reply<a>
                      '''.format(form['email'], form['content'], form['email']))
        self.mailer.send(msg)
