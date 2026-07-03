# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeQosPoliciesRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        priority: int = None,
        qos_id: str = None,
        qos_policy_id: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The description of the quintuple rule instance in the QoS policy.
        # 
        # The description must be 1 to 512 characters in length, start with a letter or a Chinese character, and can contain digits, underscores (_), and hyphens (-).
        self.description = description
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number. The default value is **1**.
        self.page_number = page_number
        # The number of quintuple rules to return on each page.
        # 
        # The default value is **10**. The maximum value is **50**.
        self.page_size = page_size
        # The priority of the throttling rule to which the quintuple rule in the QoS policy belongs.
        # 
        # The priority range is 1 to **3**. A smaller value indicates a higher priority.
        # 
        # > If you have submitted a ticket and created a priority-4 QoS policy by calling the [CreateQosPolicy](https://help.aliyun.com/document_detail/131575.html) operation, you can use this operation to query the configurations of quintuple rules for the priority-4 QoS policy.
        self.priority = priority
        # The ID of the QoS policy instance.
        # 
        # This parameter is required.
        self.qos_id = qos_id
        # The ID of the quintuple rule instance in the QoS policy.
        self.qos_policy_id = qos_policy_id
        # The ID of the region where the QoS policy instance resides.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.qos_id is not None:
            result['QosId'] = self.qos_id

        if self.qos_policy_id is not None:
            result['QosPolicyId'] = self.qos_policy_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('QosId') is not None:
            self.qos_id = m.get('QosId')

        if m.get('QosPolicyId') is not None:
            self.qos_policy_id = m.get('QosPolicyId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

