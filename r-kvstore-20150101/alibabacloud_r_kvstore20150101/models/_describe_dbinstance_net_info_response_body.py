# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_r_kvstore20150101 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstanceNetInfoResponseBody(DaraModel):
    def __init__(
        self,
        instance_network_type: str = None,
        net_info_items: main_models.DescribeDBInstanceNetInfoResponseBodyNetInfoItems = None,
        request_id: str = None,
    ):
        # The network type. Valid values:
        # 
        # *   **CLASSIC**: The instance runs in a classic network.
        # *   **VPC**: The instance runs in a virtual private cloud (VPC).
        self.instance_network_type = instance_network_type
        # The network information about the instance.
        self.net_info_items = net_info_items
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.net_info_items:
            self.net_info_items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type

        if self.net_info_items is not None:
            result['NetInfoItems'] = self.net_info_items.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')

        if m.get('NetInfoItems') is not None:
            temp_model = main_models.DescribeDBInstanceNetInfoResponseBodyNetInfoItems()
            self.net_info_items = temp_model.from_map(m.get('NetInfoItems'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDBInstanceNetInfoResponseBodyNetInfoItems(DaraModel):
    def __init__(
        self,
        instance_net_info: List[main_models.DescribeDBInstanceNetInfoResponseBodyNetInfoItemsInstanceNetInfo] = None,
    ):
        self.instance_net_info = instance_net_info

    def validate(self):
        if self.instance_net_info:
            for v1 in self.instance_net_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceNetInfo'] = []
        if self.instance_net_info is not None:
            for k1 in self.instance_net_info:
                result['InstanceNetInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_net_info = []
        if m.get('InstanceNetInfo') is not None:
            for k1 in m.get('InstanceNetInfo'):
                temp_model = main_models.DescribeDBInstanceNetInfoResponseBodyNetInfoItemsInstanceNetInfo()
                self.instance_net_info.append(temp_model.from_map(k1))

        return self

class DescribeDBInstanceNetInfoResponseBodyNetInfoItemsInstanceNetInfo(DaraModel):
    def __init__(
        self,
        connection_string: str = None,
        dbinstance_net_type: str = None,
        direct_connection: int = None,
        expired_time: str = None,
        ipaddress: str = None,
        iptype: str = None,
        is_slave_proxy: int = None,
        port: str = None,
        upgradeable: str = None,
        vpcid: str = None,
        vpcinstance_id: str = None,
        v_switch_id: str = None,
    ):
        # The endpoint of the instance.
        self.connection_string = connection_string
        # The network type of the instance. Valid values:
        # 
        # *   **0**: Internet
        # *   **1**: classic network
        # *   **2**: Virtual Private Cloud (VPC)
        self.dbinstance_net_type = dbinstance_net_type
        # Indicates whether the address is a private endpoint. Valid values:
        # 
        # *   **0**: The address is not a private endpoint.
        # *   **1**: The address is a private endpoint.
        self.direct_connection = direct_connection
        # The expiration time of the classic network endpoint. Unit: seconds.
        self.expired_time = expired_time
        # The IP address.
        self.ipaddress = ipaddress
        # The network type of the IP address. Valid values:
        # 
        # *   **Public**: Internet
        # *   **Inner**: classic network
        # *   **Private**: VPC
        self.iptype = iptype
        # Indicates whether the address is the endpoint for the secondary zone. Valid values: 1 and 0. A value of 1 indicates that the address is the endpoint for the secondary zone.
        # 
        # >  This parameter is returned only after you enable the multi-zone read/write splitting architecture for the instance.
        self.is_slave_proxy = is_slave_proxy
        # The service port of the instance.
        self.port = port
        # The remaining validity period of the classic network endpoint. Unit: seconds.
        # 
        # >  **A value of 0 indicates that the endpoint never expires.
        self.upgradeable = upgradeable
        # The ID of the VPC to which the instance belongs.
        self.vpcid = vpcid
        # The instance ID.
        self.vpcinstance_id = vpcinstance_id
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.dbinstance_net_type is not None:
            result['DBInstanceNetType'] = self.dbinstance_net_type

        if self.direct_connection is not None:
            result['DirectConnection'] = self.direct_connection

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress

        if self.iptype is not None:
            result['IPType'] = self.iptype

        if self.is_slave_proxy is not None:
            result['IsSlaveProxy'] = self.is_slave_proxy

        if self.port is not None:
            result['Port'] = self.port

        if self.upgradeable is not None:
            result['Upgradeable'] = self.upgradeable

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.vpcinstance_id is not None:
            result['VPCInstanceId'] = self.vpcinstance_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('DBInstanceNetType') is not None:
            self.dbinstance_net_type = m.get('DBInstanceNetType')

        if m.get('DirectConnection') is not None:
            self.direct_connection = m.get('DirectConnection')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')

        if m.get('IPType') is not None:
            self.iptype = m.get('IPType')

        if m.get('IsSlaveProxy') is not None:
            self.is_slave_proxy = m.get('IsSlaveProxy')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Upgradeable') is not None:
            self.upgradeable = m.get('Upgradeable')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VPCInstanceId') is not None:
            self.vpcinstance_id = m.get('VPCInstanceId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

