msg_template = """Hello {name},
Thank you fot joining {website}. We are very
happy to have you with us
"""

def format_msg(inputName, inputWebsite):
    my_msg = msg_template.format(name=inputName, website=inputWebsite)
    # print(my_msg)
    return my_msg
    
