
from gensim.models import Word2Vec

def get_relation_keyword(keyword):

    try:
        model = Word2Vec.load("./new_api/analysis_model/word2vec_model")
        result = model.wv.most_similar(keyword)

    except KeyError as e:
        print(e)
        print("학습된 모델의 사전에 해당 키워드가 없습니다.")
        result = ''

    return dict(result)