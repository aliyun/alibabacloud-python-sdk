# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RectifyImageRequest(DaraModel):
    def __init__(
        self,
        camera_height: int = None,
        url: str = None,
    ):
        self.camera_height = camera_height
        # This parameter is required.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.camera_height is not None:
            result['CameraHeight'] = self.camera_height

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CameraHeight') is not None:
            self.camera_height = m.get('CameraHeight')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

