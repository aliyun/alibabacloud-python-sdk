# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetImageRequest(DaraModel):
    def __init__(
        self,
        id: str = None,
        image_version: str = None,
    ):
        # This parameter is required.
        self.id = id
        self.image_version = image_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.image_version is not None:
            result['ImageVersion'] = self.image_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ImageVersion') is not None:
            self.image_version = m.get('ImageVersion')

        return self

