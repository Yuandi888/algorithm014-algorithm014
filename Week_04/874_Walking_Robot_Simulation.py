# 874. Walking Robot Simulation
# 874. 模拟行走机器人



# https://leetcode-cn.com/problems/walking-robot-simulation/solution/mo-ni-xing-zou-ji-qi-ren-by-leetcode/
class Solution(object):
    def robotSim(self, commands, obstacles):
        dx = [0, 1, 0, -1] # 在[上 右 下 左]不同方向前进一步，x轴坐标的变化
        dy = [1, 0, -1, 0] # 在[上 右 下 左]不同方向前进一步，y轴坐标的变化
        x = y = di = 0 # x,y表示初始位置，di表示方向，direction
        # 必须注意使用 集合 Set 作为对障碍物使用的数据结构，以便我们可以有效地检查下一步是否受阻。如果不这样做，我们检查 该点是障碍点吗 可能会慢大约 10000 倍。
        obstacleSet = set(map(tuple, obstacles)) #[[2,4],[3,5]] -> {(2, 4), (3, 5)}
        ans = 0

        for cmd in commands:
            if cmd == -2: #left
                di = (di - 1) % 4 # 除余得到方向[上 右 下 左]，转4次为一圈
            elif cmd == -1: #right
                di = (di + 1) % 4
            else:
                for k in range(cmd): # 每走一步判断一次碰撞
                    if (x+dx[di], y+dy[di]) not in obstacleSet:
                        x += dx[di]
                        y += dy[di]
                        ans = max(ans, x*x + y*y)
                    else:
                        break
        return ans