# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class PurchaseStorageCapacityUnitRequest(DaraModel):
    def __init__(
        self,
        amount: int = None,
        capacity: int = None,
        client_token: str = None,
        description: str = None,
        from_app: str = None,
        name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        period: int = None,
        period_unit: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_time: str = None,
        tag: List[main_models.PurchaseStorageCapacityUnitRequestTag] = None,
    ):
        # The number of SCUs to purchase. Valid values: 1 to 20.
        # 
        # Default value: 1.
        self.amount = amount
        # The capacity of the SCU. Unit: GiB. Valid values: 20, 40, 100, 200, 500, 1024, 2048, 5210, 10240, 20480, and 52100.
        # 
        # This parameter is required.
        self.capacity = capacity
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but make sure that the token is unique among different requests. The ClientToken value can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The description of the SCU. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # The source of the request. The default value is OpenAPI. You do not need to manually set this parameter.
        self.from_app = from_app
        # The name of the SCU. The name must be 2 to 128 characters in length and can contain letters, digits, colons (:), underscores (_), and hyphens (-). The name must start with a letter and cannot start with `http://` or `https://`.
        self.name = name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The validity period of the SCU. Valid values:
        # 
        # - When PeriodUnit is set to Month, valid values of Period are 1, 2, 3, and 6.
        # - When PeriodUnit is set to Year, valid values of Period are 1, 3, and 5.
        # 
        # Default value: 1.
        self.period = period
        # The unit of the validity period of the SCU. Valid values:
        # 
        # - Month: month.
        # - Year: year.
        # 
        # Default value: Month.
        self.period_unit = period_unit
        # The region ID of the SCU. After you specify a region, the SCU can only offset pay-as-you-go bills for cloud disks in that region. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent list of Alibaba Cloud regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the storage capacity unit (SCU) belongs. You can specify only a resource group ID to which you have permissions.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The effective period of the SCU. The effective period cannot be more than 180 days after the creation time. Specify the time in the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHHZ format. The time must be in UTC.
        # 
        # Default value: null, which indicates that the SCU takes effect immediately after it is created.
        self.start_time = start_time
        # The tags. Array length: 1 to 20.
        self.tag = tag

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
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.capacity is not None:
            result['Capacity'] = self.capacity

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.from_app is not None:
            result['FromApp'] = self.from_app

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FromApp') is not None:
            self.from_app = m.get('FromApp')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.PurchaseStorageCapacityUnitRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class PurchaseStorageCapacityUnitRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the SCU. If you specify this parameter, the tag key cannot be an empty string. The tag key can be up to 128 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        self.key = key
        # The tag value of the SCU. If you specify this parameter, the tag value can be an empty string. The tag value can be up to 128 characters in length and cannot start with `acs:`. It cannot contain `http://` or `https://`.
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

