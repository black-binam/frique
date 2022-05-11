from fpdf import FPDF
import time

class PDF(FPDF):
	
	def logo(self, facture_num, date_facture, echeance):
		self.image('static/img/logo_v1.png', x=10, y=15,w=25)
		self.set_font('Times', 'B', 18)
		self.set_text_color(46,196,182)
		self.set_xy(190 - self.get_string_width(facture_num), 15)
		self.cell(w = self.get_string_width(facture_num), align='R', h=10, txt = facture_num, ln = True)

		# on va definir les donnéés en sous texte
		self.set_font('Times', '', 10)
		self.set_xy(190 - self.get_string_width(facture_num), self.get_y())
		self.set_text_color(75,75,75)
		self.cell(w = self.get_string_width(facture_num), align = 'R', txt = date_facture) # date de facturation
		self.ln()

		self.set_font('Times', 'B', 12)
		self.set_xy(190 - self.get_string_width(facture_num), 30)
		self.cell(w = self.get_string_width(facture_num), align = 'R', txt = echeance, ln = True) # échance de paiment

	def th_data(self):
		self.set_y(100)
		self.set_font('helvetica', 'B', 10 )
		self.set_text_color(255,255,255) # couleur texte
		self.set_fill_color(255,159,28)	 # couleur background
		self.set_line_width(0.5)
	
		self.cell(w=60.0, h=9.0, align='L', txt="Libéllé", border=False, ln=False, fill=True)
		self.cell(w=20.0, h=9.0, align='R', txt="Date", border=False, ln=False, fill=True)
		self.cell(w=30.0, h=9.0, align='R', txt="Prix unitaire", border=False, ln=False, fill=True)
		self.cell(w=20.0, h=9.0, align='R', txt="Qté", border=False, ln=False, fill=True)
		self.cell(w=30.0, h=9.0, align='R', txt="Tva", border=False, ln=False, fill=True)
		self.cell(w=30.0, h=9.0, align='R', txt="TTC", border=False, ln=False, fill=True)
		self.ln()

	def td_data(self, data):
		self.set_font('Courier', '', 10)
		self.set_text_color(0,0,0)
		self.cell(w = data[0], h=10, align= data[2], txt = data[1])
	
	def lines(self):
		self.set_line_width(0.2)
		self.set_draw_color(230,230,230)
		self.line(10,self.get_y(),200, self.get_y())


	def info_societe(self, dico):
		self.set_xy(10,50)
		self.set_font('helvetica', 'B', 12)
		self.cell(w = self.get_string_width(dico['nom_societe']) , h=9, txt = dico['nom_societe'], ln=True)

		self.set_xy(10,self.get_y())
		self.set_font('Arial', '', 10)
		self.cell(w = self.get_string_width(dico['rue'] ) , h=4, txt = dico['rue'] , ln = True)
		self.cell(w = self.get_string_width(dico['code_postal_ville']) , h=5, txt = dico['code_postal_ville'] , ln = True)
		self.cell(w = self.get_string_width(dico['fixe']) , h=4, txt = dico['fixe'] , ln = True)
		self.cell(w = self.get_string_width(dico['mobile']) , h=4, txt = dico['mobile'] , ln = True)
		self.cell(w = self.get_string_width(dico['email']) , h=4, txt = dico['email'] , ln = True)
		self.cell(w = self.get_string_width(dico['site_web']) , h=4, txt = dico['site_web'] , ln = True)


	def info_client(self, dico):
		self.set_xy(130,50)
		self.set_font('helvetica', 'B', 12)
		self.cell(w = self.get_string_width(dico['nom_societe']) , h=9, txt = dico['nom_societe'], ln=True)

		self.set_xy(130,self.get_y())
		self.set_font('Times', '', 10)
		self.cell(w = self.get_string_width(dico['rue'] ) , h=5, txt = dico['rue'] , ln = True)
		self.set_x(130)
		self.cell(w = self.get_string_width(dico['code_postal_ville']) , h=5, txt = dico['code_postal_ville'] , ln = True)

	

	def footer(self):
		self.set_fill_color(46,196,182)
		self.rect(0,277, 210,30,'F' )

		self.set_y(-18)
		self.set_font('Arial', 'B', 12)
		self.set_text_color(255,255,255)
		self.cell(w = 0, h=5, align ='C', txt = footer_info['nom_societe'], ln=True)

		self.set_font('Arial', 'I', 8)
		self.cell(w = 0, h=5, align ='C', txt = footer_info['adresse'], ln=True)
		self.cell(w = 0, h=5, align ='C', txt = footer_info['siret_tva'])

	def mode_paiement(self, info_paiement):
		self.set_font('Times', '', 10)
		self.set_x(10)
		self.cell(w=0, h=5, align='L', txt='Moyens de paiement')
		self.set_x(60)
		self.cell(w=0, h=5, align='L', txt= info_paiement['Banque']  , ln = True)
		self.set_x(60)
		self.cell(w=0, h=5, align='L', txt= info_paiement['bic'] , ln = True)
		self.set_x(60)
		self.cell(w=0, h=5, align='L', txt= info_paiement['iban'])

	

info_paiement = {
			'Banque': 'Banque: Societe Generale',
			'bic': 'SWIFT/BIC: BREDFRPPXXX',
			'iban':'IBAN: FR7610107006530092904033825'
				
			}	

footer_info = {
			'nom_societe':"Keyz formation",
			'adresse':'23 Avenue de la republique, 94500',
			'siret_tva': 'Numéro de SIRET: 83460534700022 - Numéro de TVA: FR61834605347 - 834605347'
		}
pdf = PDF()

data = {
			'line1':[(60,'achat viande','L'), (20, '24/02/2022','R'), (30, '15','R'), (20, '15', 'R'), (30, '150','R'), (30, '1544','R')]
			
		}

annee = str(time.localtime().tm_year)
num_fac = '1'
facture_num = f'FACTURE - {annee} - {num_fac}'

text= 'Facture - 2022 - 180'
pdf.add_page()

pdf.set_auto_page_break(auto = True,margin = 25)

# -------------- les parametre de logo: facture_num , date_facture, echeance ----------#
#******************************************************
annee = str(time.localtime().tm_year)
num_fac = '1'
facture_num = f'FACTURE - {annee} - {num_fac}'
#******************************************************


#*****************************************************
jour = str(time.localtime().tm_mday)
mois = str(time.localtime().tm_mon)

if time.localtime().tm_mon<10:
	mois = '0'+ str(time.localtime().tm_mon)

if time.localtime().tm_mday<10:
	jour = '0'+ str(time.localtime().tm_mday)

date_facture = f'Date de facturation: {jour}/{mois}/{annee}'
#******************************************************


#******************************************************
mois_echeance = ''
if time.localtime().tm_mon<10:
	mois_echeance = '0' + str(time.localtime().tm_mon+1)
else:
	mois_echeance = str(time.localtime().tm_mon+1)

echeance = f'Echeance : {jour}/{mois_echeance}/{annee}'
#*******************************************************

pdf.logo(facture_num, date_facture,echeance)

#-------------------------Info societe et client ----------------------------------------#
info_societe = {
	'nom_societe':"KEYZ FORMATION",
	'rue':"23 Avenue de la republique",
	'code_postal_ville':"94500 Champigny sur marne",
	'fixe':"01 01 01 01 01",
	'mobile':"06 14 84 23 16",
	'email':"keyz.formation@gmail.com",
	'site_web': "https:keyz-formation.fr"
}

info_client = {
	'nom_societe':"KEYZ FORMATION",
	'rue':"23 Avenue de la republique",
	'code_postal_ville':"94500 Champigny sur marne",

}

pdf.info_societe(info_societe)
pdf.info_client(info_client)

#---------------------------------------------------------------------------------------#
pdf.th_data()
data_values = list(data.values()) #renvoie une list de liste de tuple [ [(a,b,c,d)], [(a,b,c,d)]]


#--Boucle while permettant de récupérer l'index de chaque list dans data_values qui est une liste --#
i = 0
for n in list(range(10)):
	while i < len(data_values):

		for tup in data_values[i]:

			if tup != data_values[i][-1]:
				pdf.td_data(tup)
			elif tup == data_values[i][-1]:
				pdf.td_data(tup)
				pdf.ln()
				pdf.lines()

		break
	print(i)

#------------------------------------------------------------------------------------

pdf.ln()
pdf.mode_paiement(info_paiement)


pdf.output('test.pdf')

