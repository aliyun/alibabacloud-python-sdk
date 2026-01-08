# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribePostpayTrafficDetailResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        traffic_list: List[main_models.DescribePostpayTrafficDetailResponseBodyTrafficList] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The statistics on traffic.
        self.traffic_list = traffic_list

    def validate(self):
        if self.traffic_list:
            for v1 in self.traffic_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['TrafficList'] = []
        if self.traffic_list is not None:
            for k1 in self.traffic_list:
                result['TrafficList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.traffic_list = []
        if m.get('TrafficList') is not None:
            for k1 in m.get('TrafficList'):
                temp_model = main_models.DescribePostpayTrafficDetailResponseBodyTrafficList()
                self.traffic_list.append(temp_model.from_map(k1))

        return self

class DescribePostpayTrafficDetailResponseBodyTrafficList(DaraModel):
    def __init__(
        self,
        in_bytes: int = None,
        instance_id: str = None,
        instance_type: str = None,
        out_bytes: int = None,
        protection_duration: int = None,
        region_no: str = None,
        resource_id: str = None,
        total_bytes: int = None,
        traffic_day: str = None,
        traffic_type: str = None,
    ):
        # The inbound network throughput, which indicates the total number of bytes that are received Unit: bytes.
        self.in_bytes = in_bytes
        # The instance ID of the asset.
        self.instance_id = instance_id
        # The asset type. This value takes effect only for the Internet firewall.
        self.instance_type = instance_type
        # The outbound network throughput, which indicates the total number of bytes that are sent. Unit: bytes.
        self.out_bytes = out_bytes
        # Protection duration. Unit: hours.
        self.protection_duration = protection_duration
        # The region ID.
        self.region_no = region_no
        # The resource ID. The resource ID for the Internet firewall is the public IP address that is protected the Internet firewall, and the resource ID for a NAT firewall is the instance ID of the NAT firewall.
        self.resource_id = resource_id
        # The total inbound and outbound network throughput, which indicates the total number of bytes that are received and sent. Unit: bytes.
        self.total_bytes = total_bytes
        # The date on which the statistics are collected.
        self.traffic_day = traffic_day
        # The traffic type. Valid values:
        # 
        # *   **EIP_TRAFFIC**: traffic for the Internet firewall
        # *   **NatGateway_TRAFFIC**: traffic for NAT firewalls
        # *   **VPC_TRAFFIC**: traffic for VPC firewalls
        self.traffic_type = traffic_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.in_bytes is not None:
            result['InBytes'] = self.in_bytes

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.out_bytes is not None:
            result['OutBytes'] = self.out_bytes

        if self.protection_duration is not None:
            result['ProtectionDuration'] = self.protection_duration

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.total_bytes is not None:
            result['TotalBytes'] = self.total_bytes

        if self.traffic_day is not None:
            result['TrafficDay'] = self.traffic_day

        if self.traffic_type is not None:
            result['TrafficType'] = self.traffic_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InBytes') is not None:
            self.in_bytes = m.get('InBytes')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('OutBytes') is not None:
            self.out_bytes = m.get('OutBytes')

        if m.get('ProtectionDuration') is not None:
            self.protection_duration = m.get('ProtectionDuration')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('TotalBytes') is not None:
            self.total_bytes = m.get('TotalBytes')

        if m.get('TrafficDay') is not None:
            self.traffic_day = m.get('TrafficDay')

        if m.get('TrafficType') is not None:
            self.traffic_type = m.get('TrafficType')

        return self

