import util
from termcolor import colored


def press_enter():
    input(colored("Press Enter to continue...", "red"))


def choose_hero():
    print(colored("""
    Choose your hero:
    1. Jack Sparrow 
    2. Elizabeth Swann
    3. Will Turner \n
    """, "yellow"))


def win_screen():
    print(colored("""
               .7G&@@@@@&BY!.                                                                      
             :G@@&GY?!7YG&@@@Y.                                                                    
            P@@B^         .Y@@@7                                                                   
           G@@J             :&@@!                                                                  
          ~@@B               ?@@&                                                                  
          !@@Y               !@@&                                                                  
          .&@&.     .7G#&&B^ #@@J                                                                  
           :#@&!   ^@@@@@@@GB@@Y  ..:^~!!!!!!~^::.                                                 
             7&@@G?5B@@@@@@@@@@#&&&&&##BBGGGGB##&&&&#GY!:                                          
               :JB&&@@@@@@@&B5J7~:..            ..:^!JG#&@&P!.                                     
                 .!B@@&P?^.     ..^~!?JJJJ7!~^:..       .^JB@@&5^                                  
              .?#@@B?:.   .:~JG#&@@@@@@@@@@@@@@@&#GY7^.     .!G@@&J.                               
            ~B@@G!.   .:?G&@@@@@@@@@@@@@@@@@@@@@@@@@@@&BJ^.    .J&@@G:                             
          7&@B!.   .^5&@@@@@@@#BPY?7~~^^^^^~!7J5G#&@@@@@@@#Y^    .J@@@P.                           
        ~&@G^    :J&@@@@@#57^77                  ..:!YB&@@@@@#7.   :B@@@!                          
      .G@G:    ^P@@@@@G7:.   ^&?:?. ..........         .:!P&@@@&J.  .5@@@Y                         
     !@&!    ^G@@@@#7.   .. .55@57Y~ ...... .GG.^~....     .~P@@@&7   5@@@P                        
    5@B. . .Y@@@@#~.  ..... .J5&@GP&^ .... .7J#Y5^J#7?. ...   :5@@@G. .B@@@5                       
   B@5. . .B@@@@7.  .........:B&#@B#@^ ... .?.~&!~&JJ^........  :G@@#: ^@&G@7                      
  B@P. . .B@@@B:  .....   ... .PP&@@#?. .GY    :.~?!J. .      ..  7@@&: G@Y#@.                     
 5@&. .  P@@@G. .... .7~:. ... :P5@@#:!:.&B  .?^  .?!.....:^75BB:  !@@#.?@G?@5                     
~@@7 .. !@@@B. .... .?YYPB7.. .Y~ Y@@&#P.&5 :?~ .JBJ: . ^&GY#G^YG.  Y@? ~@&!#&                     
B@&. . .B@@&.       ~?YGB?:.   ^JY7&@@@@Y&P~?~:JG?.  ... JP:!Y^^~.. :&? ~@&!P@~                    
@@P .. ^@@@J.......!BJ!!?~ ..:^::^!B&&#&@@#!JPBJ::~?7^.  .!~.    .. .#5 ?@&!Y@7                    
@@! .. ?@@&5J?7777!?YY?!~!!!7J555555Y&P5@#57BP!~!7!:....:.   ....... 57 G@B~Y@?                    
@@~ .. J@@B^~~~!~!77J5PY777777?JYYJG##@@@@YJ~^75J7!!!7777~. ..  .....: ^@@J~5@7                    
@@? .. 7@@B          .^:   :~!!7?YP&#Y&@@#75J~7777!~^:..   ~?:::..... .B@B!~#@^                    
&@#. . :@@&. ....        ...::^!7?JY#B?7~^!G!~J?~::^~!!^..^5555P: ..  Y@&7~7@#                     
B@@7 .. G@@7 .. :5J77JG#? . .:~^^^Y#B#5BG~^55~!55J~.    :5PGY~!!...  ?@&7~~G@!                     
~@@&: . ^@@&. ...~~7G&&5~:...  .7G5^7J?~P&7~P!!!!~?YJ~. ^7^Y?B~ .. .5@&7~~J@P                      
 P@@#: . 7@@P. . .5#G5YB&B. . :PY: :57. ?@BY7?.~J?..^?5Y. ..~: .  ^#@B!~~7@B                       
 .&@@&^   J@@P. . .~7Y5?^. ..  .  .~:   7&:JPY~ .!J.  :~. .     .Y@@Y~!~?@B                        
  .&@@@7.  7@@B:   ~G^.   .. .~: ..     !&: !GG:...:..   ..   :Y@@G7~~!5@5                         
   .#@@@B^  :B@@J.    ......^Y#5Y#.:~^. .?.  :#&?5^ ....   .~P@@P7~~~?#&~                          
     P@#B&G~  ~#@@5^   ... ~5:BGJB.PG!!    . .G@GYJ~.   .^?B@&5!~~~7B@Y           .:^~!??JJJ7~.    
      !&&55BG?:.^5&@#J:.   ...^.!Y!7BY ...... .:J?G&:.^!7~^...?Y!?B&5.   .:!JPB&&@@@&&&#####&@@&P:
        7#&PJ5GGJ~:^7PBGJ~:.      .::.....      ?PG57!^. .    ^&&&G!^?G&@@@@@&#G5J7!!!~~~~~~~#@@@@!
          ^G&&PJYPGG5J77???!~:..         ..:~?JY5Y!:.    ^5?YPP5B@@@@@@#B5J7!~~~~!7777!!!!~7B@@@@@&&
            .J&&#PYJY5PGBBGGGGP5YYJJYY5GB##@#!:.  .:     ^55Y5GB#&BPJ7~~~!7JY5PGPP5YYJ?!!?PBPP@@@@@@
               :?P###BP5YYYYY5PPPPPPPPP5YJ7B#: ..~B&7^.~JB&&&B5J!~~!?YPBBBGP5J?7!!!~~~75BB?. J@@@@&&
                   :!JPB###BGP5555PPPPPGGBG5&@&&&BYJ5B##B5?!~~7JPB###G5J7!!~~~!!!~~75#&G~..!#@@@@@?
                        .:!J5GB&&&&@@@@@@@@@&@&PPGBBPJ!~~7JPB###GY?!!~~~!!!!!~~!?P#@#J: .J&@&B&@@Y 
                                ...:^:::^!YB&@&G5?!~!?5B##BGY?!~~~!!!!!!!~~~!JG&@&P~..~G&#5Y#@@@?  
                                     .!P&@&#57~~7JG#&#G5?!~~~!!!!!!!!~~~!?P#@@@G!. :?B#Y~?#@@@#:   
                                 .!P&@@#57~~7YB#&#PJ7!~~!!!!!!!!!~~~!?P#@@@&P~. .~Y5?:^J&@@@#!     
                              :Y#@@&P?!~7YB&&#PJ!~~~!!!!!!!!!~~~7JP#@@@@#J^. ..^!^..!B@@@@P^       
                           ~P&@@#Y7~!JG#&#PJ!~~~!!!!!!!!~~~!7YG&@@@@#5~..........~P@@@@B7.         
                        ^P@@@#Y!~!YB&#GJ7~~~!!!!!!!~~~!7JPB&@@@@BY~..^?B&?  ..~P&@@@B7.            
                      !&@@#Y7~~JB&#57!~~!!!!!!~~~!7J5B&@@@@&P?^::!Y#@@&P^.:7G@@@&P!.               
                    ^&@&P7~~~J##57~~!!!!~~~!!?YG#&@@@@&BJ~:^!YB&@@&G?^:~5&@@@B?:                   
                   ?@@P!~!!!JGJ~~~~~~!7?YG#&@@@@@#P?~:. .G&@@@&P?~^75#@@@BJ:                       
                  :@@&?!!!!!?77JY5G#&&@@@&&B5?~:..   ..^5BPJ?7?5#@@@@B?:                           
                  .@@@@&&&&&&&&&##BG5?!^:...       ...^7J5B&@@@@&P!.                               
                   7@@5^~~!!~^^^:.         ...:^!?5B&@@@@@@#57:                                    
                    ^#@G7^:^^^^~~~^^~!7J5PG#&@@@@@@@&B5?^.                                         
                      ^P&@@&&&&&@@@@@@@@@@@@&#GY7^:.                                               

""", "yellow"))


def print_end_game():
    print(colored('''                                                                                                      
                                            .:^~!!!!~^.                                             
                                       :7P#@@@@@@@@@@@@@#J:                                         
                                     ?&@@@@@@@@@@@@@@@@@@@@#~                                       
                                   .&@@@@@@@@@@@@@@@@@@@@@@@@B.                                     
                                   &@@G@@@@@@@@@@@@@@@@@@@@@@@@:                                    
  .^                              5@@G&@@@@@@@@@@@@@@@@@@@@@@@@&                                ~.  
  ~@Y                            ^@@@?@@@@@@@@@@@@@@@@@@@@@@@@@@Y                              Y@~  
  .@@&^                          J@@5#@@@@@@@@@@@@@@@@@@@@@@@@@@@.                           ~&@@.  
   7@@@G.                        J@&5@@P~^~!?G@@@@@@BJ!~!J#@@5&@@.                         .G@@@7   
    Y@@@@J                       7@GG@&       ?@@@@Y       #@PB@&                         J@@@@J    
     ?@@@@&!                     :@GY@@.      B@#&@@!      &@#B@^                       7&@@@@7     
      ^@@@@@#~                    ~!G@@#:  ^5@@&  G@@&Y^.:J@@@G7                      !&@@@@@^      
       .B@@@@@#~                  :@@@@@@@@@@@@~   P@@@@@@@@@@@@^                   !&@@@@@B.       
         !@@@@@@&!                 J@@&BG&@@@@&.Y: :@@@@@@#G&@&J                  ?&@@@@@&!         
           5@@@@@@&J.                ^Y~  &@@@@@@@P&@@@@@!.P5                  :5@@@@@@@Y           
            .G@@@@@@@B~              .@@Y ~@@@@@@@@@@@@&~:@@5                !B@@@@@@@P.            
              :P@@@@@@@&Y:            7@@^ 5G&@G@##@5#@: B@@.             ^P@@@@@@@@P.              
                .5@@@@@@@@&J:         ^@@G 7^5G^G77B.^5. @@J           :5&@@@@@@@&J.                
                   7#@@@@&B&@&J.      ^@@@7.##:#G^&J!&J:#@@:        :5&@&B&@@@@#!                   
                     :P@@@@#PG&@&Y^    :5&@@@@#@@&@@&@@@@B!      ~P&@&GG&@@@&Y.                     
                        ~B@@@@BPG&@@G7.   !&@@@@@@@@@@@P.    :J#@@&GP#@@@@G^                        
                          .7B@@@@BGG&@@&G!. ^77!!~!7?7.  :?B@@@#GG#@@@@G!.                          
                             .7G@@@@&BB#@@@&G?:     .^Y#@@@&#GB&@@@&P~                              
                                 ^5&@@@@&#B&@@@@&G?5#@@&###&@@@@#J:                                 
                   ?#&&&B?.         .~5&@@@@&BBB&@@@@&#GB&&@#J^          ~P#&&&P.                   
                  :@@@@@@@@Y       .:!Y#&BB#@@@@&#GPGB&@@@@&P7^.       ^&@@@@@@@5                   
                   5&@&!Y@@@# .JG&@@@@&#BP55###&&@@@@&#GPPGB&@@@@&B5~ 7@@@#~G@@#:                   
           :^:  ^^ .??.:^!@@@&JP5JY5PG#&@@@@@&G?. :75#@@@@@@&BGPPPYPPB@@@G:^ ~?~ :^. .::.           
         Y@@@@#7@@&5@@#G@#?@@@@B^#@@@@@&GY!:.          .^?P#&@@@@@J~@@@@GJ@@5@@&P@@GY@@@@B          
        :@@@@@@:G@@@@@@@@@&Y@@@77#5?^.                       .:!YG#.&@@&?@@@@@@@@@@:#@@@@@J         
         #@@@P~^^!PGBGGGGGY &@@5                                   .@@@~^PGGGGGGP?^~:Y@@@@^         
          7G#BY^            ~@@@!.JY~                         .?5~.G@@#            ~5G#BY.          
                             G@@@@@@@:                        G@@@@@@@:                             
                              7#&@@&P                         ~#&@@&P:                              

    HA HA HA! Your Pirate adventure is finished,
    and your crew belongs to Davy Jones now!
    You LOSE!
    ''', "yellow"))


def game_name():
    print(colored("""




                                                   .                                                
                              .:^~!?JY~       .?B##BY.   .JYJ?!~^::.                                
                     ..^:   .Y#&&&&&&&#P!    .Y&&&&&&Y. :5&&&&&&&&&#J    .~:.                       
           ,:7!.    ^G&&B! .Y&&&BY7?B&&#!     7#&&&&&?  !P##5P&&&G&@&J. ^P&&#BG5?^                  
      .:!YG#&&&GJ^ :5&&&#?  ~G&&5. :P&&G:     J&&#G&&5.   .~.J&&B7YPJ~. ~B&&&#&&&#7     .           
    ^5#&&&&#G#&&#7  ?#&&G:  .P&&5:.~G&&#7    :G&&PJ&&#7      J&&#!       J&&#7!G&BY^  .!GP?^.       
   ~G&&&G7^.^G&&G:  ~B&&P:  .P&&##&&&&#P~    7#&#7~G&&5.     J&&#!       J&&#! .:   .J#&&&&&#P?:    
   ~P&&&5.  :G&&P.  ~B&&G:  .P&&#BB&&&J.    .5&&BYJP&&#!     J&&#!       J&&#Y!:     7&&&5YG#&&B~   
    :P&&5.  :G&&G^  ~B&&G:  .P&&5:^G&&5.    ~B&&&&&&&&&5.    J&&#!       J&&&&&5.    7#&&? .J#&&Y:  
    :P&&5.  ~B&&&?  ~B&&G:  .P&&P. Y&&B~   .Y&&#?^^~Y&&#7    J&&#!       J&&#JJ?.   ^P&&&Y. .:!J^   
    :P&&5?YG#&&&5:  ~B&&P:  :G&&B! !#&&B7 .J&&&#?  .Y&&&B7  !B&&&?      .Y&&#!       ~G&&&#5?!~:    
    :P&&&&&&##B?    7#&&#7 .Y&&&&5..P&&#7  ^G##P:   ~G##5:  !B&&&P^     7#&&#!  ^.    !Y5G#&&&&?    
    :P&&B57^...    :P&&&B~  ^PBGY^  ^^:.    ....     ...     ~J5Y^      !#&&&G5G&B?. ..   .!G&&#J.  
    :P&&5.          ^5GY~                                                !5G#&&&&G~  J#GJ: .5&&B~   
    :P&&5.                                                                  .:^7!.  :5&&&5^^P&&P.   
    :P&&G~                                                                           :5#&&&#&&&G^   
    ~B&&&P^                                                                            .~JG#&G?~:   
    7#&&#7                                                                                 .^       
     ~Y7:                                                                                           



                                                          """, "cyan"))

    press_enter()


def intro_story():
    print(colored("""

    As the fearless captain of the Black Pearl, 
    you venture into uncharted waters 
    to recover your priceless treasure 
    from the treacherous Barbossa....
                                    .~P?@G:                                                         
                                 :!B&P!^!7?~:.                                                      
                                 :@&Y.                                                              
                                 :G^ .      .:~?77^.                                                
                              :~: .!   ..^7J???7!~!~~^.                                             
                           .^^:  .:G7~?J??77!~^:::~~~~~~:.:..                                       
                      ...:~7!~7?JJ7?#~~~^^^^:^^~^:::^^::^7BY~:                                      
                 ...   .^~!JY!!~^^^:P5:^^^::::^^^^^:::::.::^:                                       
          .:...:^.   ^:.    .!^^:^^:^#!:^:::^:~~:^::...:::^:!.                                      
     .7JY7^.  ^~.^^~^: :^    .7:::::.?B          ......^:^!77^:.                                    
        :5577^.   .^?!~^G     7.::..~7BJ??           .:~!??^::.                                     
          !55PJ!.     ..YG^^. ! .:. Y#BB&Y      ..:::... .?             ^^~~^                       
           ^57!!5Y7.   ~7&PB#YJ!:.   .7GJ..::::..        .P57:    .:^!?YPJ7!~!~:                    
            ^!!~^^!7J7~JYB@PJ:..^^...:^B#^              :Y#@#7~??J??7~^^^^^^^^~!!.             :.   
             ~~~.::::!75?~@5:^^:::..   5@J         .:!!~!7P@&77!~~^^^^^^^:^^:^^^^~.          :?:.   
             :!:: :^^!::7J#@7.         ?G@:   .~JGGP5??J7!75#Y~~^^^^^::^:^^^::::^.!        :7~   .: 
             :7^! .^:~^~!^^&#J!.      .?7&#   .. ..^7!~^~~^?Y&~~~~^^^^^:^^~~:...:.~:     .!!..:^^^: 
             7~..  ..  .  :B@!!5Y~     !^7@~         :~!~!~^~&P^::. ....:^^^^..: .~: .:~JY!^:..     
          .:..             7&G.:7YY7.  ^ :B&           ^7!!:~?&.          .:^:::.^?7!JBY.           
      ..^G&G~        ..... :7&:..: ~GJ^! .7@?           ^?!:~:#5          .::^^.^~..!7.             
    .?J~:5@@G    ~7~.      :.PB     .~Y#7.:B@.           !. .:!@^          ~!~^~..7P&               
       .^7&@G7YY5@#B#.     . !&? .    ::YG::@P           :  ::^#&...  .. .:~7^..!?:!?               
       ^?5GBG5YG#&&&#7Y~^^^!.7YB. ::   :!5:.5@^          ^  ~^^!&7     7^!:  .!?!?P:                
      :#&GGGPBG&5#GB#P&J^&~G75B^P!~G!7:~?B..^&&        .7.  ::..PB.  :!7~^^^?PGG@B.                 
       ^PGY#P&BP&5&B@&PG!YPJG7GP5B7B5~7J5P :~?&7     .::     ^  ~BG!J5B@&PJ777GB~                   
         P#GBY&#B@#@&BJ~~~!?G5!~YJ?^!5PY^^?J~.~YJ!!^..       ?!YJJ5#PJ??7~~JBG.                     
          B#J#YBGY#5#B#Y^:!J7~!~??Y^^YPY:.!P?^.J5!!YY~..  :7BJ!.^G&P~JGPB&@@B.                      
           5YP#5&G#B#&&&P!:~!^~7~~~^~7!~!Y&&BY77!J#&#?~7?JB#5?Y5#@&&@@@@@@@@?                       
           .Y##&####@@&&&&&#5J????JJJ???JJYY55PGBGGGGGGGBBBGB####&##&&&@@@@@~                       
            .5B&##@&##&&&&B&#5J?!!~~^^~::^:~777JGB55PGGGBB###&&@@&@@&@@@@@@B.                       
             G#BG#5#GGB#@@@B&P??7!!~:^^^:..^~!!?J555PJ5P7#JG#&#GPB&G!^?G#@&~                        
    ....:::.:B@B@#5B&##&&@@#&PYJ?7!!!^^~~?YY5PPPGGG@5:^YYG?P7YB&BGGGGY5P#&#7.                                          
                        """, "yellow"))

    press_enter()


def game_rules():
    print(colored("""
    Game Rules:
    1. Collect RUM (R) and GOLD (G) to keep your crew in good mood and health.
    2. Collect CANON_BALLS (C) - they will be useful for the final fight.
    3. Find the KEY (K) to go to the next level.
    4. To use an item from your INVENTORY press I.
    5. Give the winds the right direction, 
       use the keys to move: W, S, A, D.
     """, "yellow"))

    press_enter()


def first_board_rules():
    print(colored("""
    Hints:
    1. Watch out for opponents - KRAKEN (%) and  WHALES (W).
    2. You can move between seas using whirlpools (O).
    3. Collect useful items - RUM (R), GOLD (G), CANON_BALLS (C).
    4. Remember to find the KEY.
    """, "yellow"))

    press_enter()


def second_board_rules():
    print(colored("""
    Hints:
    1. Be careful when crossing the stormy waters there are MERMAIDS (M) and ROCKS (^) on it.
    2. Find a friendly Tia Dalma (T), maybe she can help.
    3. Collect useful items - RUM (R), GOLD (G), CANON BALLS (C).
    4. Remember to find the key.
    """, "yellow"))
    press_enter()


def third_board_rules():
    print(colored("""
    Hints:
    1. Watch out for the treacherous Barbossa (B).
    2. Collect useful items - RUM (R), GOLD (G), CANON BALLS (C).
    3. Use the CANON BALLS to sink Barbossa.
    """, "yellow"))

    press_enter()


def start_game():
    util.clear_screen()
    game_name()
    util.clear_screen()
    intro_story()
    util.clear_screen()
    game_rules()
    util.clear_screen()
