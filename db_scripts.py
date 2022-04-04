from dotenv import load_dotenv
load_dotenv()
from app import app, db
from app.models import *
import pandas as pd


def insert_data(title, url, image_path, icon_path, description):
    if Projects.query.filter_by(title=title, url=url).all():
        print("{} and {} already in database".format(title, url))
        return

    db.session.add(
        Projects(title=title, url=url, image_path=image_path, icon_path=icon_path, description=description)
    )
    db.session.commit()
    print("Data has been added")


def insert_data_from_csv(table_name):
    # Connect to database
    conn = db.get_engine(app)

    # Insert filepath
    fn = input("Filepath: ")

    # Read csv
    df = pd.read_csv(fn)

    # Get first columns of id
    id_col = Projects.__table__.columns.keys()[0]

    # Insert data to sql
    df.to_sql(table_name, con=conn, if_exists="replace", index_label=id_col)

    print("Data added successfully")


def update_data(filter_dict, update_dict):
    db.session.query(Projects).filter(filter_dict).update(update_dict)
    db.session.commit()


def delete_all_data():
    db.session.query(Projects).delete()
    


if __name__ == "__main__":
    ...
    # add_data(
    #     title="Indonesian Minimum Wage Dashboard",
    #     url="https://public.tableau.com/app/profile/rakka.alhazimi/viz/shared/6F44MGH8H",
    #     image_path="projects/ump_indonesia.png",
    #     icon_path="projects/tableau.png",
    #     description="""
    #     Analysis of Indonesian minimum wage in 2021 through geographic visualization. The data is consist 
    #     of 33 provinces of Indonesian and was scrapped from minister of manpower website.
    #     """,
    # )

    # update_data(
    #     filter_dict=...,
    #     update_dict=...
    # )

    # insert_data_from_csv("projects")