from django.db.models import query
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product

class ProductListView(ListView):
    template_name = 'index.html'
    queryset = Product.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mensaje'] = 'Listado de productos'
        print(context)
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'productos/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        print(context)
        return context

class ProductSearchListView(ListView):
    template_name = 'productos/search.html'
    
    def get_queryset(self):
        return Product.objects.filter(title=self.query)

    def query(self):
        return self.request.GET.get('q')