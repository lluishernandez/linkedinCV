linkedinCV
==========

Simple Django webpage that crawls the information from LinkedIn and expose it after.


Installation
------------

- Development
apt-get install python-virtualenv
virtualenv (Directory of the project)/vsys
source vsys/bin/activate
(Now follow the Production steps)

- Production
pip install -r dependencies.txt
wget https://raw.github.com/ozgur/python-linkedin/master/linkedin/linkedin.py -O vsys/lib/python2.7/site-packages/linkedin/linkedin.py


How to run application
----------------------

Just configure your Apache/Nginx as a web application.
