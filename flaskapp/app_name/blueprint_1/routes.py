from app_name import render_template, request, Blueprint

blueprint_1 = Blueprint('main', __name__)

@blueprint_1.route('/blueprint_1')
def blueprint_1():
    return render_template('blueprint_1.html')