# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddosbgp20180720 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceSpecsResponseBody(DaraModel):
    def __init__(
        self,
        instance_specs: List[main_models.DescribeInstanceSpecsResponseBodyInstanceSpecs] = None,
        request_id: str = None,
    ):
        # The specifications of the Anti-DDoS Origin instance, including whether best-effort protection is enabled, the number of available best-effort protection sessions, and the number of used best-effort protection sessions.
        self.instance_specs = instance_specs
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.instance_specs:
            for v1 in self.instance_specs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceSpecs'] = []
        if self.instance_specs is not None:
            for k1 in self.instance_specs:
                result['InstanceSpecs'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_specs = []
        if m.get('InstanceSpecs') is not None:
            for k1 in m.get('InstanceSpecs'):
                temp_model = main_models.DescribeInstanceSpecsResponseBodyInstanceSpecs()
                self.instance_specs.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeInstanceSpecsResponseBodyInstanceSpecs(DaraModel):
    def __init__(
        self,
        available_defense_times: int = None,
        available_delete_blackhole_count: str = None,
        defense_times_percent: int = None,
        downgrade_status: int = None,
        instance_id: str = None,
        is_full_defense_mode: int = None,
        pack_config: main_models.DescribeInstanceSpecsResponseBodyInstanceSpecsPackConfig = None,
        region: str = None,
        total_defense_times: int = None,
    ):
        # The available best-effort protection sessions.
        self.available_defense_times = available_defense_times
        # The number of times that blackhole filtering can be deactivated.
        self.available_delete_blackhole_count = available_delete_blackhole_count
        # The percentage of the used best-effort protection sessions. Unit: %.
        self.defense_times_percent = defense_times_percent
        # Indicates whether the instance is downgraded. Valid value:
        # 
        # *   **8**: The instance is downgraded due to excessive bandwidth usage.
        self.downgrade_status = downgrade_status
        # The ID of the Anti-DDoS Origin instance.
        self.instance_id = instance_id
        # Indicates whether best-effort protection is enabled. Valid values:
        # 
        # *   **0**: Best-effort protection is disabled.
        # *   **1**: Best-effort protection is enabled.
        self.is_full_defense_mode = is_full_defense_mode
        # The configurations of the Anti-DDoS Origin instance, including the number of protected IP addresses and protection bandwidth.
        self.pack_config = pack_config
        # The region ID of the Anti-DDoS Origin instance.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/118703.html) operation to query the name of the region.
        self.region = region
        # The total best-effort protection sessions.
        self.total_defense_times = total_defense_times

    def validate(self):
        if self.pack_config:
            self.pack_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_defense_times is not None:
            result['AvailableDefenseTimes'] = self.available_defense_times

        if self.available_delete_blackhole_count is not None:
            result['AvailableDeleteBlackholeCount'] = self.available_delete_blackhole_count

        if self.defense_times_percent is not None:
            result['DefenseTimesPercent'] = self.defense_times_percent

        if self.downgrade_status is not None:
            result['DowngradeStatus'] = self.downgrade_status

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.is_full_defense_mode is not None:
            result['IsFullDefenseMode'] = self.is_full_defense_mode

        if self.pack_config is not None:
            result['PackConfig'] = self.pack_config.to_map()

        if self.region is not None:
            result['Region'] = self.region

        if self.total_defense_times is not None:
            result['TotalDefenseTimes'] = self.total_defense_times

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableDefenseTimes') is not None:
            self.available_defense_times = m.get('AvailableDefenseTimes')

        if m.get('AvailableDeleteBlackholeCount') is not None:
            self.available_delete_blackhole_count = m.get('AvailableDeleteBlackholeCount')

        if m.get('DefenseTimesPercent') is not None:
            self.defense_times_percent = m.get('DefenseTimesPercent')

        if m.get('DowngradeStatus') is not None:
            self.downgrade_status = m.get('DowngradeStatus')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IsFullDefenseMode') is not None:
            self.is_full_defense_mode = m.get('IsFullDefenseMode')

        if m.get('PackConfig') is not None:
            temp_model = main_models.DescribeInstanceSpecsResponseBodyInstanceSpecsPackConfig()
            self.pack_config = temp_model.from_map(m.get('PackConfig'))

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('TotalDefenseTimes') is not None:
            self.total_defense_times = m.get('TotalDefenseTimes')

        return self

class DescribeInstanceSpecsResponseBodyInstanceSpecsPackConfig(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        bind_ip_count: int = None,
        elastic_bw_mbps: int = None,
        elastic_bw_mode: str = None,
        ip_advance_thre: int = None,
        ip_basic_thre: int = None,
        ip_spec: int = None,
        normal_bandwidth: int = None,
        pack_adv_thre: int = None,
        pack_basic_thre: int = None,
    ):
        # The bandwidth. Unit: Gbit/s.
        self.bandwidth = bandwidth
        # The number of IP addresses that are protected by the Anti-DDoS Origin Enterprise instance.
        self.bind_ip_count = bind_ip_count
        # The burstable clean bandwidth. Unit: Mbit/s.
        self.elastic_bw_mbps = elastic_bw_mbps
        # The metering method of burstable clean bandwidth. Valid values:
        # 
        # *   **month**: the monthly 95th percentile metering method.
        # *   **day**: the daily 95th percentile metering method.
        self.elastic_bw_mode = elastic_bw_mode
        # The burstable protection bandwidth of each protected IP address. Unit: Gbit/s.
        self.ip_advance_thre = ip_advance_thre
        # The basic protection bandwidth of each protected IP address. Unit: Gbit/s.
        self.ip_basic_thre = ip_basic_thre
        # The number of IP addresses that can be protected by the Anti-DDoS Origin Enterprise instance.
        self.ip_spec = ip_spec
        # The clean bandwidth. Unit: Mbit/s.
        self.normal_bandwidth = normal_bandwidth
        # The burstable protection bandwidth of the Anti-DDoS Origin instance. Unit: Gbit/s.
        self.pack_adv_thre = pack_adv_thre
        # The basic protection bandwidth of the Anti-DDoS Origin instance. Unit: Gbit/s.
        self.pack_basic_thre = pack_basic_thre

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.bind_ip_count is not None:
            result['BindIpCount'] = self.bind_ip_count

        if self.elastic_bw_mbps is not None:
            result['ElasticBwMbps'] = self.elastic_bw_mbps

        if self.elastic_bw_mode is not None:
            result['ElasticBwMode'] = self.elastic_bw_mode

        if self.ip_advance_thre is not None:
            result['IpAdvanceThre'] = self.ip_advance_thre

        if self.ip_basic_thre is not None:
            result['IpBasicThre'] = self.ip_basic_thre

        if self.ip_spec is not None:
            result['IpSpec'] = self.ip_spec

        if self.normal_bandwidth is not None:
            result['NormalBandwidth'] = self.normal_bandwidth

        if self.pack_adv_thre is not None:
            result['PackAdvThre'] = self.pack_adv_thre

        if self.pack_basic_thre is not None:
            result['PackBasicThre'] = self.pack_basic_thre

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('BindIpCount') is not None:
            self.bind_ip_count = m.get('BindIpCount')

        if m.get('ElasticBwMbps') is not None:
            self.elastic_bw_mbps = m.get('ElasticBwMbps')

        if m.get('ElasticBwMode') is not None:
            self.elastic_bw_mode = m.get('ElasticBwMode')

        if m.get('IpAdvanceThre') is not None:
            self.ip_advance_thre = m.get('IpAdvanceThre')

        if m.get('IpBasicThre') is not None:
            self.ip_basic_thre = m.get('IpBasicThre')

        if m.get('IpSpec') is not None:
            self.ip_spec = m.get('IpSpec')

        if m.get('NormalBandwidth') is not None:
            self.normal_bandwidth = m.get('NormalBandwidth')

        if m.get('PackAdvThre') is not None:
            self.pack_adv_thre = m.get('PackAdvThre')

        if m.get('PackBasicThre') is not None:
            self.pack_basic_thre = m.get('PackBasicThre')

        return self

