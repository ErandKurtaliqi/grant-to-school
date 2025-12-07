## Konkluzioni i Përgjithshëm për Fazën 2

Puna e realizuar përfshin një proces të plotë dhe të strukturuar të përgatitjes së të dhënave, duke nisur nga detektimi i vlerave të jashtëzakonshme, 
eliminimi i tyre dhe përfundimisht eksplorimi statistikor i dataset-it të pastruar. Fillimisht, skripti i detektimit të outliers identifikon me saktësi 
rreshtat problematikë duke përdorur metodën e IQR dhe krijon një kolonë të dedikuar për të shënuar secilën vlerë të skajshme. 
Më pas, skripti i dytë organizon dhe ndan dataset-in në dy versionet e nevojshme:<br>
— atë të pastër dhe <br>
— atë që përmban vetëm outliers,<br>
duke siguruar që analiza e mëtejshme të jetë e saktë dhe pa devijime statistikore. 

Në fazën finale, skripti i EDA-s analizon në detaje të dhënat e filtruara, duke gjeneruar statistika përmbledhëse, 
vizualizime dhe analiza korelacionesh që ndihmojnë në kuptimin e shpërndarjes, marrëdhënieve dhe modeleve të brendshme të dataset-it. <br>
Bazuar në histogramet dhe boxplot-et, shpërndarja e bursave (amount_of_scholarship) rezulton të jetë e pabarabartë, me shumicën e vlerave të përqendruara në intervale të ulëta dhe 
vetëm një numër të vogël rastesh që marrin vlera më të larta (efekt që ulet ndjeshëm pas heqjes së outliers).<br> Nga analiza e grupeve (category_name, gender_male, aspirational_final), 
rezulton se disa kategori përfitojnë mesatarisht më shumë se të tjerat, duke sugjeruar se shpërndarja e bursave nuk është homogjene mes grupeve. <br>
Ndërkohë, matrica e korelacionit tregon se bursat kanë korrelacione të ulëta me shumicën e variablave të tjerë, duke sugjeruar se faktorë të tjerë kategorik, e jo variabla numerikë, 
ndikojnë më shumë në shumat e mbështetjes financiare.

Këto tre hapa së bashku krijojnë një pipeline të plotë dhe të mirëstrukturuar për pastrimin, validimin dhe eksplorimin e të dhënave, 
duke garantuar një bazë të fortë për analiza të avancuara, modelim apo vendimmarrje të mëtejshme.
