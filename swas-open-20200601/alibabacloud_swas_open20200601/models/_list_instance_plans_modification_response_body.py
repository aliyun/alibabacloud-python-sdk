# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_swas_open20200601 import models as main_models
from darabonba.model import DaraModel

class ListInstancePlansModificationResponseBody(DaraModel):
    def __init__(
        self,
        plans: List[main_models.ListInstancePlansModificationResponseBodyPlans] = None,
        request_id: str = None,
    ):
        # The array of plans.
        self.plans = plans
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.plans:
            for v1 in self.plans:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Plans'] = []
        if self.plans is not None:
            for k1 in self.plans:
                result['Plans'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.plans = []
        if m.get('Plans') is not None:
            for k1 in m.get('Plans'):
                temp_model = main_models.ListInstancePlansModificationResponseBodyPlans()
                self.plans.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListInstancePlansModificationResponseBodyPlans(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        core: int = None,
        currency: str = None,
        disk_size: int = None,
        disk_type: str = None,
        flow: int = None,
        memory: int = None,
        origin_price: float = None,
        plan_id: str = None,
        support_platform: str = None,
    ):
        # The peak bandwidth. Unit: Mbps.
        self.bandwidth = bandwidth
        # The number of vCPU cores.
        self.core = core
        # The unit of the price. Valid values:
        # 
        # - CNY: Chinese Yuan
        # 
        # - USD: US Dollar
        self.currency = currency
        # The disk capacity. Unit: GiB.
        self.disk_size = disk_size
        # The disk type. Valid values:
        # 
        # - SSD: a standard SSD.
        # 
        # - ESSD: an Enhanced SSD (ESSD) at performance level (PL) 0.
        # 
        # - CLOUD_EFFICIENCY: an ultra disk.
        self.disk_type = disk_type
        # The monthly traffic. Unit: GB.
        self.flow = flow
        # The memory size. Unit: GiB.
        self.memory = memory
        # The price of the plan.
        self.origin_price = origin_price
        # The plan ID.
        self.plan_id = plan_id
        # The operating systems supported by the plan.
        self.support_platform = support_platform

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.core is not None:
            result['Core'] = self.core

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size

        if self.disk_type is not None:
            result['DiskType'] = self.disk_type

        if self.flow is not None:
            result['Flow'] = self.flow

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.origin_price is not None:
            result['OriginPrice'] = self.origin_price

        if self.plan_id is not None:
            result['PlanId'] = self.plan_id

        if self.support_platform is not None:
            result['SupportPlatform'] = self.support_platform

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('Core') is not None:
            self.core = m.get('Core')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')

        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')

        if m.get('Flow') is not None:
            self.flow = m.get('Flow')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('OriginPrice') is not None:
            self.origin_price = m.get('OriginPrice')

        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')

        if m.get('SupportPlatform') is not None:
            self.support_platform = m.get('SupportPlatform')

        return self

