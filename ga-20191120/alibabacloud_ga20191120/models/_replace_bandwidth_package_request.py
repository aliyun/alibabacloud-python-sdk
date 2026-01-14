# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReplaceBandwidthPackageRequest(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        bandwidth_package_id: str = None,
        region_id: str = None,
        target_bandwidth_package_id: str = None,
    ):
        # The GA instance ID.
        self.accelerator_id = accelerator_id
        # The ID of the required bandwidth plan. When you specify a replacement bandwidth plan, take note of the following items:
        # 
        # *   Only a bandwidth plan that is not associated with a GA instance can be specified.
        # *   If you want to replace a basic bandwidth plan, make sure that the bandwidth provided by the replacement bandwidth plan is not less than the total bandwidth allocated to the acceleration area.
        # 
        # This parameter is required.
        self.bandwidth_package_id = bandwidth_package_id
        # The region ID of the GA instance. Set the value to **cn-hangzhou**.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the bandwidth plan that you want to replace.
        # 
        # This parameter is required.
        self.target_bandwidth_package_id = target_bandwidth_package_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id

        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.target_bandwidth_package_id is not None:
            result['TargetBandwidthPackageId'] = self.target_bandwidth_package_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TargetBandwidthPackageId') is not None:
            self.target_bandwidth_package_id = m.get('TargetBandwidthPackageId')

        return self

