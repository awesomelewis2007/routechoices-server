from django.apps import apps as django_apps
from django.core.exceptions import ImproperlyConfigured

from .app_settings import app_settings

try:
    import importlib
except ImportError:
    from django.utils import importlib


def import_attribute(path):
    assert isinstance(path, str)
    pkg, attr = path.rsplit(".", 1)
    ret = getattr(importlib.import_module(pkg), attr)
    return ret


def get_invite_form():
    """
    Returns the form for sending an invite.
    """
    return import_attribute(app_settings.INVITE_FORM)


def get_invitation_admin_add_form():
    """
    Returns the form for creating a new invitation in admin.
    """
    return import_attribute(app_settings.ADMIN_ADD_FORM)


def get_invitation_admin_change_form():
    """
    Returns the form for changing invitations in admin.
    """
    return import_attribute(app_settings.ADMIN_CHANGE_FORM)


def get_invitation_model():
    """
    Returns the Invitation model that is active in this project.
    """
    path = app_settings.INVITATION_MODEL
    try:
        return django_apps.get_model(path)
    except ValueError:
        raise ImproperlyConfigured("path must be of the form 'app_label.model_name'")
    except LookupError:
        raise ImproperlyConfigured(
            f"path refers to model '{app_settings.INVITATION_MODEL}' that has not "
            "been installed"
        )
