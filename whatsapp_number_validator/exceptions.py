"""Public exception hierarchy for the WhatsApp Number Validator SDK."""

class WhatsAppNumberValidatorError(Exception):
    """Base SDK error."""

class AuthenticationError(WhatsAppNumberValidatorError):
    """The Apify token is missing or rejected."""

class ActorRunError(WhatsAppNumberValidatorError):
    """The Actor run or Dataset request failed."""

class ActorTimeoutError(WhatsAppNumberValidatorError):
    """The client stopped waiting before the Actor completed."""
