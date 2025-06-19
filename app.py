import streamlit as st
st.title("Inclusive Prompt Engineering Tool")

inclusivity_options = ["Diverse ages", "Multiple ethnicities", "Gender balance",
"Disability representation", "LGBTQ+ inclusion", "Body positivity",]

selected_goals = st.multiselect("Select Inclusivity Goals:",
    options=inclusivity_options, default=[])

target_audience = st.text_area("Describe your target audience")

purpose_options = ["Marketing", "Education", "Social Media", "Artistic", "Research"]
selected_purpose = st.selectbox(
    "Select the purpose of the generated image/prompt:",
    options=purpose_options)

def cues():
    cues_options = ["Clothing style", "Accessories", "Lighting",
        "Background elements", "Facial expressions", "Body language and posture",
        "Colors and textures",]

    selected_cues = st.multiselect(
        "Select 1 to 3 visual cues to include:",
        options=cues_options)

    if len(selected_cues) < 1:
        st.warning("Please select at least one visual cue.")
        return None
    elif len(selected_cues) > 3:
        st.warning("Please select no more than three visual cues.")
        return None

    detailed_cues = {}
    if 1 <= len(selected_cues) <= 3:
        for cue in selected_cues:
            desc = st.text_input(f"Describe details for: {cue}", key=cue)
            detailed_cues[cue] = desc.strip()

    return detailed_cues

user_prompt = st.text_area(
    "Describe the scene or action")

def generate_inclusive_prompt(base_prompt, goals, audience, purpose, cues):
    goals_text = ", ".join(goal.lower() for goal in goals) if goals else "inclusivity"
    audience_text = audience.strip() if audience.strip() else "everyone"

    if cues:
        cues_text = ", ".join(
            f"{cue.lower()} ({desc})" if desc else cue.lower() for cue, desc in cues.items()
        )
    else:
        cues_text = ""

    prompt = (
        f"For {purpose.lower()} purposes, create an image that speaks to {audience_text}. "
        f"Imagine a scene with {base_prompt}, highlighting {goals_text}. "
    )

    if cues_text:
        prompt += f"Pay particular attention to visual cues such as {cues_text}, "

    prompt += "making sure the image feels diverse and representative."

    return prompt

detailed_cues = cues()

if st.button("Generate Inclusive Prompt"):
    if not user_prompt:
        st.error("Please describe the scene or action.")
    else:
        cues_for_prompt = detailed_cues if detailed_cues else {}
        full_prompt = generate_inclusive_prompt(
            user_prompt, selected_goals, target_audience, selected_purpose, cues_for_prompt
        )
        st.markdown("### Generated Inclusive Prompt")
        st.code(full_prompt, language="text")
