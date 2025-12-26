# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateChatConfigRequest(DaraModel):
    def __init__(
        self,
        avatar_id: str = None,
        background_id: str = None,
    ):
        self.avatar_id = avatar_id
        self.background_id = background_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avatar_id is not None:
            result['avatarId'] = self.avatar_id

        if self.background_id is not None:
            result['backgroundId'] = self.background_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('avatarId') is not None:
            self.avatar_id = m.get('avatarId')

        if m.get('backgroundId') is not None:
            self.background_id = m.get('backgroundId')

        return self

