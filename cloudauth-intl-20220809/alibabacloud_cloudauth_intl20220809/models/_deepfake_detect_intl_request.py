# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeepfakeDetectIntlRequest(DaraModel):
    def __init__(
        self,
        face_base_64: str = None,
        face_input_type: str = None,
        face_url: str = None,
        merchant_biz_id: str = None,
        product_code: str = None,
        scene_code: str = None,
    ):
        # The Base64-encoded string of the face image.
        # > You must specify either FaceUrl or FaceBase64.
        self.face_base_64 = face_base_64
        # The face input type. Valid value: **IMAGE**, which indicates a face image.
        self.face_input_type = face_input_type
        # The URL of the face image.
        # > You must specify either FaceUrl or FaceBase64.
        self.face_url = face_url
        # The unique identifier of the merchant request. The value is a 32-character alphanumeric string. The first few characters consist of a custom merchant abbreviation, the middle part can contain a time period, and the latter part can be a random or incremental sequence.
        # 
        # This parameter is required.
        self.merchant_biz_id = merchant_biz_id
        # The product solution to access. Valid value: **FACE_DEEPFAKE**.
        # 
        # This parameter is required.
        self.product_code = product_code
        # The custom authentication scene ID. You can use this ID to query related records in the console. The value can be up to 10 characters in length and can contain letters, digits, and underscores.
        self.scene_code = scene_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.face_base_64 is not None:
            result['FaceBase64'] = self.face_base_64

        if self.face_input_type is not None:
            result['FaceInputType'] = self.face_input_type

        if self.face_url is not None:
            result['FaceUrl'] = self.face_url

        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceBase64') is not None:
            self.face_base_64 = m.get('FaceBase64')

        if m.get('FaceInputType') is not None:
            self.face_input_type = m.get('FaceInputType')

        if m.get('FaceUrl') is not None:
            self.face_url = m.get('FaceUrl')

        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')

        return self

