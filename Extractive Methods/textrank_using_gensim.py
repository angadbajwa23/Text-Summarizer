import gensim
from gensim.summarization.summarizer import summarize

data="""
They become high in calories, high in cholesterol, low in healthy nutrients, high in sodium mineral, high in sugar, starch, unhealthy fat, lack of protein and lack of dietary fibers.
Processed and junk foods are the means of rapid and unhealthy weight gain and negatively impact the whole body throughout the life.
Junk foods tastes good and looks good however do not fulfil the healthy calorie requirement of the body.
It is found according to the Centres for Disease Control and Prevention that Kids and children eating junk food are more prone to the type-2 diabetes.
Eating junk food daily lead us to the nutritional deficiencies in the body because it is lack of essential nutrients, vitamins, iron, minerals and dietary fibers.
It increases risk of cardiovascular diseases because it is rich in saturated fat, sodium and bad cholesterol.
High sodium and bad cholesterol diet increases blood pressure and overloads the heart functioning.
One who like junk food develop more risk to put on extra weight and become fatter and unhealthier.
Junk foods contain high level carbohydrate which spike blood sugar level and make person more lethargic, sleepy and less active and alert.
For instance, foods like French fries, burgers, candy, and cookies, all have high amounts of sugar and fats."""

summary=summarize(data,ratio=0.3)
print(summary)