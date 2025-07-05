
Next, generating your **NLU JSON schema** and **API architecture** to make this pretotype real.

Here’s how to structure the **NLU training schema** and system architecture so your hospitality agent can perform out-of-the-box during a pilot:

---

## 🧠 1. Sample JSON Schema — NLU Training Data (Hospitality)

Trains your model on typical utterances, grouped by intent.

```json
{
  "intents": [
    {
      "name": "check_availability",
      "examples": [
        "Do you have rooms available this weekend?",
        "Can I book a room for Friday?",
        "Is there availability for two adults?"
      ]
    },
    {
      "name": "get_directions",
      "examples": [
        "How do I get there from the airport?",
        "Can you text me directions?",
        "Where exactly are you located?"
      ]
    },
    {
      "name": "amenities_inquiry",
      "examples": [
        "Do you have a pool?",
        "Is breakfast included?",
        "Is there a gym on site?"
      ]
    },
    {
      "name": "check_in_out_times",
      "examples": [
        "What time is check-in?",
        "Can I check out late?",
        "When do I need to leave the room?"
      ]
    },
    {
      "name": "room_service_request",
      "examples": [
        "Can I get more towels?",
        "I'd like an extra pillow",
        "Can someone bring up water?"
      ]
    },
    {
      "name": "speak_to_human",
      "examples": [
        "Let me talk to someone",
        "Can I speak to the front desk?",
        "I need to talk to a person"
      ]
    }
  ]
}
```

You can expand this with slots (e.g., date, time, number of guests) and localization for multilingual versions.

---

## 🔌 2. Notional API List & Architecture (Pretotype Ready)

Here’s what you’d wire up (or simulate) for a fast-moving prototype, especially for voice or phone-line use.

### 📚 Agent Architecture Overview

**Frontend (Voice Interface)**:

- Twilio Voice or SignalWire SIP routing
    
- Text-to-Speech / ASR (Google Speech, AWS Polly)
    
- Web version: Widget for mobile browser
    

**Core Agent / Middleware**:

- Intent handling (Dialogflow CX, Rasa, or custom LLM layer)
    
- Context tracking + fallback logic
    
- NLU model trained via schema above
    

---

### 🧩 APIs to Integrate or Simulate

|Function|System|Example API|
|---|---|---|
|📅 Room Availability|Booking Engine|`GET /availability?date=YYYY-MM-DD` (mock or Cloudbeds API)|
|🗺️ Directions|Google Maps|`GET https://maps.googleapis.com/maps/api/directions/json?origin=airport&destination=hotel`|
|📖 Hotel Policies|CMS / Config|`GET /hotel-info` returns amenities, check-in times, etc.|
|🔄 Human Transfer|VoIP|Twilio `call.forward(toNumber)` or webhook callback|
|📈 Logs / Feedback|Analytics|Store in Firebase, Supabase, or lightweight webhook|

---

## 🎯 Deployment Tips for Pretotyping

- Use a **hardcoded booking response**: Always return “Yes, we have availability on [Date]” unless real integration is needed.
    
- Set up **admin config JSON file** per hotel:
    
    ```json
    {
      "hotelName": "The Seaside Inn",
      "checkInTime": "3:00 PM",
      "checkOutTime": "11:00 AM",
      "amenities": ["pool", "free WiFi", "continental breakfast"]
    }
    ```
    
- Store in-memory session context for:
    
    - Language
        
    - Intent history
        
    - Escalation reason
        

---

Would you like:

- A Notion page template with this system mapped visually?
    
- A prototype flowchart or voice agent storyboard?
    
- A Dialogflow CX export or Twilio flow scaffold?
    

Just say the word.