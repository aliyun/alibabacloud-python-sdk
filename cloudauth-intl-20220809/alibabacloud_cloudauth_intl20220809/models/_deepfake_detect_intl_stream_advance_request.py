# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import BinaryIO

from darabonba.model import DaraModel

class DeepfakeDetectIntlStreamAdvanceRequest(DaraModel):
    def __init__(
        self,
        face_base_64: str = None,
        face_file_object: BinaryIO = None,
        face_input_type: str = None,
        face_url: str = None,
        merchant_biz_id: str = None,
        product_code: str = None,
        scene_code: str = None,
    ):
        # The Base64-encoded string of the face image. For videos, pass the data as a stream.
        self.face_base_64 = face_base_64
        # The input stream of the image.
        self.face_file_object = face_file_object
        # The input type of the face material. Valid values:
        # - IMAGE: face image. This is the default value.
        # - VIDEO: face video.
        # 
        # Note: Video processing takes a long time. Set the timeout period to a value greater than 3 seconds.
        self.face_input_type = face_input_type
        # The URL of the face image.
        self.face_url = face_url
        # The unique identifier of the merchant request. The value is a 32-character alphanumeric string. The first few characters consist of a custom merchant abbreviation, the middle part can contain a time period, and the latter part can be a random or incremental sequence.
        self.merchant_biz_id = merchant_biz_id
        # The product solution to be integrated. Valid values: FACE_DEEPFAKE.
        self.product_code = product_code
        # The custom authentication scenario ID, which is used to query related records by entering this scenario ID in the console. The value must be 10 characters in length and can contain letters, digits, and underscores.
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

        if self.face_file_object is not None:
            result['FaceFile'] = self.face_file_object

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
            self.face_file_object = m.get('FaceFile')

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

