from frique_app import app
from flask import render_template, url_for, request, redirect
from flask_wtf.csrf import CSRFProtect
from frique_app.MyForms import New_client , Facture_field, Login, Count_create


csrf =  CSRFProtect() # protege contre les attaque csrf
csrf.init_app(app)



@app.route('/')
@app.route('/connexion', methods = ['POST', 'GET'])
def connexion():

	if request.method =='POST':
		data = request.form
		
		if 'connexion_btn' in data:

			form = Login()
			return render_template('connexion.html', connexion = data['connexion_btn'], form = form )
		
		if 'nv_compte' in data:

			form = Count_create()
			return render_template('connexion.html', nv_compte = data['nv_compte'], form = form )

	return render_template('connexion.html')
#--------------------------------------------------------------------



#------------ Page d'acceuil après ( à changer ) connexion -----------
@app.route('/accueil', methods=['GET'])
def home():

	return render_template('accueil.html')
#--------------------------------------------------------------------


#------------ nouveau client --------------------------------------
@app.route('/add_client', methods = ['POST', 'GET'])
def add_client():

	client_form = New_client()

		
	return render_template('nouveau_client.html', form = client_form)
#--------------------------------------------------------------------


@app.route('/facture')
def facture():
	form_facture = Facture_field()

	return render_template('nouvelle_facture.html', form_facture = form_facture)




@app.route('/check', methods = ['POST'])
def check():
	form = New_client()
	if form.is_submitted():


		return request.form
	return "ne fonctionne pas"

