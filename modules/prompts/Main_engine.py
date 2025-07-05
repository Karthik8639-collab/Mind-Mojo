from modules.introvert_assist import generate_introvert_response

def run_mindmojo():
    user_input = input("User says: ")
    response = generate_introvert_response(user_input)
    print("MindMojo:", response)

if __name__ == "__main__":
    run_mindmojo()
