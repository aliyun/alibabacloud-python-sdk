# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAvatarRequest(DaraModel):
    def __init__(
        self,
        avatar_id: str = None,
    ):
        # *   The ID of the digital human.
        # 
        # This parameter is required.
        self.avatar_id = avatar_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avatar_id is not None:
            result['AvatarId'] = self.avatar_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvatarId') is not None:
            self.avatar_id = m.get('AvatarId')

        return self

