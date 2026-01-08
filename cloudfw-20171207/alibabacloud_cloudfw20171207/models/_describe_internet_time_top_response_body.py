# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeInternetTimeTopResponseBody(DaraModel):
    def __init__(
        self,
        data_count: int = None,
        data_list: List[main_models.DescribeInternetTimeTopResponseBodyDataList] = None,
        request_id: str = None,
        traffic_time: int = None,
    ):
        self.data_count = data_count
        self.data_list = data_list
        self.request_id = request_id
        self.traffic_time = traffic_time

    def validate(self):
        if self.data_list:
            for v1 in self.data_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_count is not None:
            result['DataCount'] = self.data_count

        result['DataList'] = []
        if self.data_list is not None:
            for k1 in self.data_list:
                result['DataList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.traffic_time is not None:
            result['TrafficTime'] = self.traffic_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataCount') is not None:
            self.data_count = m.get('DataCount')

        self.data_list = []
        if m.get('DataList') is not None:
            for k1 in m.get('DataList'):
                temp_model = main_models.DescribeInternetTimeTopResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TrafficTime') is not None:
            self.traffic_time = m.get('TrafficTime')

        return self

class DescribeInternetTimeTopResponseBodyDataList(DaraModel):
    def __init__(
        self,
        ip: str = None,
        in_bps: int = None,
        in_pps: int = None,
        nat_gateway_id: str = None,
        nat_gateway_name: str = None,
        nat_ip: str = None,
        new_conn: int = None,
        out_bps: int = None,
        out_pps: int = None,
        private_ip: str = None,
        region_no: str = None,
        resource_instance_id: str = None,
        resource_instance_name: str = None,
        resource_type: str = None,
        session_count: int = None,
        total_bps: int = None,
        total_pps: int = None,
        vpc_id: str = None,
    ):
        self.ip = ip
        self.in_bps = in_bps
        self.in_pps = in_pps
        self.nat_gateway_id = nat_gateway_id
        self.nat_gateway_name = nat_gateway_name
        self.nat_ip = nat_ip
        self.new_conn = new_conn
        self.out_bps = out_bps
        self.out_pps = out_pps
        self.private_ip = private_ip
        self.region_no = region_no
        self.resource_instance_id = resource_instance_id
        self.resource_instance_name = resource_instance_name
        self.resource_type = resource_type
        self.session_count = session_count
        self.total_bps = total_bps
        self.total_pps = total_pps
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip is not None:
            result['IP'] = self.ip

        if self.in_bps is not None:
            result['InBps'] = self.in_bps

        if self.in_pps is not None:
            result['InPps'] = self.in_pps

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.nat_gateway_name is not None:
            result['NatGatewayName'] = self.nat_gateway_name

        if self.nat_ip is not None:
            result['NatIP'] = self.nat_ip

        if self.new_conn is not None:
            result['NewConn'] = self.new_conn

        if self.out_bps is not None:
            result['OutBps'] = self.out_bps

        if self.out_pps is not None:
            result['OutPps'] = self.out_pps

        if self.private_ip is not None:
            result['PrivateIP'] = self.private_ip

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.resource_instance_id is not None:
            result['ResourceInstanceId'] = self.resource_instance_id

        if self.resource_instance_name is not None:
            result['ResourceInstanceName'] = self.resource_instance_name

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.session_count is not None:
            result['SessionCount'] = self.session_count

        if self.total_bps is not None:
            result['TotalBps'] = self.total_bps

        if self.total_pps is not None:
            result['TotalPps'] = self.total_pps

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IP') is not None:
            self.ip = m.get('IP')

        if m.get('InBps') is not None:
            self.in_bps = m.get('InBps')

        if m.get('InPps') is not None:
            self.in_pps = m.get('InPps')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('NatGatewayName') is not None:
            self.nat_gateway_name = m.get('NatGatewayName')

        if m.get('NatIP') is not None:
            self.nat_ip = m.get('NatIP')

        if m.get('NewConn') is not None:
            self.new_conn = m.get('NewConn')

        if m.get('OutBps') is not None:
            self.out_bps = m.get('OutBps')

        if m.get('OutPps') is not None:
            self.out_pps = m.get('OutPps')

        if m.get('PrivateIP') is not None:
            self.private_ip = m.get('PrivateIP')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('ResourceInstanceId') is not None:
            self.resource_instance_id = m.get('ResourceInstanceId')

        if m.get('ResourceInstanceName') is not None:
            self.resource_instance_name = m.get('ResourceInstanceName')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('SessionCount') is not None:
            self.session_count = m.get('SessionCount')

        if m.get('TotalBps') is not None:
            self.total_bps = m.get('TotalBps')

        if m.get('TotalPps') is not None:
            self.total_pps = m.get('TotalPps')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

