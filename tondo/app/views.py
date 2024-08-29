from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Data
from .serializer import DataSerialiser
import logging

logger = logging.getLogger(__name__)


@api_view(['GET'])
def get_details(request, userid):
    try:
        user_data = Data.objects.get(pk=userid)
        logger.info("User found in DB, show details")
        return Response(DataSerialiser(user_data).data)

    except Data.DoesNotExist:
        logger.error(f"User {userid} not exist in DB")
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def save_details(request, userid):
    try:
        user_data = Data.objects.get(pk=userid)
        user_data.add_role(request.data['role'])
        user_data.save()
        serializer = DataSerialiser(user_data)

        logger.info(f"Update user {userid} roles by add the new role")
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    except Data.DoesNotExist:
        logger.info(f"The user {userid} not exist, create new user")
        serializer = DataSerialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
