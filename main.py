if [ -z "$1" ] 
then
	echo "Enter project name"
	read proj
else
	proj="$1"
fi

#Create a virtualenv
virtualenv $proj
cd $proj
source bin/activate




echo "PIP_RESPECT_VIRTUALENV=true" >> bin/activate
touch requirements.txt
echo "django" >> requirements.txt
pip install -r requirements.txt


python lib/python2.7/site-packages/django/bin/django.py startproject $proj

export DJANGO_SETTINGS_MODULE="$proj.settings"
export PYTHONPATH="$VIRTUAL_ENV/$proj"


echo "export DJANGO_SETTINGS_MODULE=$proj.settings" >> bin/activate
echo "export PYTHONPATH=$VIRTUAL_ENV/$proj" >> bin/activate
