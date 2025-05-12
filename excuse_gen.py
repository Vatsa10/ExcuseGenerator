import random
import json

# Define prompt categories
scenarios = {
    "work": {
        "prompts": [
            "Why wasn't the report submitted on time?",
            "Why did you miss the team meeting?",
            "Why is the project delayed?",
            "Can you explain why the client hasn't been contacted yet?",
            "Why was the deadline missed?"
        ],
        "excuses": {
            "technical": [
                "My internet crashed during the upload.",
                "The system was down all morning.",
                "My computer froze after an unexpected update.",
                "The cloud storage failed to sync the files.",
                "I lost access to the internal portal."
            ],
            "personal": [
                "I had a family emergency last night.",
                "I wasn't feeling well and took a sick day.",
                "I overslept due to a late-night work session.",
                "I got stuck in traffic and couldn't log in on time.",
                "I forgot because I was overwhelmed with personal matters."
            ],
            "misunderstanding": [
                "I thought the task was delegated to someone else.",
                "I misunderstood the timeline and started too late.",
                "I assumed we were waiting for feedback before proceeding.",
                "I thought it was scheduled for next week.",
                "I missed the email notification."
            ]
        }
    },
    "school": {
        "prompts": [
            "Why didn't you turn in your homework?",
            "Why were you absent from class today?",
            "Why didn't you participate in the group project?",
            "Where is your science fair project?",
            "Why are your assignments incomplete?"
        ],
        "excuses": {
            "forgetfulness": [
                "I completely forgot about it until now.",
                "I thought it was due next week.",
                "I left my notebook at school.",
                "I wrote it but forgot to bring it home.",
                "I saved it in the wrong folder."
            ],
            "misunderstanding": [
                "I misunderstood the instructions and did something else.",
                "I thought we were working in groups.",
                "I thought the deadline was extended.",
                "I didn’t realize it was assigned.",
                "I didn’t see the email about the task."
            ],
            "external": [
                "My dog ate my printed copy.",
                "I had to help my sibling study for a test.",
                "I caught a cold and couldn’t focus.",
                "There was a power outage and I couldn’t print it.",
                "I tried scanning it but the app kept crashing."
            ]
        }
    },
    "social": {
        "prompts": [
            "Why didn't you show up to the party?",
            "Why did you leave early from dinner?",
            "Why didn't you reply to my message?",
            "What happened, you ghosted me?",
            "Why weren't you at the event?"
        ],
        "excuses": {
            "external": [
                "My phone died and I couldn't contact anyone.",
                "I got stuck helping someone with their car.",
                "There was no way to reach you back.",
                "I tried calling, but it kept going to voicemail.",
                "I lost track of time while working."
            ],
            "personal": [
                "I wasn't feeling confident enough to go out.",
                "I was too stressed to socialize.",
                "I had a panic attack earlier and couldn't come.",
                "I didn't feel comfortable attending without more context.",
                "I had a bad headache and needed rest."
            ],
            "tech_issue": [
                "My calendar glitched and changed the date.",
                "The app gave me the wrong address.",
                "I thought the event was online.",
                "I clicked 'maybe' instead of 'going'.",
                "My notification settings muted the reminder."
            ]
        }
    },
    "family": {
        "prompts": [
            "Why aren't you coming over this weekend?",
            "Why did you cancel our plans?",
            "Why didn't you pick up the kids?",
            "Why didn't you help with the chores?",
            "Why were you late to the family dinner?"
        ],
        "excuses": {
            "unexpected": [
                "The babysitter canceled last minute.",
                "Something came up with my neighbor and I had to help.",
                "The car broke down on the way.",
                "I had to rush my sibling to the hospital.",
                "An old friend showed up unannounced."
            ],
            "forgetfulness": [
                "I completely forgot about the schedule change.",
                "I mixed up the dates and thought it was next week.",
                "I meant to do it but forgot in the chaos.",
                "I thought someone else handled it.",
                "I thought we agreed on another time."
            ],
            "health": [
                "I had a sudden migraine and couldn't drive.",
                "I felt nauseous and stayed in bed.",
                "I caught a bug going around and couldn't risk spreading it.",
                "I was running a fever and couldn't get out of bed.",
                "I was exhausted from insomnia."
            ]
        }
    },
    "everyday": {
        "prompts": [
            "Why didn't you call me back?",
            "Why were you so late?",
            "Why didn't you clean your room?",
            "Why is the trash still here?",
            "Why didn't you make it to the store?"
        ],
        "excuses": {
            "technical": [
                "My alarm didn't go off this morning.",
                "My phone auto-updated and restarted.",
                "The app glitched and gave me the wrong address.",
                "My GPS led me in the opposite direction.",
                "I couldn't find parking anywhere nearby."
            ],
            "external": [
                "There was a sudden blackout in the area.",
                "A tree fell on the road and blocked traffic.",
                "I had to wait for a delivery person.",
                "I helped an elderly person cross the street and got delayed.",
                "My pet ran away and I had to chase him."
            ],
            "absurd": [
                "Aliens abducted me for five minutes and messed up my schedule.",
                "My goldfish had a meltdown and I needed to calm him down.",
                "I accidentally locked myself in the pantry.",
                "The microwave beeped so loudly I panicked and forgot everything.",
                "I mistook my alarm clock for a dream and hit snooze in my sleep."
            ]
        }
    },
    "tech_issues": {
        "prompts": [
            "Why haven't you replied to the email?",
            "Why did the software crash again?",
            "Why can't you join the Zoom call?",
            "How did you delete that important file?",
            "Why isn't the database responding?"
        ],
        "excuses": {
            "software": [
                "The update corrupted the entire system.",
                "I clicked the wrong button by accident.",
                "The browser extension caused a conflict.",
                "The firewall blocked access to the server.",
                "I accidentally opened a phishing link and had to reboot."
            ],
            "hardware": [
                "My laptop overheated and shut down.",
                "The monitor went black and I couldn't fix it.",
                "I spilled water on my keyboard and had to replace it.",
                "The mouse stopped responding randomly.",
                "My battery died right before submitting the form."
            ],
            "network": [
                "The Wi-Fi dropped every time I tried to connect.",
                "The router reset itself multiple times.",
                "The ISP had an outage across the city.",
                "I connected to someone else’s network by mistake.",
                "The firewall blocked outgoing connections."
            ]
        }
    },
    "health_mental": {
        "prompts": [
            "Why didn't you come into work today?",
            "Why have you been so quiet lately?",
            "Why didn't you attend therapy?",
            "Why did you skip the workout class?",
            "Why are you always distracted?"
        ],
        "excuses": {
            "physical_health": [
                "I woke up with a terrible stomachache.",
                "I’ve been battling a persistent flu.",
                "I pulled a muscle and couldn't move properly.",
                "I had a dental emergency and couldn't focus.",
                "I got food poisoning last night."
            ],
            "mental_health": [
                "I was dealing with a lot emotionally and couldn't cope.",
                "I had a panic attack and needed space.",
                "I've been struggling with anxiety and couldn't function.",
                "I was too overwhelmed to think straight.",
                "I had a depressive episode and couldn't motivate myself."
            ]
        }
    }
}

# Generate 1000 entries
with open("extensive_excuse_dataset.jsonl", "w") as f:
    for _ in range(1000):
        # Randomly choose a scenario
        scenario_key = random.choice(list(scenarios.keys()))
        scenario = scenarios[scenario_key]

        # Choose a prompt
        prompt = random.choice(scenario["prompts"])

        # Choose a type of excuse
        excuse_type = random.choice(list(scenario["excuses"].keys()))
        excuse = random.choice(scenario["excuses"][excuse_type])

        # Build JSON object
        entry = {"prompt": prompt, "excuse": excuse}

        # Write to file
        f.write(json.dumps(entry) + "\n")