#!/bin/bash

###############################################################
#Author: Hernandez Lopez Raul @Neo                            #
#e-mail:  freeenergy1974@gmail.com                            #
#date: friday,   february 4,  2022                            #
#is placed in the directory where the environment should be   #
#found                                                        #
###############################################################
cd ../Back/Python/


if [ -d "environment" ]; then
    printf "\nThe environment already exists and is configured\n"
    source environment/bin/activate
else
    """Creation and configuration of the python environment"""
    printf "\nConfiguring python environment...\n"
    python -m venv environment

    source environment/bin/activate

    pip install Flask
    pip install flask_marshmallow
    pip install Flask-Cors
    pip install Flask-SQLAlchemy
    pip install PyMySQL
    pip install marshmallow
    pip install marshmallow-sqlalchemy
   

    environment/bin/python -m pip install --upgrade pip
fi

