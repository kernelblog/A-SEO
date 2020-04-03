if [ $(echo $PREFIX | wc -c) -lt 2 ] && [ $(id -g) -ne 0 ]
then
	echo "Bu komutu sadece root erişimiyle çalıştırabilirsiniz"
	exit 1
fi

if [ -f /usr/bin/apt ]
then
	apt update
	apt install python3 python3-pip
elif [ -f $PREFIX/bin/apt ]
then
	pkg install python
elif [ -f /usr/bin/pacman ]
then
	pacman -S --needed python3 python-pip python3-pip
fi

PIP_CMD="pip3"

if [ -f /usr/bin/pip3 ]
then
	PIP_CMD="/usr/bin/pip3"
elif [ -f $PREFIX/bin/pip ]
then
	PIP_CMD=$PREFIX"/bin/pip"
fi

$PIP_CMD install beautifulsoup4 requests

SETUP_ROOT="/usr"

if [ $(echo $PREFIX | wc -c) -gt 2 ]
then
	SETUP_ROOT=$PREFIX
fi

mkdir $SETUP_ROOT/share/aseo 2>&1
cp aseo $SETUP_ROOT/bin/
cp *.py $SETUP_ROOT/share/aseo/
cp Kernelblog.jpg $SETUP_ROOT/share/aseo/
cp kb_b.jpg $SETUP_ROOT/share/aseo/
chmod 755 $SETUP_ROOT/bin/aseo
chmod 755 $SETUP_ROOT/share/aseo/*

echo "Yükleme başarıyla tamamlandı. Terminale aseo yazarak kullanabilirsiniz."
