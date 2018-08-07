from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(topic, title, rating):
	article_object = Knowledge(
		topic = topic,
		title = title,
		rating = rating)
	session.add(article_object)
	session.commit()

add_article("theatre", "acting", 5)
# add_article("love", "peace", 8)


def query_all_articles():
	articles = session.query(Knowledge).all()
	return articles
# print(query_all_articles())
print(query_all_articles())

def query_article_by_topic(topic):
	article = session.query(Knowledge).filter_by(topic=topic).all()
	return(article)

# print(query_article_by_topic("theatre"))

# def query_article_by_rating(rating):
# 	b = session.query(Knowledge).filter_by(rating=rating).all()
# 	trsh = input("Give an input between 1 and 10")
def delete_article_by_topic(topic):
	session.query(Knowledge).filter_by(topic=topic).delete()
	session.commit()

def delete_all_articles():
	session.query(Knowledge).delete()
	session.commit()

def edit_article_rating():
	title = input("What is the title of the article you want to change?")
	new_rating = input("What is the new rating of the article?")
	articles = session.query(Knowledge).filter_by(title=title).all()
	for article in articles:
		article.rating = new_rating
	session.commit()

# delete_article_by_topic("theatre")
# print(query_all_articles())
# delete_all_articles()
# print(query_all_articles())
def delete_articles_by_rating(threshold):
	session.query(Knowledge).filter(Knowledge.rating<threshold).delete()


# edit_article_rating()
delete_articles_by_rating(7)
print(query_all_articles())