# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FaceLivenessV2Request(DaraModel):
    def __init__(
        self,
        face_picture_base_64: str = None,
        face_picture_file: str = None,
        face_picture_url: str = None,
        face_quality_check: str = None,
        merchant_biz_id: str = None,
        merchant_user_id: str = None,
        product_code: str = None,
    ):
        # The Base64-encoded face image.
        # 
        # > **Note**
        # 
        # - If you use this method to pass in the image, check the image size and do not pass in an excessively large image.
        # - Specify one of the following parameters: FacePictureBase64, FacePictureUrl, or FacePictureFile.
        self.face_picture_base_64 = face_picture_base_64
        # The file stream of the face image.
        self.face_picture_file = face_picture_file
        # The URL of the face image. The URL must be a publicly accessible HTTPS URL.
        self.face_picture_url = face_picture_url
        # Specifies whether to check the quality of the face image. Valid values:
        # - Y: enabled.
        # - N: disabled. This is the default value.
        self.face_quality_check = face_quality_check
        # The merchant-defined unique business ID for subsequent troubleshooting. The value can be a combination of letters and digits with a maximum length of 32 characters. Make sure the value is unique.
        self.merchant_biz_id = merchant_biz_id
        # The custom user ID or another identifier that can identify a specific user, such as a phone number or email address. We strongly recommend that you desensitize the value of this field in advance, for example, by hashing the value.
        self.merchant_user_id = merchant_user_id
        # The product plan to use. Valid values: FACE_LIVENESS_MIN_PRO and FACE_LIVENESS_MIN.
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
        if self.face_picture_base_64 is not None:
            result['FacePictureBase64'] = self.face_picture_base_64

        if self.face_picture_file is not None:
            result['FacePictureFile'] = self.face_picture_file

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
            self.face_picture_file = m.get('FacePictureFile')

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

