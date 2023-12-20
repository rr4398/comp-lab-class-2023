grep "Excitation Energy" acetone_tddft.out -A 15 | sed "1d"| sed "1d"|sed "1d"| awk {'print$6'} > acetone.dat
grep "Excitation Energy" water_tddft.out -A 15 | sed "1d"| sed "1d"|sed "1d"| awk {'print$6'} > water.dat
grep "Excitation Energy" imidazole_tddft.out -A 15 | sed "1d"| sed "1d"|sed "1d"| awk {'print$6'} > imidazole.dat
grep "Excitation Energy" formaldehyde_tddft.out -A 15 | sed "1d"| sed "1d"|sed "1d"| awk {'print$6'} > formaldehyde.dat
