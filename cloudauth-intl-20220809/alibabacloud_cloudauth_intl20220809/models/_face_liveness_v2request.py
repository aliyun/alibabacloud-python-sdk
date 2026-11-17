# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FaceLivenessV2Request(DaraModel):
    def __init__(
        self,
        face_attribute_check: str = None,
        face_picture_base_64: str = None,
        face_picture_file: str = None,
        face_picture_url: str = None,
        face_quality_check: str = None,
        merchant_biz_id: str = None,
        merchant_user_id: str = None,
        product_code: str = None,
    ):
        # Specifies whether to detect face attributes.
        self.face_attribute_check = face_attribute_check
        # The Base64-encoded face image.
        # 
        # Note
        # 
        # - If you choose this method to pass the face image, check the image size and do not pass oversized images.
        # - Specify only one of the following parameters: FacePictureBase64, FacePictureUrl, and FacePictureFile.
        self.face_picture_base_64 = face_picture_base_64
        # The file stream of the face photo.
        self.face_picture_file = face_picture_file
        # The URL of the face photo. The URL must be a publicly accessible HTTPS link.
        self.face_picture_url = face_picture_url
        # Specifies whether to check the quality of the face image. Valid values:
        # - Y: enabled
        # - N: disabled (default)
        self.face_quality_check = face_quality_check
        # The custom unique business identifier on the merchant side, which is used for subsequent troubleshooting. The value can contain letters and digits and must be up to 32 characters in length. Make sure that the value is unique.
        self.merchant_biz_id = merchant_biz_id
        # The custom user ID or another identifier that can identify a specific user, such as a mobile phone number or an email address. Desensitize the value of this field in advance, such as by hashing the value.
        self.merchant_user_id = merchant_user_id
        # The product solution to be integrated. Valid values: FACE_LIVENESS_MIN_PRO and FACE_LIVENESS_MIN.
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
        if self.face_attribute_check is not None:
            result['FaceAttributeCheck'] = self.face_attribute_check

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
        if m.get('FaceAttributeCheck') is not None:
            self.face_attribute_check = m.get('FaceAttributeCheck')

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

