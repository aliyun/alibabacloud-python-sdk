# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeepfakeDetectRequest(DaraModel):
    def __init__(
        self,
        face_base_64: str = None,
        face_input_type: str = None,
        face_url: str = None,
        outer_order_no: str = None,
    ):
        # The Base64-encoded face image.
        # > Specify either FaceUrl or FaceBase64.
        self.face_base_64 = face_base_64
        # The input type of the face material. Valid values:
        # 
        # - IMAGE (default): face image
        # - VIDEO: face video
        # 
        # > Video processing takes longer. Set the timeout to more than 3 seconds.
        self.face_input_type = face_input_type
        # The URL of the face image.
        # > Specify either FaceUrl or FaceBase64.
        self.face_url = face_url
        # The unique identifier of the merchant request. The value is a 32-character alphanumeric string. The first few characters consist of a custom merchant abbreviation, the middle part can contain a time segment, and the last part can use a random or incremental sequence.
        self.outer_order_no = outer_order_no

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

        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceBase64') is not None:
            self.face_base_64 = m.get('FaceBase64')

        if m.get('FaceInputType') is not None:
            self.face_input_type = m.get('FaceInputType')

        if m.get('FaceUrl') is not None:
            self.face_url = m.get('FaceUrl')

        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')

        return self

