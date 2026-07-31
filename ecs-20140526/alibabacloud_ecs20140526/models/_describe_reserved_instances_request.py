# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeReservedInstancesRequest(DaraModel):
    def __init__(
        self,
        allocation_type: str = None,
        instance_type: str = None,
        instance_type_family: str = None,
        lock_reason: str = None,
        offering_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        reserved_instance_id: List[str] = None,
        reserved_instance_name: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scope: str = None,
        status: List[str] = None,
        tag: List[main_models.DescribeReservedInstancesRequestTag] = None,
        zone_id: str = None,
    ):
        # The allocation type. Valid values:
        # 
        # - Normal: queries reserved instances under the current account.
        # - Shared: queries reserved instances that have been shared between the current account and linked accounts.
        # 
        # Default value: Normal.
        self.allocation_type = allocation_type
        # The instance type that the reserved instance can be applied to. For more information, see [Instance families](https://help.aliyun.com/document_detail/25378.html). 
        # 
        # > This is the instance type selected when you purchased the reserved instance. During actual deduction, region-level reserved instances support size-flexible deduction within the same instance family.
        self.instance_type = instance_type
        # The instance family that the reserved instance can be applied to. For more information, see [Instance families](https://help.aliyun.com/document_detail/25378.html).
        self.instance_type_family = instance_type_family
        # The lock type. Valid values:
        # 
        # - financial: The account has an overdue payment or the service has expired.
        # - security: Locked for security reasons.
        self.lock_reason = lock_reason
        # The payment type of the reserved instance. Valid values:
        # 
        # - No Upfront: no upfront.
        # - Partial Upfront: partial upfront.
        # - All Upfront: all upfront.
        self.offering_type = offering_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number of the reserved instance list. Minimum value: 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page for a paged query. Maximum value: 100.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The region ID of the reserved instance. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The IDs of reserved instances. Array length: 1 to 100.
        self.reserved_instance_id = reserved_instance_id
        # The name of the reserved instance.
        # 
        # > Only exact match is supported. Fuzzy match is not supported.
        self.reserved_instance_name = reserved_instance_name
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The scope of the reserved instance. Valid values:
        #          
        # - Region: regional.
        # - Zone: zonal.
        self.scope = scope
        # The statuses of reserved instances.
        self.status = status
        # The tags. Array length: 1 to 20.
        self.tag = tag
        # The zone ID of the instance. This parameter is required and takes effect only when Scope is set to Zone. You can call [DescribeZones](https://help.aliyun.com/document_detail/25610.html) to query the zone list.
        self.zone_id = zone_id

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocation_type is not None:
            result['AllocationType'] = self.allocation_type

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.instance_type_family is not None:
            result['InstanceTypeFamily'] = self.instance_type_family

        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason

        if self.offering_type is not None:
            result['OfferingType'] = self.offering_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.reserved_instance_id is not None:
            result['ReservedInstanceId'] = self.reserved_instance_id

        if self.reserved_instance_name is not None:
            result['ReservedInstanceName'] = self.reserved_instance_name

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.status is not None:
            result['Status'] = self.status

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationType') is not None:
            self.allocation_type = m.get('AllocationType')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('InstanceTypeFamily') is not None:
            self.instance_type_family = m.get('InstanceTypeFamily')

        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')

        if m.get('OfferingType') is not None:
            self.offering_type = m.get('OfferingType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReservedInstanceId') is not None:
            self.reserved_instance_id = m.get('ReservedInstanceId')

        if m.get('ReservedInstanceName') is not None:
            self.reserved_instance_name = m.get('ReservedInstanceName')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeReservedInstancesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeReservedInstancesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the reserved instance. The tag key cannot be an empty string and can be up to 128 characters in length. It cannot start with aliyun or acs: and cannot contain http:// or https://.
        # 
        # > If you use a single tag to filter resources, the resource count with the specified tag cannot exceed 1,000. If you use multiple tags to filter resources, the resource count with all specified tags attached cannot exceed 1,000. If the resource count exceeds 1,000, call the [ListTagResources](https://help.aliyun.com/document_detail/110425.html) operation to query resources.
        self.key = key
        # The tag value of the reserved instance. The tag value cannot be an empty string and can be up to 128 characters in length. It cannot start with acs: and cannot contain http:// or https://.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

