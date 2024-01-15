
cd /mnt/summer/DATA_MEOM/workdir/alberta/test-mask

#ncks -O -v tmask -d z,23,23 /mnt/summer/DATA_MEOM/MODEL_SET/eNATL60/eNATL60-I/mask_eNATL60_3.6.nc tmask_eNATL60_60m.nc
#ncwa -O -a z tmask_eNATL60_60m.nc tmask_eNATL60_60m.nc

for file in $(ls /mnt/summer/DATA_MEOM/MODEL_SET/eNATL60/eNATL60-BLBT02/1d/eNATL60/eNATL60-BLBT02_y*.1d_TSW_60m.nc); do
	fileo=$(basename $file | sed "s/TSW/TSWm/g")
	if [ ! -f $fileo ]; then
		cp $file $fileo
		ncrename -d time_counter,t $fileo
		ncks -A -v tmask tmask_eNATL60_60m.nc $fileo
		ncap2 -O -s 'where(tmask==0) votemper=nan;' $fileo $fileo
		ncap2 -O -s 'where(tmask==0) vosaline=nan;' $fileo $fileo
		ncap2 -O -s 'where(tmask==0) vovecrtz=nan;' $fileo $fileo
		ncks -C -O -x -v nav_lat,nav_lon $fileo $fileo
		ncks -A -v nav_lat,nav_lon /mnt/summer/DATA_MEOM/MODEL_SET/eNATL60/eNATL60-I/mask_eNATL60_3.6.nc $fileo
		ncrename -d t,time $fileo
	
		mv $fileo /mnt/summer/DATA_MEOM/MODEL_SET/eNATL60/eNATL60-BLBT02/1d/eNATL60/.
	fi
done


