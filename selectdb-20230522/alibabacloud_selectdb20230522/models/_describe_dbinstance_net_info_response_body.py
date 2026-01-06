# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_selectdb20230522 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstanceNetInfoResponseBody(DaraModel):
    def __init__(
        self,
        dbclusters_net_infos: List[main_models.DescribeDBInstanceNetInfoResponseBodyDBClustersNetInfos] = None,
        dbinstance_net_infos: List[main_models.DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfos] = None,
        request_id: str = None,
    ):
        # The network information about the backend (BE) clusters.
        self.dbclusters_net_infos = dbclusters_net_infos
        # The network information about the instance.
        self.dbinstance_net_infos = dbinstance_net_infos
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.dbclusters_net_infos:
            for v1 in self.dbclusters_net_infos:
                 if v1:
                    v1.validate()
        if self.dbinstance_net_infos:
            for v1 in self.dbinstance_net_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DBClustersNetInfos'] = []
        if self.dbclusters_net_infos is not None:
            for k1 in self.dbclusters_net_infos:
                result['DBClustersNetInfos'].append(k1.to_map() if k1 else None)

        result['DBInstanceNetInfos'] = []
        if self.dbinstance_net_infos is not None:
            for k1 in self.dbinstance_net_infos:
                result['DBInstanceNetInfos'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbclusters_net_infos = []
        if m.get('DBClustersNetInfos') is not None:
            for k1 in m.get('DBClustersNetInfos'):
                temp_model = main_models.DescribeDBInstanceNetInfoResponseBodyDBClustersNetInfos()
                self.dbclusters_net_infos.append(temp_model.from_map(k1))

        self.dbinstance_net_infos = []
        if m.get('DBInstanceNetInfos') is not None:
            for k1 in m.get('DBInstanceNetInfos'):
                temp_model = main_models.DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfos()
                self.dbinstance_net_infos.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfos(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        connection_string: str = None,
        ip: str = None,
        net_type: str = None,
        port_list: List[main_models.DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfosPortList] = None,
        user_visible: bool = None,
        vpc_id: str = None,
        vpc_instance_id: str = None,
        vswitch_id: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The connection string of the instance.
        self.connection_string = connection_string
        # The IP address of the instance.
        self.ip = ip
        # The network type of the instance. Valid values:
        # 
        # *   **VPC**: indicates a virtual private cloud (VPC)-connected instance.
        # *   **PUBLIC**: indicates an Internet-connected instance.
        self.net_type = net_type
        # The ports.
        self.port_list = port_list
        # Indicates whether the network information is visible to users. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.user_visible = user_visible
        # The VPC ID.
        self.vpc_id = vpc_id
        # The ID of the VPC-connected instance.
        self.vpc_instance_id = vpc_instance_id
        # The vSwitch ID.
        self.vswitch_id = vswitch_id

    def validate(self):
        if self.port_list:
            for v1 in self.port_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.net_type is not None:
            result['NetType'] = self.net_type

        result['PortList'] = []
        if self.port_list is not None:
            for k1 in self.port_list:
                result['PortList'].append(k1.to_map() if k1 else None)

        if self.user_visible is not None:
            result['UserVisible'] = self.user_visible

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_instance_id is not None:
            result['VpcInstanceId'] = self.vpc_instance_id

        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        self.port_list = []
        if m.get('PortList') is not None:
            for k1 in m.get('PortList'):
                temp_model = main_models.DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfosPortList()
                self.port_list.append(temp_model.from_map(k1))

        if m.get('UserVisible') is not None:
            self.user_visible = m.get('UserVisible')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcInstanceId') is not None:
            self.vpc_instance_id = m.get('VpcInstanceId')

        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        return self

class DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfosPortList(DaraModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
    ):
        # The port that is used to connect to the instance.
        self.port = port
        # The protocol of the port. Valid values:
        # 
        # *   **HttpPort**: HTTP port.
        # *   **MySQLPort**: MySQL port.
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.port is not None:
            result['Port'] = self.port

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        return self

class DescribeDBInstanceNetInfoResponseBodyDBClustersNetInfos(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        connection_string: str = None,
        ip: str = None,
        net_type: str = None,
        port_list: List[main_models.DescribeDBInstanceNetInfoResponseBodyDBClustersNetInfosPortList] = None,
        user_visible: bool = None,
        vpc_id: str = None,
        vpc_instance_id: str = None,
        vswitch_id: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The connection string of the BE cluster.
        self.connection_string = connection_string
        # The IP address of the BE cluster.
        self.ip = ip
        # The network type of the BE cluster.
        self.net_type = net_type
        self.port_list = port_list
        # Indicates whether the network information is visible to users.
        self.user_visible = user_visible
        # VPC ID
        self.vpc_id = vpc_id
        # The VPC ID.
        self.vpc_instance_id = vpc_instance_id
        # The vSwitch ID.
        self.vswitch_id = vswitch_id

    def validate(self):
        if self.port_list:
            for v1 in self.port_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.net_type is not None:
            result['NetType'] = self.net_type

        result['PortList'] = []
        if self.port_list is not None:
            for k1 in self.port_list:
                result['PortList'].append(k1.to_map() if k1 else None)

        if self.user_visible is not None:
            result['UserVisible'] = self.user_visible

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_instance_id is not None:
            result['VpcInstanceId'] = self.vpc_instance_id

        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        self.port_list = []
        if m.get('PortList') is not None:
            for k1 in m.get('PortList'):
                temp_model = main_models.DescribeDBInstanceNetInfoResponseBodyDBClustersNetInfosPortList()
                self.port_list.append(temp_model.from_map(k1))

        if m.get('UserVisible') is not None:
            self.user_visible = m.get('UserVisible')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcInstanceId') is not None:
            self.vpc_instance_id = m.get('VpcInstanceId')

        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        return self

class DescribeDBInstanceNetInfoResponseBodyDBClustersNetInfosPortList(DaraModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
    ):
        # The port that is used to connect to the BE cluster.
        self.port = port
        # The protocol of the port.
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.port is not None:
            result['Port'] = self.port

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        return self

