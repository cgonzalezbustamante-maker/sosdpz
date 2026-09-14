# -*- coding: utf-8 -*-
# Construye el JSON maestro de ubicaciones fusionando los lotes devueltos por los
# agentes de investigacion (transcritos de sus resultados). Faltan 161-185 (se anaden aparte).
import json, os

lotes = []

# 1-20
lotes += [
{"pos":1,"nombre":"BSH ELECTRODOMESTICOS ESPAÑA SA","municipio":"Zaragoza","ubicacion":"Plantas de La Cartuja (Las Fuentes) y Montañana (centro mundial de inducción), término municipal de Zaragoza","confianza":"alta","domicilio_fiscal":"","fuente":"enjoyzaragoza.es"},
{"pos":2,"nombre":"ALLIANCE HEALTHCARE ESPAÑA SA","municipio":"Villanueva de Gállego","ubicacion":"Pol. Ind. San Miguel, Sector IV, 50830","confianza":"alta","domicilio_fiscal":"","fuente":"empresite"},
{"pos":3,"nombre":"RIVASAM INTERCONTINENTAL SA","municipio":"Zuera","ubicacion":"Pol. Ind. El Campillo (matadero de porcino), 50800","confianza":"alta","domicilio_fiscal":"","fuente":"empresite"},
{"pos":4,"nombre":"ESPRINET IBERICA SLU","municipio":"Zaragoza","ubicacion":"Plataforma Logística PLAZA, C/ Osca 2, 50197","confianza":"alta","domicilio_fiscal":"","fuente":"plazalogistica"},
{"pos":5,"nombre":"SOCIEDAD ANONIMA INDUSTRIAS CELULOSA ARAGONESA (SAICA)","municipio":"El Burgo de Ebro","ubicacion":"Pol. El Espartal (fábricas SAICA-2 y SAICA-3); sede y SAICA-1 en La Cartuja, Zaragoza","confianza":"alta","domicilio_fiscal":"Zaragoza","fuente":"paper-world"},
{"pos":6,"nombre":"ADIDAS ESPAÑA SAU","municipio":"Caspe","ubicacion":"Centro logístico Ctra. Alcañiz-Fraga s/n; sede admin. en PLAZA (Zaragoza)","confianza":"alta","domicilio_fiscal":"Zaragoza","fuente":"paginasamarillas"},
{"pos":7,"nombre":"CARNICAS CINCO VILLAS SA","municipio":"Ejea de los Caballeros","ubicacion":"Pol. Ind. Valdeferrín, 50600","confianza":"alta","domicilio_fiscal":"","fuente":"paginasamarillas"},
{"pos":8,"nombre":"FUJIKURA AUTOMOTIVE EUROPE SAU","municipio":"Zaragoza","ubicacion":"Sede Avda. de Ranillas 3, Ed. Dinamiza (plantas de producción en Rumanía/Marruecos)","confianza":"alta","domicilio_fiscal":"","fuente":"kompass"},
{"pos":9,"nombre":"ADIENT SEATING SPAIN SL","municipio":"Pedrola","ubicacion":"C/ General Motors 30, Pol. El Pradillo (planta JIT asientos), 50690","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":10,"nombre":"CUARTE SL","municipio":"Zaragoza","ubicacion":"Ctra. de Logroño km 9,2, Monzalbarba (Zaragoza)","confianza":"media","domicilio_fiscal":"Zaragoza","fuente":"iberinform"},
{"pos":11,"nombre":"TRANS SESE SL","municipio":"Zaragoza","ubicacion":"Plataforma Logística PLAZA; complejo Grupo Sesé","confianza":"alta","domicilio_fiscal":"","fuente":"empresite"},
{"pos":12,"nombre":"NOVALTIA S.COOP.","municipio":"Zaragoza","ubicacion":"Ctra. Autovía de Huesca s/n, 50015 (almacén)","confianza":"alta","domicilio_fiscal":"","fuente":"einforma"},
{"pos":13,"nombre":"SCHINDLER SA","municipio":"Zaragoza","ubicacion":"Pol. Empresarium, Cartuja Baja, C/ Albardín 58","confianza":"media","domicilio_fiscal":"San Sebastián de los Reyes (Madrid)","fuente":"empresite"},
{"pos":14,"nombre":"SAICA PACK SL","municipio":"El Burgo de Ebro","ubicacion":"Pol. El Espartal I, Ctra. Castellón km 21","confianza":"media","domicilio_fiscal":"Zaragoza","fuente":"papeleriahada"},
{"pos":15,"nombre":"CARRERAS GRUPO LOGISTICO SA","municipio":"Zaragoza","ubicacion":"Plataforma Logística PLAZA, C/ Messina 2","confianza":"alta","domicilio_fiscal":"","fuente":"grupocarreras"},
{"pos":16,"nombre":"MEGASIDER ZARAGOZA SA","municipio":"Zaragoza","ubicacion":"Pol. José López Soriano, La Cartuja (acería grupo Megasa)","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":17,"nombre":"AMPLIFON IBERICA SAU","municipio":"Zaragoza","ubicacion":"C/ Poetisa María Zambrano 31, WTCZ (sede; cadena de audífonos)","confianza":"media","domicilio_fiscal":"Zaragoza","fuente":"einforma"},
{"pos":18,"nombre":"LECITRAILER SA","municipio":"Zaragoza","ubicacion":"Camino de Los Huertos s/n, Casetas (planta de semirremolques)","confianza":"alta","domicilio_fiscal":"","fuente":"lecitrailer"},
{"pos":19,"nombre":"ARGAL ALIMENTACION SA","municipio":"Zaragoza","ubicacion":"C/ Mosén Domingo Agudo 11, 50015 (grupo con centros también fuera de la provincia)","confianza":"media","domicilio_fiscal":"Zaragoza","fuente":"iberinform"},
{"pos":20,"nombre":"PROFAND ZARAGOZA SL","municipio":"Zaragoza","ubicacion":"C/ Bari 3, zona Mercazaragoza/Malpica (antigua Caladero)","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform"},
]

# 21-40
lotes += [
{"pos":21,"nombre":"SAICA NATUR SL","municipio":"El Burgo de Ebro","ubicacion":"Ctra. de Castellón km 21, Pol. El Espartal, 50730","confianza":"alta","domicilio_fiscal":"","fuente":"gestoresderesiduos"},
{"pos":22,"nombre":"HMY YUDIGAR EQUIPAMIENTO SLU","municipio":"Cariñena","ubicacion":"Pol. Veguilla s/n, 50400","confianza":"alta","domicilio_fiscal":"","fuente":"empresite"},
{"pos":23,"nombre":"INDUSTRIE CARTARIE TRONCHETTI IBERICA SLU","municipio":"El Burgo de Ebro","ubicacion":"Planta de tisú marca Foxy","confianza":"alta","domicilio_fiscal":"","fuente":"empresite"},
{"pos":24,"nombre":"VIAN AS AUTOMOBILE SL","municipio":"Zaragoza","ubicacion":"Ctra. Autovía de Logroño (Casetas) 28 / P.I. Molino del Pilar","confianza":"alta","domicilio_fiscal":"","fuente":"empresite"},
{"pos":25,"nombre":"NOVAPET SA","municipio":"FUERA","ubicacion":"Planta principal en Barbastro (Huesca); oficina en Zaragoza","confianza":"alta","domicilio_fiscal":"Zaragoza","fuente":"empresite"},
{"pos":26,"nombre":"S.C. GANADERA DE CASPE SL","municipio":"Caspe","ubicacion":"Caspe (fabricación de piensos)","confianza":"alta","domicilio_fiscal":"","fuente":"ranking-empresas"},
{"pos":27,"nombre":"PRIMACARNE SL","municipio":"Zuera","ubicacion":"Pol. Campillo, parc. 75, 50800","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":28,"nombre":"ARAGOCIAS SA","municipio":"Zaragoza","ubicacion":"C/ San Juan de la Peña 144","confianza":"media","domicilio_fiscal":"","fuente":"einforma"},
{"pos":29,"nombre":"DANIEL AGUILO PANISELLO SA","municipio":"Zaragoza","ubicacion":"C/ San Juan de la Peña 144 (grupo SAICA; planta DAPSA en L'Aldea, Tarragona)","confianza":"media","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":30,"nombre":"CASEN RECORDATI SL","municipio":"Utebo","ubicacion":"Planta/centro operativo en Utebo","confianza":"alta","domicilio_fiscal":"Madrid","fuente":"casenrecordati"},
{"pos":31,"nombre":"YUDIGAR SL","municipio":"Cariñena","ubicacion":"Pol. Ind. La Veguilla s/n, 50400","confianza":"alta","domicilio_fiscal":"","fuente":"empresite"},
{"pos":32,"nombre":"PROCLINIC SAU","municipio":"Zaragoza","ubicacion":"C/ Palermo 9, PLAZA (centro logístico)","confianza":"alta","domicilio_fiscal":"","fuente":"proclinic"},
{"pos":33,"nombre":"IBERCAJA GESTION SGIIC SA","municipio":"Zaragoza","ubicacion":"Paseo Constitución 4, 50008","confianza":"alta","domicilio_fiscal":"","fuente":"empresite"},
{"pos":34,"nombre":"ADIENT AUTOMOTIVE SL","municipio":"Alagón","ubicacion":"Carrera Caballos 53, 50630 (también Pedrola y Calatorao)","confianza":"alta","domicilio_fiscal":"","fuente":"empresite"},
{"pos":35,"nombre":"TEREOS STARCH & SWEETENERS IBERIA SAU","municipio":"Zaragoza","ubicacion":"Avda. Salvador Allende 76-78, 50015 (antigua Campo Ebro/Syral)","confianza":"alta","domicilio_fiscal":"","fuente":"empresite"},
{"pos":36,"nombre":"BEBINTER SA","municipio":"Zaragoza","ubicacion":"Ctra. de Castellón km 4,3 (zona Malpica)","confianza":"alta","domicilio_fiscal":"","fuente":"empresite"},
{"pos":37,"nombre":"AVES NOBLES Y DERIVADOS SL","municipio":"Zaragoza","ubicacion":"Plataforma Logística PLAZA","confianza":"media","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":38,"nombre":"EIGO GESTION DE OBRAS SL","municipio":"Zaragoza","ubicacion":"C/ Bari 31, Ed. Technocenter, PLAZA","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":39,"nombre":"GRANJA BAILON SL","municipio":"La Almunia de Doña Godina","ubicacion":"Ctra. de Alpartir km 1,8, 50100","confianza":"alta","domicilio_fiscal":"","fuente":"paginasamarillas"},
{"pos":40,"nombre":"PIKOLIN SL","municipio":"Zaragoza","ubicacion":"Centro logístico-industrial PLAZA","confianza":"alta","domicilio_fiscal":"","fuente":"wikipedia"},
]

# 41-60
lotes += [
{"pos":41,"nombre":"MANN-HUMMEL IBERICA SA","municipio":"Zaragoza","ubicacion":"Pol. PLAZA, C/ Pertusa 8, 50197","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":42,"nombre":"SALTOKI LOGISTICA ZARAGOZA SA","municipio":"Zaragoza","ubicacion":"Pol. Cogullada, Av. Alcalde Francisco Caballero 16","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":43,"nombre":"SOLITIUM SL","municipio":"Zaragoza","ubicacion":"Pol. PLAZA, C/ Bari 39, 50197","confianza":"alta","domicilio_fiscal":"","fuente":"paginasamarillas"},
{"pos":44,"nombre":"DELSO FERTILIZANTES GRUPO SL","municipio":"Calatayud","ubicacion":"Av. Pascual Marquina 12, 50300","confianza":"alta","domicilio_fiscal":"","fuente":"dnb"},
{"pos":45,"nombre":"MOWI IBERIA SL","municipio":"Zaragoza","ubicacion":"Mercazaragoza, Ctra. Cogullada, 50014 (envasado de pescado)","confianza":"alta","domicilio_fiscal":"","fuente":"infonif"},
{"pos":46,"nombre":"LEAR CORPORATION ASIENTOS SL","municipio":"Épila","ubicacion":"Pol. Ind. Valdemuel, Camino Sabinar s/n, 50290","confianza":"alta","domicilio_fiscal":"","fuente":"paginasamarillas"},
{"pos":47,"nombre":"ARAGONESA DE PIENSOS SAU","municipio":"Zaragoza","ubicacion":"Ctra. de Logroño km 9,2 - Monzalbarba, 50011","confianza":"alta","domicilio_fiscal":"","fuente":"einforma"},
{"pos":48,"nombre":"SMR AUTOMOTIVE SYSTEMS SPAIN SAU","municipio":"Épila","ubicacion":"Pol. Ind. Valdemuel, 50290 (retrovisores)","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":49,"nombre":"INDUSTRIAS QUIMICAS DEL EBRO SA","municipio":"Zaragoza","ubicacion":"Pol. Ind. Malpica, Calle D nº 97","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":50,"nombre":"AGREDA AUTOMOVIL SA","municipio":"Zaragoza","ubicacion":"Av. Manuel Rodríguez Ayuso 110 (Ctra. de Madrid km 315,7), 50012","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":51,"nombre":"OMYA CLARIANA SLU","municipio":"Belchite","ubicacion":"Ctra. A-222 km 21,4, 50130 (carbonato cálcico y cantera)","confianza":"alta","domicilio_fiscal":"","fuente":"einforma"},
{"pos":52,"nombre":"CABLES RCT SA","municipio":"Zaragoza","ubicacion":"La Cartuja Baja, Pol. Prydes, Ctra. Castellón A-68 km 226,9, 50720","confianza":"alta","domicilio_fiscal":"","fuente":"paginasamarillas"},
{"pos":53,"nombre":"COMERCIAL CHOCOLATES LACASA SA","municipio":"Utebo","ubicacion":"Autovía de Logroño 14, 50180 (fábrica de chocolates)","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":54,"nombre":"FERTINAGRO AGROVIP SL","municipio":"Zaragoza","ubicacion":"Ctra. Madrid km 315, C.E. Miralbueno, 50012","confianza":"media","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":55,"nombre":"DISTRIBUCIONES AGROPECUARIAS DE ARAGON SL","municipio":"Zaragoza","ubicacion":"Casetas (barrio de Zaragoza), 50620","confianza":"media","domicilio_fiscal":"","fuente":"qdq"},
{"pos":56,"nombre":"FARMHISPANIA SA","municipio":"Zaragoza","ubicacion":"Pol. Ind. Malpica II, Calle J parc. 3 (planta cGMP de APIs)","confianza":"alta","domicilio_fiscal":"","fuente":"farmhispaniagroup"},
{"pos":57,"nombre":"VITALIA HOME SL","municipio":"Zaragoza","ubicacion":"C/ Joaquín Costa 2, 50001 (sede; residencias de mayores)","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":58,"nombre":"BRASS & FITTINGS SL","municipio":"Zaragoza","ubicacion":"Pol. Ind. Cogullada, Av. Alcalde Francisco Caballero 16, 50014","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":59,"nombre":"ARAGON WAGEN SL","municipio":"Zaragoza","ubicacion":"Av. Navarra 135, 50017 (concesionario VW/Audi)","confianza":"alta","domicilio_fiscal":"","fuente":"paginasamarillas"},
{"pos":60,"nombre":"DEXIBERICA SOLUCIONES INDUSTRIALES SAU","municipio":"Zaragoza","ubicacion":"Plataforma Logística PLAZA, Calle Caraë 1","confianza":"alta","domicilio_fiscal":"","fuente":"einforma"},
]

# 61-80
lotes += [
{"pos":61,"nombre":"NUREL SA","municipio":"Zaragoza","ubicacion":"Pol. Ind. Malpica, Ctra. Barcelona (N-IIa) km 329, Santa Isabel","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":62,"nombre":"MASTER DISTANCIA SA","municipio":"Zaragoza","ubicacion":"Plataforma Logística PLAZA (calle Bari); centro Master D","confianza":"alta","domicilio_fiscal":"","fuente":"paginasamarillas"},
{"pos":63,"nombre":"SPORTS EMOTION HUB SL","municipio":"Zaragoza","ubicacion":"Plataforma Logística PLAZA, C/ Turiaso 27 (Fútbol Emotion)","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":64,"nombre":"SUCESORES DE SIMON FRANCO SA","municipio":"Cuarte de Huerva","ubicacion":"Calle de la Constitución 30","confianza":"alta","domicilio_fiscal":"","fuente":"kompass"},
{"pos":65,"nombre":"INDUSTRIAS ARAGONESAS DEL ALUMINIO SA","municipio":"Zaragoza","ubicacion":"Pol. Cogullada, Ctra. de Cogullada 31","confianza":"media","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":66,"nombre":"SERVISAR SERVICIOS SOCIALES SL","municipio":"Zaragoza","ubicacion":"Av. Salvador Allende 56 (residencias)","confianza":"media","domicilio_fiscal":"Bilbao","fuente":"paginasamarillas"},
{"pos":67,"nombre":"CHEMIEURO INTERNATIONAL SL","municipio":"Zaragoza","ubicacion":"Av. Juan Pablo II 35, Torre Aragonia (oficinas)","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":68,"nombre":"AVANZA ZARAGOZA SA","municipio":"Zaragoza","ubicacion":"C/ Miguel Servet 199 (cocheras autobús urbano)","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":69,"nombre":"ENERLAND ENGINEERING PROCUREMENT AND CONSTRUCTION SL","municipio":"Zaragoza","ubicacion":"Plataforma Logística PLAZA, C/ Bílbilis 18, nave A-4","confianza":"alta","domicilio_fiscal":"","fuente":"infoempresa"},
{"pos":70,"nombre":"SAT N 1733 GRANJA SAN MIGUEL","municipio":"Villarreal de Huerva","ubicacion":"Polígono Las Lomas s/n (avicultura)","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":71,"nombre":"ENTERPRISE SOLUTIONS OUTSOURCING ESPAÑA SL","municipio":"Zaragoza","ubicacion":"Av. Cesáreo Alierta 11 (servicios TI)","confianza":"media","domicilio_fiscal":"","fuente":"infonif"},
{"pos":72,"nombre":"PREFABRICADOS TECNYCONTA SLU","municipio":"Tauste","ubicacion":"Ctra. Gallur-Sangüesa km 11 s/n (prefabricados de hormigón)","confianza":"alta","domicilio_fiscal":"","fuente":"tecnyconta"},
{"pos":73,"nombre":"COFERDROZA SCL","municipio":"Zuera","ubicacion":"Pol. Ind. Llanos de la Estación, C/ Isaac Peral 1 (centro logístico)","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":74,"nombre":"ADVANCED ACCELERATOR APPLICATIONS IBERICA SLU","municipio":"La Almunia de Doña Godina","ubicacion":"Pol. Ind. La Cuesta, Av. Navarra 3 (radiofármacos, Novartis)","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":75,"nombre":"IBERCAJA MEDIACION DE SEGUROS SA","municipio":"Zaragoza","ubicacion":"Paseo de la Constitución 4","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":76,"nombre":"INDUSTRIAL GANADERA PREMIER SA","municipio":"Bujaraloz","ubicacion":"Ctra. A-230 km 32,5 s/n (Premier Pigs, porcino)","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":77,"nombre":"GRUPOS ELECTROGENOS EUROPA SA","municipio":"Muel","ubicacion":"Pol. Ind. Pitarco II, parcela 20 (GESAN)","confianza":"alta","domicilio_fiscal":"","fuente":"panjiva"},
{"pos":78,"nombre":"CAMPODULCE CURADOS SAU","municipio":"Zuera","ubicacion":"Pol. Ind. El Campillo 75 (secadero de jamones, Grupo Jorge)","confianza":"alta","domicilio_fiscal":"","fuente":"paginasamarillas"},
{"pos":79,"nombre":"SALTOKI SUMINISTROS ZARAGOZA SL","municipio":"Zaragoza","ubicacion":"Pol. Cogullada, Av. Alcalde Caballero 16","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":80,"nombre":"SPHERE GROUP SPAIN SL","municipio":"Pedrola","ubicacion":"Pol. Ind. El Pradillo, C/ Aneto 5 (films plásticos)","confianza":"alta","domicilio_fiscal":"","fuente":"dnb"},
]

# 81-100
lotes += [
{"pos":81,"nombre":"LA ZARAGOZANA SA","municipio":"Zaragoza","ubicacion":"C/ Ramón Berenguer IV 2 (San José) - Cervezas Ámbar","confianza":"alta","domicilio_fiscal":"","fuente":"empresite"},
{"pos":82,"nombre":"ARQUISOCIAL SLU","municipio":"Zaragoza","ubicacion":"C/ Cabezo Buenavista 7 (ayuda a domicilio)","confianza":"alta","domicilio_fiscal":"","fuente":"arquisocial"},
{"pos":83,"nombre":"VELPIRI SAU","municipio":"Zuera","ubicacion":"Pol. Ind. El Campillo (porcino, entorno Grupo Jorge)","confianza":"media","domicilio_fiscal":"Zaragoza","fuente":"einforma"},
{"pos":84,"nombre":"COMERCIAL PRODUCTOS PORCINOS SECUNDARIOS SA","municipio":"Zuera","ubicacion":"Pol. Ind. El Campillo (tripería, Grupo Jorge)","confianza":"alta","domicilio_fiscal":"","fuente":"ppssa"},
{"pos":85,"nombre":"ELECTRICAL COMPONENTS INTERNATIONAL SLU","municipio":"Zaragoza","ubicacion":"Pol. Ind. El Portazgo, Autovía de Logroño km 6,6 (cableados)","confianza":"alta","domicilio_fiscal":"","fuente":"dnb"},
{"pos":86,"nombre":"GESTAMP ARAGON SA","municipio":"Pedrola","ubicacion":"Pol. El Pradillo, C/ General Motors 6 (componentes automoción)","confianza":"alta","domicilio_fiscal":"","fuente":"kompass"},
{"pos":87,"nombre":"ARDISTEL SL","municipio":"Zaragoza","ubicacion":"C/ Caravis 18-20-22, 50197","confianza":"alta","domicilio_fiscal":"","fuente":"empresite"},
{"pos":88,"nombre":"JG GLOBAL LIVESTOCK TRADE SL","municipio":"Zaragoza","ubicacion":"C/ María Zambrano 31, WTCZ (comercio de ganado)","confianza":"alta","domicilio_fiscal":"","fuente":"einforma"},
{"pos":89,"nombre":"NOVAPET ENVASE SL","municipio":"Zaragoza","ubicacion":"Oficinas Paseo Independencia 21 (plantas del grupo en Barbastro y Fuenlabrada, fuera)","confianza":"media","domicilio_fiscal":"Zaragoza","fuente":"alimarket"},
{"pos":90,"nombre":"CELULOSA FABRIL SA","municipio":"Zaragoza","ubicacion":"Pol. Malpica, Calle E parc. 5 (CEFA, interior automoción)","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":91,"nombre":"HIAB CRANES SL","municipio":"Zaragoza","ubicacion":"Pol. Ind. Malpica, Calle E 86 (Santa Isabel; grúas articuladas)","confianza":"alta","domicilio_fiscal":"","fuente":"alimarket"},
{"pos":92,"nombre":"PUNT ROMA SL","municipio":"FUERA","ubicacion":"Sede operativa en Mataró (Barcelona); en Zaragoza solo tienda/domicilio en C/ Alfonso I 36","confianza":"media","domicilio_fiscal":"Zaragoza","fuente":"linkedin"},
{"pos":93,"nombre":"CONSTRUCCIONES MARIANO LOPEZ NAVARRO SA","municipio":"Zaragoza","ubicacion":"C/ Uncastillo 19 bajo, 50008","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":94,"nombre":"LACASA SA","municipio":"Utebo","ubicacion":"Ctra. N-232 / A-68 km 14 (fábrica de chocolates)","confianza":"alta","domicilio_fiscal":"","fuente":"cakedreams"},
{"pos":95,"nombre":"GRANJA VIRGEN DEL ROSARIO SL","municipio":"Villarreal de Huerva","ubicacion":"C/ Arrabal s/n, 50490 (producción de huevos)","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":96,"nombre":"DISTRIBUIDORA INTERNACIONAL CARMEN SA","municipio":"Zaragoza","ubicacion":"Pol. Alcalde Caballero, C/ Virgen Buen Acuerdo s/n (DICSA)","confianza":"alta","domicilio_fiscal":"","fuente":"dnb"},
{"pos":97,"nombre":"FOODIBEV INTERNATIONAL SL","municipio":"Zaragoza","ubicacion":"C/ Teniente Coronel Valenzuela 5 (oficinas); almacén C/ Vicente Berdusán","confianza":"alta","domicilio_fiscal":"","fuente":"empresite"},
{"pos":98,"nombre":"MARCO INFRAESTRUCTURAS Y MEDIO AMBIENTE SA","municipio":"Zaragoza","ubicacion":"C/ Messina 5, Plataforma Logística PLAZA, 50197","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":99,"nombre":"VIALEX CONSTRUCTORA ARAGONESA SLU","municipio":"Zaragoza","ubicacion":"C/ Enrique Val 4, 50011 (Grupo Sorigué)","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":100,"nombre":"INSTALAZA SA","municipio":"Zaragoza","ubicacion":"C/ Monreal 27 (armamento); factorías también en Cadrete y A-23 km 270","confianza":"alta","domicilio_fiscal":"","fuente":"empresite"},
]

# 101-120
lotes += [
{"pos":101,"nombre":"INTERNATIONAL CASING PRODUCTS SLU","municipio":"Zaragoza","ubicacion":"Mercazaragoza, Ctra. de Cogullada 65 (grupo Vall Companys)","confianza":"alta","domicilio_fiscal":"","fuente":"empresite"},
{"pos":102,"nombre":"GENEROS DE PUNTO VICTRIX SL","municipio":"Zaragoza","ubicacion":"C/ Alfonso I 36 (comercio textil; origen registral Barcelona)","confianza":"media","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":103,"nombre":"PASTAS ALIMENTICIAS ROMERO SA","municipio":"Daroca","ubicacion":"Avda. de Madrid 43 (fábrica de pastas)","confianza":"alta","domicilio_fiscal":"","fuente":"pastasromero"},
{"pos":104,"nombre":"ENTERPRISE SOLUTIONS CONSULTORIA Y APLICACIONES ESPAÑA SL","municipio":"Zaragoza","ubicacion":"Av. Cesáreo Alierta 11, 1ª","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":105,"nombre":"ARAIZ SUMINISTROS ELECTRICOS SAU","municipio":"Zaragoza","ubicacion":"C/ Jaime Ferrán 17 (Pol. Malpica-Alfindén, 50014)","confianza":"alta","domicilio_fiscal":"","fuente":"empresite"},
{"pos":106,"nombre":"PATATAS GOMEZ SL","municipio":"Zaragoza","ubicacion":"Mercazaragoza, Camino de Cogullada 65","confianza":"alta","domicilio_fiscal":"","fuente":"paginasamarillas"},
{"pos":107,"nombre":"LABORATORIOS SAPHIR SA","municipio":"Zaragoza","ubicacion":"Pol. Malpica, Calle D parc. 66, 50016 (perfumería/cosmética)","confianza":"alta","domicilio_fiscal":"","fuente":"empresite"},
{"pos":108,"nombre":"IBERICA DE ALEACIONES LIGERAS SL","municipio":"Pradilla de Ebro","ubicacion":"Ctra. Tudela-Alagón A-126 km 42,5 (IDALSA, aluminio)","confianza":"alta","domicilio_fiscal":"","fuente":"empresite"},
{"pos":109,"nombre":"SALTOKI LOGISTICA EMPRESARIUM SL","municipio":"Zaragoza","ubicacion":"Pol. Empresarium (La Cartuja), C/ Capitana 6","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":110,"nombre":"ADI HOGAR Y HOSTELERIA IBERIA SL","municipio":"Villanueva de Gállego","ubicacion":"C/ Río Piedra s/n, Pol. Ind. San Miguel, 50830","confianza":"alta","domicilio_fiscal":"Madrid","fuente":"iberinform"},
{"pos":111,"nombre":"GARDA SERVICIOS DE SEGURIDAD SA","municipio":"Zaragoza","ubicacion":"C/ Maestro Estremiana 22, 1º (seguridad privada)","confianza":"media","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":112,"nombre":"AVIATO MOTORS SL","municipio":"Zaragoza","ubicacion":"Pol. Ind. Molino del Pilar, C/ David Fahrenheit 22, 50015 (concesionario)","confianza":"alta","domicilio_fiscal":"","fuente":"motor.es"},
{"pos":113,"nombre":"SOCIEDAD ARAGONESA DE GESTION AGROAMBIENTAL SL","municipio":"Zaragoza","ubicacion":"Av. de Ranillas 5, edif. A (SARGA; empresa pública)","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":114,"nombre":"FERSA BEARINGS SA","municipio":"Zaragoza","ubicacion":"PLAZA, C/ Bari 18 (fábrica de rodamientos)","confianza":"alta","domicilio_fiscal":"","fuente":"plazalogistica"},
{"pos":115,"nombre":"AUTOMOVILES SANCHEZ SA","municipio":"Zaragoza","ubicacion":"Ctra. de Logroño 32, 50011 (concesionario)","confianza":"alta","domicilio_fiscal":"","fuente":"automovilessanchez"},
{"pos":116,"nombre":"EBROSA SAU","municipio":"Zaragoza","ubicacion":"Paseo Independencia 21, 3ª (promoción inmobiliaria)","confianza":"alta","domicilio_fiscal":"","fuente":"empresite"},
{"pos":117,"nombre":"EXPORTACIONES APOLO GROUP SL","municipio":"Zaragoza","ubicacion":"C/ Bari 57, Edif. TIC XXI (PLAZA); registros antiguos en Cadrete","confianza":"media","domicilio_fiscal":"","fuente":"infonif"},
{"pos":118,"nombre":"DKV SERVICIOS SA","municipio":"Zaragoza","ubicacion":"C/ Poetisa María Zambrano 31, 50018 (sede DKV Seguros)","confianza":"alta","domicilio_fiscal":"","fuente":"informa"},
{"pos":119,"nombre":"BUDENHEIM IBERICA SLU","municipio":"La Zaida","ubicacion":"Calle Extramuros s/n, 50784 (química inorgánica)","confianza":"alta","domicilio_fiscal":"","fuente":"qdq"},
{"pos":120,"nombre":"DR. SCHAR ESPAÑA SLU","municipio":"Alagón","ubicacion":"Pol. Ind. La Ciruela, Av. de Repol parc. 2, 50630 (fábrica sin gluten)","confianza":"alta","domicilio_fiscal":"","fuente":"alimentosmadeinaragon"},
]

# 121-140
lotes += [
{"pos":121,"nombre":"MAS PREVENCION SERVICIO DE PREVENCION SL","municipio":"Zaragoza","ubicacion":"C/ Alfonso I 17 (sede); centro C/ Monasterio de Samos 31, 50013","confianza":"alta","domicilio_fiscal":"","fuente":"axesor"},
{"pos":122,"nombre":"ESPUBLICO SERVICIOS PARA LA ADMINISTRACION SAU","municipio":"Zaragoza","ubicacion":"Pol. PLAZA, C/ Bari 39, 50197","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":123,"nombre":"VITALIA SUITE SL","municipio":"Zaragoza","ubicacion":"C/ Joaquín Costa 2 (residencias de mayores)","confianza":"media","domicilio_fiscal":"","fuente":"empresite"},
{"pos":124,"nombre":"MINERA DE SANTA MARTA SA","municipio":"Zaragoza","ubicacion":"Paseo Independencia 21 (Grupo SAMCA; plantas de sulfato sódico en Burgos y Toledo, fuera)","confianza":"media","domicilio_fiscal":"","fuente":"einforma"},
{"pos":125,"nombre":"EUROARCE MINERIA SA","municipio":"Zaragoza","ubicacion":"Paseo Independencia 21, 50001 (oficina; Grupo SAMCA)","confianza":"media","domicilio_fiscal":"","fuente":"infoempresa"},
{"pos":126,"nombre":"VALORISTA SL","municipio":"Zaragoza","ubicacion":"Pol. PLAZA, C/ Bari 11 / almacén C/ Bari 28 nave B, 50197","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":127,"nombre":"WITTUR ELEVATOR COMPONENTS SA","municipio":"Zaragoza","ubicacion":"Pol. Ind. Malpica, Calle E 8, 50016","confianza":"alta","domicilio_fiscal":"","fuente":"wittur"},
{"pos":128,"nombre":"SCANFISK SEAFOOD SL","municipio":"Zaragoza","ubicacion":"Mercazaragoza, Ctra. de Cogullada 65, Calle P parc. 29, 50014","confianza":"alta","domicilio_fiscal":"","fuente":"einforma"},
{"pos":129,"nombre":"COALVI SA","municipio":"Zaragoza","ubicacion":"C/ George Stephenson 46, 50015","confianza":"alta","domicilio_fiscal":"","fuente":"einforma"},
{"pos":130,"nombre":"CABLES DE COMUNICACIONES ZARAGOZA SL","municipio":"Zaragoza","ubicacion":"Pol. Ind. Malpica, Calle D 83, 50016 (planta 77.000 m²)","confianza":"alta","domicilio_fiscal":"","fuente":"paginasamarillas"},
{"pos":131,"nombre":"GESTAMP MANUFACTURING AUTOCHASIS SL","municipio":"Pedrola","ubicacion":"Pol. El Pradillo, C/ Aneto 5, 50690","confianza":"alta","domicilio_fiscal":"","fuente":"kompass"},
{"pos":132,"nombre":"GRUPO METALGRAFICO SA","municipio":"Sobradiel","ubicacion":"Ctra. de Logroño km 16, 50629","confianza":"alta","domicilio_fiscal":"","fuente":"einforma"},
{"pos":133,"nombre":"TROX ESPAÑA SA","municipio":"Zaragoza","ubicacion":"Pol. Ind. La Cartuja, Ctra. Castellón km 7, 50720 (La Cartuja Baja)","confianza":"alta","domicilio_fiscal":"","fuente":"aragonhoy"},
{"pos":134,"nombre":"SAT VIDRIO","municipio":"Ricla","ubicacion":"Paraje Tejas Royas, 50270 (cerezas; SAT Red Fruits)","confianza":"alta","domicilio_fiscal":"","fuente":"aragonhoy"},
{"pos":135,"nombre":"ARCELORMITTAL TAILORED BLANKS ZARAGOZA SL","municipio":"Pedrola","ubicacion":"Pol. El Pradillo II, C/ General Motors 7, 50690","confianza":"alta","domicilio_fiscal":"","fuente":"innovatus"},
{"pos":136,"nombre":"ELECTRONICA CERLER SA","municipio":"La Muela","ubicacion":"Pol. Ind. Centrovía, Av. Los Ángeles 17, 50196","confianza":"alta","domicilio_fiscal":"","fuente":"einforma"},
{"pos":137,"nombre":"PROFESIONALES DE LA CARNE SL","municipio":"Villanueva de Gállego","ubicacion":"C/ Río Vero 1, 50830 (central)","confianza":"alta","domicilio_fiscal":"","fuente":"profecarne"},
{"pos":138,"nombre":"TRENDICO GROUP SL","municipio":"Ejea de los Caballeros","ubicacion":"Paseo del Muro 60 bajos, 50600 (origen Twinner; oficina también en WTCZ Zaragoza)","confianza":"alta","domicilio_fiscal":"","fuente":"empresite"},
{"pos":139,"nombre":"COMPAÑIA DE OBRAS PUBLICAS HORMIGONES Y ASFALTOS SL","municipio":"Zaragoza","ubicacion":"C/ Uncastillo 19 bajos, 50008 (COPHASA)","confianza":"alta","domicilio_fiscal":"","fuente":"axesor"},
{"pos":140,"nombre":"LINAMAR LIGHT METALS ZARAGOZA SA","municipio":"Zaragoza","ubicacion":"Ctra. de Castellón km 6,4, 50720 (La Cartuja; antigua Alumalsa)","confianza":"alta","domicilio_fiscal":"","fuente":"einforma"},
]

# 141-160
lotes += [
{"pos":141,"nombre":"EXPLOTACIONES BAJO ARAGON SL","municipio":"Caspe","ubicacion":"Partida Vuelta del Rey s/n, 50700 (porcino)","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":142,"nombre":"PROMA HISPANIA SA","municipio":"Épila","ubicacion":"Avenida Opel España, 50290 (componentes automoción)","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":143,"nombre":"ARQUITECTURA INGENIERIA Y CONSTRUCCION LOBE SA","municipio":"Zaragoza","ubicacion":"C/ Monasterio de las Descalzas Reales 26 (Grupo Lobe)","confianza":"alta","domicilio_fiscal":"","fuente":"einforma"},
{"pos":144,"nombre":"INSTRUMENTACION Y COMPONENTES SA","municipio":"Zaragoza","ubicacion":"C/ Alaún 8, PLAZA, 50197 (INYCOM)","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":145,"nombre":"OVIARAGON SCL","municipio":"Zaragoza","ubicacion":"Camino de Cogullada 65, Mercazaragoza, Ed. Pastores, 50014","confianza":"alta","domicilio_fiscal":"","fuente":"oviaragon"},
{"pos":146,"nombre":"ARTAL VEHICULOS ZARAGOZA SL","municipio":"Zaragoza","ubicacion":"C/ Langa del Castillo 8, 50013 (concesionario Toyota)","confianza":"alta","domicilio_fiscal":"","fuente":"einforma"},
{"pos":147,"nombre":"AUGUSTA ARAGON SA","municipio":"Zaragoza","ubicacion":"Av. Alcalde Francisco Caballero 112, 50014 (concesionario BMW/MINI)","confianza":"alta","domicilio_fiscal":"","fuente":"augustaaragon"},
{"pos":148,"nombre":"MOLINOS DEL EBRO SA","municipio":"Zaragoza","ubicacion":"Paseo Independencia 21 (Grupo SAMCA)","confianza":"media","domicilio_fiscal":"","fuente":"alimarket"},
{"pos":149,"nombre":"JORGE PORK MEAT SLU","municipio":"Zuera","ubicacion":"Complejo cárnico de Grupo Jorge (matadero/despiece)","confianza":"media","domicilio_fiscal":"Zaragoza","fuente":"jorgesl"},
{"pos":150,"nombre":"BRILEN TECH SA","municipio":"FUERA","ubicacion":"Planta en Pol. Valle del Cinca, Barbastro (Huesca); fibras poliéster (Grupo SAMCA)","confianza":"media","domicilio_fiscal":"Zaragoza","fuente":"empresite"},
{"pos":151,"nombre":"VALENTO TEXTILE SL","municipio":"Zaragoza","ubicacion":"C/ Burtina 12, PLAZA, 50197 (ropa laboral/deportiva)","confianza":"alta","domicilio_fiscal":"","fuente":"valento"},
{"pos":152,"nombre":"GLOBAL SPEDITION SL","municipio":"Zaragoza","ubicacion":"C/ Guillermo Gúdel Martí 50, Pol. Malpica, 50016 (transporte ADR)","confianza":"alta","domicilio_fiscal":"","fuente":"alimarket"},
{"pos":153,"nombre":"KDK-DONGKOOK AUTOMOTIVE SPAIN SA","municipio":"Borja","ubicacion":"Av. Campo de Borja 23, Pol. Ind. Barbalanca, 50540 (plásticos automoción)","confianza":"alta","domicilio_fiscal":"","fuente":"kdkautomotive"},
{"pos":154,"nombre":"ZALUX SA","municipio":"Alhama de Aragón","ubicacion":"Dos plantas (42.000 m²) en Alhama de Aragón; oficinas en Zaragoza (Grupo Trilux)","confianza":"alta","domicilio_fiscal":"Zaragoza","fuente":"interempresas"},
{"pos":155,"nombre":"HIBERUS TECNOLOGIAS DE LA INFORMACION SL","municipio":"Zaragoza","ubicacion":"Paseo Isabel la Católica 6, 50009 (y oficinas en PLAZA, C/ Bari 25)","confianza":"alta","domicilio_fiscal":"","fuente":"einforma"},
{"pos":156,"nombre":"INSONORIZANTES PELZER SA","municipio":"Zaragoza","ubicacion":"Pol. Ind. Malpica, C/ D parc. 36 (Grupo Adler Pelzer)","confianza":"alta","domicilio_fiscal":"","fuente":"kompass"},
{"pos":157,"nombre":"OPEL EUROPE HOLDINGS SL","municipio":"Figueruelas","ubicacion":"Pol. Entrerríos km 29 s/n, 50639 (planta Stellantis/Opel España)","confianza":"alta","domicilio_fiscal":"","fuente":"infoempresa"},
{"pos":158,"nombre":"IDE ELECTRIC SL","municipio":"Zuera","ubicacion":"C/ Leonardo da Vinci 2, Pol. Los Huertos, 50800 (envolventes eléctricas)","confianza":"alta","domicilio_fiscal":"","fuente":"ide.es"},
{"pos":159,"nombre":"ITESAL SL","municipio":"Pina de Ebro","ubicacion":"Polígono Industrial (C/ G) s/n, 50750 (perfiles de aluminio)","confianza":"alta","domicilio_fiscal":"","fuente":"einforma"},
{"pos":160,"nombre":"CONTAZARA SA","municipio":"Zaragoza","ubicacion":"Ctra. de Castellón km 5,5, Pol. San Valero, 50720 (La Cartuja Baja; contadores de agua)","confianza":"alta","domicilio_fiscal":"","fuente":"contazara"},
]

# 186-200
lotes += [
{"pos":186,"nombre":"ZOILO RIOS SA","municipio":"Zaragoza","ubicacion":"Oficinas y E.S. El Portazgo, Autovía de Logroño p.k. 0,3, 50011","confianza":"alta","domicilio_fiscal":"","fuente":"firmania"},
{"pos":187,"nombre":"MONCAYO AGRICOLA SL","municipio":"Vera de Moncayo","ubicacion":"Calle Portaza s/n, 50580","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":188,"nombre":"INDUSTRIAS LOPEZ SORIANO SL","municipio":"Zaragoza","ubicacion":"Pol. Tecnológico del Reciclado López Soriano, C/ Aluminio 71, Cartuja Baja","confianza":"alta","domicilio_fiscal":"","fuente":"paginasamarillas"},
{"pos":189,"nombre":"NTT DATA SPAIN SOLUCIONES TECNOLOGICAS SL","municipio":"Zaragoza","ubicacion":"C.E. El Trovador, Plaza de Antonio Beltrán Martínez 1, 50002 (centro operativo)","confianza":"media","domicilio_fiscal":"Madrid","fuente":"infonif"},
{"pos":190,"nombre":"DESARROLLO AGRICOLA Y MINERO SA (DAYMSA)","municipio":"Zaragoza","ubicacion":"Camino de Enmedio 120, Pol. Ind. Miraflores, 50013","confianza":"alta","domicilio_fiscal":"","fuente":"daymsa"},
{"pos":191,"nombre":"GRUPO DELIFACTORY SL","municipio":"Utebo","ubicacion":"Ctra. de Logroño 92, 50180 (grupo SAMCA); domicilio social en Zaragoza","confianza":"media","domicilio_fiscal":"Zaragoza","fuente":"iberinform"},
{"pos":192,"nombre":"AUTOSALDUBA SA","municipio":"Zaragoza","ubicacion":"Av. Cataluña 103-105, 50014 (concesionario Kia)","confianza":"alta","domicilio_fiscal":"","fuente":"empresite"},
{"pos":193,"nombre":"ÑAMING SLU","municipio":"Mallén","ubicacion":"C/ País Vasco 5, Pol. El Zafranar, 50550","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":194,"nombre":"COOP AGRICOLA ARAGONESA DEL EBRO","municipio":"Zaragoza","ubicacion":"CADEBRO/Agroveco, Av. de Logroño 136, 50011 (Casetas)","confianza":"alta","domicilio_fiscal":"","fuente":"empresite"},
{"pos":195,"nombre":"OLEOHIDRAULICA FERRUZ SA","municipio":"Zaragoza","ubicacion":"C/ Cobalto 31, Parque Tecnológico de Reciclado (PTR), 50720","confianza":"alta","domicilio_fiscal":"","fuente":"empresite"},
{"pos":196,"nombre":"AGROPECUARIA DEL VALLE DEL EBRO S.COOP","municipio":"Zaragoza","ubicacion":"Ctra. de Logroño, 50620 (Casetas, barrio de Zaragoza)","confianza":"media","domicilio_fiscal":"","fuente":"kompass"},
{"pos":197,"nombre":"ESPADESA RETAIL SL","municipio":"Zaragoza","ubicacion":"Ronda del Ferrocarril 24, PLAZA, 50197 (Española del Descanso)","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":198,"nombre":"DIAGNOSTICA LONGWOOD SL","municipio":"Zaragoza","ubicacion":"Av. Diagonal 40, Pol. PLAZA, 50197","confianza":"alta","domicilio_fiscal":"","fuente":"dlongwood"},
{"pos":199,"nombre":"SERVICIOS LOGISTICOS MARTORELL SIGLO XXI SL","municipio":"Zaragoza","ubicacion":"C/ Virgen del Buen Acuerdo 5, 50014 (Grupo Sesé)","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":200,"nombre":"CERTEST BIOTEC SL","municipio":"San Mateo de Gállego","ubicacion":"Pol. Ind. Río Gállego II, Calle J nº 1, 50840","confianza":"alta","domicilio_fiscal":"","fuente":"certest"},
]

# 161-180
lotes += [
{"pos":161,"nombre":"MULTIANAU SL","municipio":"Zaragoza","ubicacion":"Calle A 24, Plataforma Ciudad del Transporte (Cogullada/Malpica), 50820","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":162,"nombre":"MAETEL INSTALACIONES Y SERVICIOS INDUSTRIALES SAU","municipio":"Zaragoza","ubicacion":"C/ Bari 33, Edificio 3, PLAZA, 50197","confianza":"alta","domicilio_fiscal":"","fuente":"axesor"},
{"pos":163,"nombre":"CABLENA SA","municipio":"Zaragoza","ubicacion":"Pol. Ind. Malpica, calle E 43-44, 50016","confianza":"alta","domicilio_fiscal":"","fuente":"kompass"},
{"pos":164,"nombre":"BM SPORTECH IB SL","municipio":"Zaragoza","ubicacion":"C/ Terracina 12, PLAZA, 50197","confianza":"alta","domicilio_fiscal":"","fuente":"empresite"},
{"pos":165,"nombre":"BRILEN SA","municipio":"FUERA","ubicacion":"Oficina en Paseo Independencia 21, Zaragoza; fábrica de hilo de poliéster en Barbastro (Huesca)","confianza":"media","domicilio_fiscal":"Zaragoza","fuente":"infoempresa"},
{"pos":166,"nombre":"CARVISA CONTAINER SL","municipio":"Remolinos","ubicacion":"Ctra. Alagón-Tudela km 44,9, Nave 2, 50637 (grupo Eurocontainer)","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":167,"nombre":"INTERLAZARO SL","municipio":"Calatayud","ubicacion":"Ctra. Madrid-Barcelona km 238,8, 50300","confianza":"alta","domicilio_fiscal":"","fuente":"empresia"},
{"pos":168,"nombre":"INGENIERIA Y APLICACIONES SOLARES ZARAGOZA 2005 SL","municipio":"Zaragoza","ubicacion":"C/ Argualas 40, 1º, 50012 (IASOL)","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":169,"nombre":"ADIEGO HERMANOS SA","municipio":"Cuarte de Huerva","ubicacion":"Ctra. de Valencia km 5,9, 50410 (también almacén en Cartuja Baja, Zaragoza)","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":170,"nombre":"FRUTARIA MARKETS MADRID SA","municipio":"Zaragoza","ubicacion":"C/ Bilbao 5, 50004 (mayorista de frutas; domicilio en Zaragoza pese al nombre)","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":171,"nombre":"ITALPANNELLI SA","municipio":"La Almunia de Doña Godina","ubicacion":"Pol. Ind. La Cuesta, 50100 (paneles sándwich)","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":172,"nombre":"SOCIEDAD ANONIMA DE MINERIA Y TECNOLOGIA DE ARCILLAS","municipio":"Zaragoza","ubicacion":"Paseo Independencia 21, 50001 (MyTA, Grupo SAMCA; explotaciones no localizadas)","confianza":"media","domicilio_fiscal":"","fuente":"empresite"},
{"pos":173,"nombre":"COMERCIAL SALGAR SL","municipio":"Zaragoza","ubicacion":"Autovía de Logroño km 9,5, 50011 (mueble de baño Salgar)","confianza":"alta","domicilio_fiscal":"","fuente":"salgar"},
{"pos":174,"nombre":"GRUPO LOGISTICO SESE SL","municipio":"Zaragoza","ubicacion":"Sede Grupo Sesé, C/ Virgen del Buen Acuerdo, 50014 (zona Malpica)","confianza":"alta","domicilio_fiscal":"","fuente":"gruposese"},
{"pos":175,"nombre":"TUBOS PERFILADOS SA","municipio":"El Burgo de Ebro","ubicacion":"Ctra. de Castellón km 15,5, Pol. La Noria, 50730","confianza":"alta","domicilio_fiscal":"","fuente":"datoscif"},
{"pos":176,"nombre":"TELTRONIC SAU","municipio":"Zaragoza","ubicacion":"Pol. Ind. Malpica, calle F Oeste, 50016 (radiocomunicaciones TETRA)","confianza":"alta","domicilio_fiscal":"","fuente":"teltronic"},
{"pos":177,"nombre":"SAICA FLEXIBLE SAU","municipio":"Zaragoza","ubicacion":"Sede SAICA, C/ San Juan de la Peña 144, 50015 (planta específica no confirmada)","confianza":"media","domicilio_fiscal":"","fuente":"saica"},
{"pos":178,"nombre":"ADLER PELZER SPAIN SL","municipio":"Zaragoza","ubicacion":"Pol. Ind. Malpica, calle E 36 (insonorizantes automoción)","confianza":"alta","domicilio_fiscal":"","fuente":"infoempresa"},
{"pos":179,"nombre":"SERVICIOS RENOVADOS DE ALIMENTACION SAU (SERAL)","municipio":"Zaragoza","ubicacion":"C/ Castilla 8-10, 50009 (catering/restauración colectiva)","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform/alimarket"},
{"pos":180,"nombre":"PROMOCIONES ARAOPESA SL","municipio":"Zaragoza","ubicacion":"C/ Monasterio de las Descalzas Reales 26 (promoción inmobiliaria)","confianza":"alta","domicilio_fiscal":"","fuente":"empresia"},
]

# 181-185 (investigadas directamente por WebSearch)
lotes += [
{"pos":181,"nombre":"BUSINESS TELECOMMUNICATIONS SERVICES EUROPE SA","municipio":"Zaragoza","ubicacion":"C/ San Miguel 7 / C/ Josefa Amar y Borbón 10, 50001 (telecom, oficina)","confianza":"alta","domicilio_fiscal":"","fuente":"iberinform"},
{"pos":182,"nombre":"KETER IBERIA SL","municipio":"Zaragoza","ubicacion":"Autovía de Logroño (N-232) km 4,5, 50011 (Monzalbarba; planta/almacén)","confianza":"alta","domicilio_fiscal":"","fuente":"kompass/waze"},
{"pos":183,"nombre":"ARALOGIC SL","municipio":"Zuera","ubicacion":"Pol. Ind. El Campillo 75, 50800 (transporte de mercancías)","confianza":"alta","domicilio_fiscal":"","fuente":"alimarket"},
{"pos":184,"nombre":"ROLABO OUTSOURCING SL","municipio":"Zaragoza","ubicacion":"Pol. Ind. Malpica, Calle J parc. 3-4, 50016 (fabricación farmacéutica)","confianza":"alta","domicilio_fiscal":"","fuente":"kompass/iberinform"},
{"pos":185,"nombre":"DISTRIBUCIONES RODRIGO SA","municipio":"Zaragoza","ubicacion":"Pol. Ind. El Portazgo, Ctra. Logroño 2, nave 73, 50011 (distribución alimentaria)","confianza":"alta","domicilio_fiscal":"","fuente":"paginasamarillas"},
]

# ── Fusion final: cruzar con empresas_ranking.json (facturacion, cnae) y ordenar ──
d = {o["pos"]: o for o in lotes}
faltan = [p for p in range(1,201) if p not in d]
rank = {e["pos"]: e for e in json.load(open("empresas_ranking.json", encoding="utf-8"))}
final = []
for p in range(1, 201):
    o = d.get(p, {"pos": p, "municipio": "DESCONOCIDO", "ubicacion": "", "confianza": "baja", "domicilio_fiscal": "", "fuente": ""})
    r = rank.get(p, {})
    final.append({
        "pos": p,
        "nombre": o.get("nombre") or r.get("nombre", ""),
        "cnae": r.get("cnae", ""),
        "facturacion": r.get("facturacion", ""),
        "municipio": o.get("municipio", ""),
        "ubicacion": o.get("ubicacion", ""),
        "domicilio_fiscal": o.get("domicilio_fiscal", ""),
        "confianza": o.get("confianza", ""),
        "fuente": o.get("fuente", ""),
    })
json.dump(final, open("empresas_ubicaciones.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# Tabla Markdown
def md_row(c): return "| {pos} | {nombre} | {municipio} | {ubicacion} | {conf} |".format(
    pos=c["pos"], nombre=c["nombre"], municipio=c["municipio"],
    ubicacion=(c["ubicacion"][:70]), conf=c["confianza"])
lines = ["| # | Empresa | Municipio | Ubicación | Conf. |", "|---:|---|---|---|---|"]
lines += [md_row(c) for c in final]
open("empresas_ubicaciones.md", "w", encoding="utf-8").write("\n".join(lines) + "\n")

# CSV
import csv
with open("empresas_ubicaciones.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f, delimiter=";")
    w.writerow(["pos","nombre","cnae","facturacion","municipio","ubicacion","domicilio_fiscal","confianza","fuente"])
    for c in final:
        w.writerow([c["pos"],c["nombre"],c["cnae"],c["facturacion"],c["municipio"],c["ubicacion"],c["domicilio_fiscal"],c["confianza"],c["fuente"]])

# Resumen
from collections import Counter
faltan2 = [c["pos"] for c in final if c["municipio"] in ("DESCONOCIDO","")]
fuera = [c["pos"] for c in final if c["municipio"] == "FUERA"]
muni = Counter(c["municipio"] for c in final if c["municipio"] not in ("DESCONOCIDO","FUERA",""))
conf = Counter(c["confianza"] for c in final)
print("TOTAL:", len(final), "| sin municipio:", faltan2, "| FUERA:", fuera)
print("confianza:", dict(conf))
print("TOP municipios:")
for m,n in muni.most_common(15): print("  %3d  %s" % (n, m))
print("municipios distintos (provincia):", len(muni))
