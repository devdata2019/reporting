# Report week 2

## Monday 18/11/2019

### Create a database [A]

**Create a database on MySQL, in wich we will create some table**

```
mysql -u username -p

CREATE DATABASE dbname;

USE dbname;

CREATE TABLE example ( id smallint unsigned not null auto_increment, name varchar(20) not null, constraint pk_example primary key (id) );
INSERT INTO example ( id, name ) VALUES ( null, 'Sample data' );
```

----

### Setup SGBD WorkBench 

**Install WorkBench on Ubuntu**

```
$ sudo apt-get update && sudo apt-get upgrade
$ sudo apt install mysql-workbench
$ mysql-workbench
```

## Thuesday 19/11/2019
- ??

## Wednesday 20/11/2019

### Setup Anaconda [D]

Go to : https://www.anaconda.com/distribution/

```
$ cd /tmp
$ curl -O https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh
$ sha256sum Anaconda3-2019.03-Linux-x86_64.sh
$ bash Anaconda3-2019.03-Linux-x86_64.sh
```

## Thursday 21/11/2019

### MathPlotLib

**Learning Using MatPlotLib** [ECA]

Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms. Matplotlib can be used in Python scripts, the Python and IPython shells, the Jupyter notebook, web application servers, and four graphical user interface toolkits.

---

- Conception de graphique à partir de la base de données

### Friday 22/11/2019
- Revue des exercices de la semaine 