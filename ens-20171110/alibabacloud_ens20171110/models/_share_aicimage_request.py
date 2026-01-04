# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ShareAICImageRequest(DaraModel):
    def __init__(
        self,
        image_id: str = None,
        users: List[str] = None,
    ):
        # The image name.
        # 
        # This parameter is required.
        self.image_id = image_id
        # The user groups.
        # 
        # This parameter is required.
        self.users = users

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.users is not None:
            result['Users'] = self.users

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('Users') is not None:
            self.users = m.get('Users')

        return self

