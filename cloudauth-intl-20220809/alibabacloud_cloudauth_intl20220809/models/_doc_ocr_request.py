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
        # CardSide
        self.card_side = card_side
        # Document type
        self.doc_type = doc_type
        # Whether to perform ID face quality detection
        # - T: Indicates that detection is required
        # - F: Indicates that detection is not required (default F)
        self.id_face_quality = id_face_quality
        # Base64 of the front side of the document image
        self.id_ocr_picture_base_64 = id_ocr_picture_base_64
        # URL of the front side of the document image
        self.id_ocr_picture_url = id_ocr_picture_url
        # IdThreshold
        self.id_threshold = id_threshold
        # A unique business identifier defined by the merchant, used for subsequent troubleshooting. It supports a combination of letters and numbers, with a maximum length of 32 characters. Please ensure uniqueness.
        self.merchant_biz_id = merchant_biz_id
        # A custom user ID in the business, please keep it unique.
        self.merchant_user_id = merchant_user_id
        # Whether to perform document OCR
        # - T: Indicates that document OCR is required
        # - F: Indicates that document OCR is not required
        self.ocr = ocr
        # Product code
        self.product_code = product_code
        # Whether to enable anti-counterfeiting detection
        # - T: Indicates that anti-counterfeiting is enabled
        # - F: Indicates that anti-counterfeiting is disabled
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

