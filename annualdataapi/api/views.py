# from django.shortcuts import render

# # Create your views here.
# from django.http import JsonResponse
# from api.models import AnnualData

# def get_annual_data(request):
#     API_WELL_NUMBER = request.GET.get('API_WELL_NUMBER', '')
#     data = AnnualData.objects.filter(API_WELL_NUMBER=API_WELL_NUMBER).values('OIL', 'GAS', 'BRINE').first()

#     if data:
#         return JsonResponse(data)
#     else:
#         return JsonResponse({"error": "No data found for the provided well."})


from django.http import JsonResponse
from api.models import AnnualData

def get_annual_data(request):
    well_number = request.GET.get('well')
    if well_number:
        try:
            data = AnnualData.objects.get(well=well_number)
            response = {
                'oil': data.oil,
                'gas': data.gas,
                'brine': data.brine
            }
            return JsonResponse(response)
        except AnnualData.DoesNotExist:
            return JsonResponse({'error': 'Well not found.'}, status=404)
    else:
        return JsonResponse({'error': 'Well parameter is required.'}, status=400)
