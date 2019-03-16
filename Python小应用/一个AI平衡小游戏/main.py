import gym
import numpy as np

# 设置一个 gym 环境
env = gym.make('CartPole-v1')


# 首先我们理解函数的定义，然后将游戏设置为开始状态
def play(env, policy):
    observation = env.reset()

    # 初始化一些变量以跟踪游戏是够已经结束，包括策略的总分以及游戏中每个步骤的快照
    done = False
    score = 0
    observations = []

    # 现在我们多次运行游戏，直到gym告诉我们游戏已经完成
    for _ in range(5000):
        observations += [observation.tolist()]  # 记录用于正则化的观察值，并回放

        # 如果模拟在最后一次迭代中结束，则退出循环
        if done:
            break

        # 根据策略矩阵选择一种行为
        outcome = np.dot(policy, observation)
        action = 1 if outcome > 0 else 0

        # 创建行为，记录反馈
        observation, reward, done, info = env.step(action)
        score += reward

    return score, observation


print('Traning Policy')

max = (0, [], [])
for _ in range(100):
    # 随机初始化策略
    policy = np.random.randn(1, 4) - 0.5
    # 根据策略和上面创建的环境，用它来玩游戏，获得一个分数
    score, observations = play(env, policy)

    if score > max[0]:
        max = (score, observations, policy)

print('Max Score', max[0], 'out of 500')

# 首先我们创建一个名为max的元组，它将存储我们迄今为止看到的最佳策略的得分，观察值和策略数组。
max = (0, [], [])

# 接着我们会生成和评估10个策略，并将最优策略保存在max中
for _ in range(10):
    policy = np.random.rand(1, 4)
    score, observations = play(env, policy)

    if score > max[0]:
        max = (score, observations, policy)

print('Max score', max[0])

# 展示
from flask import Flask
import json

app = Flask(__name__, static_folder='.')


@app.route('/data')
def data():
    return json.dumps(max[1])


@app.route('/')
def root():
    return app.send_static_file('./index.html')


app.run(host='127.0.0.1', port=8080)
