# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAxgGroupRequest(DaraModel):
    def __init__(
        self,
        group_id: int = None,
        owner_id: int = None,
        pool_key: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The G group ID (GID).
        # 
        # - Log on to the Phone Number Privacy Protection console. On the [Number Pool Management](https://dyplsnext.console.aliyun.com/number-pool) page, filter for number pools of the **AXG Privacy Number** type and click **G Number Group Management** to view the IDs of all G groups.
        # 
        # - If you created the G group by calling the [CreateAxgGroup](https://help.aliyun.com/document_detail/110250.html) API, use the returned **GroupID** as the value for this **GroupId** parameter.
        # 
        # This parameter is required.
        self.group_id = group_id
        self.owner_id = owner_id
        # The key of the number pool.
        # 
        # You can obtain the **key of the number pool** on the [Number Pool Management](https://dyplsnext.console.aliyun.com/number-pool) page in the Phone Number Privacy Protection console.
        # 
        # This parameter is required.
        self.pool_key = pool_key
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

