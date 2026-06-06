# ROS2 Turtle Figure-8 Project
## 项目简介

本项目基于ROS2 Lyrical与 ython实现了一个 TurtleSim 小乌龟控制节点，使小乌龟能够在屏幕中持续按照 Figure-8（8 字轨迹）运动。
这是我学习 ROS2 的基础项目，也是我第一次完整经历：

* ROS2 工作区创建
* Python 节点编写
* Launch 文件配置
* `colcon build` 构建
* GitHub 仓库管理与代码上传

## 项目目标
实现：
* 使用 ROS2 控制 TurtleSim 小乌龟运动
* 发布速度消息到 `/turtle1/cmd_vel`
* 实现小乌龟 **8 字轨迹（Figure-8）**
* 使用 Launch 文件一键启动节点
   最终效果：
---
## 技术栈

* `ROS2 Lyrical`
* `Python`
* `TurtleSim`
* `colcon`
* `Git / GitHub`
* `VS Code`
---

## 项目结构

text
my_turtle_pkg
├── launch
│   └── turtle_figure8_launch.py
├── my_turtle_pkg
│   ├── __init__.py
│   └── turtle_figure8.py
├── resource
│   └── my_turtle_pkg
├── test
├── package.xml
├── setup.cfg
├── setup.py
└── README.md

----------------------------------------------------------------------------

## 核心文件说明

### `turtle_figure8.py`
核心 ROS2 节点。
功能：
* 创建 ROS2 Node
* 发布 `Twist` 消息
* 控制小乌龟速度
* 实现 Figure-8 轨迹

----------------------------------------------------------------------------
### `turtle_figure8_launch.py`
Launch 文件。
作用：
一键启动 Turtle 节点，无需手动运行 Python 文件。
启动方式：
```bash
ros2 launch my_turtle_pkg turtle_figure8_launch.py
```
----------------------------------------------------------------------------

#### 项目运行方法
### 1. 打开工作区
```bash
cd ~/ros2_ws
```
### 2. 加载 ROS2 环境
```bash
source /opt/ros/lyrical/setup.bash
```
### 3. 加载工作区环境
```bash
source ~/ros2_ws/install/setup.bash
```
### 4. 编译工作区
```colcon build --symlink-install
colcon build --symlink-install
```

### 5. 启动 TurtleSim
打开一个新终端：
```bash
ros2 run turtlesim turtlesim_node
```
会出现 TurtleSim 小乌龟窗口。

### 6. 启动 Figure-8 节点
再打开一个终端：
```bash
source /opt/ros/lyrical/setup.bash
source ~/ros2_ws/install/setup.bash
ros2 launch my_turtle_pkg turtle_figure8_launch.py
```
运行后：
小乌龟会自动开始运动，并持续画出 **8 字轨迹**。

### 7. 查看消息

查看速度控制消息：

```bash
ros2 topic echo /turtle1/cmd_vel
```
可以看到持续发布的速度消息。

----------------------------------------------------------------------------

## 我遇到的问题
## 1. Python 环境问题
问题：
`numpy` 冲突
`base` 环境影响 ROS2
 Python 版本混乱
解决：学会使用```bashconda deactivate‘’‘退出 `base` 环境。

## 2. colcon build 报错
问题：
`setup.py` 格式错误。
解决：重新检查括号、引号和 Python 

## 3. launch 文件找不到
问题：launch 文件没有被安装到：
解决：修改 `setup.py`：反复调节，靠gpt给个范本先跑起来，然后再手动复现


## ChatGPT 对我的作用

诚实地说，在这个项目中，ChatGPT 的作用非常大。

它帮助我：

* 理解 ROS2 工作区结构
* 一步一步配置环境
* 修复 `setup.py`
* 理解错误信息
* 调试 launch 文件
* 学会 Git 和 GitHub 上传流程
* 用 VS Code 编辑项目
陪我一点点排错和理解。我几乎从头至尾都是教我的。GPT大爷燃尽了


-------------------------------------------------------------------------

## 我的收获

完成这个项目后，我已经能够独立打开并且完成项目流程了，小乌龟法igure8 节点的python代码反而是现在最难复现的了，因为我的python代码功底一般，之前还花时间补充了C语言。然后现在和深度学习焦头烂额的，还在弄catia。之前算法也还在攻克。文科都没有学过，真的及力了。


