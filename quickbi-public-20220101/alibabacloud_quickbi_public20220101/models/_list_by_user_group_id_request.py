# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListByUserGroupIdRequest(DaraModel):
    def __init__(
        self,
        user_group_ids: str = None,
    ):
        # The ID of the user group that you want to query. Separate multiple user groups with commas (,).
        # 
        # This parameter is required.
        self.user_group_ids = user_group_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')

        return self

