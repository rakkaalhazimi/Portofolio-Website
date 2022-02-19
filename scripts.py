from app import db
from app.models import *


def add_data(title, url, image_path, icon_path, description):
    if Projects.query.filter_by(title=title, url=url).all():
        print("{} and {} already in database".format(title, url))
        return

    db.session.add(
        Projects(title=title, url=url, image_path=image_path, icon_path=icon_path, description=description)
    )
    db.session.commit()
    print("Data has been added")


def update_data(filter_dict, update_dict):
    db.session.query(Projects).filter(filter_dict).update(update_dict)
    db.session.commit()


if __name__ == "__main__":
    add_data(
        title="Indonesian Minimum Wage Dashboard",
        url="https://public.tableau.com/app/profile/rakka.alhazimi/viz/shared/6F44MGH8H",
        image_path="projects/ump_indonesia.png",
        icon_path="projects/tableau.png",
        description="""
        Analysis of Indonesian minimum wage in 2021 through geographic visualization. The data is consist 
        of 33 provinces of Indonesian and was scrapped from minister of manpower website.
        """,
    )

    # update_data(
    #     filter_dict=...,
    #     update_dict=...
    # )