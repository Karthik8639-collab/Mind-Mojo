def generate_introvert_response(user_input):
    tone = "calm, friendly, non-judgmental"
    base_reply = f"I'm here with you. Let's take it slow. You said: '{user_input}'"
    return f"[{tone.upper()} MODE] {base_reply}"
