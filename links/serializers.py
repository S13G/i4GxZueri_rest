from rest_framework import serializers


class LinkSerializer(serializers.ModelSerializers):
    class Meta:
        model = Link
        fields = "__all__"
