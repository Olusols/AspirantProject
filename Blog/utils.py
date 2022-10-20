from django.shortcuts import render, get_object_or_404

class DetailPostMixin:
    model = None
    template_name = None
    
    def get(self,request, slug ):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context = {
            self.model.__name__.lower(): obj,
        })
    


