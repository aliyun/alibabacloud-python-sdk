# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ShareAICImageShrinkRequest(DaraModel):
    def __init__(
        self,
        image_id: str = None,
        users_shrink: str = None,
    ):
        # The image name.
        # 
        # This parameter is required.
        self.image_id = image_id
        # The user groups.
        # 
        # This parameter is required.
        self.users_shrink = users_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.users_shrink is not None:
            result['Users'] = self.users_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('Users') is not None:
            self.users_shrink = m.get('Users')

        return self

