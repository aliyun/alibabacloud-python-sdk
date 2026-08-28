# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CredentialSubmitIntlRequest(DaraModel):
    def __init__(
        self,
        check_rule_config: str = None,
        credential_ocr_picture_base_64: str = None,
        credential_ocr_picture_url: str = None,
        doc_type: str = None,
        fraud_check: str = None,
        id_quality: str = None,
        merchant_biz_id: str = None,
        ocr_area: str = None,
        ocr_translation: str = None,
        ocr_value_standard: str = None,
        product_code: str = None,
        scene_code: str = None,
    ):
        # The field validation rule configuration in JSON string format.
        self.check_rule_config = check_rule_config
        # The Base64-encoded image. If you use this method to submit a photo, check the photo size and do not submit an excessively large photo.
        self.credential_ocr_picture_base_64 = credential_ocr_picture_base_64
        # The URL of the image. The URL must be a publicly accessible HTTP or HTTPS link.
        self.credential_ocr_picture_url = credential_ocr_picture_url
        # The credential type. Valid values:
        # - 02: vehicle registration certificate
        # 
        # This parameter is required.
        self.doc_type = doc_type
        # Specifies whether to enable tampering detection. Valid values:
        # - true: Enabled.
        # - false: Disabled.
        # 
        # This parameter is required.
        self.fraud_check = fraud_check
        # Specifies whether to enable quality detection. Valid values:
        # - Y: Enabled.
        # - N: Disabled.
        self.id_quality = id_quality
        # The merchant-defined unique business identifier, used for subsequent troubleshooting. The value can be a combination of letters and numbers with a maximum length of 32 characters. Ensure that the value is unique.
        # 
        # This parameter is required.
        self.merchant_biz_id = merchant_biz_id
        # The extraction type. Valid values:
        # 
        # - 0201: Thailand vehicle registration certificate
        # 
        # This parameter is required.
        self.ocr_area = ocr_area
        # Specifies whether to enable translation. Valid values:
        # - 0: Disabled.
        # - 1: Enabled.
        self.ocr_translation = ocr_translation
        # Specifies whether to enable OCR result standardization. Valid values:
        # - 0: Disabled.
        # - 1: Enabled.
        self.ocr_value_standard = ocr_value_standard
        # The product solution to use. Set this to CREDENTIAL_RECOGNITION.
        # 
        # This parameter is required.
        self.product_code = product_code
        # The custom authentication scenario ID. You can use this ID to query related records in the console. The value can be a combination of letters, numbers, or underscores with a maximum length of 10 characters.
        # 
        # This parameter is required.
        self.scene_code = scene_code

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

        if self.fraud_check is not None:
            result['FraudCheck'] = self.fraud_check

        if self.id_quality is not None:
            result['IdQuality'] = self.id_quality

        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id

        if self.ocr_area is not None:
            result['OcrArea'] = self.ocr_area

        if self.ocr_translation is not None:
            result['OcrTranslation'] = self.ocr_translation

        if self.ocr_value_standard is not None:
            result['OcrValueStandard'] = self.ocr_value_standard

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code

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

        if m.get('FraudCheck') is not None:
            self.fraud_check = m.get('FraudCheck')

        if m.get('IdQuality') is not None:
            self.id_quality = m.get('IdQuality')

        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')

        if m.get('OcrArea') is not None:
            self.ocr_area = m.get('OcrArea')

        if m.get('OcrTranslation') is not None:
            self.ocr_translation = m.get('OcrTranslation')

        if m.get('OcrValueStandard') is not None:
            self.ocr_value_standard = m.get('OcrValueStandard')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')

        return self

