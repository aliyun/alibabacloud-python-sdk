# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class GetDBInstanceTopologyResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetDBInstanceTopologyResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # An internal parameter. You can ignore this parameter.
        self.code = code
        # The details about the topology.
        self.data = data
        # An internal parameter. You can ignore this parameter.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetDBInstanceTopologyResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetDBInstanceTopologyResponseBodyData(DaraModel):
    def __init__(
        self,
        connections: List[main_models.GetDBInstanceTopologyResponseBodyDataConnections] = None,
        dbinstance_name: str = None,
        nodes: List[main_models.GetDBInstanceTopologyResponseBodyDataNodes] = None,
    ):
        # The network connection information of the instance.
        self.connections = connections
        # The instance ID.
        self.dbinstance_name = dbinstance_name
        # The queried nodes.
        self.nodes = nodes

    def validate(self):
        if self.connections:
            for v1 in self.connections:
                 if v1:
                    v1.validate()
        if self.nodes:
            for v1 in self.nodes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Connections'] = []
        if self.connections is not None:
            for k1 in self.connections:
                result['Connections'].append(k1.to_map() if k1 else None)

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        result['Nodes'] = []
        if self.nodes is not None:
            for k1 in self.nodes:
                result['Nodes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.connections = []
        if m.get('Connections') is not None:
            for k1 in m.get('Connections'):
                temp_model = main_models.GetDBInstanceTopologyResponseBodyDataConnections()
                self.connections.append(temp_model.from_map(k1))

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        self.nodes = []
        if m.get('Nodes') is not None:
            for k1 in m.get('Nodes'):
                temp_model = main_models.GetDBInstanceTopologyResponseBodyDataNodes()
                self.nodes.append(temp_model.from_map(k1))

        return self

class GetDBInstanceTopologyResponseBodyDataNodes(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        dedicated_host_group_id: str = None,
        dedicated_host_id: str = None,
        node_id: str = None,
        role: str = None,
        zone_id: str = None,
    ):
        # The ID of the instance.
        self.dbinstance_name = dbinstance_name
        # The ID of the dedicated cluster.
        # 
        # > : If the instance does not reside in the specified dedicated cluster, no value is returned.
        self.dedicated_host_group_id = dedicated_host_group_id
        # The host ID of the instance in the dedicated cluster.
        # 
        # > : If the instance does not reside in the specified dedicated cluster, no value is returned.
        self.dedicated_host_id = dedicated_host_id
        # The ID of the instance.
        # 
        # > : The value \\*\\*-1\\*\\* is returned for an instance that does not reside in a dedicated cluster.
        self.node_id = node_id
        # The type of the node. The following result is returned:
        # 
        # *   **Master**: a primary node
        # *   **Slave**: a secondary node
        self.role = role
        # The zone ID of the instance.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id

        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.role is not None:
            result['Role'] = self.role

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')

        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class GetDBInstanceTopologyResponseBodyDataConnections(DaraModel):
    def __init__(
        self,
        connection_string: str = None,
        dbinstance_name: str = None,
        net_type: str = None,
        zone_id: str = None,
    ):
        # The endpoint that is used to connect to the database instance.
        self.connection_string = connection_string
        # The instance ID.
        self.dbinstance_name = dbinstance_name
        # The network type of the endpoint. Valid values:
        # 
        # *   **vpc**
        # *   **public**
        self.net_type = net_type
        # The zone ID of the instance.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.net_type is not None:
            result['NetType'] = self.net_type

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

