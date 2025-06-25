def parse_intent(text):
    if "appointment" in text:
        return {"intent": "booking", "response": "Sure, I can help you book an appointment."}
    elif "hours" in text or "open" in text:
        return {"intent": "hours", "response": "We are open Monday to Friday from 9 AM to 5 PM."}
    else:
        return {"intent": "unknown", "response": "Please repeat your request or call back later."}