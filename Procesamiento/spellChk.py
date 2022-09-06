from spellchecker import SpellChecker

spell = SpellChecker(language='es')

misspelled = spell.unknown(['Fodurea', 'SA', 'us', 'N°', 'De', 'FacTuRA', 'DE', 'FPEDITO', 'Bolttas', 'INC', 'CORP', 'Conetera', 'cobtes', 'Medellin', 'Colombia', 'VENeIMientO', 'FACTURAR', 'Ay', 'ENVIAR', 'Manane', 'Gialdo', 'Danid', 'Madand', 'Coraasin', 'AG', 'Graders', 'Burges', 'Bergos', '44300', 'Cadiz', 'Cadiz', 'CANT.', 'DES', 'CRIP', 'CION', '4', 'Fastelttode', 'Tiesa', 'grande', '4OO-0', '2', 'Fansito', 'de', 'Chocolate', 'Pequc', 'Chuurtlo', 'Azvcaradoe', 'Medi', 'Café', 'con', 'Chocolate', "ConDic'"])

for word in misspelled:
    print(spell.correction(word))    
    print(spell.candidates(word))
