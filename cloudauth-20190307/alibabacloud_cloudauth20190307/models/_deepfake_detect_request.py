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
        # Enter the Base64 encoded string of the face image.
        # > Either FaceUrl or FaceBase64 must be provided.
        self.face_base_64 = face_base_64
        # Input **IMAGE** to indicate an image type.
        self.face_input_type = face_input_type
        # Enter the URL of the face image.
        # > Either FaceUrl or FaceBase64 must be provided.
        self.face_url = face_url
        # A unique identifier for the merchant\\"s request, consisting of a 32-character alphanumeric combination. The first few characters can be a custom abbreviation defined by the merchant, the middle part may include a timestamp, and the latter part can use a random or incrementing sequence.
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

