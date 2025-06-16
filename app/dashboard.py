from flask import Blueprint,render_template

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/', methods=['GET', 'POST'])
def index():
    return (render_template("index.html"))


@dashboard_bp.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return "Dashboard"
