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

add_article("theatre", "acting", 9)
	

def query_all_articles():
	articles = session.query(Knowledge).all()
	return articles
print(query_all_articles())

def query_article_by_topic(topic):
	article = session.query(Knowledge).filter_by(topic=topic).all()
	return(article)

print(query_article_by_topic("theatre"))

def query_article_by_rating(rating):
	b = session.query(Knowledge).filter_by(rating=rating).all()
	trsh = input("Give an input between 1 and 10")
def delete_article_by_topic():
	pass

def delete_all_articles():
	pass

def edit_article_rating():
	pass
