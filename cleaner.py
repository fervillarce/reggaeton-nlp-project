def clean_html_tags(l):
    """
    Receive a list, remove the 'p' and 'br' html tags and return a clean list.
    List can contain any type (lists, strings, bs4.elements...)
    """
    clean_list = []
    for e in l:
        e = str(e)
        e = e.replace("<p>", "")
        e = e.replace("</p>", "")
        e = e.replace("<br>", "<br/>")
        e = e.replace("</br>", "<br/>")
        e = e.split("<br/>")
        clean_list.append(e)
    return clean_list


def flatten_list(l):
    """
    Receive a list of lists and return a list with just one element.
    """
    return sum(l, [])

def remove_linebreak(l):
    """
    Receive a list and remove the elements which are ''.
    """
    if '' in l:
        l.remove('')
    return l

