# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddFaceRecordRequest(DaraModel):
    def __init__(
        self,
        face_group_code: str = None,
        face_picture: str = None,
        face_picture_file: str = None,
        face_picture_url: str = None,
        face_quality_check: str = None,
        merchant_user_id: str = None,
        product_code: str = None,
    ):
        # This parameter is required.
        self.face_group_code = face_group_code
        self.face_picture = face_picture
        self.face_picture_file = face_picture_file
        self.face_picture_url = face_picture_url
        self.face_quality_check = face_quality_check
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
        if self.face_group_code is not None:
            result['FaceGroupCode'] = self.face_group_code

        if self.face_picture is not None:
            result['FacePicture'] = self.face_picture

        if self.face_picture_file is not None:
            result['FacePictureFile'] = self.face_picture_file

        if self.face_picture_url is not None:
            result['FacePictureUrl'] = self.face_picture_url

        if self.face_quality_check is not None:
            result['FaceQualityCheck'] = self.face_quality_check

        if self.merchant_user_id is not None:
            result['MerchantUserId'] = self.merchant_user_id

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceGroupCode') is not None:
            self.face_group_code = m.get('FaceGroupCode')

        if m.get('FacePicture') is not None:
            self.face_picture = m.get('FacePicture')

        if m.get('FacePictureFile') is not None:
            self.face_picture_file = m.get('FacePictureFile')

        if m.get('FacePictureUrl') is not None:
            self.face_picture_url = m.get('FacePictureUrl')

        if m.get('FaceQualityCheck') is not None:
            self.face_quality_check = m.get('FaceQualityCheck')

        if m.get('MerchantUserId') is not None:
            self.merchant_user_id = m.get('MerchantUserId')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        return self

