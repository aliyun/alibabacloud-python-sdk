# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstanceEndpointResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeDBInstanceEndpointResponseBodyData = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeDBInstanceEndpointResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDBInstanceEndpointResponseBodyData(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeDBInstanceEndpointResponseBodyDataItems] = None,
    ):
        self.items = items

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeDBInstanceEndpointResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        return self

class DescribeDBInstanceEndpointResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        endpoint: main_models.DescribeDBInstanceEndpointResponseBodyDataItemsEndpoint = None,
        real_server: List[main_models.DescribeDBInstanceEndpointResponseBodyDataItemsRealServer] = None,
    ):
        self.endpoint = endpoint
        self.real_server = real_server

    def validate(self):
        if self.endpoint:
            self.endpoint.validate()
        if self.real_server:
            for v1 in self.real_server:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint.to_map()

        result['RealServer'] = []
        if self.real_server is not None:
            for k1 in self.real_server:
                result['RealServer'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            temp_model = main_models.DescribeDBInstanceEndpointResponseBodyDataItemsEndpoint()
            self.endpoint = temp_model.from_map(m.get('Endpoint'))

        self.real_server = []
        if m.get('RealServer') is not None:
            for k1 in m.get('RealServer'):
                temp_model = main_models.DescribeDBInstanceEndpointResponseBodyDataItemsRealServer()
                self.real_server.append(temp_model.from_map(k1))

        return self

class DescribeDBInstanceEndpointResponseBodyDataItemsRealServer(DaraModel):
    def __init__(
        self,
        activated: bool = None,
        class_: str = None,
        ip: str = None,
        port: str = None,
        replica_id: int = None,
        weight: int = None,
    ):
        self.activated = activated
        self.class_ = class_
        self.ip = ip
        self.port = port
        self.replica_id = replica_id
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activated is not None:
            result['Activated'] = self.activated

        if self.class_ is not None:
            result['Class'] = self.class_

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.port is not None:
            result['Port'] = self.port

        if self.replica_id is not None:
            result['ReplicaId'] = self.replica_id

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Activated') is not None:
            self.activated = m.get('Activated')

        if m.get('Class') is not None:
            self.class_ = m.get('Class')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('ReplicaId') is not None:
            self.replica_id = m.get('ReplicaId')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

class DescribeDBInstanceEndpointResponseBodyDataItemsEndpoint(DaraModel):
    def __init__(
        self,
        address: str = None,
        class_: str = None,
        endpoint_group_id: int = None,
        id: int = None,
        is_default: bool = None,
        kind: str = None,
        net_type: str = None,
        read_type: str = None,
        target_name: str = None,
        tunnel_id: int = None,
        type: str = None,
        user_visible: bool = None,
        v_switch_id: str = None,
        vip: str = None,
        vpc_id: str = None,
        vport: int = None,
        zone_id: str = None,
    ):
        self.address = address
        self.class_ = class_
        self.endpoint_group_id = endpoint_group_id
        self.id = id
        self.is_default = is_default
        self.kind = kind
        self.net_type = net_type
        self.read_type = read_type
        self.target_name = target_name
        self.tunnel_id = tunnel_id
        self.type = type
        self.user_visible = user_visible
        self.v_switch_id = v_switch_id
        self.vip = vip
        self.vpc_id = vpc_id
        self.vport = vport
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.class_ is not None:
            result['Class'] = self.class_

        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id

        if self.id is not None:
            result['Id'] = self.id

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.kind is not None:
            result['Kind'] = self.kind

        if self.net_type is not None:
            result['NetType'] = self.net_type

        if self.read_type is not None:
            result['ReadType'] = self.read_type

        if self.target_name is not None:
            result['TargetName'] = self.target_name

        if self.tunnel_id is not None:
            result['TunnelId'] = self.tunnel_id

        if self.type is not None:
            result['Type'] = self.type

        if self.user_visible is not None:
            result['UserVisible'] = self.user_visible

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vip is not None:
            result['Vip'] = self.vip

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vport is not None:
            result['Vport'] = self.vport

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('Class') is not None:
            self.class_ = m.get('Class')

        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('Kind') is not None:
            self.kind = m.get('Kind')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        if m.get('ReadType') is not None:
            self.read_type = m.get('ReadType')

        if m.get('TargetName') is not None:
            self.target_name = m.get('TargetName')

        if m.get('TunnelId') is not None:
            self.tunnel_id = m.get('TunnelId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UserVisible') is not None:
            self.user_visible = m.get('UserVisible')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('Vip') is not None:
            self.vip = m.get('Vip')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('Vport') is not None:
            self.vport = m.get('Vport')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

