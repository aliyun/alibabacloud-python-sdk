# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class CreateIpSetsResponseBody(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        ip_sets: List[main_models.CreateIpSetsResponseBodyIpSets] = None,
        request_id: str = None,
    ):
        # The GA instance ID.
        self.accelerator_id = accelerator_id
        # The details about the acceleration regions.
        self.ip_sets = ip_sets
        # The request ID.
        self.request_id = request_id

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
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id

        result['IpSets'] = []
        if self.ip_sets is not None:
            for k1 in self.ip_sets:
                result['IpSets'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        self.ip_sets = []
        if m.get('IpSets') is not None:
            for k1 in m.get('IpSets'):
                temp_model = main_models.CreateIpSetsResponseBodyIpSets()
                self.ip_sets.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateIpSetsResponseBodyIpSets(DaraModel):
    def __init__(
        self,
        accelerate_region_id: str = None,
        bandwidth: int = None,
        ip_set_id: str = None,
        isp_type: str = None,
    ):
        # The acceleration region ID.
        self.accelerate_region_id = accelerate_region_id
        # The bandwidth allocated to the acceleration region. Unit: **Mbit/s**.
        self.bandwidth = bandwidth
        # The acceleration region ID.
        self.ip_set_id = ip_set_id
        # The line type of the EIP in the acceleration region.
        self.isp_type = isp_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerate_region_id is not None:
            result['AccelerateRegionId'] = self.accelerate_region_id

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.ip_set_id is not None:
            result['IpSetId'] = self.ip_set_id

        if self.isp_type is not None:
            result['IspType'] = self.isp_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccelerateRegionId') is not None:
            self.accelerate_region_id = m.get('AccelerateRegionId')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('IpSetId') is not None:
            self.ip_set_id = m.get('IpSetId')

        if m.get('IspType') is not None:
            self.isp_type = m.get('IspType')

        return self

