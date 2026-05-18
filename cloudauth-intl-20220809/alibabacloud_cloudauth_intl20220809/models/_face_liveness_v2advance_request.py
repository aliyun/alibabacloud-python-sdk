# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import BinaryIO

from darabonba.model import DaraModel

class FaceLivenessV2AdvanceRequest(DaraModel):
    def __init__(
        self,
        face_picture_base_64: str = None,
        face_picture_file_object: BinaryIO = None,
        face_picture_url: str = None,
        face_quality_check: str = None,
        merchant_biz_id: str = None,
        merchant_user_id: str = None,
        product_code: str = None,
    ):
        self.face_picture_base_64 = face_picture_base_64
        self.face_picture_file_object = face_picture_file_object
        self.face_picture_url = face_picture_url
        self.face_quality_check = face_quality_check
        self.merchant_biz_id = merchant_biz_id
        self.merchant_user_id = merchant_user_id
        # This parameter is required.
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.face_picture_base_64 is not None:
            result['FacePictureBase64'] = self.face_picture_base_64

        if self.face_picture_file_object is not None:
            result['FacePictureFile'] = self.face_picture_file_object

        if self.face_picture_url is not None:
            result['FacePictureUrl'] = self.face_picture_url

        if self.face_quality_check is not None:
            result['FaceQualityCheck'] = self.face_quality_check

        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id

        if self.merchant_user_id is not None:
            result['MerchantUserId'] = self.merchant_user_id

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FacePictureBase64') is not None:
            self.face_picture_base_64 = m.get('FacePictureBase64')

        if m.get('FacePictureFile') is not None:
            self.face_picture_file_object = m.get('FacePictureFile')

        if m.get('FacePictureUrl') is not None:
            self.face_picture_url = m.get('FacePictureUrl')

        if m.get('FaceQualityCheck') is not None:
            self.face_quality_check = m.get('FaceQualityCheck')

        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')

        if m.get('MerchantUserId') is not None:
            self.merchant_user_id = m.get('MerchantUserId')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        return self

