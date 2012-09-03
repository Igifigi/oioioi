from django.shortcuts import render_to_response
from django.template import TemplateDoesNotExist, RequestContext
from django.template.response import TemplateResponse
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from oioioi.contests.views import default_contest_view
from oioioi.base.menu import account_menu_registry

account_menu_registry.register('change_password', _("Change password"),
        lambda request: reverse('auth_password_change'), order=100)

account_menu_registry.register('logout', _("Log out"),
        lambda request: reverse('auth_logout'), order=200)

def index_view(request):
    try:
        return render_to_response("index.html",
                context_instance=RequestContext(request))
    except TemplateDoesNotExist, e:
        if not request.contest:
            return TemplateResponse(request, "index-no-contests.html")
        return default_contest_view(request, request.contest.id)

def force_error_view(request):
    raise StandardError("Visited /force_error")
