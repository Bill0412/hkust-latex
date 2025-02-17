from flask import Flask, render_template
import json
from slugify import slugify
import os

app = Flask(__name__)

with open('data/tags.json', 'r') as infile:
    tags = json.load(infile)
    tag_keys = [str(key) for key in tags.keys()]
    tag_keys.sort()
    slug_tags = dict()
    unslug = dict()
    for tag_key in tag_keys:
        slug_tags[tag_key] = slugify(tag_key)
        unslug[slug_tags[tag_key]] = tag_key

@app.route('/')
def index():
    return render_template('index.html', tags=tag_keys, slug_tags=slug_tags)


@app.route('/<slug_tag>')
def category(slug_tag):
    items = tags[unslug[slug_tag]]
    # make sure that the image exists
    for item in items:
        if not os.path.exists('static/{}.png'.format(item)):
            items.remove(item)
            print(item)
    return render_template('category.html', items=items, title=unslug[slug_tag])


if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=80)

