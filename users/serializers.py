from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "password",
        )


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        ref_name = "CustomUserSerializer"

        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
        )
        read_only_fields = ("id", "email", "password")
