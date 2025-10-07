def build_profile(first, last, **user_info):
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info
#Builds a dictonary that contains user information with optional parameters

my_profile = build_profile("Jorge", "Diaz", age=18, single=True, birthday="10/15/2006")
print(my_profile)