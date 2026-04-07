# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DsgUserGroupAddOrUpdateShrinkRequest(DaraModel):
    def __init__(
        self,
        user_groups_shrink: str = None,
    ):
        # The information about the user group.
        # 
        # This parameter is required.
        self.user_groups_shrink = user_groups_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_groups_shrink is not None:
            result['UserGroups'] = self.user_groups_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserGroups') is not None:
            self.user_groups_shrink = m.get('UserGroups')

        return self

