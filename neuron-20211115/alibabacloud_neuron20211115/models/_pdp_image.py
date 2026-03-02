# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PdpImage(DaraModel):
    def __init__(
        self,
        image_id: str = None,
        image_tag: str = None,
    ):
        # This parameter is required.
        self.image_id = image_id
        # This parameter is required.
        self.image_tag = image_tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_id is not None:
            result['imageId'] = self.image_id

        if self.image_tag is not None:
            result['imageTag'] = self.image_tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('imageId') is not None:
            self.image_id = m.get('imageId')

        if m.get('imageTag') is not None:
            self.image_tag = m.get('imageTag')

        return self

