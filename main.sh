#!/bin/bash
while IFS="" read -r p || [ -n "$p" ]
do
  printf '%s\n' "$p"
  printf '%s\n'
#  scp -i kp-hom.pem ubuntu@10.10.196.94:/var/www/$p/.env .
#  mv .env $p.env
python.exe main.py $p
done < peptides.txt
