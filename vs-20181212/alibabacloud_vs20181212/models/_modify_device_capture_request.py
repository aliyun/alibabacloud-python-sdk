# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDeviceCaptureRequest(DaraModel):
    def __init__(
        self,
        id: str = None,
        image: int = None,
        owner_id: int = None,
        video: int = None,
    ):
        # This parameter is required.
        self.id = id
        self.image = image
        self.owner_id = owner_id
        self.video = video

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.image is not None:
            result['Image'] = self.image

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.video is not None:
            result['Video'] = self.video

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Image') is not None:
            self.image = m.get('Image')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Video') is not None:
            self.video = m.get('Video')

        return self

