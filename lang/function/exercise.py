# Modify this function to return a list of strings as defined above
def list_benefits():
    benefits = ("More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together")
    return(benefits)

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    benefit = benefit + " is a benefit of functions!"
    return(benefit)

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()
