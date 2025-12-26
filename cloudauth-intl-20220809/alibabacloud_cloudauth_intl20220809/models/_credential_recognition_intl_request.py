# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CredentialRecognitionIntlRequest(DaraModel):
    def __init__(
        self,
        credential_ocr_picture_base_64: str = None,
        credential_ocr_picture_url: str = None,
        doc_type: str = None,
        fraud_check: str = None,
        ocr_area: str = None,
        product_code: str = None,
    ):
        # Base64 encoded image. If you choose to upload the photo via IdOcrPictureBase64 (photo Base64 encoding), please check the photo size and do not upload overly large photos.
        self.credential_ocr_picture_base_64 = credential_ocr_picture_base_64
        # Image URL, accessible over the public network via HTTP or HTTPS links.
        self.credential_ocr_picture_url = credential_ocr_picture_url
        # Voucher type.
        # - Transaction Voucher: 01 (including: water, electricity, gas, credit card, and other types of e-bill images)
        # 
        # This parameter is required.
        self.doc_type = doc_type
        # Whether to enable tampering detection
        # - true: Enable
        # - false: Disable
        # 
        # This parameter is required.
        self.fraud_check = fraud_check
        # Extraction type:
        # - 0101: E-bill Address & Name Module (extracts address and name modules through intelligent analysis)
        # 
        # This parameter is required.
        self.ocr_area = ocr_area
        # The product solution to be integrated. Value: CREDENTIAL_RECOGNITION.
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
        if self.credential_ocr_picture_base_64 is not None:
            result['CredentialOcrPictureBase64'] = self.credential_ocr_picture_base_64

        if self.credential_ocr_picture_url is not None:
            result['CredentialOcrPictureUrl'] = self.credential_ocr_picture_url

        if self.doc_type is not None:
            result['DocType'] = self.doc_type

        if self.fraud_check is not None:
            result['FraudCheck'] = self.fraud_check

        if self.ocr_area is not None:
            result['OcrArea'] = self.ocr_area

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

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

        if m.get('OcrArea') is not None:
            self.ocr_area = m.get('OcrArea')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        return self

