# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DsgWhiteListAddOrUpdateShrinkRequest(DaraModel):
    def __init__(
        self,
        white_lists_shrink: str = None,
    ):
        # A collection of whitelists.
        # 
        # This parameter is required.
        self.white_lists_shrink = white_lists_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.white_lists_shrink is not None:
            result['WhiteLists'] = self.white_lists_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WhiteLists') is not None:
            self.white_lists_shrink = m.get('WhiteLists')

        return self

