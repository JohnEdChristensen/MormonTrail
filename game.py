import time
import sys
helpMessage = "try the 'hint' command"
def checkInput(prompt,hintMessage="try a command in 'quotes'"):
    ans = ''
    while True:
        
        ans = raw_input(prompt + "\n" + ">" )
        if ans == "help":
            print helpMessage
        elif ans == "hint":
            print hintMessage
        else:
            break
    return ans
def matchInput(prompt, answer):
    while True:
        if answer == checkInput(prompt):
            break
def wait(num=3):
    for i in range(num):
        time.sleep(0.5);
    print
def main():
    print "------------------------------------"
    print "Welcome to Mormon trail"
    print "type 'help' for a list of commands"
    print "type 'hint' if you get stuck"
    print "------------------------------------"

    name = checkInput("What is your name?")

    print "\n\n"

    print "You just finished packing all of your belongings into a small wagon as you prepare for the long journey to the west."
    wait(3)
    print "You are a part of a group of Mormons that have been pushed out from your homes in Nauvoo."
    wait(3)
    print "This group is lead by the acting president of the church - Brigham Young"
    wait(3)
    matchInput("type 'begin' to start your journey","begin")

    print "\n\n"
    print "We were told that we would be able to cross Iowa in 4-6 weeks and then cross the Mississippi River, but it seems like we are never going to do it that quickly. The incessant rains have made the ground extremely muddy and difficult to cross."
    wait(3)
    while True:
        prompt =  "\nDo you 'wait' for the ground to dry, possibly falling behind the rest of the group, or do you push forward to 'continue' through the difficult terrain."
        answer = checkInput(prompt);
        if answer == "wait":
            behind()
            break
        elif answer == "continue":
            mud_covered()
            break

def behind():
    print "\n\n"
    fellbehind = True
    print "Some members of the group give you disapproving looks as they pass your wagon, but you are confident that you will be able to catch up when the rain subsides and the ground drys."
    wait(3)
    print "You wake up and find the ground conditions have only improved slightly, You likely won't be able to wait any longer if you want to catch up with the rest of the group"
    prompt =  "\nDo you 'wait' for or 'continue' through the difficult terrain."
    answer = checkInput(prompt)
    while True:
        if answer == "wait":
            print "You have fallen to far behind and are forced to turn around and return home"
            break
        elif answer == "continue":
            caught_up()
            break

def mud_covered():
    print "\n\n"
    fellbehind = False
    print "As you fall knee deep into the cold mud you wonder if you should have waited for the ground to dry, but at least you haven't fallen behind the group"
    chast()

def caught_up():
    print "\n\n"
    print "Although it took a few very long days you were able to successfully catch up with the group"
    wait()
    print "When you reconvened with the group you find out that Brigham Young has been chastising those that have been holding the group back."
    wait()
    print "You want to avoid falling behind from now on."
    sing()
def chast():
    print "\n\n"
    print "You overhear that Brigham Young has been chastising those that have been holding the group back."
    wait()
    print "You are glad that you have managed to keep up so far"
    sing()
def sing():
    print "\n\n"
    print "Temperatures begin to drop."
    wait(3)
    print "You can't decide if you grateful or resentful, while the nights are difficult to sleep through, the mud is frozen in the morning making the trek much easier."
    wait(3)
    print "While on the trail someone began singing a song that I have never heard before:"
    wait()
    print "Come, come, ye Saints, no toil nor labor fear;"
    wait()
    print "But with joy wend your way."
    wait()
    print "Though hard to you this journey may appear,"
    wait()
    print "Grace shall be as your day..."
    wait(6)
    coldMorning();
def coldMorning():
    print "\n\n"
    print "The next night is painfully cold"
    wait()
    print "You don't sleep for the entire night"
    wait()
    print "Finally the sun rises and you get warm enough to sleep"
    wait()
    print "In what feels like no time at all your are awoken to the sounds of the group getting ready to leave"
    prompt = "\nDo you 'sleep' or wake up and 'continue' with the group?"
    answer = checkInput(prompt)
    while True:
        if answer == "sleep":
            quarters_late()
            break
        elif answer == "continue":
            quarters()
            break
def quarters():
    print "\n\n"
    print "You arrive at the location that will later be known as Winter Quarters"
    wait()
    print "You need to quickly build shelter to survive the quickly approaching winter"
    wait() 
    print "Some members of the group are building crude cabins, while others fear that there is not enough time for even that and begin digging trenches in the side of a hill for their winter shelter"
    wait()
    prompt = "\nWill you build a 'cabin' or dig a 'trench'?"
    answer = checkInput(prompt)
    while True:
        if answer == "cabin":
            cabin()
            break
        elif answer == "trench":
            trench()
            break
def quarters_late():
    print "\n\n"
    print "Without the help of the rest of the group you can't make as much progress and fall further and further behind"
    wait()
    print "Eventually you reach what would later be known as Winter Quarters"
    wait()
    print "You see a few partially constructed cabins huddled in groups around the camp, you also see trenches that have been dug into the hillside that will serve as shelter for the winter."
    print "Because you have arrived late, there is no time to build a cabin, you must dig a trench."
    wait()
    trench()

def cabin():
    print "The cabin turned out suprisingly well, while it will be difficult winter, you are confident you will survive it."
    print "Despite your confidence, many members of the group got sick over the winter, and many died."
    wait()
    selected()
def trench():
    print "The nights are unbearably cold."
    wait()
    print "You badly regret falling behind and not being able to adequately prepare for the winter."
    wait()
    print "Many of the people in the group that were living in similar conditions got sick and died over the frigid winter."
    selected()
def selected():
    print "\n\n"
    print "You managed to survive the winter and find out that Brigham Young has selected you to be a member of the team that will be the first to make the rest of the Journey west across the Rocky Mountains."
    wait()
    print "The team consists of those that are considered proficient in pioneering skills" 
    wait()
    print "This smaller team makes progress much faster than the large group did in crossing Iowa"
    wait()
    print "One of your primary concerns in the expedition is running into hostile Native American Indians"
    wait()
    print "You encounter an Indian tribe known as the Pawnee"
    wait()
    print "While many members of the team express their distrust of the tribe, You overhear Brigham Young explaining that the Pawnee were much less likely to cause harm than the Sioux Indian tribe."
    wait() 
    prompt = "\nDo you 'enter' the Pawnee village of 'stay back' and set up camp away from the tribe?"
    answer = checkInput(prompt)
    while True:
        if answer == "enter":
            village()
            break
        elif answer == "stay back":
            depart()
            break
def village():
    print "\n\n"
    print "As you enter the village it is immediately obvious that the Pawnee have suffered great losses recently"
    wait()
    print "Nearly half of their settlement has been burned down."
    wait()
    print "They explain to us that the Sioux have been attacking their settlement"
    wait()
    depart()
def depart():
    print "\n\n"
    print "The team continues onward, no with extra suspicion of the various native tribes."
    wait()
    print "But with the help and direction of the Pawnee, the team is able to quickly navigate the remaining portion of the expedition."
    print "As you come over a particularly steep hill, you are met with the site of the desert like salt lake valley."
    print "Congratulations you survived!"
    raw_input()

fellbehind = True
if __name__ == '__main__':
    main()
