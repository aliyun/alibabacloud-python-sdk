# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateEduHomeworkCorrectSubmitRequest(DaraModel):
    def __init__(
        self,
        dewarp: bool = None,
        image_base_64: str = None,
        image_url: str = None,
        request_id: str = None,
    ):
        # Specifies whether to correct the image distortion.
        self.dewarp = dewarp
        # The Base64-encoded image.
        self.image_base_64 = image_base_64
        # The URL of the image.
        self.image_url = image_url
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dewarp is not None:
            result['dewarp'] = self.dewarp

        if self.image_base_64 is not None:
            result['imageBase64'] = self.image_base_64

        if self.image_url is not None:
            result['imageUrl'] = self.image_url

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dewarp') is not None:
            self.dewarp = m.get('dewarp')

        if m.get('imageBase64') is not None:
            self.image_base_64 = m.get('imageBase64')

        if m.get('imageUrl') is not None:
            self.image_url = m.get('imageUrl')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

