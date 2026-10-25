def main():
    code = input("code: ")
    tag = make_tag(code)    
    print(tag)        


def make_tag(text): 
    """Return the text cleaned and upper-cased, preceded by #."""        
    return f"#{text.strip().upper()}"     


main()