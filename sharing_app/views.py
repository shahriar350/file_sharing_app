from django.contrib import messages
from django.db import transaction, DatabaseError
from django.shortcuts import render
from django.template.defaulttags import url
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, FormView

from sharing_app.forms import FileSharingForm
from sharing_app.models import FileLink, ShareFile


# Create your views here.
class SharingView(FormView):
    template_name = 'sharing.html'
    form_class = FileSharingForm

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('files')
        if form.is_valid():
            try:
                with transaction.atomic():
                    link = FileLink.objects.create()
                    for f in files:
                        ShareFile.objects.create(file=f, link=link)
                    messages.success(
                        self.request,
                        f"Download link: http://{request.get_host()}{reverse_lazy('sharing_download_view', kwargs={'link': link.link})}")
                    return self.form_valid(form)
            except DatabaseError:
                return self.form_invalid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('sharing_view')


class SharingDownloadView(TemplateView):
    template_name = 'download.html'

    def get_context_data(self, **kwargs):
        data = super(SharingDownloadView, self).get_context_data()
        link = FileLink.objects.prefetch_related("get_files").get(link=self.kwargs.get('link'))
        data['downloads'] = link.get_files.all()
        return data
