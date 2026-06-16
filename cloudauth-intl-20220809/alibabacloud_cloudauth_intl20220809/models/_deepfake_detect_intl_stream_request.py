# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeepfakeDetectIntlStreamRequest(DaraModel):
    def __init__(
        self,
        face_base_64: str = None,
        face_file: str = None,
        face_input_type: str = None,
        face_url: str = None,
        merchant_biz_id: str = None,
        product_code: str = None,
        scene_code: str = None,
    ):
        # The Base64-encoded face image. For videos, we recommend that you use the stream method for transmission.
        self.face_base_64 = face_base_64
        # The image input stream.
        self.face_file = face_file
        # The type of facial material input:
        # 
        # - IMAGE (default): Face image
        # - VIDEO: Face video
        # 
        # Note
        # Video processing takes a long time. We recommend that you set the timeout period to more than 3 seconds.
        self.face_input_type = face_input_type
        # The URL of the face image.
        self.face_url = face_url
        # The unique identifier of the merchant request. The value is an alphanumeric string with a length of 32 characters.
        # 
        # The first few characters consist of a custom abbreviation defined by the merchant, the middle part can contain a timestamp, and the last part can use a random or incremental sequence.
        self.merchant_biz_id = merchant_biz_id
        # The product solution to integrate.
        # Valid value: FACE_DEEPFAKE
        self.product_code = product_code
        # A custom verification scenario ID that you define. This ID is used to query related records in the console.
        # 
        # The value is a combination of letters, digits, or underscores (_) with a maximum length of 10 characters.
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

        if self.face_file is not None:
            result['FaceFile'] = self.face_file

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

        if m.get('FaceFile') is not None:
            self.face_file = m.get('FaceFile')

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

