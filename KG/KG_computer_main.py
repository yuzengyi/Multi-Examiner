from py2neo import Graph,Node,Relationship,NodeMatcher

# uri = "http://localhost:7474"
# user = "neo4j"
# password = "Yuzeyu777"

# 删除
# MATCH (n) DETACH DELETE n

# ,(:Computer_Hardware {name:'辅助存储器',desc:''})

g=Graph('http://localhost:7474',name='neo4j',password='Yuzeyu777')
cypher_1 = ("CREATE (:Unit {name:'信息系统的支撑技术', desc:'在组成信息系统的五大要素中，硬件、软件和通信网络是其支撑技术,正是由于这些支撑技术的紧密配合，使得信息系统可以异时异地高效地收集、分析与处理数据，满足不同用户的需求。随着移动网络与物联网的发展，移动终端、传感与控制等在支撑技术中变得越来越重要，其硬件与软件呈现出不可分割的特点，且便捷化程度、智能化程度越来越高。',type:'程序性知识'}),"
            "(:Supporting_Technologies_for_Information_Systems {name:'计算机硬件',desc:'计算机硬件是信息系统中最主要的组成部分，主要负责对信息进行加工、处理和存储。计算机硬件主要由运算器、控制器、存储器、输入设备和输出设备五大部件组成。从外观上看，计算机一般由主机、显示器、键盘和鼠标组成，在主机中最重要的部件是主板，它将计算机中的各个部件紧密连接在一起，在主板上有中央处理器(CentraProcessing Unit，简称CPU)、内存条和适配器的插槽等，许多主板还同时集成了声卡、显卡和网卡等设备。计算机的性能主要由CPU、存储器等部件的性能指标决定。',type:'元认知知识'}),"
            "(:Supporting_Technologies_for_Information_Systems {name:'计算机软件',desc:'软件是相对硬件而言的，它是指在计算机上运行的程序及其数据和文档的总和。计算机的硬件与软件密不可分，如果将人类躯体比作硬件，人类的思想就好比软件，没有躯体，思想是无法存在的，没有思想的躯体也只是一个植物人。计算机也与此类似，没有主机等硬件，软件是无法存在的，而一个没有软件的计算机是不能工作的，没有安装任何软件的计算机被称为裸机。根据软件所起的作用不同，计算机软件可分为系统软件和应用软件等。',type:'程序性知识'}),"
            "(:Supporting_Technologies_for_Information_Systems {name:'移动终端',desc:'移动终端是指可以在移动中使用的计算机设备，广义地讲，包括POS机、手机、PDA和平板电脑等。移动终端作为简单通信设备伴随移动通信发展已有几十年的历史，早在1973年摩托罗拉公司就发明了移动电话。2007年开始，移动智能终端的出现引发了颠覆性变革，揭开了移动互联网产业发展的序幕，人们能随时随地使用移动智能终端接入互联网。随着移动互联网的快速发展，平板电脑、智能手机等移动智能终端的使用越来越普及。',type:'元认知知识'}),"
            "(:Supporting_Technologies_for_Information_Systems {name:'传感与控制',desc:'',type:'事实性知识'}),"
            "(:Supporting_Technologies_for_Information_Systems {name:'网络系统',desc:'',type:'事实性知识'}),"
            "(:Computer_Hardware {name:'中央处理器',desc:'中央处理器(CPU)是计算机最核心的部件，它由运算器和控制器组成。在一块超大规模集成电路上包含了实现控制器和运算器功能所需的全部电路，现代处理器芯片中还包含浮点处理部件(FPU)、内部高速缓冲存储器(Cache)和存储管理部件，以加快计算机执行指令的速度。CPU是计算机的核心部件它的性能指标主要由主频、字长、核心数量、高速缓存等参数决定。',type:'程序性知识'}),"
            "(:Computer_Hardware {name:'存储器',desc:'存储器的功能是存放程序和数据，CPU执行的指令和需要运算的操作数及运算结果都存储在存储器中。存储器按用途可分为主存储器(内存)、辅助存储器(外存)和高速缓冲存储器。存储器也是计算机的核心部件，CPU执行的指令和需要运算的操作数及运算结果都存储在存储器中。存储器的存储容量、读写速度都是影响存储器性能的重要指标。',type:'事实性知识'}),"
            "(:Computer_Hardware {name:'主存储器',desc:'主存储器也就是内存。内存是计算机硬件的一个重要部件，通常分为只读存储器Read-Only Memory，简称ROM)和随机存取存储器(Random Access Memory，简称RAM)两种，两者之间最大的区别是在关闭电源后，RAM中的信息会丢失，而ROM中的信息仍然会保留。目前内存容量在GB级，大量数据的保存还需要辅助存储器来完成。',type:'事实性知识'}),"
            "(:Computer_Hardware {name:'辅助存储器',desc:'常见的辅助存储器有硬盘和闪存盘。硬盘是由金属磁盘制成，在磁盘上通过磁性介质磁化时不同的极性方向表示二进制数据的0和1，断电后，磁化后的介质极性方向不会改变，因此断电后仍然能够保留存储在硬盘中的数据。硬盘的容量很大，目前在TB级。而固态硬盘(SolidSateDisk,简称SSD)也是一种存储器，采用闪存(FLASH芯片)作为存储介质，具有传统机械硬盘不具备的快速读写、重量轻、能耗低以及体积小等特点，而在外形、尺寸、接口、功能和使用方法上与普通硬盘完全相同，目前容量接近TB级。闪存盘(USBFlashDisk，简称U盘)也是以闪存作为存储介质，采用通用USB接口，即插即用，存储容量在GB级，方便携带，可以满足不同的需求。',type:'事实性知识'}),"
            "(:Computer_Hardware {name:'高速缓冲存储器',desc:'',type:'事实性知识'}),"
            "(:Computer_Hardware {name:'输入设备',desc:'常用的输人设备有键盘和鼠标，它们的主要功能是将程序和数据以机器能识别和接受的信息形式输人计算机。输入输出设备中，兼具输入输出功能的，主要有声卡、网卡、光盘驱动器等。声卡的功能是将声音在数字信号和模拟信号间进行转换网卡是计算机与网线之间的接口，光盘驱动器是计算机用来读写光盘内容的设备。',type:'概念性知识'}),"
            "(:Computer_Hardware {name:'输出设备',desc:'常用的输出设备有显示器和打印机，它们的主要功能是将计算机处理的结果以人们能接受的信息形式输出。输入输出设备中，兼具输入输出功能的，主要有声卡、网卡、光盘驱动器等。声卡的功能是将声音在数字信号和模拟信号间进行转换网卡是计算机与网线之间的接口，光盘驱动器是计算机用来读写光盘内容的设备。',type:'概念性知识'}),"
            "(:Computer_Software {name:'系统软件',desc:'系统软件是指控制和协调计算机及外部设备，支持应用软件开发和运行的软件，负责管理计算机系统中各种独立的硬件，使得它们可以协调工作。随着计算机硬件性能的不断提高，计算机的运行速度越来越快，为了提高计算机硬件的使用效率，采用了系统软件实现对多个运行程序的管理，而操作系统是最重要的系统软件。',type:'程序性知识'}),"
            "(:Computer_Software {name:'应用软件',desc:'应用软件是为了某种特定用途而开发的软件，可以满足用户不同领域、不同问题的应用需求，如办公软件、工具软件、娱乐软件管理软件等等。应用软件是利用计算机的软、硬件资源为解决某一应用领域的某个实际问题而专门开发的软件。它可以满足用户的特定需求，拓宽计算机系统的应用领域。',type:'概念性知识'}),"
            "(:Computer_Software {name:'操作系统',desc:'目前常用的计算机操作系统有Windows、MacOSLinux、Unix等。操作系统的主要功能是对计算机系统的全部软、硬件和数据资源进行统一控制、调度和管理，使得它们可以协调工作，便于计算机使用者和其他软件将计算机当作一个整体而不需要顾及底层每个硬件是如何工作的。',type:'事实性知识'}),"
            "(:Computer_Software {name:'办公软件',desc:'办公软件满足用户在文字处理、表格制作、幻灯片制作、图形图像处理简单数据库处理等方面的常见办公需求。',type:'元认知知识'}),"
            "(:Computer_Software {name:'工具软件',desc:'工具软件则满足用户在系统维护、系统美化、图像编辑、音视频处理等方面的专业工作需求。',type:'事实性知识'}),"
			"(:Mobile_Terminal {name:'移动终端的硬件与软件',desc:'移动终端同普通计算机一样，也是由硬件和软件组成。硬件普遍采用计算机经典的体系结构，软件也分为系统软件和应用软件。由于移动终端要求较小的尺寸、较低的功耗、较高的性能，但性能的提高往往意味着尺寸和功耗都会增加，因此，尺寸、功耗与性能三者之间需要合理平衡。同时，移动终端的软件和硬件也要互相匹配、紧密融合，才能使性能更佳。',type:'概念性知识'}),"
			"(:Mobile_Terminal {name:'移动终端的硬件',desc:'移动终端的中央处理器是整个设备的控制中枢系统和逻辑控制中心，通过运行存储器内的软件及调用存储器内的数据库，实现语音处理、输入输出控制等。移动终端常见的中央处理器有苹果、三星、高通（Qualcomm)、英特尔( Intel )、英伟达(Nvidia)、联发科(MTK)等，麒麟CPU是我国首款国产移动终端中央处理器。',type:'概念性知识'}),"
			"(:Mobile_Terminal {name:'移动终端的软件',desc:'移动终端的操作系统主要有安卓(Android)系统、苹果iOS系统、Windows系统等。移动终端的应用软件往往与工作、生活密切相关，针对性较强，如出游有专门的订票、订房APP，购物有专门的购物APP等。智能手机作为最常见的移动终端设备，有着丰富的移动应用软件，让我们在手机上就可以实现网上学习、听音乐、看视频、购物、订票、订房等，足不出户就能正常地生活、工作和学习。智能手机的移动支付功能正在使“无现金支付”成为当前消费方式的主流。通过安装支付宝、微信等软件，智能手机可以实现扫码支付;也可以通过使用Apple Pay、天翼支付等NFC( Near Field Communication，近距离无线通信)方式直接支付。便捷的消费支付方式吸引了越来越多的用户。',type:'概念性知识'}),"
			"(:Mobile_Terminal {name:'移动终端的工作原理',desc:'移动终端跟计算机一样，包括输入、处理（运算与控制)、存储和输出四个部分，其工作原理与计算机基本相同。同时，移动终端具备的“移动性”和“智能性”，使移动终端在工作时表现出更多的人性化功能和强大的多媒体特性。',type:'概念性知识'}),"
			"(:Mobile_Terminal {name:'移动终端的智能性',desc:'移动终端的“智能性”在硬件上主要基于传感器的植入。传感器增加了移动终端的自动检测与适应功能，使移动终端能根据不同人群的使用习惯自动做出调整。如手机中的光线传感器，一般位于手机前置摄像头附近，会根据所处环境的光线亮度来自动调整手机屏幕亮度。当检测到光线不足的时候，信息传递到手机系统，系统就会调低屏幕亮度，下降到人眼舒适的亮度，同时也起到省电的作用，而检测到光线比较充足的时候，信息传递到手机系统，系统又会调高屏幕亮度，使人们能清晰地看到屏幕上显示的内容。',type:'程序性知识'}),"
			"(:Mobile_Terminal {name:'移动终端的移动性',desc:'移动终端和移动APP的“移动性”，使一些与移动终端相关的应用在使用时有别于其在个人计算机上使用，并逐渐改变人们的一些行为习惯。如共享单车的使用，用户须借助移动终端中的APP程序扫描共享单车上的二维码信息，选择开始用车，经过租车系统确认之后，系统进行远程开锁，用户就可以使用单车了;当使用完毕后，用户只需手工将车子上锁，系统就会停止计费，完成租车过程，并可在APP程序中查看租车情况，借车、还车、付费流程都在一部手机上操作完成。',type:'程序性知识'})")
g.run(cypher_1)
cypher_2 = "MATCH (from:Unit{name:'信息系统的支撑技术'}),(to:Supporting_Technologies_for_Information_Systems{name:'计算机硬件'}) MERGE (from)-[r:包含]->(to)"
g.run(cypher_2)
cypher_3 = "MATCH (from:Unit{name:'信息系统的支撑技术'}),(to:Supporting_Technologies_for_Information_Systems{name:'计算机软件'}) MERGE (from)-[r:包含]->(to)"
g.run(cypher_3)
cypher_4 = "MATCH (from:Unit{name:'信息系统的支撑技术'}),(to:Supporting_Technologies_for_Information_Systems{name:'移动终端'}) MERGE (from)-[r:包含]->(to)"
g.run(cypher_4)
cypher_5 = "MATCH (from:Unit{name:'信息系统的支撑技术'}),(to:Supporting_Technologies_for_Information_Systems{name:'传感与控制'}) MERGE (from)-[r:包含]->(to)"
g.run(cypher_5)
cypher_6 = "MATCH (from:Unit{name:'信息系统的支撑技术'}),(to:Supporting_Technologies_for_Information_Systems{name:'网络系统'}) MERGE (from)-[r:包含]->(to)"
g.run(cypher_6)
cypher_8 = "MATCH (from:Supporting_Technologies_for_Information_Systems{name:'计算机硬件'}),(to:Computer_Hardware{name:'中央处理器'}) MERGE (from)-[r:包含]->(to)"
g.run(cypher_8)
cypher_9 = "MATCH (from:Supporting_Technologies_for_Information_Systems{name:'计算机硬件'}),(to:Computer_Hardware{name:'存储器'}) MERGE (from)-[r:包含]->(to)"
g.run(cypher_9)
cypher_10 = "MATCH (from:Supporting_Technologies_for_Information_Systems{name:'计算机硬件'}),(to:Computer_Hardware{name:'输入设备'}) MERGE (from)-[r:包含]->(to)"
g.run(cypher_10)
cypher_11 = "MATCH (from:Supporting_Technologies_for_Information_Systems{name:'计算机硬件'}),(to:Computer_Hardware{name:'输出设备'}) MERGE (from)-[r:包含]->(to)"
g.run(cypher_11)
cypher_12 = "MATCH (from:Computer_Hardware{name:'存储器'}),(to:Computer_Hardware{name:'主存储器'}) MERGE (from)-[r:属于]->(to)"
g.run(cypher_12)
cypher_13 = "MATCH (from:Computer_Hardware{name:'存储器'}),(to:Computer_Hardware{name:'辅助存储器'}) MERGE (from)-[r:属于]->(to)"
g.run(cypher_13)
cypher_14 = "MATCH (from:Computer_Hardware{name:'存储器'}),(to:Computer_Hardware{name:'高速缓冲存储器'}) MERGE (from)-[r:属于]->(to)"
g.run(cypher_14)
cypher_15 = "MATCH (from:Supporting_Technologies_for_Information_Systems{name:'计算机软件'}),(to:Computer_Software{name:'系统软件'}) MERGE (from)-[r:包含]->(to)"
g.run(cypher_15)
cypher_16 = "MATCH (from:Supporting_Technologies_for_Information_Systems{name:'计算机软件'}),(to:Computer_Software{name:'应用软件'}) MERGE (from)-[r:包含]->(to)"
g.run(cypher_16)
cypher_17 = "MATCH (from:Computer_Software{name:'系统软件'}),(to:Computer_Software{name:'操作系统'}) MERGE (from)-[r:属于]->(to)"
g.run(cypher_17)
cypher_18 = "MATCH (from:Computer_Software{name:'应用软件'}),(to:Computer_Software{name:'办公软件'}) MERGE (from)-[r:属于]->(to)"
g.run(cypher_18)
cypher_19 = "MATCH (from:Computer_Software{name:'应用软件'}),(to:Computer_Software{name:'工具软件'}) MERGE (from)-[r:属于]->(to)"
g.run(cypher_19)
cypher_20 = "MATCH (from:Computer_Software{name:'办公软件'}),(to:Computer_Software{name:'工具软件'}) MERGE (from)-[r:关联]->(to)"
g.run(cypher_20)
cypher_21 = "MATCH (to:Computer_Hardware{name:'主存储器'}),(to:Computer_Hardware{name:'高速缓冲存储器'}) MERGE (from)-[r:关联]->(to)"
g.run(cypher_21)
cypher_21 = "MATCH (to:Computer_Hardware{name:'主存储器'}),(to:Computer_Hardware{name:'辅助存储器'}) MERGE (from)-[r:关联]->(to)"
g.run(cypher_21)
cypher_22 = "MATCH (to:Computer_Hardware{name:'高速缓冲存储器'}),(to:Computer_Hardware{name:'辅助存储器'}) MERGE (from)-[r:关联]->(to)"
g.run(cypher_22)
cypher_23= "MATCH (from:Computer_Software{name:'应用软件'}),(to:Computer_Software{name:'系统软件'}) MERGE (from)-[r:前置]->(to)"
g.run(cypher_23)

cypher_24 = "MATCH (from:Supporting_Technologies_for_Information_Systems {name:'移动终端'}),(to: Mobile_Terminal {name:'移动终端的工作原理'}) MERGE (from)-[r:包含]->(to)"
g.run(cypher_24)
cypher_25 = "MATCH (from:Supporting_Technologies_for_Information_Systems {name:'移动终端'}),(to: Mobile_Terminal {name:'移动终端的硬件与软件'}) MERGE (from)-[r:包含]->(to)"
g.run(cypher_25)
cypher_26 = "MATCH (from:Mobile_Terminal {name:'移动终端的硬件与软件'}),(to: Mobile_Terminal {name:'移动终端的硬件'}) MERGE (from)-[r:包含]->(to)"
g.run(cypher_26)
cypher_27 = "MATCH (from:Mobile_Terminal {name:'移动终端的硬件与软件'}),(to: Mobile_Terminal {name:'移动终端的软件'}) MERGE (from)-[r:包含]->(to)"
g.run(cypher_27)
cypher_28 = "MATCH (from:Mobile_Terminal {name:'移动终端的硬件与软件'}),(to: Mobile_Terminal {name:'移动终端的软件'}) MERGE (from)-[r:包含]->(to)"
g.run(cypher_28)

cypher_29 = "MATCH (from:Mobile_Terminal {name:'移动终端的工作原理'}),(to: Mobile_Terminal {name:'移动终端的智能性'}) MERGE (from)-[r:包含]->(to)"
g.run(cypher_29)
cypher_30 = "MATCH (from:Mobile_Terminal {name:'移动终端的工作原理'}),(to: Mobile_Terminal {name:'移动终端的移动性'}) MERGE (from)-[r:包含]->(to)"
g.run(cypher_30)