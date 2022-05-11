from frique_app import db


class add_client(db.Model):

	id = db.Column(db.Integer, primary_key = True)
	dir_nom = db.Column(db.String(64), nullable = False)
	dir_prenom = db.Column(db.String(64), nullable = False)
	nom_societe = db.Column(db.String(64), nullable = False)
	siret = db.Column(db.Integer(14), unique = True, nullable = False)
	tel_societe = db.Column(db.String(12), unique= True,nullable = False)
	email = db.Column(db.String(64), unique = True, nullable = False)
	dir_nom = db.Column(db.String(64), nullable = False)