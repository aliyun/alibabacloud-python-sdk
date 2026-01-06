# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateUserAvatarRequest(DaraModel):
    def __init__(
        self,
        avatar_media_id: str = None,
    ):
        self.avatar_media_id = avatar_media_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avatar_media_id is not None:
            result['AvatarMediaId'] = self.avatar_media_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvatarMediaId') is not None:
            self.avatar_media_id = m.get('AvatarMediaId')

        return self

