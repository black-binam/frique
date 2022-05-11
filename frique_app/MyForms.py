from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length, InputRequired
from wtforms.fields.html5 import EmailField

class New_client(FlaskForm):
	nom = StringField('nom', validators = [InputRequired()])
	prenom = StringField('prenom', validators = [DataRequired()])
	nom_societe = StringField('nom_societe', validators = [DataRequired()])
	nom_rue = StringField('nom_rue', validators = [DataRequired()])
	code_postal = StringField('code_postal', validators = [DataRequired()])
	siret = StringField('siret', validators = [DataRequired()])
	telephone = StringField('telephone',  validators = [DataRequired()])
	email = EmailField('email', validators = [DataRequired(), Email(), Length(max=50)])
	submit = SubmitField('Valider')


class Facture_field(FlaskForm):
	description = StringField('Description', validators = [DataRequired()])
	quantite = StringField('Quantite', validators = [DataRequired()])
	prix_u = StringField('Prix Unitaire HT', validators = [DataRequired()])
	tva = StringField('Taux TVA', validators = [DataRequired()])
	submit = SubmitField('Valider')

class Login(FlaskForm):
	identifiant = StringField('Identifiant', validators = [DataRequired()])
	mot_de_pass = PasswordField('Mot de passe', validators = [DataRequired()])
	submit = SubmitField('Valider')


class Count_create(FlaskForm):
	dirigeant_nom = StringField('Nom du dirigeant', validators = [DataRequired()])
	dirigeant_prenom = StringField('Préom du dirigeant', validators = [DataRequired()])
	nom_societe = StringField('Nom de la societe', validators = [DataRequired()])
	nom_rue = StringField('Nom et N° de rue', validators = [DataRequired()])
	code_postal = StringField('Code postal', validators = [DataRequired()])
	siret = StringField('siret', validators = [DataRequired()])
	telephone = StringField('Telephone',  validators = [DataRequired()])
	email = EmailField('email', validators = [DataRequired(), Email(), Length(max=50)])
	mot_de_pass = PasswordField('Mot de passe', validators = [DataRequired()])
	confirmation_pw = PasswordField('Confirmez le Mot de passe', validators = [DataRequired()])
	submit = SubmitField('Valider')