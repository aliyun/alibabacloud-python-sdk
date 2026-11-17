# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CredentialRecognitionIntlRequest(DaraModel):
    def __init__(
        self,
        check_rule_config: str = None,
        credential_ocr_picture_base_64: str = None,
        credential_ocr_picture_url: str = None,
        doc_type: str = None,
        file_input_type: str = None,
        fraud_check: str = None,
        id_quality: str = None,
        ocr_area: str = None,
        ocr_translation: str = None,
        ocr_value_standard: str = None,
        product_code: str = None,
    ):
        # The field validation rule configuration. The value is a JSON string.
        self.check_rule_config = check_rule_config
        # The Base64-encoded image. If you use the IdOcrPictureBase64 parameter to pass the Base64-encoded photo, check the photo size and do not pass oversized photos.
        self.credential_ocr_picture_base_64 = credential_ocr_picture_base_64
        # The URL of the image. The URL must be a publicly accessible HTTP or HTTPS link.
        self.credential_ocr_picture_url = credential_ocr_picture_url
        # The credential type. Valid values:
        # - 01: transaction credentials, including electronic bills for utilities such as water, electricity, and gas, as well as credit card statements.
        # 
        # This parameter is required.
        self.doc_type = doc_type
        # The material input type. Valid values:
        # - IMAGE: image. This is the default value.
        # - PDF: PDF format.
        self.file_input_type = file_input_type
        # Specifies whether to enable tampering detection. Valid values:
        # - true: enabled.
        # - false: disabled.
        # 
        # This parameter is required.
        self.fraud_check = fraud_check
        # Specifies whether to enable the quality check. Valid values:
        # - Y: enabled.
        # - N: disabled.
        self.id_quality = id_quality
        # The extraction type. Valid values:
        # - 0101: electronic bill address and name module. The address and name are extracted through intelligent analysis.
        # 
        # This parameter is required.
        self.ocr_area = ocr_area
        # Specifies whether to enable translation. Valid values:
        # - 0: disabled.
        # - 1: enabled.
        self.ocr_translation = ocr_translation
        # Specifies whether to enable OCR result standardization. Valid values:
        # - 0: disabled.
        # - 1: enabled.
        self.ocr_value_standard = ocr_value_standard
        # The product solution to be integrated. Valid value: CREDENTIAL_RECOGNITION.
        # 
        # This parameter is required.
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_rule_config is not None:
            result['CheckRuleConfig'] = self.check_rule_config

        if self.credential_ocr_picture_base_64 is not None:
            result['CredentialOcrPictureBase64'] = self.credential_ocr_picture_base_64

        if self.credential_ocr_picture_url is not None:
            result['CredentialOcrPictureUrl'] = self.credential_ocr_picture_url

        if self.doc_type is not None:
            result['DocType'] = self.doc_type

        if self.file_input_type is not None:
            result['FileInputType'] = self.file_input_type

        if self.fraud_check is not None:
            result['FraudCheck'] = self.fraud_check

        if self.id_quality is not None:
            result['IdQuality'] = self.id_quality

        if self.ocr_area is not None:
            result['OcrArea'] = self.ocr_area

        if self.ocr_translation is not None:
            result['OcrTranslation'] = self.ocr_translation

        if self.ocr_value_standard is not None:
            result['OcrValueStandard'] = self.ocr_value_standard

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckRuleConfig') is not None:
            self.check_rule_config = m.get('CheckRuleConfig')

        if m.get('CredentialOcrPictureBase64') is not None:
            self.credential_ocr_picture_base_64 = m.get('CredentialOcrPictureBase64')

        if m.get('CredentialOcrPictureUrl') is not None:
            self.credential_ocr_picture_url = m.get('CredentialOcrPictureUrl')

        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')

        if m.get('FileInputType') is not None:
            self.file_input_type = m.get('FileInputType')

        if m.get('FraudCheck') is not None:
            self.fraud_check = m.get('FraudCheck')

        if m.get('IdQuality') is not None:
            self.id_quality = m.get('IdQuality')

        if m.get('OcrArea') is not None:
            self.ocr_area = m.get('OcrArea')

        if m.get('OcrTranslation') is not None:
            self.ocr_translation = m.get('OcrTranslation')

        if m.get('OcrValueStandard') is not None:
            self.ocr_value_standard = m.get('OcrValueStandard')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        return self

