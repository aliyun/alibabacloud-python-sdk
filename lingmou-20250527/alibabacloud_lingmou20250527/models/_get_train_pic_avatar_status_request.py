# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTrainPicAvatarStatusRequest(DaraModel):
    def __init__(
        self,
        avatar_id: str = None,
    ):
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
            result['avatarId'] = self.avatar_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('avatarId') is not None:
            self.avatar_id = m.get('avatarId')

        return self

