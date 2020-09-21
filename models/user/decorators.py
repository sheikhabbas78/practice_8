import functools
from typing import Callable
from flask import session, flash, current_app, redirect, url_for


def require_login(f: Callable) -> Callable:
    @functools.wraps(f)
    def decorator(*args, **kwargs):
        if not session.get('email'):
            flash('you need to login to excess this page', 'danger')
            return redirect(url_for('user.user_login'))
        return f(*args, **kwargs)
    return decorator


def require_admin_login(f: Callable):
    @functools.wraps(f)
    def decorator(*args, **kwargs):
        if session.get('email') != current_app.config.get('ADMIN', ''):
            flash('you need to admin login to excess this page', 'danger')
            return 'require_admin_login'
        return f(*args, **kwargs)
    return decorator
