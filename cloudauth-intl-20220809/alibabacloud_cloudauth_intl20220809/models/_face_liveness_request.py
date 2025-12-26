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
        merchant_biz_id: str = None,
        merchant_user_id: str = None,
        occlusion: str = None,
        product_code: str = None,
    ):
        # Specifies whether to crop the facial image. The default value is F.
        # 
        # - **T**: allows cropping.
        # 
        # - **F**: Forbidden
        self.crop = crop
        self.face_picture_base_64 = face_picture_base_64
        # The URL of the portrait image. The URL must be an HTTP or HTTPS link accessible over the Internet.
        self.face_picture_url = face_picture_url
        # Specifies whether to return the facial image quality score. The default value is F.
        # 
        # - **T**: returns the score.
        # 
        # - **F**: does not return the score.
        self.face_quality = face_quality
        # A custom unique business identifier. You can use this identifier to track and troubleshoot issues. The identifier can be up to 32 characters in length and can contain letters and digits. Make sure the identifier is unique.
        # 
        # > Alibaba Cloud servers do not check the uniqueness of this value. For better tracking, ensure this value is unique.
        self.merchant_biz_id = merchant_biz_id
        # A  custom user ID or another identifier for a specific user, such as a mobile number or email address. For security, desensitize this value in advance, for example, by hashing it.
        self.merchant_user_id = merchant_user_id
        # Specifies whether to enable occlusion detection. The default value is F.
        # 
        # - **T**: enables the feature.
        # 
        # - **F**: disables the feature.
        self.occlusion = occlusion
        # The product solution to use. Set the value to **FACE_LIVENESS_MIN** to use the passive liveness detection API.
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

        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')

        if m.get('MerchantUserId') is not None:
            self.merchant_user_id = m.get('MerchantUserId')

        if m.get('Occlusion') is not None:
            self.occlusion = m.get('Occlusion')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        return self

