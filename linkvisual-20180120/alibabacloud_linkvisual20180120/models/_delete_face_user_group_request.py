# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteFaceUserGroupRequest(DaraModel):
    def __init__(
        self,
        isolation_id: str = None,
        user_group_id: str = None,
    ):
        # The business isolation ID, which is used to isolate data between different business applications under the same Alibaba Cloud account. This value must be the same as the **IsolationId** specified when you call the [AddFaceUserGroup](https://help.aliyun.com/document_detail/288341.html) operation to add a user.
        # 
        # This parameter is required.
        self.isolation_id = isolation_id
        # The ID of the user group. Specify the user group ID that you obtained and saved locally after calling the [AddFaceUserGroup](https://help.aliyun.com/document_detail/288341.html) operation to add the user group.
        # 
        # This parameter is required.
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id

        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')

        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')

        return self

