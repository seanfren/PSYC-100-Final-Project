from drafter import *
from bakery import assert_equal
from dataclasses import dataclass

@dataclass
class Event:
    id_number: str
    event_text: str
    button_text: str
    options: list[str]
    resolutions: list[str]

@dataclass
class State:
    current_event: Event
    Energy: int
    Equilibrium: int
    Thermodynamics: int
    Acids_and_Bases: int
    Structures: int
    events_seen: int
    
def append_options(state: State, page_list: list[str]) -> list[str]:
    for option in state.current_event.options:
        page_list.append(option)
    return page_list

def append_hud(state: State, page_list: list[str]) -> list[str]:
    page_list.append("Energy: " + str(state.Energy))
    page_list.append("Equilibrium: " + str(state.Equilibrium))
    page_list.append("Thermodynamics: " + str(state.Thermodynamics))
    page_list.append("Acids and Bases: " + str(state.Acids_and_Bases))
    page_list.append("Structures: " + str(state.Structures))
    return page_list

def count_options(option_list: list[str]) -> int:
    count = 0
    for option in option_list:
        count += 1
    return count

def calculate_results(state: State, player_response: str):
    if state.current_event.id_number[0] == "1":
        if state.current_event.id_number[1] == "0":
            if int(player_response) == 1:
                state.Energy = increment(state.Energy, 20, "+")
            else:
                state.Structures = increment(state.Structures, 20, "+")
                state.Energy = increment(state.Energy, 20, "-")
        elif state.current_event.id_number[1] == "1":
            if int(player_response) == 1:
                state.Structures = increment(state.Structures, 10, "+")
                state.Energy = increment(state.Energy, 20, "-")
            elif int(player_response) == 2:
                state.Equilibrium = increment(state.Equilibrium, 20, "+")
                state.Thermodynamics = increment(state.Thermodynamics, 20, "+")
                state.Acids_and_Bases = increment(state.Acids_and_Bases, 20, "+")
                state.Energy = increment(state.Energy, 35, "-")
            else:
                state.Energy = increment(state.Energy, 30, "+")
        elif state.current_event.id_number[1] == "2":
            if int(player_response) == 1:
                state.Equilibrium = increment(state.Equilibrium, 25, "+")
                state.Energy = increment(state.Energy, 20, "-")
            elif int(player_response) == 2:
                state.Thermodynamics = increment(state.Thermodynamics, 25, "+")
                state.Energy = increment(state.Energy, 20, "-")
            else:
                state.Acids_and_Bases = increment(state.Acids_and_Bases, 25, "+")
                state.Energy = increment(state.Energy, 20, "-")
        else:
            if int(player_response) == 1:
                state.Structures = increment(state.Structures, 5, "+")
                state.Energy = increment(state.Energy, 5, "+")
            else:
                state.Energy = increment(state.Energy, 50, "+")
    elif state.current_event.id_number[0] == "2":
        if state.current_event.id_number[1] == "1":
            if int(player_response) == 1:
                state.Thermodynamics = increment(state.Thermodynamics, 5, "+")
                state.Energy = increment(state.Energy, 5, "-")
            elif int(player_response) == 2:
                state.Thermodynamics = increment(state.Thermodynamics, 25, "+")
                state.Energy = increment(state.Energy, 20, "-")
            else:
                state.Energy = increment(state.Energy, 30, "+")
        elif state.current_event.id_number[1] == "2":
            if int(player_response) == 1:
                state.Acids_and_Bases = increment(state.Acids_and_Bases, 10, "+")
                state.Energy = increment(state.Energy, 20, "-")
            else:
                state.Acids_and_Bases = increment(state.Acids_and_Bases, 30, "+")
                state.Energy = increment(state.Energy, 25, "-")
        else:
            if int(player_response) == 1:
                state.Equilibrium = increment(state.Equilibrium, 5, "+")
                state.Energy = increment(state.Energy, 5, "+")
            else:
                state.Energy = increment(state.Energy, 50, "+")
    else:
        if state.current_event.id_number[1] == "0":
            if int(player_response) == 1:
                state.Energy = increment(state.Energy, 50, "+")
            else:
                state.Equilibrium = increment(state.Equilibrium, 15, "+")
                state.Energy = increment(state.Energy, 15, "-")
        elif state.current_event.id_number[1] == "1":
            if int(player_response) == 1:
                state.Structures = increment(state.Structures, 5, "+")
                state.Energy = increment(state.Energy, 5, "-")
            elif int(player_response) == 2:
                state.Structures = increment(state.Structures, 30, "+")
                state.Energy = increment(state.Energy, 25, "-")
            else:
                state.Structures = increment(state.Structures, 25, "+")
                state.Energy = increment(state.Energy, 10, "-")
        elif state.current_event.id_number[1] == "2":
            if int(player_response) == 1:
                state.Equilibrium = increment(state.Equilibrium, 15, "+")
                state.Thermodynamics = increment(state.Thermodynamics, 15, "+")
                state.Acids_and_Bases = increment(state.Acids_and_Bases, 15, "+")
                state.Structures = increment(state.Structures, 15, "+")
            elif int(player_response) == 2:
                compare_values(state)
            else:
                state.Energy = increment(state.Energy, 0, "+")
        else:
            if int(player_response) == 2:
                state.Equilibrium = increment(state.Equilibrium, 10, "-")
                state.Thermodynamics = increment(state.Thermodynamics, 10, "-")
                state.Acids_and_Bases = increment(state.Acids_and_Bases, 10, "-")
                state.Structures = increment(state.Structures, 10, "-")
            
def increment(value: int, change: int, sign: str) -> int:
    if sign == "+":
        new_value = value + change
    else:
        new_value = value - change
    if new_value > 100:
        return 100
    elif new_value < 0:
        return 0
    else:
        return new_value

def compare_values(state: State):
    values_list = [state.Equilibrium, state.Thermodynamics, state.Acids_and_Bases, state.Structures]
    minimum = 100
    for value in values_list:
        if value < minimum:
            minimum = value
    if minimum == state.Equilibrium:
        state.Equilibrium = increment(state.Equilibrium, 35, "+")
    elif minimum == state.Thermodynamics:
        state.Thermodynamics = increment(state.Thermodynamics, 35, "+")
    elif minimum == state.Acids_and_Bases:
        state.Acids_and_Bases = increment(state.Acids_and_Bases, 35, "+")
    else:
        state.Structures = increment(state.Structures, 35, "+")

def calculate_score(state: State) -> str:
    total_points = state.Equilibrium + state.Thermodynamics + state.Acids_and_Bases + state.Structures
    average_score = total_points // 4
    if average_score > 90:
        return "A"
    elif average_score > 80:
        return "B"
    elif average_score > 70:
        return "C"
    else:
        return "F"

@route
def index(state: State) -> Page:
    return Page(state, ["Ace the Exam!",
                        Button("Play", tutorial)])

@route
def tutorial(state: State) -> Page:
    return Page(state, [state.current_event.event_text,
                        Button("Proceed", display_event)])
@route
def display_event(state: State) -> Page:
    state.events_seen += 1
    state.current_event = Event_list[state.events_seen]
    if state.current_event.id_number[0] == "0":
        return Page(state, [state.current_event.event_text,
                           "Energy: " + str(state.Energy),
                           "Equilibrium: " + str(state.Equilibrium),
                           "Thermodynamics: " + str(state.Thermodynamics),
                           "Acids and Bases: " + str(state.Acids_and_Bases),
                           "Structures: " + str(state.Structures),
                           Button(state.current_event.button_text, display_event)])
    else:
        page_list = [state.current_event.event_text,"You: ",]
        page_list = append_options(state, page_list)
        page_list = append_hud(state, page_list)
        page_list.append(TextBox("player_response", ""))
        page_list.append(Button(state.current_event.button_text, resolve_event))
        return Page(state, page_list)
    
@route
def retry_event(state: State) -> Page:
    page_list = [state.current_event.event_text,"You: ",]
    page_list = append_options(state, page_list)
    page_list.append(TextBox("player_response", ""))
    page_list.append(Button(state.current_event.button_text, resolve_event))
    return Page(state, page_list)

@route
def resolve_event(state: State, player_response: str) -> Page:
    player_choice = player_response
    if player_choice.isdigit():
        option_amount = count_options(state.current_event.options)
        player_number = int(player_response)
        if player_number < 0:
            return Page(state, ["Oops! Something went wrong. Next time, make sure your input is a number for one of the options.",
                                Button("Try again", retry_event)])
        elif player_number > option_amount:
            return Page(state, ["Oops! Something went wrong. Next time, make sure your input is a number for one of the options.",
                                Button("Try again", retry_event)])
        else:
            calculate_results(state, player_choice)
            if state.Energy == 0:
                return Page(state, ["""Uh Oh! Looks like you pushed yourself a little too hard, and now you are all out of energy!
You're too exhausted mentally to study, so you end up failing your exam. Looks like you'll have to retake the class after all..."""])
            elif state.current_event.id_number == "33":
                return Page(state, [state.current_event.resolutions[player_number - 1],
                                    Button("Proceed", exam_day)])
            else:
                return Page(state, [state.current_event.resolutions[player_number - 1],
                                    Button("Proceed", display_event)])
    else:
        return Page(state, ["Oops! Something went wrong. Next time, make sure you input a number corresponding to the choice you want to make.",
                            Button("Try again", retry_event)])
    
@route
def exam_day(state: State) -> Page:
    return Page(state, ["""Well, this is it. The final exam. You wake up early and quickly go to the lecuture hall where the exam is
taking place. You take a seat just as they begin passing out exams. Your nerves overwhelm you as you contemplate the possibility of
having to retake this class. The professor announces the beginning of the exam, so you grab you pencil and flip open the test booklet.""",
                        Button("Good Luck!", results)])

@route
def results(state: State) -> Page:
    grade = calculate_score(state)
    if grade == "A":
        return Page(state, ["""Congratulations! You passed with flying colors! An A+!""",
                            Button("Woohoo!", conclusion)])
    elif grade == "B":
        return Page(state, ["""Good job! You got a B! A perfectly fine grade!""",
                            Button("Nice!", conclusion)])
    elif grade == "C":
        return Page(state, ["""Well, you got a C. It's certainly not the grade you hoped for, but at least you passed the class.""",
                            Button("Okay", conclusion)])
    else:
        return Page(state, ["""I have some bad news for you. You failed the final, and the class. You'll have to take it again next
semester.""",
                            Button("Dang.", conclusion)])

@route
def conclusion(state: State) -> Page:
    return Page(state, ["""Thanks for playing this little game! I hope you learned something about studying, whether that be techniques
which are effective that you want to try, or its things you were doing which are not really effective. I hope you can take what you
learned from this game and us it to Ace your Exams!"""])
    
tutorial_event = Event("00", """Uh oh! Finals are just three days away, and you just realized you have not be studying for
your super important Chemistry exam. If you fail the exam, you'll have to retake the class,
and you don't want that! Better use some effective study strategies in order to Ace that Exam!""",
                       "Proceed", [], [])

tutorial_event_2 = Event("01", """Below you'll see your current state. Your Energy is is self explanatory, it is used by doing
tasks and replenished by resting. Be careful, if you run out of energy, you'll be too tired to do anything!""",
                         "Proceed", [], [])

tutorial_event_3 = Event("02", """Below your energy is your understanding in each topic which is on the exam. These can go up to
100, and you'll need to have these quite high to do well on your exam.""",
                         "Proceed", [], [])

tutorial_event_4 = Event("003", """Well, that's all you need to know. Good luck and work hard!""",
                         "Begin!", [], [])

day_1_dawn = Event("10", """Today you have Chemistry class to attend. Fairly drowsy, you arrive at the classroom and take a seat. As your
Professor begins to discuss the different structures of molecules,""",
                      "Continue", ["1: Take a nap.", "2: Pay attention."],
                      ["""You probably should have payed attention, as you might have missed valuable information. But at least you feel well rested! +20 Energy.""",
                       """Good choice! Paying attention is the basis for understanding! +15 understanding in structures. However, the lecture was quite boring. -20 Energy."""])

day_1_noon = Event("11", """After Chemistry class, you go have a hamburger for lunch. Next you decide to go to the library to study. The only question is,
what should you study?""", "Continue", ["1: Continue studying molecular structures.",
                                        "2: Study multiple different topics instead.",
                                        "3: Screw studying! I'm going to play games on my laptop!"],
                        ["""You feel like you really understand structures! +10 understanding in structures. However, it was a lot of the same information, so you fell like your time
and energy may have been better spent studying something else. -20 Energy.""",
                         """By mixing together multiple different subjects into your studying, you have done what is known as interleaving.
This study strategy is much more difficult than studying a single concept at a time, as it requires your brain to repeatedly switch
between different concepts. However, this added challenge also makes it more effective than regular studying! +20 understanding to
equilibrium, thermodynamics, and acids and bases! -35 Energy.""",
                         """Really? Your exam is in a couple of days and you're goofing off? You really need to manage your time
wisely! Well, I guess it is quite fun... +30 Energy."""])

day_1_dusk = Event("12", """You go eat dinner, then arrive back at your dorm room. With little time left,""", "Continue",
                      ["1: Study equilibrium.",
                       "2: Study thermodynamics.",
                       "3: Study acids and bases.",],
                      ["""As you really dig deep into equilibirum, you feel like you really understand it better! +25 understanding to equilibirum. -20 Energy.""",
                       """As you really dig deep into thermodynamics, you feel like you really understand it better! +25 understanding to thermodynamics. -20 Energy.""",
                       """As you really dig deep into acids and bases, you feel like you really understand it better! +25 understanding to acids and bases. -20 Energy.""",])

day_1_midnight = Event("13", """As you study, you begin to feel quite tired. Looking at the clock, you notice it is nearing midnight.""",
                       "Continue", ["1: Keep studying", "2: Call it a night."],
                       ["""Cramming for the exam, you try to fit in studying structures tonight. However, you were so tired, you don't
feel like you got much out of it. +5 understanding to structures. You get to bed quite late, and your sleep is not as restful as it should be.
+5 Energy.""",
                        """Good choice!. A good night's sleep is important for a healthy mind! +50 Energy."""])

day_2_noon = Event("21", """You get up early in the morning to go to class, but it's Physics class, so whatever you do there is
not really relevent for this game. After eating lunch, you head back to your room and begin to study thermodynamics. But how should you do it?""",
                        "Continue", ["1: Go through the textbook and highlight key concepts.",
                                     "2: Ask questions about thermodynamics to yourself and try to answer them.",
                                     "3: Take a nap instead."],
                        ["""Studies show that what you have just done is not a very effective method of studying. Just highlighting does
not really help with memorizing information, let alone help with knowing how to solve problems. +5 understanding to
thermodynamics. -5 Energy""",
                         """What you have just done is elaboration. It is a rather effective study method where you ask yourself questions
about a concept and try to connect it with what you already know, as well as look more into it for a deeper understanding. +20 understanding
in thermodynamics. -20 Energy""",
                         """You must be quite tired from that late night of studying, huh? Well, at least the nap was quite refreshing.
+30 Energy."""])

day_2_dusk = Event("22", """After a long session of studying (hopefully), you decide to go eat dinner. After returning, you begin studying
acids and bases instead. To study, you begin solving practice problems on the topic.""", "Continue",
                      ["1: Regularly check notes and the answer key while working.",
                       "2: Try to do as much as you can without notes."],
                      ["""By regulary checking your notes while working, you did not really challenge yourself. While you still learned
some, you could have learned a lot more. +10 understanding to acids and bases. -20 energy.""",
                       """By doing as much as possible without help, you have engaged in a study technique known as retrieval practice.
Retrieval practice is a very good study technique, as it greatly challenges you to retrieve information from memory, much like the final will.
+30 understanding to acids and bases. -25 energy."""])

day_2_midnight = Event("23", """You once again look at the clock and notice that it is getting quite late.""", "Continue",
                       ["1: Keep studying.", "2: Call it a night"],
                       ["""Cramming for the exam, you try to fit in studying equilibrium tonight. However, you were so tired, you don't
feel like you got much out of it. +5 understanding to equilibrium. You get to bed quite late, and your sleep is not as restful as it should be.
+5 Energy.""",
                        """Good choice!. A good night's sleep is important for a healthy mind! +50 Energy."""])

day_3_dawn = Event("30", """You eyes fly open as you hear the obnoxious sound of your alarm clock. As you quickly turn it off,
you remember that it is Reading Day, so you do not have classes today.""", "Continue",
                      ["1: Go back to bed.", "2: Get an early start on studying equilibrium."],
                      ["""Still tired from last night, you decide to get some much needed shuteye. +50 Energy.""",
                       """Worried about your upcoming exam, you decide to start studying early. You are still quite tired, but you manage to
learn something. +15 understanding to equilibrium. -15 Energy."""])

day_3_noon = Event("31", """As you notice the time nearing lunchtime, you decide to order a pizza so you can eat and study at
the same time. You decide to tackle molecular structures next, the only question is: How will you study?""", "Continue",
                        ["1: Reread the textbook section about structures.",
                         "2: Try to draw diagrams of common structures from memory.",
                         "3: Draw and label a diagram of a chemical formula"],
                        ["""Sadly, while it is easy, rereading has been found to be one of the least effective studying strategies.
It certainly will not help you on a concept that is so visual. +5 understanding to structures. -5 Energy.""",
                         """By trying to draw diagrams from memory, you have engaged in retrieval practice. Retrieval practice is a
very good study technique, as it greatly challenges you to retrieve information from memory, much like the final will. +30 understanding
to structures. -25 Energy.""",
                         """By drawing and labeling a diagram, you have engaged in the study technique dual coding. Dual coding is when
you take textual information, and represent it visually. It is effective because it combines two different mediums, text and visuals, to
help you learn. +25 understanding to structures. -10 Energy."""])

day_3_dusk = Event("32", """This is it, your last chance to study before the exam tommorow morning!""", "Continue",
                      ["1: Study a little bit of everything.",
                       "2: Focus on the topic you are doing the worst in.",
                       "3: Screw studying! I'm just going to watch YouTube videos instead!"],
                      ["""In a last bit of preparation, you study a little bit of everything. +15 to all understanding!""",
                       """In a last bit of preparation, you study your weakest topic extensively. +35 to your weakest understanding!""",
                       """Are you kidding me? That's literally the worst possible decision you could make. Maybe that's what you would do
in real life, but this is a game! All it takes to study in this game is to push a button, and you couldn't even do that! I'm not even going
to give you extra energy, because it does not really even matter at this point."""])

day_3_midnight = Event("33", """It is again getting quite late. You should probably go to bed...""", "Continue",
                       ["1: Go to bed.", "2: Pull an all-nighter."],
                       ["""You head to bed immediately in order to feel well-rested for your exam tomorrow.""",
                        """You pull an all-nighter trying to cram as much information into your head as possible, but to no avail.
In fact, you now feel so tired that you're probably going to do worse on the exam! -10 to all understanding."""])

Event_list = [tutorial_event, tutorial_event_2, tutorial_event_3, tutorial_event_4, day_1_dawn, day_1_noon, day_1_dusk,
              day_1_midnight, day_2_noon, day_2_dusk, day_2_midnight, day_3_dawn, day_3_noon, day_3_dusk, day_3_midnight]

default_state = State(tutorial_event, 80, 30, 30, 30, 30, 0)

start_server(default_state)
