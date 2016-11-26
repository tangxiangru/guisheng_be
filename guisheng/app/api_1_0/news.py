# coding: utf-8
from flask import render_template,jsonify,Response,g,request
import json
from ..models import Role,User,News
from . import api


@api.route('/news/<int:id>/', methods=['GET','POST'])
def get_news(id):
    news = News.query.get_or_404(id)
    return Response(json.dumps({
        "title":news.title,
        "author":User.query.get_or_404(news.author_id).name,
        "time":news.time.strftime('%m/%d/%Y'),
        "body":news.body,
        }),mimetype='application/json')

