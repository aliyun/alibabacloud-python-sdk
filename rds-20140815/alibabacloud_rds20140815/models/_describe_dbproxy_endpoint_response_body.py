# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeDBProxyEndpointResponseBody(DaraModel):
    def __init__(
        self,
        causal_consist_read_timeout: str = None,
        dbproxy_connect_string: str = None,
        dbproxy_connect_string_net_type: str = None,
        dbproxy_connect_string_port: str = None,
        dbproxy_endpoint_id: str = None,
        dbproxy_endpoint_min_slave_count: str = None,
        dbproxy_engine_type: str = None,
        dbproxy_features: str = None,
        dbproxy_nodes: main_models.DescribeDBProxyEndpointResponseBodyDBProxyNodes = None,
        db_proxy_endpoint_aliases: str = None,
        db_proxy_endpoint_read_write_mode: str = None,
        db_proxy_endpoint_vpc_id: str = None,
        db_proxy_endpoint_vswitch_id: str = None,
        db_proxy_endpoint_zone_id: str = None,
        endpoint_connect_items: main_models.DescribeDBProxyEndpointResponseBodyEndpointConnectItems = None,
        read_only_instance_distribution_type: str = None,
        read_only_instance_max_delay_time: str = None,
        read_only_instance_weight: str = None,
        request_id: str = None,
    ):
        self.causal_consist_read_timeout = causal_consist_read_timeout
        self.dbproxy_connect_string = dbproxy_connect_string
        self.dbproxy_connect_string_net_type = dbproxy_connect_string_net_type
        self.dbproxy_connect_string_port = dbproxy_connect_string_port
        self.dbproxy_endpoint_id = dbproxy_endpoint_id
        self.dbproxy_endpoint_min_slave_count = dbproxy_endpoint_min_slave_count
        self.dbproxy_engine_type = dbproxy_engine_type
        self.dbproxy_features = dbproxy_features
        self.dbproxy_nodes = dbproxy_nodes
        self.db_proxy_endpoint_aliases = db_proxy_endpoint_aliases
        self.db_proxy_endpoint_read_write_mode = db_proxy_endpoint_read_write_mode
        self.db_proxy_endpoint_vpc_id = db_proxy_endpoint_vpc_id
        self.db_proxy_endpoint_vswitch_id = db_proxy_endpoint_vswitch_id
        self.db_proxy_endpoint_zone_id = db_proxy_endpoint_zone_id
        self.endpoint_connect_items = endpoint_connect_items
        self.read_only_instance_distribution_type = read_only_instance_distribution_type
        self.read_only_instance_max_delay_time = read_only_instance_max_delay_time
        self.read_only_instance_weight = read_only_instance_weight
        self.request_id = request_id

    def validate(self):
        if self.dbproxy_nodes:
            self.dbproxy_nodes.validate()
        if self.endpoint_connect_items:
            self.endpoint_connect_items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.causal_consist_read_timeout is not None:
            result['CausalConsistReadTimeout'] = self.causal_consist_read_timeout

        if self.dbproxy_connect_string is not None:
            result['DBProxyConnectString'] = self.dbproxy_connect_string

        if self.dbproxy_connect_string_net_type is not None:
            result['DBProxyConnectStringNetType'] = self.dbproxy_connect_string_net_type

        if self.dbproxy_connect_string_port is not None:
            result['DBProxyConnectStringPort'] = self.dbproxy_connect_string_port

        if self.dbproxy_endpoint_id is not None:
            result['DBProxyEndpointId'] = self.dbproxy_endpoint_id

        if self.dbproxy_endpoint_min_slave_count is not None:
            result['DBProxyEndpointMinSlaveCount'] = self.dbproxy_endpoint_min_slave_count

        if self.dbproxy_engine_type is not None:
            result['DBProxyEngineType'] = self.dbproxy_engine_type

        if self.dbproxy_features is not None:
            result['DBProxyFeatures'] = self.dbproxy_features

        if self.dbproxy_nodes is not None:
            result['DBProxyNodes'] = self.dbproxy_nodes.to_map()

        if self.db_proxy_endpoint_aliases is not None:
            result['DbProxyEndpointAliases'] = self.db_proxy_endpoint_aliases

        if self.db_proxy_endpoint_read_write_mode is not None:
            result['DbProxyEndpointReadWriteMode'] = self.db_proxy_endpoint_read_write_mode

        if self.db_proxy_endpoint_vpc_id is not None:
            result['DbProxyEndpointVpcId'] = self.db_proxy_endpoint_vpc_id

        if self.db_proxy_endpoint_vswitch_id is not None:
            result['DbProxyEndpointVswitchId'] = self.db_proxy_endpoint_vswitch_id

        if self.db_proxy_endpoint_zone_id is not None:
            result['DbProxyEndpointZoneId'] = self.db_proxy_endpoint_zone_id

        if self.endpoint_connect_items is not None:
            result['EndpointConnectItems'] = self.endpoint_connect_items.to_map()

        if self.read_only_instance_distribution_type is not None:
            result['ReadOnlyInstanceDistributionType'] = self.read_only_instance_distribution_type

        if self.read_only_instance_max_delay_time is not None:
            result['ReadOnlyInstanceMaxDelayTime'] = self.read_only_instance_max_delay_time

        if self.read_only_instance_weight is not None:
            result['ReadOnlyInstanceWeight'] = self.read_only_instance_weight

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CausalConsistReadTimeout') is not None:
            self.causal_consist_read_timeout = m.get('CausalConsistReadTimeout')

        if m.get('DBProxyConnectString') is not None:
            self.dbproxy_connect_string = m.get('DBProxyConnectString')

        if m.get('DBProxyConnectStringNetType') is not None:
            self.dbproxy_connect_string_net_type = m.get('DBProxyConnectStringNetType')

        if m.get('DBProxyConnectStringPort') is not None:
            self.dbproxy_connect_string_port = m.get('DBProxyConnectStringPort')

        if m.get('DBProxyEndpointId') is not None:
            self.dbproxy_endpoint_id = m.get('DBProxyEndpointId')

        if m.get('DBProxyEndpointMinSlaveCount') is not None:
            self.dbproxy_endpoint_min_slave_count = m.get('DBProxyEndpointMinSlaveCount')

        if m.get('DBProxyEngineType') is not None:
            self.dbproxy_engine_type = m.get('DBProxyEngineType')

        if m.get('DBProxyFeatures') is not None:
            self.dbproxy_features = m.get('DBProxyFeatures')

        if m.get('DBProxyNodes') is not None:
            temp_model = main_models.DescribeDBProxyEndpointResponseBodyDBProxyNodes()
            self.dbproxy_nodes = temp_model.from_map(m.get('DBProxyNodes'))

        if m.get('DbProxyEndpointAliases') is not None:
            self.db_proxy_endpoint_aliases = m.get('DbProxyEndpointAliases')

        if m.get('DbProxyEndpointReadWriteMode') is not None:
            self.db_proxy_endpoint_read_write_mode = m.get('DbProxyEndpointReadWriteMode')

        if m.get('DbProxyEndpointVpcId') is not None:
            self.db_proxy_endpoint_vpc_id = m.get('DbProxyEndpointVpcId')

        if m.get('DbProxyEndpointVswitchId') is not None:
            self.db_proxy_endpoint_vswitch_id = m.get('DbProxyEndpointVswitchId')

        if m.get('DbProxyEndpointZoneId') is not None:
            self.db_proxy_endpoint_zone_id = m.get('DbProxyEndpointZoneId')

        if m.get('EndpointConnectItems') is not None:
            temp_model = main_models.DescribeDBProxyEndpointResponseBodyEndpointConnectItems()
            self.endpoint_connect_items = temp_model.from_map(m.get('EndpointConnectItems'))

        if m.get('ReadOnlyInstanceDistributionType') is not None:
            self.read_only_instance_distribution_type = m.get('ReadOnlyInstanceDistributionType')

        if m.get('ReadOnlyInstanceMaxDelayTime') is not None:
            self.read_only_instance_max_delay_time = m.get('ReadOnlyInstanceMaxDelayTime')

        if m.get('ReadOnlyInstanceWeight') is not None:
            self.read_only_instance_weight = m.get('ReadOnlyInstanceWeight')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDBProxyEndpointResponseBodyEndpointConnectItems(DaraModel):
    def __init__(
        self,
        endpoint_connect_items: List[main_models.DescribeDBProxyEndpointResponseBodyEndpointConnectItemsEndpointConnectItems] = None,
    ):
        self.endpoint_connect_items = endpoint_connect_items

    def validate(self):
        if self.endpoint_connect_items:
            for v1 in self.endpoint_connect_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EndpointConnectItems'] = []
        if self.endpoint_connect_items is not None:
            for k1 in self.endpoint_connect_items:
                result['EndpointConnectItems'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.endpoint_connect_items = []
        if m.get('EndpointConnectItems') is not None:
            for k1 in m.get('EndpointConnectItems'):
                temp_model = main_models.DescribeDBProxyEndpointResponseBodyEndpointConnectItemsEndpointConnectItems()
                self.endpoint_connect_items.append(temp_model.from_map(k1))

        return self

class DescribeDBProxyEndpointResponseBodyEndpointConnectItemsEndpointConnectItems(DaraModel):
    def __init__(
        self,
        db_proxy_endpoint_connect_string: str = None,
        db_proxy_endpoint_net_type: str = None,
        db_proxy_endpoint_port: str = None,
    ):
        self.db_proxy_endpoint_connect_string = db_proxy_endpoint_connect_string
        self.db_proxy_endpoint_net_type = db_proxy_endpoint_net_type
        self.db_proxy_endpoint_port = db_proxy_endpoint_port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_proxy_endpoint_connect_string is not None:
            result['DbProxyEndpointConnectString'] = self.db_proxy_endpoint_connect_string

        if self.db_proxy_endpoint_net_type is not None:
            result['DbProxyEndpointNetType'] = self.db_proxy_endpoint_net_type

        if self.db_proxy_endpoint_port is not None:
            result['DbProxyEndpointPort'] = self.db_proxy_endpoint_port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbProxyEndpointConnectString') is not None:
            self.db_proxy_endpoint_connect_string = m.get('DbProxyEndpointConnectString')

        if m.get('DbProxyEndpointNetType') is not None:
            self.db_proxy_endpoint_net_type = m.get('DbProxyEndpointNetType')

        if m.get('DbProxyEndpointPort') is not None:
            self.db_proxy_endpoint_port = m.get('DbProxyEndpointPort')

        return self

class DescribeDBProxyEndpointResponseBodyDBProxyNodes(DaraModel):
    def __init__(
        self,
        dbproxy_nodes: List[main_models.DescribeDBProxyEndpointResponseBodyDBProxyNodesDBProxyNodes] = None,
    ):
        self.dbproxy_nodes = dbproxy_nodes

    def validate(self):
        if self.dbproxy_nodes:
            for v1 in self.dbproxy_nodes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DBProxyNodes'] = []
        if self.dbproxy_nodes is not None:
            for k1 in self.dbproxy_nodes:
                result['DBProxyNodes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbproxy_nodes = []
        if m.get('DBProxyNodes') is not None:
            for k1 in m.get('DBProxyNodes'):
                temp_model = main_models.DescribeDBProxyEndpointResponseBodyDBProxyNodesDBProxyNodes()
                self.dbproxy_nodes.append(temp_model.from_map(k1))

        return self

class DescribeDBProxyEndpointResponseBodyDBProxyNodesDBProxyNodes(DaraModel):
    def __init__(
        self,
        cpu_cores: str = None,
        node_id: str = None,
        zone_id: str = None,
    ):
        self.cpu_cores = cpu_cores
        self.node_id = node_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu_cores is not None:
            result['cpuCores'] = self.cpu_cores

        if self.node_id is not None:
            result['nodeId'] = self.node_id

        if self.zone_id is not None:
            result['zoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpuCores') is not None:
            self.cpu_cores = m.get('cpuCores')

        if m.get('nodeId') is not None:
            self.node_id = m.get('nodeId')

        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')

        return self

