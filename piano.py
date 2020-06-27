import mido
from imp import load_source

Prefix = '!!piano'
#mid = mido.MidiFile('./plugins/nyan.mid')
mid = None
PlayerInfoAPI = load_source('PlayerInfoAPI','./plugins/PlayerInfoAPI.py')

player=""
tone2pos={}

def print_message(server, info, msg, tell=True, prefix='[MinePiano] '):  # 输出信息方法
    msg = prefix + msg
    if info.is_player and not tell:
        server.say(msg)
    else:
        server.reply(info, msg)

def playMidi(server,info):
    global player
    server.execute("gamemode survival {}".format(player))
    for msg in mid.play():
        if msg.type=='note_on':
            
            server.execute("execute positioned as {} run tp {} ~ ~ ~ facing {}".format(player,player,tone2pos.get(msg.note)))
            server.execute("player {} attack once".format(player))

def on_user_info(server,info):
    global player,mid
    command = info.content.split()
    if len(command) == 0 or command[0] != Prefix:  # len()得到字符长度
        return

    del command[0]

    #!!piano
    if len(command) == 0:
        print_message(server,info,">_<")

    elif len(command) >= 1 and command[0] == 'play':
        print_message(server, info, "检测到!!piano play")
        playMidi(server,info)

    elif len(command) >= 1 and command[0] == 'log':
        print_message(server, info, "检测到!!piano log")
        if len(command) != 5:
            print_message(server,info,"输入有误，请按!!piano log <音高> <音符盒x> <y> <z> 格式输入")
        else:
            tone = int(command[1])
            x = int(command[2])
            y = int(command[3]) - 1
            z = int(command[4])
            tone2pos[tone]="{} {} {}".format(x,y,z)
            print_message(server,info,"音高{}的音符盒位置已被记录为{}|{}|{}".format(tone,x,y,z))
    
    elif len(command) >= 1 and command[0] == 'player':
        print_message(server, info, "检测到!!piano player")
        if len(command) != 2:
            print_message(server,info,"输入有误，请按!!piano player <player_name>格式输入")
        else:
            player=command[1]
            print_message(server,info,"演奏者已设置为{}".format(player))
    
    elif len(command) >= 1 and command[0] == 'load':
        print_message(server, info, "检测到!!piano load")
        if len(command) != 2:
            print_message(server,info,"输入有误，请按!!piano player <midi_name>格式输入")
        else:
            mid = mido.MidiFile('./plugins/{}.mid'.format(command[1]))
            print_message(server,info,"MIDI文件已加载为{}".format('./plugins/{}.mid'.format(command[1])))

        
    

def on_load(server,old):
	server.add_help_message('!!piano', '自动弹钢琴')