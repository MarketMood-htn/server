import cohere
from cohere.classify import Example
co = cohere.Client('1e23qAOMoin4GlWWLtcB70Iwd5CsVc7faT2mNNfb')


def analyzeSentiment(article,link):
    try:
        if type(article) == 'NoneType' and (article == "" or len(article) <= 0):
            return
        # print(article)
        response = co.classify(
            model='finance-sentiment',
            inputs=[article])
        confidence = response.classifications[0].confidence
        results = {'link': link, "prediction": response.classifications[0].prediction, confidence[0].label.lower(): confidence[0].confidence,
                confidence[1].label.lower(): confidence[1].confidence, confidence[2].label.lower(): confidence[2].confidence}
        return results
    except Exception as e: print(e)
