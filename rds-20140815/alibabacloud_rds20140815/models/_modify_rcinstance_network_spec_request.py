# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyRCInstanceNetworkSpecRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        internet_max_bandwidth_out: str = None,
        network_charge_type: str = None,
        region_id: str = None,
    ):
        # The ID of the RDS Custom instance.
        self.instance_id = instance_id
        # The maximum outbound public bandwidth. Unit: Mbit/s.
        # 
        # Valid values: 0 to 1024. Default value: 0.
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # The billing method of the bandwidth. Only the **pay-by-traffic** billing method is supported.
        # 
        # >  If the **pay-by-traffic** billing method is used for network usage, the maximum inbound and outbound bandwidths are used as the upper limits of bandwidths instead of guaranteed performance specifications. In scenarios where demand outstrips resource supplies, these maximum bandwidth values may not be limited.
        self.network_charge_type = network_charge_type
        # The region ID of the instance. You can call the DescribeRegions operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out

        if self.network_charge_type is not None:
            result['NetworkChargeType'] = self.network_charge_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')

        if m.get('NetworkChargeType') is not None:
            self.network_charge_type = m.get('NetworkChargeType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

