# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeDBProxyResponseBody(DaraModel):
    def __init__(
        self,
        dbproxy_avzones: main_models.DescribeDBProxyResponseBodyDBProxyAVZones = None,
        dbproxy_connect_string_items: main_models.DescribeDBProxyResponseBodyDBProxyConnectStringItems = None,
        dbproxy_engine_type: str = None,
        dbproxy_instance_current_minor_version: str = None,
        dbproxy_instance_latest_minor_version: str = None,
        dbproxy_instance_minor_versions: main_models.DescribeDBProxyResponseBodyDBProxyInstanceMinorVersions = None,
        dbproxy_instance_name: str = None,
        dbproxy_instance_num: int = None,
        dbproxy_instance_size: str = None,
        dbproxy_instance_status: str = None,
        dbproxy_instance_type: str = None,
        dbproxy_kind_code: str = None,
        dbproxy_nodes: main_models.DescribeDBProxyResponseBodyDBProxyNodes = None,
        dbproxy_persistent_connection_status: str = None,
        dbproxy_service_status: str = None,
        db_proxy_endpoint_items: main_models.DescribeDBProxyResponseBodyDbProxyEndpointItems = None,
        request_id: str = None,
        resource_group_id: str = None,
    ):
        # The list of zones that are available for the database proxy.
        self.dbproxy_avzones = dbproxy_avzones
        # An array consisting of the information about the database proxy endpoint that is created for the instance.
        self.dbproxy_connect_string_items = dbproxy_connect_string_items
        # An internal parameter. You can ignore this parameter.
        self.dbproxy_engine_type = dbproxy_engine_type
        # The version of the proxy instance.
        self.dbproxy_instance_current_minor_version = dbproxy_instance_current_minor_version
        # The latest version that is available for the proxy instance.
        self.dbproxy_instance_latest_minor_version = dbproxy_instance_latest_minor_version
        self.dbproxy_instance_minor_versions = dbproxy_instance_minor_versions
        # The name of the proxy instance.
        self.dbproxy_instance_name = dbproxy_instance_name
        # The number of proxies that are enabled on the instance.
        self.dbproxy_instance_num = dbproxy_instance_num
        # This parameter is available only for ApsaraDB RDS for PostgreSQL instances. The specifications of the proxy instance that is enabled.
        # 
        # Format: `Number of cores/Memory capacity`.
        # 
        # For example, a value of 4/8 indicates that the proxy instance has 4 cores and 8 GB of memory.
        self.dbproxy_instance_size = dbproxy_instance_size
        # The status of the proxy instance.
        # 
        # *   DBInstanceClassChanging: The specifications of the proxy instance are being changed.
        # *   Creating: The proxy instance is being created.
        # *   Running: The proxy instance is running.
        # *   Deleting: The proxy instance is being deleted.
        self.dbproxy_instance_status = dbproxy_instance_status
        # The type of the database proxy that is enabled on the instance. Valid values:
        # 
        # *   1: shared database proxy
        # *   2: dedicated database proxy
        # *   3: general-purpose database proxy
        # 
        # >  ApsaraDB RDS for PostgreSQL does not support shared database proxies.
        self.dbproxy_instance_type = dbproxy_instance_type
        # An internal parameter. You do not need to specify this parameter.
        self.dbproxy_kind_code = dbproxy_kind_code
        # The proxy nodes.
        self.dbproxy_nodes = dbproxy_nodes
        # The status of persistence connections. Valid values:
        # 
        # *   **Enabled**
        # *   **Disabled**
        # *   **Unsupported**
        self.dbproxy_persistent_connection_status = dbproxy_persistent_connection_status
        # The status of the database proxy.
        # 
        # *   Shutdown: disabled
        # *   Startup: enabled
        self.dbproxy_service_status = dbproxy_service_status
        # The proxy terminals of the instance.
        self.db_proxy_endpoint_items = db_proxy_endpoint_items
        # The ID of the request.
        self.request_id = request_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        if self.dbproxy_avzones:
            self.dbproxy_avzones.validate()
        if self.dbproxy_connect_string_items:
            self.dbproxy_connect_string_items.validate()
        if self.dbproxy_instance_minor_versions:
            self.dbproxy_instance_minor_versions.validate()
        if self.dbproxy_nodes:
            self.dbproxy_nodes.validate()
        if self.db_proxy_endpoint_items:
            self.db_proxy_endpoint_items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbproxy_avzones is not None:
            result['DBProxyAVZones'] = self.dbproxy_avzones.to_map()

        if self.dbproxy_connect_string_items is not None:
            result['DBProxyConnectStringItems'] = self.dbproxy_connect_string_items.to_map()

        if self.dbproxy_engine_type is not None:
            result['DBProxyEngineType'] = self.dbproxy_engine_type

        if self.dbproxy_instance_current_minor_version is not None:
            result['DBProxyInstanceCurrentMinorVersion'] = self.dbproxy_instance_current_minor_version

        if self.dbproxy_instance_latest_minor_version is not None:
            result['DBProxyInstanceLatestMinorVersion'] = self.dbproxy_instance_latest_minor_version

        if self.dbproxy_instance_minor_versions is not None:
            result['DBProxyInstanceMinorVersions'] = self.dbproxy_instance_minor_versions.to_map()

        if self.dbproxy_instance_name is not None:
            result['DBProxyInstanceName'] = self.dbproxy_instance_name

        if self.dbproxy_instance_num is not None:
            result['DBProxyInstanceNum'] = self.dbproxy_instance_num

        if self.dbproxy_instance_size is not None:
            result['DBProxyInstanceSize'] = self.dbproxy_instance_size

        if self.dbproxy_instance_status is not None:
            result['DBProxyInstanceStatus'] = self.dbproxy_instance_status

        if self.dbproxy_instance_type is not None:
            result['DBProxyInstanceType'] = self.dbproxy_instance_type

        if self.dbproxy_kind_code is not None:
            result['DBProxyKindCode'] = self.dbproxy_kind_code

        if self.dbproxy_nodes is not None:
            result['DBProxyNodes'] = self.dbproxy_nodes.to_map()

        if self.dbproxy_persistent_connection_status is not None:
            result['DBProxyPersistentConnectionStatus'] = self.dbproxy_persistent_connection_status

        if self.dbproxy_service_status is not None:
            result['DBProxyServiceStatus'] = self.dbproxy_service_status

        if self.db_proxy_endpoint_items is not None:
            result['DbProxyEndpointItems'] = self.db_proxy_endpoint_items.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBProxyAVZones') is not None:
            temp_model = main_models.DescribeDBProxyResponseBodyDBProxyAVZones()
            self.dbproxy_avzones = temp_model.from_map(m.get('DBProxyAVZones'))

        if m.get('DBProxyConnectStringItems') is not None:
            temp_model = main_models.DescribeDBProxyResponseBodyDBProxyConnectStringItems()
            self.dbproxy_connect_string_items = temp_model.from_map(m.get('DBProxyConnectStringItems'))

        if m.get('DBProxyEngineType') is not None:
            self.dbproxy_engine_type = m.get('DBProxyEngineType')

        if m.get('DBProxyInstanceCurrentMinorVersion') is not None:
            self.dbproxy_instance_current_minor_version = m.get('DBProxyInstanceCurrentMinorVersion')

        if m.get('DBProxyInstanceLatestMinorVersion') is not None:
            self.dbproxy_instance_latest_minor_version = m.get('DBProxyInstanceLatestMinorVersion')

        if m.get('DBProxyInstanceMinorVersions') is not None:
            temp_model = main_models.DescribeDBProxyResponseBodyDBProxyInstanceMinorVersions()
            self.dbproxy_instance_minor_versions = temp_model.from_map(m.get('DBProxyInstanceMinorVersions'))

        if m.get('DBProxyInstanceName') is not None:
            self.dbproxy_instance_name = m.get('DBProxyInstanceName')

        if m.get('DBProxyInstanceNum') is not None:
            self.dbproxy_instance_num = m.get('DBProxyInstanceNum')

        if m.get('DBProxyInstanceSize') is not None:
            self.dbproxy_instance_size = m.get('DBProxyInstanceSize')

        if m.get('DBProxyInstanceStatus') is not None:
            self.dbproxy_instance_status = m.get('DBProxyInstanceStatus')

        if m.get('DBProxyInstanceType') is not None:
            self.dbproxy_instance_type = m.get('DBProxyInstanceType')

        if m.get('DBProxyKindCode') is not None:
            self.dbproxy_kind_code = m.get('DBProxyKindCode')

        if m.get('DBProxyNodes') is not None:
            temp_model = main_models.DescribeDBProxyResponseBodyDBProxyNodes()
            self.dbproxy_nodes = temp_model.from_map(m.get('DBProxyNodes'))

        if m.get('DBProxyPersistentConnectionStatus') is not None:
            self.dbproxy_persistent_connection_status = m.get('DBProxyPersistentConnectionStatus')

        if m.get('DBProxyServiceStatus') is not None:
            self.dbproxy_service_status = m.get('DBProxyServiceStatus')

        if m.get('DbProxyEndpointItems') is not None:
            temp_model = main_models.DescribeDBProxyResponseBodyDbProxyEndpointItems()
            self.db_proxy_endpoint_items = temp_model.from_map(m.get('DbProxyEndpointItems'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

class DescribeDBProxyResponseBodyDbProxyEndpointItems(DaraModel):
    def __init__(
        self,
        db_proxy_endpoint_items: List[main_models.DescribeDBProxyResponseBodyDbProxyEndpointItemsDbProxyEndpointItems] = None,
    ):
        self.db_proxy_endpoint_items = db_proxy_endpoint_items

    def validate(self):
        if self.db_proxy_endpoint_items:
            for v1 in self.db_proxy_endpoint_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DbProxyEndpointItems'] = []
        if self.db_proxy_endpoint_items is not None:
            for k1 in self.db_proxy_endpoint_items:
                result['DbProxyEndpointItems'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.db_proxy_endpoint_items = []
        if m.get('DbProxyEndpointItems') is not None:
            for k1 in m.get('DbProxyEndpointItems'):
                temp_model = main_models.DescribeDBProxyResponseBodyDbProxyEndpointItemsDbProxyEndpointItems()
                self.db_proxy_endpoint_items.append(temp_model.from_map(k1))

        return self

class DescribeDBProxyResponseBodyDbProxyEndpointItemsDbProxyEndpointItems(DaraModel):
    def __init__(
        self,
        db_proxy_endpoint_aliases: str = None,
        db_proxy_endpoint_name: str = None,
        db_proxy_endpoint_type: str = None,
        db_proxy_read_write_mode: str = None,
    ):
        # The description of the database proxy endpoint.
        self.db_proxy_endpoint_aliases = db_proxy_endpoint_aliases
        # The ID of the database proxy endpoint.
        self.db_proxy_endpoint_name = db_proxy_endpoint_name
        # The type of the database proxy endpoint. Valid values:
        # 
        # *   Custom: custom database proxy endpoint
        # *   RWSplit: default database proxy endpoint
        self.db_proxy_endpoint_type = db_proxy_endpoint_type
        # The read and write attributes of the database proxy endpoint.
        # 
        # *   ReadOnly
        # *   ReadWrite
        self.db_proxy_read_write_mode = db_proxy_read_write_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_proxy_endpoint_aliases is not None:
            result['DbProxyEndpointAliases'] = self.db_proxy_endpoint_aliases

        if self.db_proxy_endpoint_name is not None:
            result['DbProxyEndpointName'] = self.db_proxy_endpoint_name

        if self.db_proxy_endpoint_type is not None:
            result['DbProxyEndpointType'] = self.db_proxy_endpoint_type

        if self.db_proxy_read_write_mode is not None:
            result['DbProxyReadWriteMode'] = self.db_proxy_read_write_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbProxyEndpointAliases') is not None:
            self.db_proxy_endpoint_aliases = m.get('DbProxyEndpointAliases')

        if m.get('DbProxyEndpointName') is not None:
            self.db_proxy_endpoint_name = m.get('DbProxyEndpointName')

        if m.get('DbProxyEndpointType') is not None:
            self.db_proxy_endpoint_type = m.get('DbProxyEndpointType')

        if m.get('DbProxyReadWriteMode') is not None:
            self.db_proxy_read_write_mode = m.get('DbProxyReadWriteMode')

        return self

class DescribeDBProxyResponseBodyDBProxyNodes(DaraModel):
    def __init__(
        self,
        dbproxy_nodes: List[main_models.DescribeDBProxyResponseBodyDBProxyNodesDBProxyNodes] = None,
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
                temp_model = main_models.DescribeDBProxyResponseBodyDBProxyNodesDBProxyNodes()
                self.dbproxy_nodes.append(temp_model.from_map(k1))

        return self

class DescribeDBProxyResponseBodyDBProxyNodesDBProxyNodes(DaraModel):
    def __init__(
        self,
        cpu_cores: str = None,
        node_id: str = None,
        zone_id: str = None,
    ):
        # The number of CPU cores of the node.
        self.cpu_cores = cpu_cores
        # The ID of the proxy node.
        self.node_id = node_id
        # The ID of the zone in which the node is deployed.
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

class DescribeDBProxyResponseBodyDBProxyInstanceMinorVersions(DaraModel):
    def __init__(
        self,
        dbproxy_instance_minor_versions: List[str] = None,
    ):
        self.dbproxy_instance_minor_versions = dbproxy_instance_minor_versions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbproxy_instance_minor_versions is not None:
            result['DBProxyInstanceMinorVersions'] = self.dbproxy_instance_minor_versions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBProxyInstanceMinorVersions') is not None:
            self.dbproxy_instance_minor_versions = m.get('DBProxyInstanceMinorVersions')

        return self

class DescribeDBProxyResponseBodyDBProxyConnectStringItems(DaraModel):
    def __init__(
        self,
        dbproxy_connect_string_items: List[main_models.DescribeDBProxyResponseBodyDBProxyConnectStringItemsDBProxyConnectStringItems] = None,
    ):
        self.dbproxy_connect_string_items = dbproxy_connect_string_items

    def validate(self):
        if self.dbproxy_connect_string_items:
            for v1 in self.dbproxy_connect_string_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DBProxyConnectStringItems'] = []
        if self.dbproxy_connect_string_items is not None:
            for k1 in self.dbproxy_connect_string_items:
                result['DBProxyConnectStringItems'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbproxy_connect_string_items = []
        if m.get('DBProxyConnectStringItems') is not None:
            for k1 in m.get('DBProxyConnectStringItems'):
                temp_model = main_models.DescribeDBProxyResponseBodyDBProxyConnectStringItemsDBProxyConnectStringItems()
                self.dbproxy_connect_string_items.append(temp_model.from_map(k1))

        return self

class DescribeDBProxyResponseBodyDBProxyConnectStringItemsDBProxyConnectStringItems(DaraModel):
    def __init__(
        self,
        dbproxy_connect_string: str = None,
        dbproxy_connect_string_net_type: str = None,
        dbproxy_connect_string_net_work_type: str = None,
        dbproxy_connect_string_port: str = None,
        dbproxy_endpoint_id: str = None,
        dbproxy_endpoint_name: str = None,
        dbproxy_vpc_id: str = None,
        dbproxy_vpc_instance_id: str = None,
        dbproxy_vswitch_id: str = None,
    ):
        # The database proxy endpoint.
        self.dbproxy_connect_string = dbproxy_connect_string
        # The network type of the database proxy endpoint. A database proxy endpoint is formerly referred to as a proxy terminal. Valid values:
        # 
        # *   OuterString: Internet
        # *   InnerString: internal network
        self.dbproxy_connect_string_net_type = dbproxy_connect_string_net_type
        # The network type of the database proxy. Valid values:
        # 
        # *   0: Internet
        # *   1: classic network
        # *   2: virtual private cloud (VPC)
        self.dbproxy_connect_string_net_work_type = dbproxy_connect_string_net_work_type
        # The port that is associated with the database proxy endpoint.
        self.dbproxy_connect_string_port = dbproxy_connect_string_port
        # The ID of the backend database proxy endpoint.
        self.dbproxy_endpoint_id = dbproxy_endpoint_id
        # The name of the database proxy endpoint. The name can be replaced by the ID of the database proxy endpoint.
        self.dbproxy_endpoint_name = dbproxy_endpoint_name
        # The VPC of the database proxy.
        self.dbproxy_vpc_id = dbproxy_vpc_id
        # The ID of the database proxy instance.
        self.dbproxy_vpc_instance_id = dbproxy_vpc_instance_id
        # The vSwitch of the database proxy.
        self.dbproxy_vswitch_id = dbproxy_vswitch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbproxy_connect_string is not None:
            result['DBProxyConnectString'] = self.dbproxy_connect_string

        if self.dbproxy_connect_string_net_type is not None:
            result['DBProxyConnectStringNetType'] = self.dbproxy_connect_string_net_type

        if self.dbproxy_connect_string_net_work_type is not None:
            result['DBProxyConnectStringNetWorkType'] = self.dbproxy_connect_string_net_work_type

        if self.dbproxy_connect_string_port is not None:
            result['DBProxyConnectStringPort'] = self.dbproxy_connect_string_port

        if self.dbproxy_endpoint_id is not None:
            result['DBProxyEndpointId'] = self.dbproxy_endpoint_id

        if self.dbproxy_endpoint_name is not None:
            result['DBProxyEndpointName'] = self.dbproxy_endpoint_name

        if self.dbproxy_vpc_id is not None:
            result['DBProxyVpcId'] = self.dbproxy_vpc_id

        if self.dbproxy_vpc_instance_id is not None:
            result['DBProxyVpcInstanceId'] = self.dbproxy_vpc_instance_id

        if self.dbproxy_vswitch_id is not None:
            result['DBProxyVswitchId'] = self.dbproxy_vswitch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBProxyConnectString') is not None:
            self.dbproxy_connect_string = m.get('DBProxyConnectString')

        if m.get('DBProxyConnectStringNetType') is not None:
            self.dbproxy_connect_string_net_type = m.get('DBProxyConnectStringNetType')

        if m.get('DBProxyConnectStringNetWorkType') is not None:
            self.dbproxy_connect_string_net_work_type = m.get('DBProxyConnectStringNetWorkType')

        if m.get('DBProxyConnectStringPort') is not None:
            self.dbproxy_connect_string_port = m.get('DBProxyConnectStringPort')

        if m.get('DBProxyEndpointId') is not None:
            self.dbproxy_endpoint_id = m.get('DBProxyEndpointId')

        if m.get('DBProxyEndpointName') is not None:
            self.dbproxy_endpoint_name = m.get('DBProxyEndpointName')

        if m.get('DBProxyVpcId') is not None:
            self.dbproxy_vpc_id = m.get('DBProxyVpcId')

        if m.get('DBProxyVpcInstanceId') is not None:
            self.dbproxy_vpc_instance_id = m.get('DBProxyVpcInstanceId')

        if m.get('DBProxyVswitchId') is not None:
            self.dbproxy_vswitch_id = m.get('DBProxyVswitchId')

        return self

class DescribeDBProxyResponseBodyDBProxyAVZones(DaraModel):
    def __init__(
        self,
        dbproxy_avzones: List[str] = None,
    ):
        self.dbproxy_avzones = dbproxy_avzones

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbproxy_avzones is not None:
            result['DBProxyAVZones'] = self.dbproxy_avzones

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBProxyAVZones') is not None:
            self.dbproxy_avzones = m.get('DBProxyAVZones')

        return self

