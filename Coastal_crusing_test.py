

print("Identify the following boat parts")

questions = ["Turnbuckle", "Chain plate","Stem Fitting","Transom",
                "Through Hull Fitting","Seacock","Binnacle","Cockpit lockers",
                "Bilge","Companionway","Stairway from cockpit to cabin"]

answer_choices = ('')


correct_choices =   ["device which adjusts the tension in the stays & shrouds","straps which attaches the shrouds to the hull",
            "strap which attaches forestay to the hull","the flat surface of the hull at the stern",
            "fitting designed to take in or discharge water through the hull","valve on a through hull fitting",
            "stand holding the steering compass","Storage area in the cockpit","Lowest part of boats interior",
            "Stairway from cockpit to cabin"]


answers =   ["device which adjusts the tension in the stays & shrouds",
            "straps which attaches the shrouds to the hull",
            "strap which attaches forestay to the hull",
            "the flat surface of the hull at the stern",
            "fitting designed to take in or discharge water through the hull",
            "valve on a through hull fitting",
            "stand holding the steering compass",
            "Storage area in the cockpit","Lowest part of boats interior",
            "Stairway from cockpit to cabin"]

def quiz():
    score = 0
    for question, choices, correct_choice, answer in zip(questions, answer_choices, correct_choices, answers):
        print(question)
        user_answer = input(choices).lower()
        if user_answer in correct_choice:
            print("Correct")
            score += 1
        else:
            print("Incorrect", answer)
    print(score, "out of", len(questions), "that is", float(score / len(questions)) * 100, "%")

if __name__ == "__main__":
    quiz()


# '2) Identify the following parts of an outboard engine' –
# 'line that truns over the moter' Starter cord
# 'changes the gears on a boat' Gearshift lever
# 'gives the moter power of fuel' Throttle
# 'drives water' 'Propeller'
#
# "3)The purpose of a safety harness, tether and jackline"
# " To help keep a person attached to the boat"
# #
# "4) When going forward on the side deck while sailing"
# "walk on the windward side of the boat"
#
# '5) The VHF International Distress, Safety and Calling channel is channel?' '16'
# #
# '6) The VHF Radio transmissions for imminent danger is?' 'Mayday, Mayday, Mayday'
#
# '6a) The VHF Radio transmissions when not in imminent danger is?' ' Pan-Pan'
#
# '7) The Marine Weather channels on a VHF  radio provide?' ' important weather information in U.S. Waters'
#
# '8) On a weather map winds are strongest when?' 'the isobars are close together'
#
# '9) In the U.S. The National Weather Service issues small craft advisories when?'
# 'forecast winds or sea conditions might be hazardous'
#
# '10) Rapidly falling barometric pressure is?'
# ' a sign of an approaching storm'
#
# '11) The federal carriage requirements for a 26-40 foot sloop with an outboard engine that may be sailed at night and in poor weather are?'
#  '''U.S.C.G. approved PFD’s for each person aboard \nOne type IV PFD (Throw able) \nFire extinguishers – Two B1 / or one B-II –
#   rated to extinguish petroleum based fires (Fuel / oil)n\
#   Navigation lights
# n\Visual distress signals (day & night)
# n\Sound signaling device'''
#
# '12) The A.S.A. equipment recommendations for the same boat:?'
# ''' Anchor and rode \n
#     First aid kit \n
#     Copy of local chart \n
#     Bailer or bilge pump \n
#     Workable compass \n
#     VHF Radio \n
#     Flashlights with extra batteries \n
#     Tool kit with spare parts \n
#     Soft wood plugs \n
#     Safety harness \n
#     Important tools for Coastal Navigation during a weekend cruise include a compass, navigation charts, and a timekeeping device'''
#
# '''13) Know the type of navigation lights (port bow, starboard bow, stern, steaming light, mast head light )
# required in the following situations. Include each lights color, position and arc of visibility.'''
#
# "Underway" Sailing - sidelights red port / green starboard / ahead to 112.5 degrees or 22.5 degrees abaft the beam / white stern light arc of 135 degrees
#
# "Underway" – Under power / motor sailing - same as sail plus white light (steaming light) forward at spreaders arc of 225 degrees
#
# "At Anchor" - All around 360 white light at masthead.
#
# "Navigation lights must be displayed between?" "sunset and sunrise and during periods of reduced visibility (Fog)"
#
# '14) Ships Horn – 5 short blasts' = Danger / Three short blasts = Operating astern propulsion
#
# "The recommended actions for retrieving a Man overboard under power is to" –
# "Keep the propeller away from the victim"
# """Approach heading to windward to not drift over the victim
# Once victim is secured to the boat shut down the engines"""
#
# DO NOT – have the victim climb up on the propeller
#
# '15) The recommended actions for a person who is overboard in cold water with a life jacket on waiting for a rescue are'
# "Float in the fetal “H.E.L.P” position"
#
# "16) Symptoms of moderate hypothermia are?" , "Incoherence, drowsiness, exhaustion, loss of muscular control"
#
# "17) The recommended treatment for moderate hypothermia "
# "Remove victim from the elements and apply external warmth"
# '17b) DO NOT ?''Massage extremities, administering fluids or alcohol'
#
# '18) Docking - The safest location for stepping off a boat while docking is ?' 'at the shrouds'
#
# '18b) Spring Lines?' 'Control boats movement forward and aft when docked'
#
# print('20) Know the right of way boat in the following situations is')
# '20a) Same Tack Situation ''The leeward boat'
# '20b) Opposite Tack Situation' 'The starboard tack boat'
# '20c) Overtaking Situation' 'The overtaken boat'
# '20b) Two head on powerboats'' Both must turn to starboard and pass port to port'
#
# '20e) If a collision is imminent''execute evasive action and sound 5 short blasts'
#
#
# '20f) Every vessel must maintain a lookout' 'at all times'
#
# '21) Heaving To ?' ' Method for crew to rest, make meals, make repairs'
#
# '22) Reefing ? ' 'Reducing mainsail area' 'Do it EARLY. Be sure to tension the luff  BEFORE tensioning leech.'
# 'Mainsail should be luffing when being reefed.'
#
# 'The best sail selection for heavy wind over 20 knots ?' 'reefed main and small headsail / For light wind use a full main and genoa.'
#
# "To depower the mainsail to? " "reduce excessive heeling ease the mainsheet or traveler"
#
# "When sailing in heavy weather DO NOT?" " change to a larger foresail"
#
# "23) Coast Guard recommendations when maneuvering in a restricted visibility (FOG) situation'
# 'Turn on navigation lights'
# 'Hoist a radar reflector'
# 'Slow down and use sound signals'
#
# 'Sailboats Fog (Reduced visibility) Signal is' ' (prolonged, short, short)'
#
#
# '24) The correct response to an onboard fire is to?' ' move crew upwind, have an escape route, engage the fire extinguisher.'
#
# '24b) The correct response to finding a cabin filling with water is to?' 'alert the crew and then immediately – Activate the bilge pumps'
#
# '24c) The immediate action that should take place when you foul your propeller is to?' ' shift to neutral'
#
# '24d) If the Engine High Temperature alarm sounds' 'check to see if water is flowing out of exhaust'
#
# '25) Two types of DIVE FLAGS:'
# '''A red field crossed by 1 diagonal white stripe
# A white field next to a blue field cut in a swallow’s tail'''
#
# "26) The responsibilities of a sailboat Skipper"
# " Safety of boat and crew "
# " Ensure crews knowledge of operation and location of all safety equipment "
# " Ensure safe use of equipment (head, stove etc.)"
#
# "27) Identify the following navigational aids "
# "Nun buoy" "conical top, even numbers, right side returning"
# "Can buoy" "cylinder, odd numbers, left side returning"
# "Preferred channel buoy" "Red & green horizontal stripes"
# "Mid channel , safe water buoy" "Red & white vertical stripes"
# "Starboard side day beacon" "Red triangle / even numbers"
# "Port side day beacon" "Green square / odd numbers"
# "Controlled Area" "White w/ orange circle"
# "Danger Buoy" " White w/ diamond & cross"
#
# "28) Use chart one to identify the following chart symbols."
#
# "Kelp"  			"J 13.2"
# "Wreck with only masts visible"  "K 29"
# "Current" 	 	"H 40"
# "Radio Tower" "E 29"
# "Nineteen foot sounding"  	"I 14"
#
# print ("To navigate the preferred channel on a chart, treat the preferred channel buoy as if it were fully the color of the TOP band")
#
#
# "29)The unit which measures distance on a nautical chart?" " a nautical mile (one minute of latitude)"
#
#
# "30) The most dangerous cloud type for sailors is considered to be?" "Cumulonimbus – High vertical columns of clouds usually with an anvil shaped top"
#
# "31) Garbage such as food scrapes and packaging can?" "never be dumped overboard"
#
# "32) Oily waste in the bilge ?"  " should be removed with approved absorbent pads"
#
# "33) The 4 best features of a safe anchorage are? "
# "Good holding ground"
# "Sufficient depth of water"
# "Shelter from waves and swells"
# "Room to swing at anchor"
#
# "34) Chain is used as part of your ground tackle to?"
# "Put more weight on the bottom"
# "Keep the anchors shank on the bottom so flukes dig in"
# "Keeps the rode from chafing on the bottom"
# "Acts as a shock absorber"
#
# "35) A rolling hitch is used?" " to reduce load on a line or anchor chain"
# "A round turn and two half hitches is used to secure a boat to a piling or ring"
# "A clove hitch is used to secure a fender to a lifeline"
# "A sheet bend is used to tie two lines of unequal diameter together"
#
#
# "36) The recommended proportion of scope to depth & freeboard for anchoring overnight? " " = 7 / 1 "
#
# "If you miss picking up a mooring ball on first attempt?" "Sail or motor around and try again"
#
# "37) Proper methods of freeing a small sailboat that is aground?"
# "Request a tow"
# "Use anchor as a kedge"
# "Heel the boat"
#
#
# '37) Proper methods of freeing a small sailboat that is aground'
# 'Request a tow'
# 'Use anchor as a kedge'
# 'Heel the boat'
#
# '38) The immediate action that should take place when Dragging anchor if you have room is?'  'to - - increase scope'
#
# 'The immediate action that should take place when – The Backstay fails – 'head upwind to reduce the strain on the mast'
#
# '39) When towing another vessel' 'use a bowline tied around a bridal at your stern'
#
# '40) To prevent unexpected engine failure you should perform a' ' daily engine check Water, oil, belt tension'
#
# '41) When using a smoke flare keep it?' 'low, downwind and away from the boat'
#
# '42) A right hand turning prop in forward will?' 'walk the stern to port when in reverse'
#
# '43)To refill the fuel tank of a boat that has a diesel engine you should'
# 'Estimate how much fuel is needed by checking the fuel gauge'
# 'Be sure you are pumping diesel vs. gasoline at the pump'
# 'Listen to the sound of the fuel fill pipe? so to ?'  'avoid over filling (spillage)''
#
# 'Before starting a diesel or gas engine ensure?' ' that the fuel supply is turned on'
