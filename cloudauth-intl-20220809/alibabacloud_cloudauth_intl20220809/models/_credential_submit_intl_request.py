# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CredentialSubmitIntlRequest(DaraModel):
    def __init__(
        self,
        credential_ocr_picture_base_64: str = None,
        credential_ocr_picture_url: str = None,
        doc_type: str = None,
        fraud_check: str = None,
        merchant_biz_id: str = None,
        ocr_area: str = None,
        product_code: str = None,
        scene_code: str = None,
    ):
        # Base64 encoding of the image. If you choose to upload the photo this way, please check the photo size and avoid uploading overly large photos.
        self.credential_ocr_picture_base_64 = credential_ocr_picture_base_64
        # Image URL, accessible via HTTP or HTTPS on the public network.
        self.credential_ocr_picture_url = credential_ocr_picture_url
        # Credential type:
        # - 02: Vehicle registration certificate
        # 
        # This parameter is required.
        self.doc_type = doc_type
        # Whether to enable tampering detection
        # - true: Enable
        # - false: Disable
        # 
        # This parameter is required.
        self.fraud_check = fraud_check
        # A unique business identifier defined on the merchant side, used for troubleshooting issues later. Supports a combination of letters and digits, with a maximum length of 32 characters. Ensure uniqueness.
        # 
        # This parameter is required.
        self.merchant_biz_id = merchant_biz_id
        # Extraction type:
        # 
        # - 0201: Thai vehicle registration certificate
        # 
        # This parameter is required.
        self.ocr_area = ocr_area
        # The product solution to be integrated. Value: CREDENTIAL_RECOGNITION.
        # 
        # This parameter is required.
        self.product_code = product_code
        # Your custom authentication scenario ID, used for querying related records by entering this scenario ID in the console later. Supports a combination of 10 characters, digits, or underscores.
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
        if self.credential_ocr_picture_base_64 is not None:
            result['CredentialOcrPictureBase64'] = self.credential_ocr_picture_base_64

        if self.credential_ocr_picture_url is not None:
            result['CredentialOcrPictureUrl'] = self.credential_ocr_picture_url

        if self.doc_type is not None:
            result['DocType'] = self.doc_type

        if self.fraud_check is not None:
            result['FraudCheck'] = self.fraud_check

        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id

        if self.ocr_area is not None:
            result['OcrArea'] = self.ocr_area

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialOcrPictureBase64') is not None:
            self.credential_ocr_picture_base_64 = m.get('CredentialOcrPictureBase64')

        if m.get('CredentialOcrPictureUrl') is not None:
            self.credential_ocr_picture_url = m.get('CredentialOcrPictureUrl')

        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')

        if m.get('FraudCheck') is not None:
            self.fraud_check = m.get('FraudCheck')

        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')

        if m.get('OcrArea') is not None:
            self.ocr_area = m.get('OcrArea')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')

        return self

