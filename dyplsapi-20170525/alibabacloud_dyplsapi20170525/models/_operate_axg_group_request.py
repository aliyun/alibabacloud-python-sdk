# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OperateAxgGroupRequest(DaraModel):
    def __init__(
        self,
        group_id: int = None,
        numbers: str = None,
        operate_type: str = None,
        owner_id: int = None,
        pool_key: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The group ID in the AXG binding.
        # 
        # You can view the group ID by using either of the following methods:
        # 
        # *   On the **Number Pool Management** page in the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account), filter AXG private numbers and click **Number Group G Management** to view the group IDs of number groups G.****
        # *   If the [CreateAxgGroup](https://help.aliyun.com/document_detail/110250.html) operation is called to create number group G, the value of **GroupId** in the response of the CreateAxgGroup operation is specified as the value of the request parameter **GroupId** of the OperateAxgGroup operation.
        # 
        # >  Number group G must have one or more phone numbers.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The phone numbers that you add to number group G. Separate the phone numbers with commas (,). You can add up to 200 phone numbers at a time.
        # 
        # This parameter is required.
        self.numbers = numbers
        # The type of the operation on number group G. Valid values:
        # 
        # *   **addNumbers**: adds phone numbers to number group G.
        # *   **deleteNumbers**: deletes phone numbers from number group G.
        # *   **overwriteNumbers**: replaces all phone numbers in number group G. All the original phone numbers are deleted from number group G, and new phone numbers are added to number group G.
        # 
        # > 
        # 
        # *   When you replace all phone numbers in number group G, the quantity of original phone numbers in number group G cannot exceed 200.
        # 
        # *   You can add up to 200 phone numbers to number group G at a time.
        # 
        # This parameter is required.
        self.operate_type = operate_type
        self.owner_id = owner_id
        # The key of the phone number pool. Log on to the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account) and view the key of the phone number pool on the **Number Pool Management** page.
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

        if self.numbers is not None:
            result['Numbers'] = self.numbers

        if self.operate_type is not None:
            result['OperateType'] = self.operate_type

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

        if m.get('Numbers') is not None:
            self.numbers = m.get('Numbers')

        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

