from .models import Interaction


def new_interaction(interaction_type: str):
    """
    Provide a decorator for logging new interactions.

    Example usages:
        @new_interaction("Visit view")
        def view(request):
            ...
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            Interaction.objects.create(interaction_type=interaction_type)
            return func(*args, **kwargs)
        return wrapper
    return decorator
