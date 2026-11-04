# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddFaceUserToUserGroupRequest(DaraModel):
    def __init__(
        self,
        isolation_id: str = None,
        user_group_id: str = None,
        user_id: str = None,
    ):
        # The business isolation ID. It is used to isolate data between different business applications under the same Alibaba Cloud account.
        # 
        # >Notice: 
        # The user and the user group must be under the same isolation ID. Make sure that this parameter is consistent with the **IsolationId** parameter that you specified when you called the [AddFaceUser](https://help.aliyun.com/document_detail/288338.html) operation to add the user and the [AddFaceUserGroup](https://help.aliyun.com/document_detail/288341.html) operation to create the user group.
        # 
        # This parameter is required.
        self.isolation_id = isolation_id
        # The user group ID. Set this parameter to the user group ID that you obtained and saved locally after you called the [AddFaceUserGroup](https://help.aliyun.com/document_detail/288341.html) operation to create the user group.
        # 
        # This parameter is required.
        self.user_group_id = user_group_id
        # The user ID. Set this parameter to the user ID that you obtained and saved locally after you called the [AddFaceUser](https://help.aliyun.com/document_detail/288338.html) operation to add the user.
        # 
        # This parameter is required.
        self.user_id = user_id

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

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')

        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

