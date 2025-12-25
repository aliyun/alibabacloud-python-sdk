# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeRCInstanceIpAddressResponseBody(DaraModel):
    def __init__(
        self,
        rcinstance_list: List[main_models.DescribeRCInstanceIpAddressResponseBodyRCInstanceList] = None,
        request_id: str = None,
        total: str = None,
    ):
        # An array that consists of details of the instance.
        self.rcinstance_list = rcinstance_list
        # The request ID.
        self.request_id = request_id
        # The total number of the assets.
        self.total = total

    def validate(self):
        if self.rcinstance_list:
            for v1 in self.rcinstance_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RCInstanceList'] = []
        if self.rcinstance_list is not None:
            for k1 in self.rcinstance_list:
                result['RCInstanceList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rcinstance_list = []
        if m.get('RCInstanceList') is not None:
            for k1 in m.get('RCInstanceList'):
                temp_model = main_models.DescribeRCInstanceIpAddressResponseBodyRCInstanceList()
                self.rcinstance_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeRCInstanceIpAddressResponseBodyRCInstanceList(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_name: str = None,
        instance_status: str = None,
        instance_type: str = None,
        ip_address_config: List[main_models.DescribeRCInstanceIpAddressResponseBodyRCInstanceListIpAddressConfig] = None,
    ):
        # The ID of the RDS Custom instance.
        self.instance_id = instance_id
        # The instance name.
        self.instance_name = instance_name
        # The DDoS mitigation status of the instance. Valid values:
        # 
        # *   **normal**
        # *   **abnormal**
        self.instance_status = instance_status
        # The type of the asset. The value is fixed to **ecs**.
        self.instance_type = instance_type
        # An array that consists of the details of the asset.
        self.ip_address_config = ip_address_config

    def validate(self):
        if self.ip_address_config:
            for v1 in self.ip_address_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        result['IpAddressConfig'] = []
        if self.ip_address_config is not None:
            for k1 in self.ip_address_config:
                result['IpAddressConfig'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        self.ip_address_config = []
        if m.get('IpAddressConfig') is not None:
            for k1 in m.get('IpAddressConfig'):
                temp_model = main_models.DescribeRCInstanceIpAddressResponseBodyRCInstanceListIpAddressConfig()
                self.ip_address_config.append(temp_model.from_map(k1))

        return self

class DescribeRCInstanceIpAddressResponseBodyRCInstanceListIpAddressConfig(DaraModel):
    def __init__(
        self,
        blackhole_threshold: int = None,
        defense_bps_threshold: int = None,
        defense_pps_threshold: int = None,
        elastic_threshold: int = None,
        instance_ip: str = None,
        ip_status: str = None,
        ip_version: str = None,
        is_bgppack: bool = None,
        is_full_protection: int = None,
        region_id: str = None,
    ):
        # The basic protection threshold for the asset. Unit: Mbit/s.
        self.blackhole_threshold = blackhole_threshold
        # The traffic scrubbing threshold for the asset measured in Mbit/s. Unit: Mbit/s.
        self.defense_bps_threshold = defense_bps_threshold
        # The traffic scrubbing threshold for the asset measured in packets per second (PPS). Unit: packets per second (pps).
        self.defense_pps_threshold = defense_pps_threshold
        # The burstable protection threshold for the asset. Unit: Mbit/s.
        self.elastic_threshold = elastic_threshold
        # The IP address of the asset.
        self.instance_ip = instance_ip
        # The DDoS mitigation status of the asset. Valid values:
        # 
        # *   **mitigating**
        # *   **blackholed**
        # *   **normal**
        self.ip_status = ip_status
        # The IP version of the instance. Valid values:
        # 
        # *   **v4**
        # *   **v6**
        self.ip_version = ip_version
        # Indicates whether the asset is added to the instance. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.is_bgppack = is_bgppack
        # Indicates whether best-effort protection is enabled for the asset. Valid values:
        # 
        # *   **0**: Best-effort protection is disabled.
        # *   **1**: Best-effort protection is enabled.
        self.is_full_protection = is_full_protection
        # The region code of the asset.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.blackhole_threshold is not None:
            result['BlackholeThreshold'] = self.blackhole_threshold

        if self.defense_bps_threshold is not None:
            result['DefenseBpsThreshold'] = self.defense_bps_threshold

        if self.defense_pps_threshold is not None:
            result['DefensePpsThreshold'] = self.defense_pps_threshold

        if self.elastic_threshold is not None:
            result['ElasticThreshold'] = self.elastic_threshold

        if self.instance_ip is not None:
            result['InstanceIp'] = self.instance_ip

        if self.ip_status is not None:
            result['IpStatus'] = self.ip_status

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.is_bgppack is not None:
            result['IsBgppack'] = self.is_bgppack

        if self.is_full_protection is not None:
            result['IsFullProtection'] = self.is_full_protection

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlackholeThreshold') is not None:
            self.blackhole_threshold = m.get('BlackholeThreshold')

        if m.get('DefenseBpsThreshold') is not None:
            self.defense_bps_threshold = m.get('DefenseBpsThreshold')

        if m.get('DefensePpsThreshold') is not None:
            self.defense_pps_threshold = m.get('DefensePpsThreshold')

        if m.get('ElasticThreshold') is not None:
            self.elastic_threshold = m.get('ElasticThreshold')

        if m.get('InstanceIp') is not None:
            self.instance_ip = m.get('InstanceIp')

        if m.get('IpStatus') is not None:
            self.ip_status = m.get('IpStatus')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('IsBgppack') is not None:
            self.is_bgppack = m.get('IsBgppack')

        if m.get('IsFullProtection') is not None:
            self.is_full_protection = m.get('IsFullProtection')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

