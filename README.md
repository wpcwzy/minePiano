# minePiano

## 软件功能
配合地毯端假人自动用音符盒弹奏MIDI文件

## 依赖
1. [Mido](https://mido.readthedocs.io/en/latest/) MIDI库 安装方法：`pip3 install mido`
2. [TISUnion/PlayerInfoAPI](https://github.com/TISUnion/PlayerInfoAPI) 安装方法：仓库中已自带该文件，如需更新请自行下载替换

## 使用
1. 使用 `!!piano load + <midi_filename>` 来加载MIDI文件
2. 使用 `!!piano log + <tone> + <x> <y> <z> ` 记录每个音符盒的坐标 `<tone>` 的取值请参考 [MIDI音符对应表](https://blog.csdn.net/claroja/article/details/104247327)
3. 使用 `!!piano player + <player_name>` 来指定演奏者
4. 站在合适的位置后，使用 `!!piano play` 开始演奏

* <del>教程视频还在咕，剪辑完成后将上传</del>

## 注意事项
1. 为防止无意中破坏音符盒，开始演奏后演奏者游戏模式将变为 生存模式
2. 请尽量避免同时演奏两个音符，否则可能影响演奏效果
## TODO
- [x] 解析MIDI文件
- [x] 记录每个音符对应的假人头部偏转角度
- [x] 自动控制假人转头
- [ ] 加入多声部支持