from importlib.resources import path
from app.test_app import views

# URL paths
def setup_routes(app):
    app.router.add_static('/js/', path='static/scripts', name='js')
    app.router.add_static('/css/', path='static/css', name='css')
    app.router.add_static('/img/', path='static/img', name='img')
    app.router.add_post('/api/authorization', views.api_authorization)
    app.router.add_post('/api/regisration', views.api_registration)
    app.router.add_post('/api/logout', views.api_logout)
    app.router.add_get('/', views.test_page)
