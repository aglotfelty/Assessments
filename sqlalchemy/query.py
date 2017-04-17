"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()


# -------------------------------------------------------------------
# Part 2: Discussion Questions


# 1. What is the datatype of the returned value of
# ``Brand.query.filter_by(name='Ford')``?

"""ANSWER: The datatype of the returned value of Brand.query.filter_by(name='Ford') 
is a BaseQuery object."""


# 2. In your own words, what is an association table, and what type of
# relationship (many to one, many to many, one to one, etc.) does an
# association table manage?

"""ANSWER: An association table is a table that's only purpose is to connect two 
tables that have a many to many relationship. The association table simply includes 
the primary keys for both tables so that they can talk to one another. It does
<<<<<<< HEAD
not provide any additional data (or meaningful fields) as a middle table would. An example of an 
=======
not provide any additional data (as a middle table would). An example of an 
>>>>>>> 0e8e1ab1bd4e2977aad8629634105337d65920fc
association table would be a table to connect books to their genres. Many books
can have the same genre and one book can have many genres. Therefore, the relationship
is many to many. The table includes the primary keys for both the books and the 
genres table so that they can connect with one another."""



# -------------------------------------------------------------------
# Part 3: SQLAlchemy Queries


# Get the brand with the brand_id of ``ram``.
q1 = Brand.query.get('ram')

# Get all models with the name ``Corvette`` and the brand_id ``che``.
q2 = Model.query.filter_by(name='Corvette', brand_id='che').all()

# Get all models that are older than 1960.
q3 = Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
q4 = Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with ``Cor``.
q5 = Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
q6 = Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
q7 = Brand.query.filter((Brand.discontinued != None) | (Brand.founded < 1950)).all()

# Get all models whose brand_id is not ``for``.
q8 = Model.query.filter(Model.brand_id != 'for').all()


# -------------------------------------------------------------------
# Part 4: Write Functions


def get_model_info(year):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""

    cars = Model.query.filter(Model.year == year)

    print "Model Information for %s:\n" % year
    for car in cars:
        print "Model Name: %s, Brand Name: %s, Brand Headquarters: %s" % (car.name, 
                                                                          car.brand.name, 
                                                                          car.brand.headquarters)

def get_brands_summary():
    """Prints out each brand name (once) and all of that brand's models,
    including their year, using only ONE database query."""

    brands = Brand.query.order_by(Brand.name).all()

    for brand in brands:
        print "\n%s Summary:" % brand.name
        for model in brand.models:
            print "\t%s, %s" % (model.name, model.year)


def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""

    brands_with_mystr = Brand.query.filter(Brand.name.like("%" + mystr + "%")).all()
    
    return brands_with_mystr


def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""

    models = Model.query.filter(Model.year >= start_year, Model.year < end_year).all()

    return models

