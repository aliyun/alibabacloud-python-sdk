# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FaceLivenessRequest(DaraModel):
    def __init__(
        self,
        crop: str = None,
        face_picture_base_64: str = None,
        face_picture_url: str = None,
        face_quality: str = None,
        face_quality_check: str = None,
        merchant_biz_id: str = None,
        merchant_user_id: str = None,
        occlusion: str = None,
        product_code: str = None,
    ):
        # Specifies whether to allow cropping. Default value: F. Valid values:
        # 
        # - T: enabled.
        # - F: disabled. (Default).
        self.crop = crop
        # The Base64-encoded face photo.
        # 
        # Note:
        # - If you use FacePictureBase64 to pass in the face photo, check the photo size and do not pass in an excessively large photo.
        self.face_picture_base_64 = face_picture_base_64
        # The URL of the face photo.
        self.face_picture_url = face_picture_url
        # Specifies whether to return the face quality score. Default value: F. Valid values:
        # - T: enabled.
        # - F: disabled. (Default).
        self.face_quality = face_quality
        # The face quality check.
        self.face_quality_check = face_quality_check
        # The merchant-defined unique business ID for subsequent troubleshooting. The value can contain letters and digits with a maximum length of 32 characters. Ensure that the value is unique.
        self.merchant_biz_id = merchant_biz_id
        # The merchant user ID or another identifier that can be used to identify a specific user, such as a phone number or email address. We strongly recommend that you desensitize the value of the userId field before passing it in, for example, by hashing the value.
        self.merchant_user_id = merchant_user_id
        # Specifies whether to perform occlusion detection. Default value: F. Valid values:
        # 
        # - T: enabled.
        # - F: disabled. (Default).
        self.occlusion = occlusion
        # The product code.
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.crop is not None:
            result['Crop'] = self.crop

        if self.face_picture_base_64 is not None:
            result['FacePictureBase64'] = self.face_picture_base_64

        if self.face_picture_url is not None:
            result['FacePictureUrl'] = self.face_picture_url

        if self.face_quality is not None:
            result['FaceQuality'] = self.face_quality

        if self.face_quality_check is not None:
            result['FaceQualityCheck'] = self.face_quality_check

        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id

        if self.merchant_user_id is not None:
            result['MerchantUserId'] = self.merchant_user_id

        if self.occlusion is not None:
            result['Occlusion'] = self.occlusion

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')

        if m.get('FacePictureBase64') is not None:
            self.face_picture_base_64 = m.get('FacePictureBase64')

        if m.get('FacePictureUrl') is not None:
            self.face_picture_url = m.get('FacePictureUrl')

        if m.get('FaceQuality') is not None:
            self.face_quality = m.get('FaceQuality')

        if m.get('FaceQualityCheck') is not None:
            self.face_quality_check = m.get('FaceQualityCheck')

        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')

        if m.get('MerchantUserId') is not None:
            self.merchant_user_id = m.get('MerchantUserId')

        if m.get('Occlusion') is not None:
            self.occlusion = m.get('Occlusion')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        return self

