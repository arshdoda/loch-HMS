from rest_framework import status
from rest_framework.response import Response
from rest_framework.utils.serializer_helpers import ReturnDict


def custom_success_response(data={}, message="", status=status.HTTP_200_OK):
    return Response({"message": message, "data": data}, status=status)


def custom_error_response(
    error="Bad Request",
    message="Something went wrong. Please try again",
    status=status.HTTP_400_BAD_REQUEST,
):
    msg = message
    if isinstance(message, ReturnDict):
        _error = list(message.values())
        try:
            msg = _error[0][0]
        except:
            msg = "Something went wrong."

    return Response(
        {
            "error": error,
            "message": msg,
        },
        status=status,
    )
