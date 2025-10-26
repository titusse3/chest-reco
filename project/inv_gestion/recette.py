from inv_gestion.item import Item, Recette

#### lingo_or, coeur_lune

# commun
planche = Item("planche", "ressource/commun/planche.png")
plume = Item("plume", "ressource/commun/plume.png")
tissue = Item("tissue", "ressource/commun/tissue.png")
ficelle = Item("ficelle", "ressource/commun/ficelle.png")
pomme = Item("pomme", "ressource/commun/pomme.png")
parchemin_basique = Item("parchemin basique", "ressource/commun/parchemin_basique.png")
laine = Item("laine", "ressource/commun/laine.png")
parchemin = Item("parchemin", "ressource/commun/parchemin.png")
papier = Item("papier", "ressource/commun/papier.png")
plume = Item("plume", "ressource/commun/plume.png")
laniere = Item("laniere", "ressource/commun/laniere.png")
cuivre_brute = Item("cuivre brute", "ressource/commun/cuivre_brute.png")
sphere_bois = Item("sphere de bois", "ressource/commun/sphere_bois.png")
fer_brute = Item("fer brute", "ressource/commun/fer_brute.png")
batton = Item("batton", "ressource/commun/batton.png")
acier_brute = Item("acier brute", "ressource/commun/acier_brute.png")

# rare
aluminium = Item("aluminium", "ressource/rare/aluminium.png")
bois = Item("bois", "ressource/rare/bois.png")
magnesium = Item("magnesium", "ressource/rare/magnesium.png")
cuir = Item("cuir", "ressource/rare/cuir.png")
parchemin_rare = Item("parchemin rare", "ressource/rare/parchemin_rare.png")
dain = Item("dain", "ressource/rare/dain.png")
lingo_acier = Item("lingot acier", "ressource/rare/lingot_acier.png")
lingo_fer = Item("lingot de fer", "ressource/rare/lingot_fer.png")
pochette_cuir =  Item("pochette en cuir", "ressource/rare/pochette_cuir.png")
lingo_cuivre = Item("lingot de cuivre", "ressource/rare/lingot_cuivre.png")
bronzite = Item("bronzite", "ressource/rare/bronzite.png")
manuscrit = Item("manuscrit", "ressource/rare/manuscrit.png")
metaux = Item("métaux", "ressource/rare/metaux.png")

# epic
eclat_lune = Item("eclat de lune", "ressource/epic/eclat_lune.png")
or_brute = Item("or brute", "ressource/epic/or_brute.png")
emeraude = Item("emeraude", "ressource/epic/emeraude.png")
obsidienne_brute = Item("obsidienne brute", "ressource/epic/obsidienne_brute.png")
parchemin_epic = Item("parchemin epic", "ressource/epic/parchemin_epic.png")
lingo_emeraude = Item("lingo emeraude", "ressource/epic/lingo_emeraude.png")
lingo_or = Item("lingo or", "ressource/epic/lingo_or.png")
pavot = Item("pavot", "ressource/epic/pavot.png")
lingo_obsidienne = Item("lingo obsidienne", "ressource/epic/lingot_obsidienne.png")
diamant_brute = Item("diamant brute", "ressource/epic/diamant_brute.png")

coeur_lune = Item("coeur de lune", "ressource/epic/coeur_lune.png")

# legendaire
diamant_pure = Item("diamant pur", "ressource/legendaire/diamant_pur.png")
diamant_raffiner = Item("diamant raffiné", "ressource/legendaire/diamant_raffiner.png")
pierre_volcanique = Item("pierre volcanique", "ressource/legendaire/pierre_volcanique.png")
parchemin_legendaire = Item("parchemin legendaire", "ressource/legendaire/parchemin_legendaire.png")
artefacte = Item("artefacte", "ressource/legendaire/artefacte.png")
perle_nacre = Item("perle de nacre", "ressource/legendaire/perle_nacre.png")
parchemin_dore = Item("parchemin doré", "ressource/legendaire/parchemin_dore.png")
diamant = Item("diamant", "ressource/legendaire/diamant.png")
tissue_precieux = Item("tissue précieux", "ressource/legendaire/tissue_precieux.png")

# equipement ===================================================================

## katana
katana_t2 = None
katana_t3 = None
katana_t4 = None

## bague
bague_t2 = Item("bague_t2", "ressource/equipement/bague_t2.png")
bague_t4 = Item("bague_t4", "ressource/equipement/bague_t4.png")

## boucle
boucle_t2 = Item("boucle_t2", "ressource/equipement/boucle_t2.png")
boucle_t3 = Item("boucle_t3", "ressource/equipement/boucle_t3.png")
boucle_t4 = Item("boucle_t4", "ressource/equipement/boucle_t4.png")

## bottes
bottes_t2 = Item("bottes_t2", "ressource/equipement/botte_t2.png")
bottes_t4 = Item("bottes_t4", "ressource/equipement/botte_t4.png")

## gant
gant_t2 = Item("gant_t2", "ressource/equipement/gant_t2.png")
gant_t4 = Item("gant_t4", "ressource/equipement/gant_t4.png")

## collier
collier_t2 = Item("collier_t2", "ressource/equipement/collier_t2.png")
collier_t3 = Item("collier_t3", "ressource/equipement/collier_t3.png")
collier_t4 = Item("collier_t4", "ressource/equipement/collier_t4.png")

## patalon
patalon_hp_t3 = Item("patalon_hp_t3", "ressource/equipement/pantalon_hp_t3.png")
patalon_jutsu_t4 = Item("patalon_jutsu", "ressource/equipement/pantalon_jutsu_t4.png")
# patalon_armure_t3 = Item("patalon_armure_t3", "ressource/equipement/pantalon_armure_t3.png")
patalon_armure_t4 = Item("patalon_armure_t4", "ressource/equipement/pantalon_armure_t4.png")

## torse
torse_hp_t3 = Item("torse_hp_t3", "ressource/equipement/torse_hp_t3.png")
torse_armure_t4 = Item("torse_armure_t4", "ressource/equipement/torse_armure_t4.png")
# torse_jutsu_t4 = Item("torse_jutsu_t4", "ressource/equipement/torse_jutsu_t4.png")
torse_armure_t4 = Item("torse_armure_t4", "ressource/equipement/torse_armure_t4.png")

# recette ======================================================================

# consomalbe
recette_coeur_lune = Recette(coeur_lune, [(eclat_lune, 4)])
recette_lingo_or = Recette(lingo_or, [(or_brute, 4)])
recette_lingo_fer = Recette(lingo_fer, [(fer_brute, 4)])
recette_lingo_cuivre = Recette(lingo_cuivre, [(cuivre_brute, 4)])
recette_lingo_acier = Recette(lingo_acier, [(acier_brute, 4)])
recette_lingo_emeraude = Recette(lingo_emeraude, [(emeraude, 4)])
recette_lingo_obsidienne = Recette(lingo_obsidienne, [(obsidienne_brute, 4)])

## katana
recette_katana_t2 = Recette(katana_t2, [(magnesium, 4), (lingo_fer, 4), (batton, 4)])
recette_katana_t3 = Recette(katana_t3, [(lingo_or, 1), (magnesium, 6), (lingo_fer, 6), (batton, 8)])
recette_katana_t4 = Recette(katana_t4, [(perle_nacre, 2), (batton, 8), (lingo_or, 1), (magnesium, 6), (lingo_fer, 6)])

## bague
recette_bague_t2 = Recette(bague_t2, [(aluminium, 3), (lingo_fer, 4), (laniere, 6), (lingo_cuivre, 4)])
recette_bague_t4 = Recette(bague_t4, [(aluminium, 3), (coeur_lune, 1), (artefacte, 2), (lingo_cuivre, 8), (lingo_or, 1), (lingo_fer, 8), (laniere, 6), (parchemin_dore, 2)])

## bottes
recette_bottes_t2 = Recette(bottes_t2, [(ficelle, 4), (parchemin_basique, 6), (lingo_acier, 4), (bronzite, 4)])
recette_bottes_t4 = Recette(bottes_t4, [(perle_nacre, 1), (pierre_volcanique, 1), (diamant_pure, 1), (parchemin_dore, 2), (ficelle, 8), (lingo_fer, 8), (bronzite, 8)])

## boucle
recette_boucle_t2 = Recette(boucle_t2, [(ficelle, 6), (lingo_fer, 4), (lingo_cuivre, 4), (parchemin_basique, 2)])
recette_boucle_t3 = Recette(boucle_t3, [(metaux, 3), (emeraude, 2), (or_brute, 2), (obsidienne_brute, 2), (ficelle, 6), (lingo_acier, 6), (lingo_fer, 6)])
recette_boucle_t4 = Recette(boucle_t4, [(metaux, 3), (lingo_acier, 8), (pierre_volcanique, 2), (ficelle, 6), (emeraude, 2), (perle_nacre, 2), (or_brute, 2), (lingo_fer, 8), (obsidienne_brute, 2)])

## gant
recette_gant_t2 = Recette(gant_t2, [(pochette_cuir, 4), (plume, 4), (laniere, 4)])
# recette_gant_t3 = Recette(gant_t3, [(diamant_brute, 1), (eclat_lune, 1), (emeraude, 1), (laniere, 6), (or_brute, 1), (pochette_cuir, 6), (plume, 6)])
recette_gant_t4 = Recette(gant_t4, [(diamant_pure, 1), (eclat_lune, 1), (emeraude, 1), (laniere, 8), (or_brute, 1), (pochette_cuir, 8), (plume, 8), (tissue_precieux, 2)])

## patalon
recette_patalon_hp_t3 = Recette(patalon_hp_t3, [(tissue, 6), (lingo_acier, 6), (metaux, 6), (lingo_emeraude, 1)])
recette_patalon_jutsu_t4 = Recette(patalon_jutsu_t4, [(lingo_cuivre, 8), (tissue_precieux, 2), (laine, 8), (lingo_or, 1), (lingo_acier, 8)])
# recette_patalon_armure_t3 = Recette(patalon_armure_t3, [(tissue, 6), (lingo_acier, 6), (lingo_fer, 6), (lingo_obsidienne, 1)])
recette_patalon_armure_t4 = Recette(patalon_armure_t4, [(pierre_volcanique, 2), (lingo_obsidienne, 1), (tissue, 8), (lingo_acier, 8), (lingo_fer, 8)])

## collier
recette_collier_t2 = Recette(collier_t2, [(lingo_cuivre, 4), (ficelle, 2), (lingo_acier, 4), (plume, 4), (parchemin_rare, 1)])
recette_collier_t3 = Recette(collier_t3, [(emeraude, 1), (diamant_raffiner, 1), (lingo_cuivre, 6), (ficelle, 4), (lingo_fer, 6), (plume, 4), (parchemin_epic, 1)])
recette_collier_t4 = Recette(collier_t4, [(parchemin_legendaire, 2), (diamant_raffiner, 1), (emeraude, 2), (lingo_cuivre, 8), (ficelle, 4), (lingo_fer, 8), (plume, 4)])

## torse
recette_torse_hp_t3 = Recette(torse_hp_t3, [(ficelle, 6), (dain, 6), (lingo_cuivre, 6), (or_brute, 2), (obsidienne_brute, 2)])
# recette_torse_jutsu_t4 = Recette(torse_jutsu_t4, [(ficelle, 8), (eclat_lune, 2), (pierre_volcanique, 2), (parchemin_dore, 2), (lingo_acier, 8), (lingo_fer, 8)])
recette_torse_armure_t4 = Recette(torse_armure_t4, [(dain, 8), (lingo_obsidienne, 1), (pierre_volcanique, 2), (ficelle, 8), (lingo_acier, 8)])

items = [
  planche, plume, tissue, ficelle, pomme, parchemin_basique, laine, parchemin,
  papier, laniere, cuivre_brute, sphere_bois, fer_brute, batton, acier_brute,
  aluminium, bois, magnesium, cuir, parchemin_rare, dain, lingo_acier,
  lingo_fer, pochette_cuir, lingo_cuivre, bronzite, manuscrit, metaux,
  eclat_lune, or_brute, emeraude, obsidienne_brute, parchemin_epic,
  lingo_emeraude, pavot, lingo_obsidienne, diamant_brute, diamant_pure, diamant_raffiner,
  pierre_volcanique, parchemin_legendaire, artefacte, perle_nacre,
  parchemin_dore, diamant, tissue_precieux
]

equipements = [
  bague_t2, bague_t4, boucle_t2, boucle_t3, boucle_t4, collier_t2, collier_t3, 
  collier_t4, bottes_t2, bottes_t4, gant_t2, gant_t4,
  patalon_hp_t3, patalon_jutsu_t4, patalon_armure_t4,
  torse_hp_t3, torse_armure_t4
]
