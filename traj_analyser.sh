#! /bin/bash

# i didn't had the time to make it clean so for now on just change the prtom and pdb extension to apply it to you own dynamics 

cpptraj -i cpptraj_all_frame_extract.in

touch results_contact.txt

for f in {1..5000};
do
	python3 contact_finder.py --pdb Mt_prot_frame.pdb.$f --start1 12  --end1 60 --start2 68 --end2 119 >> results_contact.txt 
	
	python3 contact_finder.py --pdb Mt_prot_frame.pdb.$f --start1 12 --end1 60 --start2 135 --end2 185 >> results_contact.txt 
        
	python3 contact_finder.py --pdb Mt_prot_frame.pdb.$f --start1 68 --end1 119 --start2 135 --end2 185 >> results_contact.txt 
done

python3 contact_result_analysis.py --result results_contact.txt > contact_matrix.csv
sed -i 's/ //g' contact_matrix.csv
exit
