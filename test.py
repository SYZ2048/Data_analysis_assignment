import pandas as pd

if __name__ == '__main__':
    filepath = './data.txt'
    data = pd.read_csv(filepath)
    print(data.shape)
    data.dropna(how='all', inplace=True)  # 清除全为空的行
    # print(data)
    res = 0
    cnt = 0
    # print(data.shape[0])
    # print(data[1])
    for idx in range(data.shape[0]-1):
        res += (data[idx+1][1]-data[idx][1])
        cnt += 1
    print(res/cnt)

