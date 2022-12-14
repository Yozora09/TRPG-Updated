#intro ni Goddess Eris-chan
from charName import *
from pygame import mixer

pygame.mixer.init()
sfx = mixer.Sound(r'sfx\select.mp3')
goddessBgm = mixer.Sound(r'sfx\goddessTheme.mp3')

def introductionBoy1():
    goddessBgm.play()
    goddessBgm.set_volume(0.5)
    print("\n\n")
    print(" ╔██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██╗ ")
    print("██                                                                                                                                                                      ██")
    print(" ║                                                                                             ..                                                                       ║ ")
    print("██                                                                            .:::==+++++++++==-:.                                                                      ██")
    print(" ║                                                                         =+*+++-::....:::-++++**.                                                                     ║ ")
    print("██                                                                        .**+=-.....       .=+++#=                                                                     ██")
    print(" ║                                                                        :==-::.            .:-***                                                                     ║ ")
    print("██                                                                        =**=:    .          ..:**:                                                                    ██")
    print(" ║                                                                       .**=.     :   .:       .-**                                                                    ║ ")
    print("██                                                                       -*+.    .:: ..::.....  ..**.                                                                   ██")
    print(" ║                                                                      -+*.....::...... ....:   .+*-                                                                   ║ ")
    print("██                                                                     +##+:...:-***-..   .:::.. .+#=.                                                                  ██")
    print(" ║                                                                   .+###*=...:=-=-:.   .::-:....-#*-                                                                  ║ ")
    print("██                                                                  :******. .:-==:.         .-.:-.:.*#*                                                                ██")
    print(" ║                                                                .=*+++**:.. :-::::..     .--: -:::..*#+                                                               ║ ")
    print("██                                                              .-++++++*-..::::.:-:---:::--=-.::-:-.-:**:  .                                                           ██")
    print(" ║                                                            .=++=:.   ..::-:. ..:-::::::---::-.:::.    .:                                                             ║ ")
    print("██                                                          .-+*++***=:.:..:.: ..:+...::::::::-*-..                                                                     ██")
    print(" ║                                                        .:-++++-:  .:: .:.:.  .=*:    -*: ..-*=.:.        .                                                           ║ ")
    print("██                                                      .:...::==-=.+#*.....:  .:.:+.   :*. ..=*#+..   .                                                                ██")
    print(" ║                                                    -=++**+=-:==:*=...:::-   .::-+-....:..-+=++..       ....:..                                                       ║ ")
    print("██                                                    -********+*=.:... :.:=....-:=++=:. ::=++-::...+-:::-**=..*+=-:                                                    ██")
    print(" ║                                                      :=+******=:.. .--.:-..:..:+++++==+++++:....:#=:-++****==+++*+:                                                  ║ ")
    print("██                                                         :=+=-:-=:---:-=:.... :=*+++++++++++*+*+=:::..-++++=-=+++++-.:                                                ██")
    print(" ║                                                             ..--:::..==+=-:-:=**++++*++++******++=.:.:-.     :==-..                                                  ║ ")
    print("██                                                              ...::..--===++=++*#**************+++===..:.       ...                                                   ██")
    print(" ║                                                             ........:--==++++**#**************+++===...:                                                             ║ ")
    print("██                                                            .........---== .+****+++**********+***+==: ..:                                                            ██")
    print(" ║                                        ╔═════════════════════════════════════════════════════════════════════════════════════╗                                       ║ ")
    print("██                                        ║     Greetings! I am known as the Goddess Eris. I am the protector of this world.    ║                                       ██")
    print(" ║                                        ║    You must be wondering why you are here. To be honest I am the one who sent you   ║                                       ║ ")
    print("██                                        ║   here and I would like to apologize for that. See, this world has been corrupted   ║                                       ██")
    print(" ║                                        ║    by darkness and I need someone to fight darkness alongside with me. That's why   ║                                       ║ ")
    print("██                                        ║    I have chosen you to be part of my mission. Please, for the sake of this world   ║                                       ██")
    print(" ║                                        ║                      and its inhabitants I beg you to help me.                      ║                                       ║ ")
    print("██                                        ╚═════════════════════════════════════════════════════════════════════════════════════╝                                       ██")
    print(" ╚██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██╝ ")

    proceedKey =  input("\n\nPress any key to proceed...")
    sfx.play()
    goddessBgm.stop()
    characterNameBoy1()


def introductionBoy2():
    goddessBgm.play()
    goddessBgm.set_volume(0.5)
    print("\n\n")
    print(" ╔██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██╗ ")
    print("██                                                                                                                                                                      ██")
    print(" ║                                                                                             ..                                                                       ║ ")
    print("██                                                                            .:::==+++++++++==-:.                                                                      ██")
    print(" ║                                                                         =+*+++-::....:::-++++**.                                                                     ║ ")
    print("██                                                                        .**+=-.....       .=+++#=                                                                     ██")
    print(" ║                                                                        :==-::.            .:-***                                                                     ║ ")
    print("██                                                                        =**=:    .          ..:**:                                                                    ██")
    print(" ║                                                                       .**=.     :   .:       .-**                                                                    ║ ")
    print("██                                                                       -*+.    .:: ..::.....  ..**.                                                                   ██")
    print(" ║                                                                      -+*.....::...... ....:   .+*-                                                                   ║ ")
    print("██                                                                     +##+:...:-***-..   .:::.. .+#=.                                                                  ██")
    print(" ║                                                                   .+###*=...:=-=-:.   .::-:....-#*-                                                                  ║ ")
    print("██                                                                  :******. .:-==:.         .-.:-.:.*#*                                                                ██")
    print(" ║                                                                .=*+++**:.. :-::::..     .--: -:::..*#+                                                               ║ ")
    print("██                                                              .-++++++*-..::::.:-:---:::--=-.::-:-.-:**:  .                                                           ██")
    print(" ║                                                            .=++=:.   ..::-:. ..:-::::::---::-.:::.    .:                                                             ║ ")
    print("██                                                          .-+*++***=:.:..:.: ..:+...::::::::-*-..                                                                     ██")
    print(" ║                                                        .:-++++-:  .:: .:.:.  .=*:    -*: ..-*=.:.        .                                                           ║ ")
    print("██                                                      .:...::==-=.+#*.....:  .:.:+.   :*. ..=*#+..   .                                                                ██")
    print(" ║                                                    -=++**+=-:==:*=...:::-   .::-+-....:..-+=++..       ....:..                                                       ║ ")
    print("██                                                    -********+*=.:... :.:=....-:=++=:. ::=++-::...+-:::-**=..*+=-:                                                    ██")
    print(" ║                                                      :=+******=:.. .--.:-..:..:+++++==+++++:....:#=:-++****==+++*+:                                                  ║ ")
    print("██                                                         :=+=-:-=:---:-=:.... :=*+++++++++++*+*+=:::..-++++=-=+++++-.:                                                ██")
    print(" ║                                                             ..--:::..==+=-:-:=**++++*++++******++=.:.:-.     :==-..                                                  ║ ")
    print("██                                                              ...::..--===++=++*#**************+++===..:.       ...                                                   ██")
    print(" ║                                                             ........:--==++++**#**************+++===...:                                                             ║ ")
    print("██                                                            .........---== .+****+++**********+***+==: ..:                                                            ██")
    print(" ║                                        ╔═════════════════════════════════════════════════════════════════════════════════════╗                                       ║ ")
    print("██                                        ║     Greetings! I am known as the Goddess Eris. I am the protector of this world.    ║                                       ██")
    print(" ║                                        ║    You must be wondering why you are here. To be honest I am the one who sent you   ║                                       ║ ")
    print("██                                        ║   here and I would like to apologize for that. See, this world has been corrupted   ║                                       ██")
    print(" ║                                        ║    by darkness and I need someone to fight darkness alongside with me. That's why   ║                                       ║ ")
    print("██                                        ║    I have chosen you to be part of my mission. Please, for the sake of this world   ║                                       ██")
    print(" ║                                        ║                      and its inhabitants I beg you to help me.                      ║                                       ║ ")
    print("██                                        ╚═════════════════════════════════════════════════════════════════════════════════════╝                                       ██")
    print(" ╚██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██╝ ")

    proceedKey =  input("\n\n\nPress any key to proceed...")
    sfx.play()
    goddessBgm.stop()
    characterNameBoy2()


def introductionGirl1():
    goddessBgm.play()
    goddessBgm.set_volume(0.5)
    print("\n\n")
    print(" ╔██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██╗ ")
    print("██                                                                                                                                                                      ██")
    print(" ║                                                                                             ..                                                                       ║ ")
    print("██                                                                            .:::==+++++++++==-:.                                                                      ██")
    print(" ║                                                                         =+*+++-::....:::-++++**.                                                                     ║ ")
    print("██                                                                        .**+=-.....       .=+++#=                                                                     ██")
    print(" ║                                                                        :==-::.            .:-***                                                                     ║ ")
    print("██                                                                        =**=:    .          ..:**:                                                                    ██")
    print(" ║                                                                       .**=.     :   .:       .-**                                                                    ║ ")
    print("██                                                                       -*+.    .:: ..::.....  ..**.                                                                   ██")
    print(" ║                                                                      -+*.....::...... ....:   .+*-                                                                   ║ ")
    print("██                                                                     +##+:...:-***-..   .:::.. .+#=.                                                                  ██")
    print(" ║                                                                   .+###*=...:=-=-:.   .::-:....-#*-                                                                  ║ ")
    print("██                                                                  :******. .:-==:.         .-.:-.:.*#*                                                                ██")
    print(" ║                                                                .=*+++**:.. :-::::..     .--: -:::..*#+                                                               ║ ")
    print("██                                                              .-++++++*-..::::.:-:---:::--=-.::-:-.-:**:  .                                                           ██")
    print(" ║                                                            .=++=:.   ..::-:. ..:-::::::---::-.:::.    .:                                                             ║ ")
    print("██                                                          .-+*++***=:.:..:.: ..:+...::::::::-*-..                                                                     ██")
    print(" ║                                                        .:-++++-:  .:: .:.:.  .=*:    -*: ..-*=.:.        .                                                           ║ ")
    print("██                                                      .:...::==-=.+#*.....:  .:.:+.   :*. ..=*#+..   .                                                                ██")
    print(" ║                                                    -=++**+=-:==:*=...:::-   .::-+-....:..-+=++..       ....:..                                                       ║ ")
    print("██                                                    -********+*=.:... :.:=....-:=++=:. ::=++-::...+-:::-**=..*+=-:                                                    ██")
    print(" ║                                                      :=+******=:.. .--.:-..:..:+++++==+++++:....:#=:-++****==+++*+:                                                  ║ ")
    print("██                                                         :=+=-:-=:---:-=:.... :=*+++++++++++*+*+=:::..-++++=-=+++++-.:                                                ██")
    print(" ║                                                             ..--:::..==+=-:-:=**++++*++++******++=.:.:-.     :==-..                                                  ║ ")
    print("██                                                              ...::..--===++=++*#**************+++===..:.       ...                                                   ██")
    print(" ║                                                             ........:--==++++**#**************+++===...:                                                             ║ ")
    print("██                                                            .........---== .+****+++**********+***+==: ..:                                                            ██")
    print(" ║                                        ╔═════════════════════════════════════════════════════════════════════════════════════╗                                       ║ ")
    print("██                                        ║     Greetings! I am known as the Goddess Eris. I am the protector of this world.    ║                                       ██")
    print(" ║                                        ║    You must be wondering why you are here. To be honest I am the one who sent you   ║                                       ║ ")
    print("██                                        ║   here and I would like to apologize for that. See, this world has been corrupted   ║                                       ██")
    print(" ║                                        ║    by darkness and I need someone to fight darkness alongside with me. That's why   ║                                       ║ ")
    print("██                                        ║    I have chosen you to be part of my mission. Please, for the sake of this world   ║                                       ██")
    print(" ║                                        ║                      and its inhabitants I beg you to help me.                      ║                                       ║ ")
    print("██                                        ╚═════════════════════════════════════════════════════════════════════════════════════╝                                       ██")
    print(" ╚██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██╝ ")

    proceedKey =  input("\n\n\nPress any key to proceed...")
    sfx.play()
    goddessBgm.stop()
    characterNameGirl1()

def introductionGirl2():
    goddessBgm.play()
    goddessBgm.set_volume(0.5)
    print("\n\n")
    print(" ╔██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██╗ ")
    print("██                                                                                                                                                                      ██")
    print(" ║                                                                                             ..                                                                       ║ ")
    print("██                                                                            .:::==+++++++++==-:.                                                                      ██")
    print(" ║                                                                         =+*+++-::....:::-++++**.                                                                     ║ ")
    print("██                                                                        .**+=-.....       .=+++#=                                                                     ██")
    print(" ║                                                                        :==-::.            .:-***                                                                     ║ ")
    print("██                                                                        =**=:    .          ..:**:                                                                    ██")
    print(" ║                                                                       .**=.     :   .:       .-**                                                                    ║ ")
    print("██                                                                       -*+.    .:: ..::.....  ..**.                                                                   ██")
    print(" ║                                                                      -+*.....::...... ....:   .+*-                                                                   ║ ")
    print("██                                                                     +##+:...:-***-..   .:::.. .+#=.                                                                  ██")
    print(" ║                                                                   .+###*=...:=-=-:.   .::-:....-#*-                                                                  ║ ")
    print("██                                                                  :******. .:-==:.         .-.:-.:.*#*                                                                ██")
    print(" ║                                                                .=*+++**:.. :-::::..     .--: -:::..*#+                                                               ║ ")
    print("██                                                              .-++++++*-..::::.:-:---:::--=-.::-:-.-:**:  .                                                           ██")
    print(" ║                                                            .=++=:.   ..::-:. ..:-::::::---::-.:::.    .:                                                             ║ ")
    print("██                                                          .-+*++***=:.:..:.: ..:+...::::::::-*-..                                                                     ██")
    print(" ║                                                        .:-++++-:  .:: .:.:.  .=*:    -*: ..-*=.:.        .                                                           ║ ")
    print("██                                                      .:...::==-=.+#*.....:  .:.:+.   :*. ..=*#+..   .                                                                ██")
    print(" ║                                                    -=++**+=-:==:*=...:::-   .::-+-....:..-+=++..       ....:..                                                       ║ ")
    print("██                                                    -********+*=.:... :.:=....-:=++=:. ::=++-::...+-:::-**=..*+=-:                                                    ██")
    print(" ║                                                      :=+******=:.. .--.:-..:..:+++++==+++++:....:#=:-++****==+++*+:                                                  ║ ")
    print("██                                                         :=+=-:-=:---:-=:.... :=*+++++++++++*+*+=:::..-++++=-=+++++-.:                                                ██")
    print(" ║                                                             ..--:::..==+=-:-:=**++++*++++******++=.:.:-.     :==-..                                                  ║ ")
    print("██                                                              ...::..--===++=++*#**************+++===..:.       ...                                                   ██")
    print(" ║                                                             ........:--==++++**#**************+++===...:                                                             ║ ")
    print("██                                                            .........---== .+****+++**********+***+==: ..:                                                            ██")
    print(" ║                                        ╔═════════════════════════════════════════════════════════════════════════════════════╗                                       ║ ")
    print("██                                        ║     Greetings! I am known as the Goddess Eris. I am the protector of this world.    ║                                       ██")
    print(" ║                                        ║    You must be wondering why you are here. To be honest I am the one who sent you   ║                                       ║ ")
    print("██                                        ║   here and I would like to apologize for that. See, this world has been corrupted   ║                                       ██")
    print(" ║                                        ║    by darkness and I need someone to fight darkness alongside with me. That's why   ║                                       ║ ")
    print("██                                        ║    I have chosen you to be part of my mission. Please, for the sake of this world   ║                                       ██")
    print(" ║                                        ║                      and its inhabitants I beg you to help me.                      ║                                       ║ ")
    print("██                                        ╚═════════════════════════════════════════════════════════════════════════════════════╝                                       ██")
    print(" ╚██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██╝ ")

    proceedKey =  input("\n\n\nPress any key to proceed...")
    sfx.play()
    goddessBgm.stop()
    characterNameGirl2()

