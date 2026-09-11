# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dts20200101 import models as main_models
from darabonba.model import DaraModel

class CreateSubscriptionInstanceRequest(DaraModel):
    def __init__(
        self,
        source_endpoint: main_models.CreateSubscriptionInstanceRequestSourceEndpoint = None,
        account_id: str = None,
        client_token: str = None,
        owner_id: str = None,
        pay_type: str = None,
        period: str = None,
        region: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        used_time: int = None,
    ):
        self.source_endpoint = source_endpoint
        # The ID of the Alibaba Cloud account. You do not need to specify this parameter. This parameter will be discontinued.
        self.account_id = account_id
        # The client token that is used to ensure the idempotence of the request. Generate a value from your client to make sure that the value is unique among different requests. **ClientToken** supports only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        self.owner_id = owner_id
        # The billing method.
        # 
        # - **Postpaid**: pay-as-you-go. This is the default value.
        # - **Prepaid**: subscription.
        self.pay_type = pay_type
        # The billing method of the subscription instance. Valid values:
        # 
        # - **Year**: annual subscription.
        # - **Month**: monthly subscription.
        # 
        # > This parameter is valid and required only when PayType is set to **Prepaid** (subscription).
        self.period = period
        # The region ID. Set this parameter to the region where the subscription object resides. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        # 
        # This parameter is required.
        self.region = region
        # The region to which the change tracking instance belongs. You do not need to specify this parameter. This parameter will be discontinued.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The purchase duration of the subscription instance.
        # 
        # - If the billing method is set to **Year** (annual subscription), the valid values are **1 to 5**.
        # - If the billing method is set to **Month** (monthly subscription), the valid values are **1 to 60**.
        # 
        # > This parameter is valid and required only when PayType is set to **Prepaid** (subscription).
        self.used_time = used_time

    def validate(self):
        if self.source_endpoint:
            self.source_endpoint.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()

        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.period is not None:
            result['Period'] = self.period

        if self.region is not None:
            result['Region'] = self.region

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.used_time is not None:
            result['UsedTime'] = self.used_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceEndpoint') is not None:
            temp_model = main_models.CreateSubscriptionInstanceRequestSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m.get('SourceEndpoint'))

        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        return self

class CreateSubscriptionInstanceRequestSourceEndpoint(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
    ):
        # 数据订阅的实例类型，取值为：**MySQL**、**PolarDB**、**DRDS**、**Oracle**。
        # > 默认取值为：**MySQL**。
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        return self

