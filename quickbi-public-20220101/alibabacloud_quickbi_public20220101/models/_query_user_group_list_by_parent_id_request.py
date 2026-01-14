# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryUserGroupListByParentIdRequest(DaraModel):
    def __init__(
        self,
        parent_user_group_id: str = None,
    ):
        # The ID of the parent user group.
        # 
        # *   If you enter the ID of the parent user group, you can obtain the information of the child user group under this ID.
        # *   If you enter -1, you can obtain the sub-user group information under the root directory.
        # 
        # This parameter is required.
        self.parent_user_group_id = parent_user_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parent_user_group_id is not None:
            result['ParentUserGroupId'] = self.parent_user_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParentUserGroupId') is not None:
            self.parent_user_group_id = m.get('ParentUserGroupId')

        return self

