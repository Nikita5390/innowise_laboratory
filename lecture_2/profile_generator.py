from datetime import date, datetime


def user_generator():
    user_name = str(input("Enter your full name: "))
    birth_year = int(input("Enter your birthyear: "))
    current_age = datetime.today().year - birth_year
    life_stage = generate_profile(current_age)
    keys = ['user_name', 'birth_year', 'current_age', 'life_stage']
    values = [user_name, birth_year, current_age, life_stage]
    user_profile = {keys: values for keys, values in zip(keys, values)}
    return user_profile


def generate_profile(age):
    if age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    return "Adult"


def hobbies_message_handler(hobbies):
    current_hobbies = ""
    for hobby in hobbies[1:]:
        current_hobbies += (f"- {hobby}\n")
    return current_hobbies


if __name__ == "__main__":

    def main():
        user_profile = user_generator()
        hobbies = ["You didn't mention any hobbies"]
        text = None
        while text != "stop":
            text = str(input("Enter a favorite hobby or type 'stop' to finish: "))
            if text != 'stop':
                hobbies.append(text)

        user_profile['hobby'] = hobbies
        amount_of_hobby = len(hobbies) - 1
        current_hobbies = hobbies_message_handler(hobbies)

        if amount_of_hobby != 0:
            message = (f"Profile Summary:\n"
                       f"Name: {user_profile['user_name']}\n"
                       f"Age: {user_profile['current_age']}\n"
                       f"Life-stage: {user_profile['life_stage']}\n"
                       f"Favorite Hobbies ({amount_of_hobby}):\n"
                       f"{current_hobbies}\n"
                       )
        else:
            message = (f"Profile Summary:\n"
                       f"Name: {user_profile['user_name']}\n"
                       f"Age: {user_profile['current_age']}\n"
                       f"Life-stage: {user_profile['life_stage']}\n"
                       f"{hobbies[0]}\n"
                       )

        return print(message)

main()
