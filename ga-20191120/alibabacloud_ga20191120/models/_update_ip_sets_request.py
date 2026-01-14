# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class UpdateIpSetsRequest(DaraModel):
    def __init__(
        self,
        ip_sets: List[main_models.UpdateIpSetsRequestIpSets] = None,
        region_id: str = None,
    ):
        # The acceleration regions.
        # 
        # This parameter is required.
        self.ip_sets = ip_sets
        # The region ID of the Global Accelerator (GA) instance. Set the value to **cn-hangzhou**.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        if self.ip_sets:
            for v1 in self.ip_sets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['IpSets'] = []
        if self.ip_sets is not None:
            for k1 in self.ip_sets:
                result['IpSets'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ip_sets = []
        if m.get('IpSets') is not None:
            for k1 in m.get('IpSets'):
                temp_model = main_models.UpdateIpSetsRequestIpSets()
                self.ip_sets.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class UpdateIpSetsRequestIpSets(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        ip_set_id: str = None,
    ):
        # The new bandwidth that you want to allocate to the acceleration regions. Unit: Mbit/s.
        # 
        # You must allocate at least 2 Mbit/s of bandwidth to each acceleration region. You can specify the bandwidth for up to 100 acceleration regions.
        # 
        # This parameter is required.
        self.bandwidth = bandwidth
        # The IDs of the acceleration regions that you want to modify.
        # 
        # You can specify the IDs of up to 100 acceleration regions.
        # 
        # This parameter is required.
        self.ip_set_id = ip_set_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.ip_set_id is not None:
            result['IpSetId'] = self.ip_set_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('IpSetId') is not None:
            self.ip_set_id = m.get('IpSetId')

        return self

