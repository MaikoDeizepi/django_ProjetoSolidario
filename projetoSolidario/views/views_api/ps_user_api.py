from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from projetoSolidario.models import User, Evento, Empresa
from projetoSolidario.serializers import (
    UserSerializer,
    EventoSerializer,
    EmpresaSerializer,
)


# Obtém todos os usuários
@api_view(["GET"])
@permission_classes([IsAdminUser])
def get_users(request):
    users = User.objects.all()  # Obtém todos os usuários
    serializer = UserSerializer(users, many=True)  # Serializa os dados
    return Response(serializer.data)


# Obtém um usuário pelo ID
@api_view(["GET"])
@permission_classes([IsAdminUser])
def get_users_by_id(request, id):
    user = get_object_or_404(User, pk=id)  # Obtém o usuário ou retorna 404
    serializer = UserSerializer(user)  # Serializa os dados
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_events(request):
    evento = Evento.objects.all()  # Obtém todos os usuários
    serializer = EventoSerializer(evento, many=True)  # Serializa os dados
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_events_by_id(request, id):
    evento = get_object_or_404(Evento, pk=id)  # Obtém o usuário ou retorna 404
    serializer = EventoSerializer(evento)  # Serializa os dados
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_empresa(request):
    empresa = Empresa.objects.all()  # Obtém todos os usuários
    serializer = EmpresaSerializer(empresa, many=True)  # Serializa os dados
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_empresa_by_id(request, id):
    empresa = get_object_or_404(Empresa, pk=id)  # Obtém o usuário ou retorna 404
    serializer = EmpresaSerializer(empresa)  # Serializa os dados
    return Response(serializer.data)
