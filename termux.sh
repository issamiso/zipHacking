red='\033[1;31m'
pkg update -y
pkg upgrade -y
pkg install python -y
pkg install python2 -y
pkg install python3 -y
pkg install pip -y
pip install pyzipper
mv .Creakzip.py /data/data/com.termux/files/usr/etc
cd $HOME
cd zipHacking
mv .passwordiso.txt /data/data/com.termux/files/usr/etc
cd $HOME
cd zipHacking
cp .uns.sh $HOME
cd zipHacking
mv ziper /data/data/com.termux/files/usr/bin
cd /data/data/com.termux/files/usr/bin;chmod +x ziper
cd $HOME
bash .uns.sh
echo -e "[*] STARTING >$red ziper "
cd $HOME






