# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RegisterCustomFaceResponseBody(DaraModel):
    def __init__(
        self,
        face_id: str = None,
        request_id: str = None,
    ):
        # The ID of the face.
        self.face_id = face_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.face_id is not None:
            result['FaceId'] = self.face_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceId') is not None:
            self.face_id = m.get('FaceId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

