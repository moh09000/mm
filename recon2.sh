#!/bin/bash
green="\033[0;32m"
nc="\033[0m"
mkdir vulnerabilities
mkdir vulnerabilities/cors/
mkdir vulnerabilities/xss/
mkdir vulnerabilities/sql/
mkdir vulnerabilities/LFI/
mkdir vulnerabilities/commandinject/
mkdir takeover
mkdir nuclei_sca
mkdir nuclei_sca/vulnerabilities/
mkdir nuclei_sca/misconfiguration/
mkdir nuclei_sca/technology/
mkdir nuclei_sca/cves/
mkdir waybackurls
mkdir nmap
mkdir vulnerabilities/dorks/
mkdir vulnerabilities/crlf/
mkdir subdomains
##########SUBDOMAIN ENUMRATIONNNNNNN#########

echo -e "${green}Start subfinder${nc}"
subfinder -all -dL scope.txt  | tee -a domain.txt

for i in $(cat scope.txt)
do
    arrIN=(${i//٠/ }) # تقسيم النطاق
    word=${arrIN[0]}
assetfinder  $i | grep -i "$i"  | tee assetfinder 
cat assetfinder | tee -a domain.txt
cat  assetfinder | assetfinder  -subs-only | tee -a domain.txt
wait
done
rm assetfinder
cat domain.txt | anew | tee -a domains.txt
rm domain.txt 
echo -e "${green}Start httpx the Output in ${red}alive.txt${nc}"
httpx  -l domains.txt  | tee -a alive.txt

echo -e "${green}CONNECTING URLS ${red}alive.txt${nc}" 
cat alive.txt | tee paramdomain
sed -i 's/https:\/\///g' paramdomain
sed -i 's/http:\/\///g' paramdomain


cat paramdomain | while read url ; do paramspider -d $url ; done 
cat results/* | awk -F'\\?' '{split($1, arr, "/"); domain = arr[3]; param = $2} {if (!seen[domain,param]++) print}' |  tee allurls.txt 

 dnsx -l domains.txt -a -aaaa -cname -ns -ptr -mx -soa -silent -retry 3 -json -o subdomains/subdomains.json
 cat subdomains/subdomains.json  | jq -r 'try . | "\(.a[0])"' | tee subdomains/ips.txt
 

echo -e "${green}GF START ${red}alive.txt${nc}" 
gf xss allurls.txt | qsreplace "FUZZ"| tee waybackurls/xss.txt  
gf ssrf allurls.txt | qsreplace "FUZZ"| tee waybackurls/ssrf.txt 
gf sqli allurls.txt | qsreplace "1"| tee waybackurls/sql.txt 
gf lfi allurls.txt | qsreplace "FUZZ"|  tee waybackurls/lfi.txt 
gf ssti allurls.txt | qsreplace "FUZZ"| tee waybackurls/ssti.txt 
gf redirect allurls.txt |qsreplace "FUZZ"|  tee waybackurls/redirect.txt  
gf idor allurls.txt |qsreplace "FUZZ"|  tee waybackurls/idor.txt 
gf rce allurls.txt |qsreplace "FUZZ"|  tee waybackurls/rce.txt 

########################first##################
echo -e "${green}SEARCH SUB TAKE OVER ${red}alive.txt${nc}" 
subzy run  --targets domains.txt --hide_fails  | tee takeover/subzy.txt 

echo -e "${green}SEARCH XSS ${red}alive.txt${nc}" 
cat waybackurls/xss.txt | kxss | tee vulnerabilities/xss/poss_xss.txt &

arjun -i alive.txt -o vulnerabilities/xss/hidden-params.txt &

echo -e "${green}CONNECTING JSURLS ${red}alive.txt${nc}" &
cat alive.txt  | getJS | anew | tee waybackurls/jsurls.txt 
########################################################


#########SECOUND##################################
echo -e "${green}NUCLEI START ${red}alive.txt${nc}" 
cat  alive.txt | nuclei -t /mnt/f/linuxfiles/nuclei-templates  -es info | tee -a nuclei_sca/vulnerabilities/all.txt &
cat waybackurls/jsurls.txt | nuclei -t /mnt/f/linuxfiles/nuclei-templates/http/exposures  | tee -a nuclei_sca/expousers.txt

echo -e "${green}NMAP SCAN ${red}alive.txt${nc}" 
nrich -l /subdomains/ips.txt | tee vulnerabilities/ports_scan.txt
nmap -T4 -sV --open --top-ports 200  --max-retries 3 --host-timeout 15m --script vulners -iL paramdomain -oA nmap/nmap-tcp 
grep Port < nmap/nmap-tcp.gnmap | cut -d' ' -f2 | sort -u > nmap/tcpips.txt &

echo -e "${green}SEARCH SQL INJECTION ${red}alive.txt${nc}" &
sqlmap -m tee waybackurls/sql.txt --batch --random-agent --level 1 | tee vulnerabilities/sql/poss_sql.txt  
###################################################




##########THREEEEE####################################

echo -e "${green}SEARCH CRLF INJECTIONZ ${red}alive.txt${nc}" &
crlfuzz -l alive.txt -o vulnerabilities/crlf/crlf-result.txt &
echo -e "${green}SEARCH command injection ${red}alive.txt${nc}" &
python3 /mnt/f/linuxfiles/tools/commix/commix.py --batch -m waybackurls/rce.txt --output-dir vulnerabilities/commandinject/  &
echo -e "${green}SEARCH LFI ${red}alive.txt${nc}"  &
python3 /mnt/f/linuxfiles/tools/LFImap/lfimap.py -F waybackurls/lfi.txt -a -v | tee vulnerabilities/LFI/lfi.txt &
echo -e "${green}GITHUB DORKS ${red}alive.txt${nc}" &
cat scope.txt | while read url ; do gitdorks_go -gd /mnt/f/linuxfiles/tools/gitdorks_go/Dorks/medium_dorks.txt -nws 20 -target  $url  -tf /mnt/f/linuxfiles/tools/github-token -ew 3 | anew | tee vulnerabilities/dorks/dork.txt  ; done 

########################################################
