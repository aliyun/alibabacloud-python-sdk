# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstanceNetInfoResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_net_infos: main_models.DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfos = None,
        instance_network_type: str = None,
        request_id: str = None,
    ):
        # The connection information of the instance.
        self.dbinstance_net_infos = dbinstance_net_infos
        # The network type of the instance. Valid values:
        # 
        # *   Classic: classic network.
        # *   VPC: VPC.
        self.instance_network_type = instance_network_type
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.dbinstance_net_infos:
            self.dbinstance_net_infos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_net_infos is not None:
            result['DBInstanceNetInfos'] = self.dbinstance_net_infos.to_map()

        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceNetInfos') is not None:
            temp_model = main_models.DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfos()
            self.dbinstance_net_infos = temp_model.from_map(m.get('DBInstanceNetInfos'))

        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfos(DaraModel):
    def __init__(
        self,
        dbinstance_net_info: List[main_models.DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfosDBInstanceNetInfo] = None,
    ):
        self.dbinstance_net_info = dbinstance_net_info

    def validate(self):
        if self.dbinstance_net_info:
            for v1 in self.dbinstance_net_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DBInstanceNetInfo'] = []
        if self.dbinstance_net_info is not None:
            for k1 in self.dbinstance_net_info:
                result['DBInstanceNetInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbinstance_net_info = []
        if m.get('DBInstanceNetInfo') is not None:
            for k1 in m.get('DBInstanceNetInfo'):
                temp_model = main_models.DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfosDBInstanceNetInfo()
                self.dbinstance_net_info.append(temp_model.from_map(k1))

        return self

class DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfosDBInstanceNetInfo(DaraModel):
    def __init__(
        self,
        address_type: str = None,
        connection_string: str = None,
        ipaddress: str = None,
        iptype: str = None,
        port: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        vpc_instance_id: str = None,
    ):
        # The type of the endpoint.
        self.address_type = address_type
        # The endpoint that is used to connect to the instance.
        self.connection_string = connection_string
        # The IP address.
        self.ipaddress = ipaddress
        # The type of the IP address.
        # 
        # *   Valid values for instances in the classic network: Inner and Public.
        # *   Valid values for instances in a virtual private cloud (VPC): Private and Public.
        self.iptype = iptype
        # The port number.
        self.port = port
        # The VPC ID of the instance.
        self.vpcid = vpcid
        # The vSwitch ID. Multiple IDs are separated by commas (,).
        self.v_switch_id = v_switch_id
        # The ID of the instance that is deployed in a VPC.
        self.vpc_instance_id = vpc_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_type is not None:
            result['AddressType'] = self.address_type

        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress

        if self.iptype is not None:
            result['IPType'] = self.iptype

        if self.port is not None:
            result['Port'] = self.port

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_instance_id is not None:
            result['VpcInstanceId'] = self.vpc_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')

        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')

        if m.get('IPType') is not None:
            self.iptype = m.get('IPType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcInstanceId') is not None:
            self.vpc_instance_id = m.get('VpcInstanceId')

        return self

