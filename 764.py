import numpy as np
class Solution:
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        # if the map is 1*1
        if N == 1:
            if [0,0] in mines:
                return 0
            else:
                return 1

        #if the map is 2*2, as long as one element is not zero, it should have no cross
        if N == 2:
            if len(mines)<4:
                #some are 1
                return 1
            else:
                return 0
        #general case when N >= 3
        original = self.get_map(N, mines)

        right_hands = self.get_right_hands(N, original)
        left_hands = self.get_left_hands(N, original)
        up_hands = self.get_up_hands(N, original)
        down_hands = self.get_down_hands(N, original)
        results = np.zeros((N,N))
        ans = 0
        for i in range(1, N-1):
            for j in range(1, N-1):
                temp = min([right_hands[i][j], left_hands[i][j],
                                     up_hands[i][j], down_hands[i][j]])
                if temp > ans:
                    ans = temp
                    
        if ans==0:
            for k in range(N):
                if original[0][k]==1:
                    return 1
                if original[N-1][k]==1:
                    return 1
                if original[k][0]==1:
                    return 1
                if original[k][N-1]==1:
                    return 1
    
        return ans
    

    def get_right_hands(self, N, original):
        right_hands = [[0 for x in range(N)] for y in range(N)]
        #先把右边倒数第二列搞好，如果这行最右边是1，那么他就是2
        column = N-2
        for i in range(1, N - 1):
            #从第二行循环到倒数第二行
            if (original[i][N-1] == 1 and original[i][N-2] == 1):
                #如果这个格子右边是1
                right_hands[i][column] = 2
            if (original[i][N-1] == 0 and original[i][N-2] == 1):
                #如果这个格子右边是1
                right_hands[i][column] = 1

        for c in range(N-3, 0, -1):
            #从倒数第三列循环到第二列
            for r in range(1, N-1):
                if original[r][c] == 1:
                    right_hands[r][c] = right_hands[r][c+1]+1
                    #比它右边原来的多一个
        return right_hands

    def get_left_hands(self, N, original):
        left_hands = [[0 for x in range(N)] for y in range(N)]
        #先把第二列搞好，如果第一列是1，那么他就是2
        column = 1
        for i in range(1, N - 1):
            #从第二行循环到倒数第二行
            if original[i][0] == 1 and original[i][1] == 1:
                #如果这个格子右边是1
                left_hands[i][column] = 2
            if original[i][0] == 0 and original[i][1] == 1:
                #如果这个格子右边是1
                left_hands[i][column] = 1

        for c in range(2, N-1):
            #从第三列循环到倒数第二列
            for r in range(1, N-1):
                if original[r][c] == 1:
                    left_hands[r][c] = left_hands[r][c-1]+1
                    #比它左边原来的多一个
        return left_hands

    def get_up_hands(self, N, original):
        up_hands = [[0 for x in range(N)] for y in range(N)]
        #先把第二行搞好，如果第一行是1，那么他就是2
        row = 1
        for i in range(1, N - 1):
            #从第二列循环到倒数第二列
            if original[0][i] == 1 and original[1][i] ==1:
                #如果这个格子上边是1
                up_hands[row][i] = 2
            if original[0][i] == 0 and original[1][i] ==1:
                #如果这个格子上边是1
                up_hands[row][i] = 1

        for r in range(2, N-1):
            #从第三行循环到倒数第二行
            for c in range(1, N-1):
                if original[r][c] == 1:
                    up_hands[r][c] = up_hands[r-1][c]+1
                    #比它上边原来的多一个
        return up_hands



    def get_down_hands(self, N, original):
        down_hands = [[0 for x in range(N)] for y in range(N)]
        #先把第二行搞好，如果第一行是1，那么他就是2
        row = N-2
        for i in range(1, N - 1):
            #从第二列循环到倒数第二列
            if original[N-1][i] == 1 and original[N-2][i] ==1:
                #如果这个格子上边是1
                down_hands[row][i] = 2
            if original[N-1][i] == 0 and original[N-2][i] ==1:
                down_hands[row][i] = 1

        for r in range(N-3, 0, -1):
            #从第三行循环到倒数第二行
            for c in range(1, N-1):
                if original[r][c] == 1:
                    down_hands[r][c] = down_hands[r+1][c]+1
                    #比它下边原来的多一个
        return down_hands

    def get_map(self, N, mines):
        m = [[1 for x in range(N)] for y in range(N)]
        for i in range(len(mines)):
            index_r = mines[i][0]
            index_c = mines[i][1]
            m[index_r][index_c] = 0
        return m

