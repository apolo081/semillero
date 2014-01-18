from django.contrib import admin
from django.contrib.admin import helpers
from django.contrib.admin.options import ModelAdmin, IS_POPUP_VAR
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.db import models
from django.forms.formsets import all_valid
from django.forms.util import ErrorList
from django.utils.encoding import force_text
from core.models import Coordinador,LiderGrupo,Estudiante
from django.utils.translation import ugettext as _
from semilleros.forms import UserForm


class ProfileAdmin(ModelAdmin):
    add_form_template = '_add_user.html'
    exclude = ['user',]

    def add_view(self, request, form_url='', extra_context=None):
        "The 'add' admin view for this model."
        model = self.model
        opts = model._meta

        if not self.has_add_permission(request):
            raise PermissionDenied

        ModelForm = self.get_form(request)
        formsets = []
        inline_instances = self.get_inline_instances(request, None)
        if request.method == 'POST':
            form = ModelForm(request.POST, request.FILES)
            if form.is_valid():
                new_object = self.save_form(request, form, change=False)
                form_validated = True
            else:
                form_validated = False
                new_object = self.model()
            prefixes = {}
            for FormSet, inline in zip(self.get_formsets(request), inline_instances):
                prefix = FormSet.get_default_prefix()
                prefixes[prefix] = prefixes.get(prefix, 0) + 1
                if prefixes[prefix] != 1 or not prefix:
                    prefix = "%s-%s" % (prefix, prefixes[prefix])
                formset = FormSet(data=request.POST, files=request.FILES,
                                  instance=new_object,
                                  save_as_new="_saveasnew" in request.POST,
                                  prefix=prefix, queryset=inline.get_queryset(request))
                formsets.append(formset)
            if all_valid(formsets) and form_validated:
                user = UserForm(request.POST)
                if user.is_valid():
                    #try:
                    new_user = User.objects.create_user(**user.cleaned_data)
                    new_user.is_staff = True
                    new_user.save()
                    new_object.user = new_user
                    self.save_model(request, new_object, form, False)
                    self.save_related(request, form, formsets, False)
                    self.log_addition(request, new_object)
                    return self.response_add(request, new_object)
                else:
                    print 'Error'
                    form._errors['__all__'] = ErrorList([u'Error, Usuario/Correo ya estan en uso'])
        else:
            # Prepare the dict of initial data from the request.
            # We have to special-case M2Ms as a list of comma-separated PKs.
            initial = dict(request.GET.items())
            for k in initial:
                try:
                    f = opts.get_field(k)
                except models.FieldDoesNotExist:
                    continue
                if isinstance(f, models.ManyToManyField):
                    initial[k] = initial[k].split(",")
            form = ModelForm(initial=initial)
            prefixes = {}
            for FormSet, inline in zip(self.get_formsets(request), inline_instances):
                prefix = FormSet.get_default_prefix()
                prefixes[prefix] = prefixes.get(prefix, 0) + 1
                if prefixes[prefix] != 1 or not prefix:
                    prefix = "%s-%s" % (prefix, prefixes[prefix])
                formset = FormSet(instance=self.model(), prefix=prefix,
                                  queryset=inline.get_queryset(request))
                formsets.append(formset)

        adminForm = helpers.AdminForm(form, list(self.get_fieldsets(request)),
                                      self.get_prepopulated_fields(request),
                                      self.get_readonly_fields(request),
                                      model_admin=self)
        media = self.media + adminForm.media

        inline_admin_formsets = []
        for inline, formset in zip(inline_instances, formsets):
            fieldsets = list(inline.get_fieldsets(request))
            readonly = list(inline.get_readonly_fields(request))
            prepopulated = dict(inline.get_prepopulated_fields(request))
            inline_admin_formset = helpers.InlineAdminFormSet(inline, formset,
                                                              fieldsets, prepopulated, readonly, model_admin=self)
            inline_admin_formsets.append(inline_admin_formset)
            media = media + inline_admin_formset.media

        context = {
            'title': _('Add %s') % force_text(opts.verbose_name),
            'adminform': adminForm,
            'is_popup': IS_POPUP_VAR in request.REQUEST,
            'media': media,
            'inline_admin_formsets': inline_admin_formsets,
            'errors': helpers.AdminErrorList(form, formsets),
            'app_label': opts.app_label,
            'preserved_filters': self.get_preserved_filters(request),
            }
        context.update(extra_context or {})
        return self.render_change_form(request, context, form_url=form_url, add=True)

class CoordinadorAdmin(ProfileAdmin):
    pass

class LiderGrupoAdmin(ProfileAdmin):
    pass

class EstudianteAdmin(ProfileAdmin):
    pass

admin.site.register(Coordinador,CoordinadorAdmin)
admin.site.register(LiderGrupo, LiderGrupoAdmin)
admin.site.register(Estudiante,EstudianteAdmin)