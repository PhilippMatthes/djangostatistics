import json
from json import JSONDecodeError

from django.core.exceptions import ValidationError
from django.forms import model_to_dict
from django.http import Http404, JsonResponse

from .models import Interaction
from .responses import IncorrectAccessMethod, MalformedJson, SuccessJsonResponse


def interactions(request) -> JsonResponse:
    """Get interactions for a given time and a given interaction type."""
    if request.method != "POST":
        return IncorrectAccessMethod()

    if not request.user:
        raise Http404()

    if not request.user.is_staff and not request.user.is_superuser:
        raise Http404()

    try:
        data = json.loads(request.body)
    except JSONDecodeError:
        return MalformedJson()

    interaction_type = data.get("interaction_type")
    from_timestamp = data.get("from_timestamp")
    to_timestamp = data.get("to_timestamp")
    if not interaction_type or not from_timestamp or not to_timestamp:
        return MalformedJson()

    try:
        filtered_interactions = Interaction.objects\
            .filter(interaction_type__iexact=interaction_type)\
            .filter(timestamp__gte=from_timestamp, timestamp__lte=to_timestamp)
    except ValidationError:
        return MalformedJson()

    return SuccessJsonResponse({
        "interactions": [
            model_to_dict(interaction) for interaction in filtered_interactions
        ]
    })
