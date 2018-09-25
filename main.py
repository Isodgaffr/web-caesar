from flask import Flask

import webapp2
import caesar
import cgi


header = "<h1> Gibraun's Web Caesar App </h1>"

def build_page(textarea_content):
    rot_label = "<label> Rotate by how many numbers? </label>"
    rotation_input = "<input type='number' name='rotation_number'/>"

    message_label = "<label> Please type any message: </label>"
    textarea = "<textarea name='mesaage_textarea' style='height: 120px; width: 540px;'>" + textarea_content + "</textarea>"

    submit_label = "<label> Now click submit and watch the action </label>"
    submit = "<input type='submit' name='mess' />"

    form = ("<form method='post' action='/'>" +
            rot_label + rotation_input + "<br><br>" +
            message_label + textarea + "<br><br>" +
            submit_label + submit +
            "</form>")

    return header + form 

class MainHandler(webapp2.RequestHandler):

    def get(self):
        content = build_page("(type anything in here)")
        self.response.write(content)

    def post(self):
        message = self.request.get("message_textarea")
        num = int(self.request.get("rotation_number"))
        encrypted_message = caesar.encrypt(message, num)
        escaped_message = cgi.escape(encrypted_message)

        content = build_page(escaped_message)
        self.response.write(content)



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return "Hello World"

app.run()