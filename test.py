import cohere 
from cohere.classify import Example 
co = cohere.Client('1e23qAOMoin4GlWWLtcB70Iwd5CsVc7faT2mNNfb') 
response = co.classify( 
  model='finance-sentiment', 
  inputs=["university is a terribly good experience"]) 
# Get All Negative and positives
confidence = response.classifications[0].confidence
results = {"prediction":response.classifications[0].prediction,confidence[0].label:confidence[0].confidence,confidence[1].label:confidence[1].confidence,confidence[2].label:confidence[2].confidence}
print(results)