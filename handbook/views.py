from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Handbook, ElementHandbook
from .serializers import HandbooksSerializer, ElementHandbookSerializer


class HandbookView(APIView):
    def get(self, request):
        paginator = PageNumberPagination()
        date = request.GET.get('date', None)
        if date:
            handbooks = Handbook.objects.raw("SELECT id, title, short_title, description,version, MAX(start_date) "
                                             "FROM handbook_handbook "
                                             "WHERE start_date <= %s "
                                             "GROUP BY title", [date])
        else:
            handbooks = Handbook.objects.all()
        context = paginator.paginate_queryset(handbooks, request)
        serializer = HandbooksSerializer(context, many=True)
        return Response(serializer.data)


class ElementsHandbookView(APIView):
    def get(self, request):
        paginator = PageNumberPagination()
        handbook_name = request.GET.get('handbook_name', None)
        version = request.GET.get('version', None)
        if version and handbook_name:
            handbook_id = Handbook.objects.filter(title=handbook_name, version=version).first()
            elements_handbook = ElementHandbook.objects.filter(handbook_id=handbook_id)
        elif handbook_name:
            handbook_id = Handbook.objects.filter(title=handbook_name).order_by('-start_date').first()
            elements_handbook = ElementHandbook.objects.filter(handbook_id=handbook_id)
        else:
            elements_handbook = ElementHandbook.objects.all()
        context = paginator.paginate_queryset(elements_handbook, request)
        serializer = ElementHandbookSerializer(context, many=True)
        return Response(serializer.data)


class ValidateElementsHandbookView(APIView):
    def get(self, request):
        handbook_name = request.GET.get('handbook_name', None)
        version = request.GET.get('version', None)
        if version and handbook_name:
            handbook_id = Handbook.objects.filter(title=handbook_name, version=version).first()
            elements_handbook = ElementHandbook.objects.filter(handbook_id=handbook_id)
        elif handbook_name:
            handbook_id = Handbook.objects.filter(title=handbook_name).order_by('-start_date').first()
            elements_handbook = ElementHandbook.objects.filter(handbook_id=handbook_id)
        else:
            elements_handbook = ElementHandbook.objects.all()
        errors = []
        if elements_handbook:
            for element in elements_handbook:
                error = {}
                if not element.handbook_id.id:
                    error['id'] = element.id
                    error['error'] = f'словарь с id {element.handbook_id} не существует'
                    errors.append(error)

        return Response(errors)
