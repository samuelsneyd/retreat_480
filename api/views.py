from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from api.models import Email, Image, FeatureItem
from api.serializers import EmailSerializer, ImageSerializer, FeatureItemSerializer
from api import util


class MainApiTestView(APIView):
    """A smoke testing view."""

    test_message = {"message": "test"}

    def get(self, request) -> Response:
        """Returns a message an 200 response."""
        return Response(self.test_message, status=status.HTTP_200_OK)


class EmailView(APIView):
    """An API View for creating emails."""

    bad_request_message = {"message": "bad request"}
    subject = "Inquiry about 480"

    def post(self, request) -> Response:
        """Creates and sends an email."""

        data = util.snake_case_dict(request.data)
        data["sender"] = data["email"]
        data["recipient"] = settings.RECIPIENT_EMAIL
        data["subject"] = f'{self.subject}: {data["first_name"]} {data["last_name"]}'

        serializer = EmailSerializer(data=data)

        if serializer.is_valid():
            email: Email = serializer.save()
            email.send()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(self.bad_request_message, status=status.HTTP_400_BAD_REQUEST)


class ImageView(APIView):
    """An API view for a single image."""

    not_found_message = {"message", "image not found"}

    def get(self, request, image_id) -> Response:
        """Gets a single image by ID."""

        try:
            image = Image.objects.get(pk=image_id)
            serializer = ImageSerializer(image)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Image.DoesNotExist:
            return Response(self.not_found_message, status.HTTP_404_NOT_FOUND)


class ImagesView(APIView):
    """An API view for multiple images."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.images = Image.objects.all().order_by("priority")

    def get(self, request) -> Response:
        """Gets all images, or images that match the keyword arguments."""

        if "tag" in request.GET:
            tag = request.GET.get("tag", "").upper()
            self.images = list(filter(lambda image: tag in image.tags, self.images))

        serializer = ImageSerializer(self.images, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class FeatureItemView(APIView):
    """An API view for a single feature item by ID."""

    not_found_message = {"message", "feature item not found"}

    def get(self, request, item_id) -> Response:
        """Gets a single feature item by ID."""

        try:
            feature_item = FeatureItem.objects.get(pk=item_id)
            serializer = FeatureItemSerializer(feature_item)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except FeatureItem.DoesNotExist:
            return Response(self.not_found_message, status.HTTP_404_NOT_FOUND)


class FeatureItemsView(APIView):
    """An API view for multiple feature items."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.feature_items = FeatureItem.objects.all().order_by("priority")

    def get(self, request) -> Response:
        """Gets all feature items, or those that match the keyword arguments."""

        if "tag" in request.GET:
            tag = request.GET.get("tag", "").upper()
            self.feature_items = list(
                filter(lambda image: tag in image.tags, self.feature_items)
            )

        serializer = FeatureItemSerializer(self.feature_items, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
