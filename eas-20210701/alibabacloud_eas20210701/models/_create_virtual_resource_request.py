# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eas20210701 import models as main_models
from darabonba.model import DaraModel

class CreateVirtualResourceRequest(DaraModel):
    def __init__(
        self,
        disable_spot_protection_period: bool = None,
        resources: List[main_models.CreateVirtualResourceRequestResources] = None,
        virtual_resource_name: str = None,
    ):
        # Specifies whether to disable the retention period of preemptible instances.
        self.disable_spot_protection_period = disable_spot_protection_period
        # The resources in the virtual resource group.
        self.resources = resources
        # The name of the virtual resource group. Default value: the ID of the virtual resource group.
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
        if self.disable_spot_protection_period is not None:
            result['DisableSpotProtectionPeriod'] = self.disable_spot_protection_period

        result['Resources'] = []
        if self.resources is not None:
            for k1 in self.resources:
                result['Resources'].append(k1.to_map() if k1 else None)

        if self.virtual_resource_name is not None:
            result['VirtualResourceName'] = self.virtual_resource_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisableSpotProtectionPeriod') is not None:
            self.disable_spot_protection_period = m.get('DisableSpotProtectionPeriod')

        self.resources = []
        if m.get('Resources') is not None:
            for k1 in m.get('Resources'):
                temp_model = main_models.CreateVirtualResourceRequestResources()
                self.resources.append(temp_model.from_map(k1))

        if m.get('VirtualResourceName') is not None:
            self.virtual_resource_name = m.get('VirtualResourceName')

        return self

class CreateVirtualResourceRequestResources(DaraModel):
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
        # 
        # >  You must specify one and only one of the InstanceType, ResourceId, and QuotaId parameters.
        self.instance_type = instance_type
        # The priority of resource scheduling. A greater number indicates a higher priority.
        self.priority = priority
        # The ID of the Lingjun resource quota.
        # 
        # >  You must specify one and only one of the InstanceType, ResourceId, and QuotaId parameters.
        self.quota_id = quota_id
        # The region in which the resource resides.
        self.region = region
        # The ID of the dedicated resource group. For information about how to obtain the ID of a dedicated resource group, see [ListResources](https://help.aliyun.com/document_detail/412133.html).
        # 
        # >  You must specify one and only one of the InstanceType, ResourceId, and QuotaId parameters.
        self.resource_id = resource_id
        # The maximum price of preemptible instances in a public resource group.
        # 
        # >  If you leave this parameter empty, preemptible instances are not used.
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

