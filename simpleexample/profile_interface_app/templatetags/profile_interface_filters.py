from django import template
from django.utils.safestring import mark_safe
import calendar
import random

register = template.Library()


@register.filter()
def month_name(month_number):
    return calendar.month_name[month_number]


@register.filter()
def skills_to_list_comma(skills):
    """
       Transform a Skills dictionary to a string with all the skills name
       separated by comma.
    """
    skills_list = map(lambda x: x['skill']['name'], skills)
    skills_list_string = ", ".join(skills_list)
    return "{0}.".format(skills_list_string)


@register.filter()
def protect_telephonenumber(phone_number):
    """ Protect my telephone number from non-desirable crawlers.
    """
    numbers = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
    }
    phone_number_list = map(lambda number: number, phone_number)
    phone_number_protected = ""
    retries = 0
    while True:
         index_to_translate = random.randint(0, len(phone_number_list)-1)
         number = phone_number_list[index_to_translate]
         if number in numbers:
             number_protected = numbers[number]
             next_index = index_to_translate + 1
             phone_number_protected = "".join([phone_number[:index_to_translate],
                                              number_protected,
                                              phone_number[next_index:]])
             break
         if retries > 4:
             break
         retries += 1

    return phone_number_protected

@register.filter()
def protect_email(email):
    """ Just apply a simple ceaser cipher method, and decipher the user using
        javascript.
    """
    email_translated = map(lambda letter: chr((ord(letter) + 1)), email)
    email_translated = "".join(email_translated)

    to_return = """<div id="protected"></div>
           <script type="text/javascript">
                  function decipher_mail(){
                      var em = "%s";
                      var str_out = "";
                      for (var i = 0; i < em.length; i++){
                          var c_code = String.fromCharCode(em.charCodeAt(i) - 1);
                          str_out = str_out + c_code;
                      }
                      return str_out;
                  }
                  var element_email = document.getElementById("protected");
                  var result = decipher_mail();
                  element_email.innerHTML = result;
           </script>"""%(email_translated)

    value = mark_safe(to_return)

    return value

