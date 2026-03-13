# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class IsvUserSaveShrinkRequest(DaraModel):
    def __init__(
        self,
        user_list_shrink: str = None,
    ):
        self.user_list_shrink = user_list_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_list_shrink is not None:
            result['user_list'] = self.user_list_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('user_list') is not None:
            self.user_list_shrink = m.get('user_list')

        return self

