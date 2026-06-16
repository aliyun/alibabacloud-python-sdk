# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_antiddos_public20170518 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceResponseBody(DaraModel):
    def __init__(
        self,
        instance_list: main_models.DescribeInstanceResponseBodyInstanceList = None,
        request_id: str = None,
        total: int = None,
    ):
        self.instance_list = instance_list
        # The ID of the request.
        self.request_id = request_id
        # The total number of the assets.
        self.total = total

    def validate(self):
        if self.instance_list:
            self.instance_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_list is not None:
            result['InstanceList'] = self.instance_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceList') is not None:
            temp_model = main_models.DescribeInstanceResponseBodyInstanceList()
            self.instance_list = temp_model.from_map(m.get('InstanceList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeInstanceResponseBodyInstanceList(DaraModel):
    def __init__(
        self,
        instance: List[main_models.DescribeInstanceResponseBodyInstanceListInstance] = None,
    ):
        self.instance = instance

    def validate(self):
        if self.instance:
            for v1 in self.instance:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Instance'] = []
        if self.instance is not None:
            for k1 in self.instance:
                result['Instance'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance = []
        if m.get('Instance') is not None:
            for k1 in m.get('Instance'):
                temp_model = main_models.DescribeInstanceResponseBodyInstanceListInstance()
                self.instance.append(temp_model.from_map(k1))

        return self

class DescribeInstanceResponseBodyInstanceListInstance(DaraModel):
    def __init__(
        self,
        blackhole_threshold: int = None,
        defense_bps_threshold: int = None,
        defense_pps_threshold: int = None,
        elastic_threshold: int = None,
        instance_id: str = None,
        instance_ip: str = None,
        instance_name: str = None,
        instance_status: str = None,
        instance_type: str = None,
        ip_version: str = None,
        is_bgppack: bool = None,
    ):
        self.blackhole_threshold = blackhole_threshold
        self.defense_bps_threshold = defense_bps_threshold
        self.defense_pps_threshold = defense_pps_threshold
        self.elastic_threshold = elastic_threshold
        self.instance_id = instance_id
        self.instance_ip = instance_ip
        self.instance_name = instance_name
        self.instance_status = instance_status
        self.instance_type = instance_type
        self.ip_version = ip_version
        self.is_bgppack = is_bgppack

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

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_ip is not None:
            result['InstanceIp'] = self.instance_ip

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.is_bgppack is not None:
            result['IsBgppack'] = self.is_bgppack

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

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceIp') is not None:
            self.instance_ip = m.get('InstanceIp')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('IsBgppack') is not None:
            self.is_bgppack = m.get('IsBgppack')

        return self

