proc init_header {arg } {
	#fonction qui va initialiser les headers a zero
	#important pour ne pas réécrire une vielle variable
	buf1 setkwd [list "ORIGIN" "LAE" string "Laboratoire d'astrophysique experimental" ""]
	buf1 setkwd [list "INSTRUME" "PESTO+Ador" string "Instrument name" ""]
	buf1 setkwd [list "TELESCOP" "OMM" string "Observatoire du Mont-Megantic" ""]
	buf1 setkwd [list "RA" 999 float "Right ascension at the begining of the sequence" ""]
	buf1 setkwd [list "DEC" 999 float "Declination at the begining of the sequence" ""]
	buf1 setkwd [list "EPOCH" 999 float "Epoch of the coordinate" ""]
	buf1 setkwd [list "HA" 999 float "Hour angle at the begining of the sequence" ""]
	buf1 setkwd [list "AIRMASS" 999 float "Air mass at the begining of the sequence" ""]
	buf1 setkwd [list "TFOCUS" 999 float "Focus of the telescope at the begining of the sequence" ""]
	buf1 setkwd [list "IROTATOR" 999 float "Angle of the instrument rotator" ""]
	buf1 setkwd [list "DOME" 999 float "Angle of the dome at the begining of the sequence" ""]
	buf1 setkwd [list "FILTRE" "" string "Filter used at the begining of the sequence" ""]
	buf1 setkwd [list "PESTOROT" 999 float "Angle of the FOV rotator at the begining of the sequence" ""]
	buf1 setkwd [list "PESTOMIR" 999 float "Position of the pickup mirror (degree) at the begining of the sequence" ""]
	buf1 setkwd [list "OBSERV" "" string "Name of the observer" ""]
	buf1 setkwd [list "OPERATOR" "" string "Name of the telescope operator" ""]
	buf1 setkwd [list "HUMIN" 999 float "Interior humidity (%) at the begining of the sequence" ""]
	buf1 setkwd [list "HUMOUT" 999 float "Exterior humidity (%) at the begining of the sequence" ""]
	buf1 setkwd [list "TEMPIN" 999 float "Interior temperature (C) at the begining of the sequence" ""]
	buf1 setkwd [list "TEMPOUT" 999 float "Exterior temperature (C) at the begining of the sequence" ""]
	buf1 setkwd [list "TEMPST" 999 float "Telescope structure temperature (C) at the begining of the sequence" ""]
	buf1 setkwd [list "TEMPM" 999 float "Mirror temperature (C) at the begining of the sequence" ""]
}
proc set_temp { Hin Hout Tin Tout Tstruct Tmir } {
	buf1 setkwd [list "HUMIN" $Hin float "Interior humidity (%) at the begining of the sequence" ""]
        buf1 setkwd [list "HUMOUT" $Hout float "Exterior humidity (%) at the begining of the sequence" ""]
        buf1 setkwd [list "TEMPIN" $Tin float "Interior temperature (C) at the begining of the sequence" ""]
        buf1 setkwd [list "TEMPOUT" $Tout float "Exterior temperature (C) at the begining of the sequence" ""]
        buf1 setkwd [list "TEMPST" $Tstruct float "Telescope structure temperature (C) at the begining of the sequence" ""]
        buf1 setkwd [list "TEMPM" $Tmir float "Mirror temperature (C) at the begining of the sequence" ""]
}
proc set_people { observ ope } {
	buf1 setkwd [list "OBSERV" $observ string "Name of the observer" ""]
        buf1 setkwd [list "OPERATOR" $ope string "Name of the telescope operator" ""]
}
proc set_telinfo { RA DEC EPOCH HA AIRMASS TFOCUS IROTATOR DOME } {
	buf1 setkwd [list "RA" $RA float "Right ascension at the begining of the sequence" ""]
        buf1 setkwd [list "DEC" $DEC float "Declination at the begining of the sequence" ""]
        buf1 setkwd [list "EPOCH" $EPOCH float "Epoch of the coordinate" ""]
        buf1 setkwd [list "HA" $HA float "Hour angle at the begining of the sequence" ""]
        buf1 setkwd [list "AIRMASS" $AIRMASS float "Air mass at the begining of the sequence" ""]
        buf1 setkwd [list "TFOCUS" $TFOCUS float "Focus of the telescope at the begining of the sequence" ""]
        buf1 setkwd [list "IROTATOR" $IROTATOR float "Angle of the instrument rotator" ""]
        buf1 setkwd [list "DOME" $DOME float "Angle of the dome at the begining of the sequence" ""]
}
proc set_pesto { filtre bras rot } {
	buf1 setkwd [list "FILTRE" $filtre string "Filter used at the begining of the sequence" ""]
        buf1 setkwd [list "PESTOROT" $bras float "Angle of the FOV rotator at the begining of the sequence" ""]
        buf1 setkwd [list "PESTOMIR" $rot float "Position of the pickup mirror (degree) at the begining of the sequence" ""]
}
	
