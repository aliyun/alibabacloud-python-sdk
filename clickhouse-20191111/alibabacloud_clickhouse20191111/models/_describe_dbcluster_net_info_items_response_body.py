# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_clickhouse20191111 import models as main_models
from darabonba.model import DaraModel

class DescribeDBClusterNetInfoItemsResponseBody(DaraModel):
    def __init__(
        self,
        cluster_network_type: str = None,
        enable_slb: bool = None,
        net_info_items: main_models.DescribeDBClusterNetInfoItemsResponseBodyNetInfoItems = None,
        request_id: str = None,
    ):
        # The network type of the cluster. Only VPC is supported.
        self.cluster_network_type = cluster_network_type
        # Indicates whether Server Load Balancer (SLB) is activated in the VPC. Valid values:
        # 
        # *   true
        # *   false
        # 
        # This parameter is required.
        self.enable_slb = enable_slb
        # The network information about the cluster.
        self.net_info_items = net_info_items
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.net_info_items:
            self.net_info_items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_network_type is not None:
            result['ClusterNetworkType'] = self.cluster_network_type

        if self.enable_slb is not None:
            result['EnableSLB'] = self.enable_slb

        if self.net_info_items is not None:
            result['NetInfoItems'] = self.net_info_items.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterNetworkType') is not None:
            self.cluster_network_type = m.get('ClusterNetworkType')

        if m.get('EnableSLB') is not None:
            self.enable_slb = m.get('EnableSLB')

        if m.get('NetInfoItems') is not None:
            temp_model = main_models.DescribeDBClusterNetInfoItemsResponseBodyNetInfoItems()
            self.net_info_items = temp_model.from_map(m.get('NetInfoItems'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDBClusterNetInfoItemsResponseBodyNetInfoItems(DaraModel):
    def __init__(
        self,
        net_info_item: List[main_models.DescribeDBClusterNetInfoItemsResponseBodyNetInfoItemsNetInfoItem] = None,
    ):
        self.net_info_item = net_info_item

    def validate(self):
        if self.net_info_item:
            for v1 in self.net_info_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NetInfoItem'] = []
        if self.net_info_item is not None:
            for k1 in self.net_info_item:
                result['NetInfoItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.net_info_item = []
        if m.get('NetInfoItem') is not None:
            for k1 in m.get('NetInfoItem'):
                temp_model = main_models.DescribeDBClusterNetInfoItemsResponseBodyNetInfoItemsNetInfoItem()
                self.net_info_item.append(temp_model.from_map(k1))

        return self

class DescribeDBClusterNetInfoItemsResponseBodyNetInfoItemsNetInfoItem(DaraModel):
    def __init__(
        self,
        connection_string: str = None,
        http_port: str = None,
        https_port: str = None,
        ipaddress: str = None,
        jdbc_port: str = None,
        my_sqlport: str = None,
        net_type: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The endpoint that is used to connect to the database.
        self.connection_string = connection_string
        # The HTTP port number.
        self.http_port = http_port
        # The HTTPS port number.
        self.https_port = https_port
        # The IP address.
        self.ipaddress = ipaddress
        # The port number that is used in Java Database Connectivity (JDBC).
        self.jdbc_port = jdbc_port
        # The port of the MySQL instance.
        self.my_sqlport = my_sqlport
        # The network type of the endpoint. Valid values:
        # 
        # *   Public: public endpoint
        # *   VPC: VPC
        self.net_type = net_type
        # The vSwitch ID.
        # 
        # >  If the value of the NetType parameter is set to Public, an empty string is returned.
        self.v_switch_id = v_switch_id
        # The virtual private cloud (VPC) ID.
        # 
        # >  If the value of the NetType parameter is set to Public, an empty string is returned.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.http_port is not None:
            result['HttpPort'] = self.http_port

        if self.https_port is not None:
            result['HttpsPort'] = self.https_port

        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress

        if self.jdbc_port is not None:
            result['JdbcPort'] = self.jdbc_port

        if self.my_sqlport is not None:
            result['MySQLPort'] = self.my_sqlport

        if self.net_type is not None:
            result['NetType'] = self.net_type

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('HttpPort') is not None:
            self.http_port = m.get('HttpPort')

        if m.get('HttpsPort') is not None:
            self.https_port = m.get('HttpsPort')

        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')

        if m.get('JdbcPort') is not None:
            self.jdbc_port = m.get('JdbcPort')

        if m.get('MySQLPort') is not None:
            self.my_sqlport = m.get('MySQLPort')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

