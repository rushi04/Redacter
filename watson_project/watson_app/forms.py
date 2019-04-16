import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, CategoriesOptions, ConceptsOptions, EntitiesOptions, KeywordsOptions, RelationsOptions, MetadataOptionsnatural_language_understanding = NaturalLanguageUnderstandingV1(
   version='2018-11-17',
   iam_apikey='xXNmTMJRiATDyZXZ7Nga1zxxwLCrKQBeX9UQ_UZ1Y4Te',
   url='https://gateway-lon.watsonplatform.net/natural-language-understanding/api'
)txt='Rohan is 16 years old and have his account number numbered 27389172783725 in Canara Bank.'response1 = natural_language_understanding.analyze(
   text='Rohan is 16 years have his account number numbered 27389172783725 in Canara Bank.',
   features=Features(categories=CategoriesOptions(limit=3))).get_result()response2 = natural_language_understanding.analyze(
   text=txt,
   features=Features(concepts=ConceptsOptions(limit=3))).get_result()response3 = natural_language_understanding.analyze(
   text=txt,
   features=Features(entities=EntitiesOptions(sentiment=True,limit=1))).get_result()response4 = natural_language_understanding.analyze(
   text=txt,
   features=Features(keywords=KeywordsOptions(sentiment=True,limit=2))).get_result()response5 = natural_language_understanding.analyze(
   text=txt,
   features=Features(relations=RelationsOptions())).get_result()print(json.dumps(response1, indent=2))print(json.dumps(response2, indent=2))print(json.dumps(response3, indent=2))print(json.dumps(response4, indent=2))print(json.dumps(response5, indent=2))
