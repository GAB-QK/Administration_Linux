
#!/usr/bin/python

import os
import sys

pwnd = '$6$fl6jcP1ZHKR9Duo.$55gSb.ejlm.v2scAc8MRkkI67pvxMZdB0na/Kw1svnRDJIHnWB9PwbnfJc1xXumC3OJ13acHDyoJP1ojzZ9pz0'
salt = 'fl6jcP1ZHKR9Duo.'
wordlist = open('/home/gabrielqaddaha/Bureau/administration linux/french_mdp.txt', 'r').readlines()

for line in wordlist:
    clear = line.strip()
    stream = os.popen("mkpasswd -m sha-512 -S " + salt + " " + clear)
    output = stream.read().strip()

    if(pwnd == output):
        print('''

                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~

\033[1;31m
 Ur pwd has been
______ _    _ _   _______ 
| ___ \ |  | | \ | |  _  \\
| |_/ / |  | |  \| | | | |
|  __/| |/\| | . ` | | | |
| |   \  /\  / |\  | |/ / 
\_|    \/  \/\_| \_/___/  

          By D4rk_H4x0r 
\033[1;0m''')
        print('password is : \033[1;41m' + clear + '\033[1;0m\n')
        print('u lazy nub kek')

        exit()

print('too bad... password not found')