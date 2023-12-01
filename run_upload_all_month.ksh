micromamba activate zenodo

for m in $(seq 3 12); do
	mm=$(printf "%02d" $m)
	case $m in
		1|2|2|3|4|5|6) year=2010;;
		7|8|9|10|11|12) year=2009;;
	esac

	case $m in
		1|3|5|7|8|10|12) dayf=31;;
		2) dayf=28;;
		4|6|9|11) dayf=30;;
	esac

	cp template_upload_eNATL60-BLBT02-TSW_60m_monthly.py tmp_upload_eNATL60-BLBT02-TSW_60m_year${year}m${mm}.py
	sed -i "s/YEAR/${year}/g" tmp_upload_eNATL60-BLBT02-TSW_60m_year${year}m${mm}.py
	sed -i "s/MONTH/${mm}/g" tmp_upload_eNATL60-BLBT02-TSW_60m_year${year}m${mm}.py
	sed -i "s/DAYF/${dayf}/g" tmp_upload_eNATL60-BLBT02-TSW_60m_year${year}m${mm}.py
	python tmp_upload_eNATL60-BLBT02-TSW_60m_year${year}m${mm}.py
done




