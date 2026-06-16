# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import BinaryIO

from darabonba.model import DaraModel

class DocOcrMaxV2AdvanceRequest(DaraModel):
    def __init__(
        self,
        authorize: str = None,
        doc_page: str = None,
        doc_type: str = None,
        id_ocr_picture_base_64: str = None,
        id_ocr_picture_file_object: BinaryIO = None,
        id_ocr_picture_url: str = None,
        id_spoof: str = None,
        id_threshold: str = None,
        merchant_biz_id: str = None,
        merchant_user_id: str = None,
        ocr_model: str = None,
        ocr_value_standard: str = None,
        product_code: str = None,
        scene_code: str = None,
    ):
        self.authorize = authorize
        self.doc_page = doc_page
        self.doc_type = doc_type
        self.id_ocr_picture_base_64 = id_ocr_picture_base_64
        self.id_ocr_picture_file_object = id_ocr_picture_file_object
        self.id_ocr_picture_url = id_ocr_picture_url
        self.id_spoof = id_spoof
        self.id_threshold = id_threshold
        self.merchant_biz_id = merchant_biz_id
        self.merchant_user_id = merchant_user_id
        self.ocr_model = ocr_model
        self.ocr_value_standard = ocr_value_standard
        self.product_code = product_code
        self.scene_code = scene_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorize is not None:
            result['Authorize'] = self.authorize

        if self.doc_page is not None:
            result['DocPage'] = self.doc_page

        if self.doc_type is not None:
            result['DocType'] = self.doc_type

        if self.id_ocr_picture_base_64 is not None:
            result['IdOcrPictureBase64'] = self.id_ocr_picture_base_64

        if self.id_ocr_picture_file_object is not None:
            result['IdOcrPictureFile'] = self.id_ocr_picture_file_object

        if self.id_ocr_picture_url is not None:
            result['IdOcrPictureUrl'] = self.id_ocr_picture_url

        if self.id_spoof is not None:
            result['IdSpoof'] = self.id_spoof

        if self.id_threshold is not None:
            result['IdThreshold'] = self.id_threshold

        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id

        if self.merchant_user_id is not None:
            result['MerchantUserId'] = self.merchant_user_id

        if self.ocr_model is not None:
            result['OcrModel'] = self.ocr_model

        if self.ocr_value_standard is not None:
            result['OcrValueStandard'] = self.ocr_value_standard

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Authorize') is not None:
            self.authorize = m.get('Authorize')

        if m.get('DocPage') is not None:
            self.doc_page = m.get('DocPage')

        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')

        if m.get('IdOcrPictureBase64') is not None:
            self.id_ocr_picture_base_64 = m.get('IdOcrPictureBase64')

        if m.get('IdOcrPictureFile') is not None:
            self.id_ocr_picture_file_object = m.get('IdOcrPictureFile')

        if m.get('IdOcrPictureUrl') is not None:
            self.id_ocr_picture_url = m.get('IdOcrPictureUrl')

        if m.get('IdSpoof') is not None:
            self.id_spoof = m.get('IdSpoof')

        if m.get('IdThreshold') is not None:
            self.id_threshold = m.get('IdThreshold')

        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')

        if m.get('MerchantUserId') is not None:
            self.merchant_user_id = m.get('MerchantUserId')

        if m.get('OcrModel') is not None:
            self.ocr_model = m.get('OcrModel')

        if m.get('OcrValueStandard') is not None:
            self.ocr_value_standard = m.get('OcrValueStandard')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')

        return self

