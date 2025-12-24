# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eas20210701 import models as main_models
from darabonba.model import DaraModel

class DescribeVirtualResourceResponseBody(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        disable_spot_protection_period: bool = None,
        features: List[str] = None,
        request_id: str = None,
        resources: List[main_models.DescribeVirtualResourceResponseBodyResources] = None,
        service_count: int = None,
        update_time: str = None,
        virtual_resource_id: str = None,
        virtual_resource_name: str = None,
    ):
        # The time when the virtual resource group was created.
        self.create_time = create_time
        # Indicates whether the retention period of preemptible instances was disabled.
        self.disable_spot_protection_period = disable_spot_protection_period
        self.features = features
        # The ID of the request.
        self.request_id = request_id
        # The list of resources in the virtual resource group.
        self.resources = resources
        # The number of deployed services.
        self.service_count = service_count
        # The time when the virtual resource group was last updated.
        self.update_time = update_time
        # The ID of the virtual resource group.
        self.virtual_resource_id = virtual_resource_id
        # The name of the virtual resource group.
        self.virtual_resource_name = virtual_resource_name

    def validate(self):
        if self.resources:
            for v1 in self.resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.disable_spot_protection_period is not None:
            result['DisableSpotProtectionPeriod'] = self.disable_spot_protection_period

        if self.features is not None:
            result['Features'] = self.features

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Resources'] = []
        if self.resources is not None:
            for k1 in self.resources:
                result['Resources'].append(k1.to_map() if k1 else None)

        if self.service_count is not None:
            result['ServiceCount'] = self.service_count

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.virtual_resource_id is not None:
            result['VirtualResourceId'] = self.virtual_resource_id

        if self.virtual_resource_name is not None:
            result['VirtualResourceName'] = self.virtual_resource_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DisableSpotProtectionPeriod') is not None:
            self.disable_spot_protection_period = m.get('DisableSpotProtectionPeriod')

        if m.get('Features') is not None:
            self.features = m.get('Features')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resources = []
        if m.get('Resources') is not None:
            for k1 in m.get('Resources'):
                temp_model = main_models.DescribeVirtualResourceResponseBodyResources()
                self.resources.append(temp_model.from_map(k1))

        if m.get('ServiceCount') is not None:
            self.service_count = m.get('ServiceCount')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('VirtualResourceId') is not None:
            self.virtual_resource_id = m.get('VirtualResourceId')

        if m.get('VirtualResourceName') is not None:
            self.virtual_resource_name = m.get('VirtualResourceName')

        return self

class DescribeVirtualResourceResponseBodyResources(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
        priority: int = None,
        quota_id: str = None,
        region: str = None,
        resource_id: str = None,
        spot_price_limit: float = None,
    ):
        # The instance type of the public resource group.
        self.instance_type = instance_type
        # The priority of resource scheduling. A greater number specifies a higher priority.
        self.priority = priority
        # The instance type of the public resource group.
        self.quota_id = quota_id
        # The region where the resource resides.
        self.region = region
        # The ID of the dedicated resource group.
        self.resource_id = resource_id
        # The maximum price of preemptible instances in a public resource group.
        self.spot_price_limit = spot_price_limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.quota_id is not None:
            result['QuotaId'] = self.quota_id

        if self.region is not None:
            result['Region'] = self.region

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('QuotaId') is not None:
            self.quota_id = m.get('QuotaId')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')

        return self

