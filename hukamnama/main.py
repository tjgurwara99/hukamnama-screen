# main.py

from flask import Blueprint, render_template, redirect, request
from flask_login import login_required, current_user
from .models import CurrentHukamnama
from . import db
from datetime import datetime
import requests

main = Blueprint("main", __name__)


@main.route("/search")
def search():
    return render_template("search.html", data=None)


@main.route("/search", methods=["POST"])
@login_required
def search_post():
    search = request.form.get("q")
    return redirect(f"/search/{search}")


@main.route("/search/<search>")
def search_search(search):
    data = requests.get(f"https://api.banidb.com/v2/search/{search}").json()
    return render_template("search.html", data=data)


@main.route("/")
def index():
    current_hukamnama = CurrentHukamnama.query.order_by(
        CurrentHukamnama.date.desc()
    ).first()
    if current_hukamnama:
        shabad_id = current_hukamnama.shabad_id
        data = requests.get(f"https://api.banidb.com/v2/shabads/{shabad_id}").json()
        return render_template("index.html", data=data, current_user=current_user)
    else:
        return redirect("/search")


@main.route("/shabads/<shabad_id>")
def shabad(shabad_id):
    data = requests.get(f"https://api.banidb.com/v2/shabads/{shabad_id}").json()
    return render_template("shabad.html", data=data, current_user=current_user)


@main.route("/shabads/<shabad_id>", methods=["POST"])
@login_required
def shabad_post(shabad_id):
    todays_hukamnama = CurrentHukamnama.query.filter_by(date=datetime.today().date())
    if todays_hukamnama:
        # warn user that today's hukamnama is already set
        pass
    hukamnama = CurrentHukamnama()
    hukamnama.shabad_id = shabad_id
    db.session.add(hukamnama)
    db.session.commit()
    return redirect(f"/shabads/{shabad_id}")
