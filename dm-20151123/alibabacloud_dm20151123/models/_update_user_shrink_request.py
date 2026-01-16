# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateUserShrinkRequest(DaraModel):
    def __init__(
        self,
        user_shrink: str = None,
    ):
        # User Information
        self.user_shrink = user_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_shrink is not None:
            result['User'] = self.user_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('User') is not None:
            self.user_shrink = m.get('User')

        return self

