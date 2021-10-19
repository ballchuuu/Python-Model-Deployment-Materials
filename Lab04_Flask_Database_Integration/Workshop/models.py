from app import db 
import datetime 

# creating table
class Lexicon_dictionary(db.Model):
    __tablename__ = 'lexicon_dictionary'

    lexiconID = db.Column(db.Integer, primary_key=True)
    lexicon = db.Column(db.String(1000), unique=False, nullable=False)
    language = db.Column(db.String(1000), unique=False, nullable=False)
    
    #one-to-many model
    pos_neg_scores = db.relationship('Sentiment_score', back_populates = 'lexicons_pos_neg', cascade ='all', lazy=True, uselist=True)

    def __init__(self, lexicon, language): 
        self.lexicon = lexicon
        self.language = language
    
    def serialize(self):
        result = {'lexicon':self.lexicon, 'language':self.language} 
        return result 

class Sentiment_score(db.Model):
    __tablename__ = 'sentiment_score'

    scoreID = db.Column(db.Integer, primary_key=True)
    sentiment = db.Column(db.String(1000), unique=False, nullable=False)
    score = db.Column(db.Float(), unique=False, nullable=False)
    lexiconID = db.Column(db.Integer, db.ForeignKey('lexicon_dictionary.lexiconID'), unique=False, nullable=False)

    #one-to-many model
    lexicons_pos_neg = db.relationship('Lexicon_dictionary', back_populates = 'pos_neg_scores')

    def __init__(self, score, lexiconID, sentiment): 
        self.score = score
        self.sentiment = sentiment
        self.lexiconID = lexiconID

    def serialize(self):
        result = {'lexicon':self.lexiconID, 'score':self.score, 'sentiment': self.sentiment} 
        return result 
