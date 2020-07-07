from app_name import render_template, request, Blueprint

blueprint_2 = Blueprint('main', __name__)

@blueprint_2.route('/blueprint_2')
def blueprint_2():
    return render_template('blueprint_2.html')