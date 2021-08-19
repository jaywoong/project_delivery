import pandas as pd
from sklearn import preprocessing
import pickle

from config.settings import DATA_DIRS
#
# kp = pickle.load(open('./data/kp.pkl','rb'))
# samples = pd.read_csv('./data/samples.csv', header=0, index_col=False);


class Kprototypes:
    def analysis(self, hjd, induty, bjd, monthsales, monthcall, pricePerCall, time):

        # 데이터 준비
        kp = pickle.load(open(DATA_DIRS[0]+'/data/kp.pkl','rb'))
        # f2 = open(DATA_DIRS[0]+'\\data\\samples.csv', header=0, index_col=False);
        # kp = pickle.load(open('./data/kp.pkl','rb'))
        samples = pd.read_csv(DATA_DIRS[0]+'/data/samples.csv', header=0, index_col=False);

        # 리스트 형태로 입력
        store = [hjd, induty, bjd, monthsales, monthcall, pricePerCall, time]

        # 샘플에 취합
        samples = samples.append(pd.Series(store, index=samples.columns), ignore_index=True)
        samples['DLVR_STORE_ADSTRD_CODE'] = samples['DLVR_STORE_ADSTRD_CODE'].astype('str')

        # 원핫인코딩(더미 변수)
        label_encoder = preprocessing.LabelEncoder()
        onehot_encoder = preprocessing.OneHotEncoder()
        onehot_hjdCode = label_encoder.fit_transform(samples['DLVR_STORE_ADSTRD_CODE'])
        onehot_induty = label_encoder.fit_transform(samples['DLVR_STORE_INDUTY_NM'])
        onehot_bjdCode = label_encoder.fit_transform(samples['DLVR_STORE_LEGALDONG_NM'])
        samples['DLVR_STORE_ADSTRD_CODE'] = onehot_hjdCode
        samples['DLVR_STORE_INDUTY_NM'] = onehot_induty
        samples['DLVR_STORE_LEGALDONG_NM'] = onehot_bjdCode

        # 정규화
        samples = preprocessing.StandardScaler().fit(samples).transform(samples)

        # 군집분석
        kp_labels = kp.predict(samples, categorical=[3])
        store_lable = kp_labels[-1]

        if store_lable == 0:
            result = ' 0 '
            print(' 0번 입니다~~~~!!!! ')
        elif store_lable == 1:
            result = ' 1 '
            print(' 1번 입니다~~~~!!!! ')
        elif store_lable == 2:
            result = ' 2 '
            print(' 2번 입니다~~~~!!!! ')
        else:
            result = ' 3 '
            print(' 3번 입니다~~~~!!!! ')

        return result


if __name__ == '__main__':
    kp = Kprototypes()
    kp.analysis('41190742', '치킨', '산현동', 73000, 100, 9000, 1300)
    print(kp.analysis('41190742', '치킨', '산현동', 73000, 100, 9000, 1300))

