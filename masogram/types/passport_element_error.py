from __future__ import annotations

from .base import MutableTelegramObject


class PassportElementError(MutableTelegramObject):
    """
    This object represents an error in the Telegram Passport element which was submitted that should be resolved by the user. It should be one of:

     - :class:`masogram.types.passport_element_error_data_field.PassportElementErrorDataField`
     - :class:`masogram.types.passport_element_error_front_side.PassportElementErrorFrontSide`
     - :class:`masogram.types.passport_element_error_reverse_side.PassportElementErrorReverseSide`
     - :class:`masogram.types.passport_element_error_selfie.PassportElementErrorSelfie`
     - :class:`masogram.types.passport_element_error_file.PassportElementErrorFile`
     - :class:`masogram.types.passport_element_error_files.PassportElementErrorFiles`
     - :class:`masogram.types.passport_element_error_translation_file.PassportElementErrorTranslationFile`
     - :class:`masogram.types.passport_element_error_translation_files.PassportElementErrorTranslationFiles`
     - :class:`masogram.types.passport_element_error_unspecified.PassportElementErrorUnspecified`

    Source: https://core.telegram.org/bots/api#passportelementerror
    """
