def my_print(txt):
    print(txt)

msg_template = """Hello {name},
Thank you fot joining {website}. We are very
happy to have you with us
"""

def format_msg(inputName, inputWebsite):
    my_msg = msg_template.format(name=inputName, website=inputWebsite)
    # print(my_msg)
    return 
    
"""
"{} {}".format("abc", 123)
"{1} {0}".format("abc", 123)
"{name} {number}".format(name="abc", number=123)
"""