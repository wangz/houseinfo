from django.shortcuts import render
from models import *
from django.shortcuts import render_to_response
# Create your views here.
vtype_des = {'r':"res"}
def index(request): 
    vtype = request.GET.get('vtype')
    if vtype == 'ms':
	data_list = MSummary.objects.order_by('-created_at') 
        return   render_to_response('index.html',{'m_sums': data_list})
    else:
    	data_list = Data.objects.filter(vtype=vtype).order_by('-created_at')  
        return   render_to_response('index.html',{'r_data_list': data_list,"vtype_des":vtype_des}) 
