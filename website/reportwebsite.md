# Reportwebsite portefolio

## Setting up my server

### Buy
buy the server on OVH ~3.80 / month
buy the domain on OVH 9.99 eu / year

### Admin.sys

**I Have follow this tutorial:https://www.idneo.fr/administration-serveur/configuration-serveur-dedie-vps-ovh-ubuntu/**

	- Change password/Adduser
	- Base securisation with some echo command
	- Add port to UFW and enable it 
	- Apt-get ntp
	- Add apache2 and setup it ( awfull )
	- 
**Maintenance : sometimes I have to reboot thoses services:**
- restart apache2
- a2enmod headers

Since I'm familiar with visual studio code I'm remotly working with it. Most of the time at this end of the session just git thoses sheet right away.

Btw I bought a brand new laptop that was a sickness to config with linux to make it work. First graphics driver problem that manage an unbootable ubuntu I had to add and "nouveau.modeset=0" next to quiet splash in the grub but it wasn't it all, I had to select the nvidia driver in the "Software" thing on ubuntu. The closing lib / hibernant / suspend messed me up aswell. So far the only solution to this was to disable lib closing thing and add "Xscreensaver" to the gnome-tweak.

Next to this anaconda messed up with me too with this rbash wich is the restricted bash. To resume while I was using the terminal trough vscode I couldn't run some python or whatever I would. I was restricted. So far aswell the only fix I had found was to install vscode trough anaconda.

03/16/2020

### SEO growthing with woorank.com:

**add thoses things :**
- robots.txt
- robots-https.txt
- sitemap.xml
- .htaccess
- error.php error-404.php
- add token HSTS
- add script that schema.org