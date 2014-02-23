GlobeLabs API Python Client
===========================

Installation
------------

```
$ pip install globelabs
```

Usage
-----

Sample usage with flask.

```
from globelabs import Globe


app_id = "BGyKAhGbyoGhRdiA8kTyMXhR9yGEhzoa"
app_secret = "8ed742b6c27e38db323ab24e19460a38eb0bf52804fc08f4df897db206b7b690"
shortcode = "1027"
globe = Globe(app_id=self.app_id,
              app_secret=self.app_secret,
              shortcode=self.shortcode)


@app.route('/login')
def login():
    return redirect(globe.get_auth_url())


@app.route('/redirect_callback')
def redirect_callback():
    r = globe.get_access_token(request.args.get('code'))
    ac = r['access_token']
    subscriber_number = r['subscriber_number']
    return redirect(url_for('.home'))


@app.route('/charge')
def charge():
    globe.charge(0, "2158%s0000099" % self.shortcode)

```

TODO
----

* Need help with documentation! :D
