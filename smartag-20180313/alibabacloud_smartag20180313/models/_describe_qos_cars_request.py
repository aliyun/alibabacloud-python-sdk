# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeQosCarsRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        order: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        qos_car_id: str = None,
        qos_id: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The description of the traffic throttling rule.
        self.description = description
        # The sorting method of the traffic throttling rules. Valid values:
        # 
        # *   **asc**: sorted in ascending order. This is the default value.
        # *   **desc**: sorted in descending order.
        # 
        # By default, traffic throttling rules are sorted in ascending order of priority.
        self.order = order
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of the page to return. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return per page. Valid values: **1** to **50**. Default value: **10**.
        self.page_size = page_size
        # The ID of the traffic throttling rule.
        self.qos_car_id = qos_car_id
        # The ID of the QoS policy.
        # 
        # This parameter is required.
        self.qos_id = qos_id
        # The ID of the region where the QoS policy is created.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
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

        if self.order is not None:
            result['Order'] = self.order

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.qos_car_id is not None:
            result['QosCarId'] = self.qos_car_id

        if self.qos_id is not None:
            result['QosId'] = self.qos_id

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

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QosCarId') is not None:
            self.qos_car_id = m.get('QosCarId')

        if m.get('QosId') is not None:
            self.qos_id = m.get('QosId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

