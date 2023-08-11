from dataclasses import dataclass


@dataclass
class EventValidatorErrorTypes:
    # Осмысленный текст появляется на стороне фронтенда

    EVENT_IS_NOT_DEFINED = ("EVENT_IS_NOT_DEFINED",)
    TITLE_IS_NOT_DEFINED = ("TITLE_IS_NOT_DEFINED",)
    TITLE_IS_TOO_SHORT = ("TITLE_IS_TOO_SHORT",)
    TITLE_IS_TOO_LONG = ("TITLE_IS_TOO_LONG",)
    DESCRIPTION_IS_NOT_DEFINED = ("DESCRIPTION_IS_NOT_DEFINED",)
    DESCRIPTION_IS_TOO_SHORT = ("DESCRIPTION_IS_TOO_SHORT",)
    DESCRIPTION_IS_TOO_LONG = ("DESCRIPTION_IS_TOO_LONG",)
    START_DATE_IS_NOT_DEFINED = ("START_DATE_IS_NOT_DEFINED",)
    START_DATE_IS_IN_THE_PAST = ("START_DATE_IS_IN_THE_PAST",)
    DURATION_IS_NEGATIVE = ("DURATION_IS_NEGATIVE",)
    LOCATION_IS_NOT_DEFINED = ("LOCATION_IS_NOT_DEFINED",)
    COUNTRY_IS_NOT_DEFINED = ("COUNTRY_IS_NOT_DEFINED",)
    CITY_IS_NOT_DEFINED = ("CITY_IS_NOT_DEFINED",)
    IMAGE_LINK_IS_TOO_SHORT = ("IMAGE_LINK_IS_TOO_SHORT",)
    IMAGE_LINK_IS_TOO_LONG = ("IMAGE_LINK_IS_TOO_LONG",)
    URL_IS_NOT_DEFINED = ("URL_IS_NOT_DEFINED",)
    URL_IS_TOO_SHORT = ("URL_IS_TOO_SHORT",)
    URL_IS_TOO_LONG = ("URL_IS_TOO_LONG",)
    TITLE_IS_NOT_CLEAN = ("TITLE_IS_NOT_CLEAN",)
    DESCRIPTION_IS_NOT_CLEAN = ("DESCRIPTION_IS_NOT_CLEAN",)
