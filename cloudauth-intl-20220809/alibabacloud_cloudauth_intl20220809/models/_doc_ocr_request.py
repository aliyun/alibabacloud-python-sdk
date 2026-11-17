# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DocOcrRequest(DaraModel):
    def __init__(
        self,
        card_side: str = None,
        doc_type: str = None,
        id_face_quality: str = None,
        id_ocr_picture_base_64: str = None,
        id_ocr_picture_url: str = None,
        id_threshold: str = None,
        merchant_biz_id: str = None,
        merchant_user_id: str = None,
        ocr: str = None,
        product_code: str = None,
        spoof: str = None,
    ):
        # Specifies the side of the certificate, which can be the national emblem side or the portrait side. If you do not specify this parameter, the portrait side is used by default. Valid values:
        # - OCR_ID_FACE: The portrait side. Default value.
        # - OCR_ID_NATIONAL_EMBLEM: The national emblem side.
        self.card_side = card_side
        # The certificate type.
        self.doc_type = doc_type
        # Specifies whether to perform face quality detection on the certificate. Valid values:
        # - T: Detection is required.
        # - F: Detection is not required. Default value: F.
        self.id_face_quality = id_face_quality
        # The Base64-encoded image of the ID card or certificate.
        # 
        # If you choose to pass the certificate photo by using the IdOcrPictureBase64 (Base64-encoded photo) method, check the photo size and do not pass oversized photos.
        self.id_ocr_picture_base_64 = id_ocr_picture_base_64
        # The URL of the front image of the certificate.
        self.id_ocr_picture_url = id_ocr_picture_url
        # The custom threshold mode for OCR quality detection. Valid values:
        # - 0: System default.
        # - 1: Strict mode.
        # - 2: Loose mode.
        # - 3: Quality detection is disabled. Default value: 3.
        self.id_threshold = id_threshold
        # The custom unique business identifier on the merchant side, which is used for subsequent troubleshooting. It supports a combination of letters and digits, with a maximum length of 32 characters. Make sure that the identifier is unique.
        self.merchant_biz_id = merchant_biz_id
        # The custom user ID in the business. Make sure that the ID is unique.
        self.merchant_user_id = merchant_user_id
        # Specifies whether to perform OCR on the certificate. Valid values:
        # - T: OCR is required.
        # - F: OCR is not required.
        self.ocr = ocr
        # The product code.
        self.product_code = product_code
        # Specifies whether to enable anti-spoofing detection. Valid values:
        # - T: Anti-spoofing is enabled.
        # - F: Anti-spoofing is disabled.
        self.spoof = spoof

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.card_side is not None:
            result['CardSide'] = self.card_side

        if self.doc_type is not None:
            result['DocType'] = self.doc_type

        if self.id_face_quality is not None:
            result['IdFaceQuality'] = self.id_face_quality

        if self.id_ocr_picture_base_64 is not None:
            result['IdOcrPictureBase64'] = self.id_ocr_picture_base_64

        if self.id_ocr_picture_url is not None:
            result['IdOcrPictureUrl'] = self.id_ocr_picture_url

        if self.id_threshold is not None:
            result['IdThreshold'] = self.id_threshold

        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id

        if self.merchant_user_id is not None:
            result['MerchantUserId'] = self.merchant_user_id

        if self.ocr is not None:
            result['Ocr'] = self.ocr

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.spoof is not None:
            result['Spoof'] = self.spoof

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CardSide') is not None:
            self.card_side = m.get('CardSide')

        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')

        if m.get('IdFaceQuality') is not None:
            self.id_face_quality = m.get('IdFaceQuality')

        if m.get('IdOcrPictureBase64') is not None:
            self.id_ocr_picture_base_64 = m.get('IdOcrPictureBase64')

        if m.get('IdOcrPictureUrl') is not None:
            self.id_ocr_picture_url = m.get('IdOcrPictureUrl')

        if m.get('IdThreshold') is not None:
            self.id_threshold = m.get('IdThreshold')

        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')

        if m.get('MerchantUserId') is not None:
            self.merchant_user_id = m.get('MerchantUserId')

        if m.get('Ocr') is not None:
            self.ocr = m.get('Ocr')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('Spoof') is not None:
            self.spoof = m.get('Spoof')

        return self

