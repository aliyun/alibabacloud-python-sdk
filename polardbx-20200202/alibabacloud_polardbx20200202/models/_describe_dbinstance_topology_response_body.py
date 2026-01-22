# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstanceTopologyResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeDBInstanceTopologyResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeDBInstanceTopologyResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDBInstanceTopologyResponseBodyData(DaraModel):
    def __init__(
        self,
        logic_instance_topology: main_models.DescribeDBInstanceTopologyResponseBodyDataLogicInstanceTopology = None,
    ):
        self.logic_instance_topology = logic_instance_topology

    def validate(self):
        if self.logic_instance_topology:
            self.logic_instance_topology.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.logic_instance_topology is not None:
            result['LogicInstanceTopology'] = self.logic_instance_topology.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogicInstanceTopology') is not None:
            temp_model = main_models.DescribeDBInstanceTopologyResponseBodyDataLogicInstanceTopology()
            self.logic_instance_topology = temp_model.from_map(m.get('LogicInstanceTopology'))

        return self

class DescribeDBInstanceTopologyResponseBodyDataLogicInstanceTopology(DaraModel):
    def __init__(
        self,
        dbinstance_conn_type: str = None,
        dbinstance_create_time: str = None,
        dbinstance_description: str = None,
        dbinstance_id: str = None,
        dbinstance_name: str = None,
        dbinstance_status: int = None,
        dbinstance_status_description: str = None,
        dbinstance_storage: int = None,
        engine: str = None,
        engine_version: str = None,
        history_items: List[main_models.DescribeDBInstanceTopologyResponseBodyDataLogicInstanceTopologyHistoryItems] = None,
        items: List[main_models.DescribeDBInstanceTopologyResponseBodyDataLogicInstanceTopologyItems] = None,
        lock_mode: int = None,
        lock_reason: str = None,
        maintain_end_time: str = None,
        maintain_start_time: str = None,
    ):
        self.dbinstance_conn_type = dbinstance_conn_type
        self.dbinstance_create_time = dbinstance_create_time
        self.dbinstance_description = dbinstance_description
        self.dbinstance_id = dbinstance_id
        self.dbinstance_name = dbinstance_name
        self.dbinstance_status = dbinstance_status
        self.dbinstance_status_description = dbinstance_status_description
        self.dbinstance_storage = dbinstance_storage
        self.engine = engine
        self.engine_version = engine_version
        self.history_items = history_items
        self.items = items
        self.lock_mode = lock_mode
        self.lock_reason = lock_reason
        self.maintain_end_time = maintain_end_time
        self.maintain_start_time = maintain_start_time

    def validate(self):
        if self.history_items:
            for v1 in self.history_items:
                 if v1:
                    v1.validate()
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_conn_type is not None:
            result['DBInstanceConnType'] = self.dbinstance_conn_type

        if self.dbinstance_create_time is not None:
            result['DBInstanceCreateTime'] = self.dbinstance_create_time

        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.dbinstance_status is not None:
            result['DBInstanceStatus'] = self.dbinstance_status

        if self.dbinstance_status_description is not None:
            result['DBInstanceStatusDescription'] = self.dbinstance_status_description

        if self.dbinstance_storage is not None:
            result['DBInstanceStorage'] = self.dbinstance_storage

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        result['HistoryItems'] = []
        if self.history_items is not None:
            for k1 in self.history_items:
                result['HistoryItems'].append(k1.to_map() if k1 else None)

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode

        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason

        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time

        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceConnType') is not None:
            self.dbinstance_conn_type = m.get('DBInstanceConnType')

        if m.get('DBInstanceCreateTime') is not None:
            self.dbinstance_create_time = m.get('DBInstanceCreateTime')

        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('DBInstanceStatus') is not None:
            self.dbinstance_status = m.get('DBInstanceStatus')

        if m.get('DBInstanceStatusDescription') is not None:
            self.dbinstance_status_description = m.get('DBInstanceStatusDescription')

        if m.get('DBInstanceStorage') is not None:
            self.dbinstance_storage = m.get('DBInstanceStorage')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        self.history_items = []
        if m.get('HistoryItems') is not None:
            for k1 in m.get('HistoryItems'):
                temp_model = main_models.DescribeDBInstanceTopologyResponseBodyDataLogicInstanceTopologyHistoryItems()
                self.history_items.append(temp_model.from_map(k1))

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeDBInstanceTopologyResponseBodyDataLogicInstanceTopologyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')

        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')

        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')

        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')

        return self

class DescribeDBInstanceTopologyResponseBodyDataLogicInstanceTopologyItems(DaraModel):
    def __init__(
        self,
        activated: bool = None,
        azone: str = None,
        azone_role_list: List[main_models.DescribeDBInstanceTopologyResponseBodyDataLogicInstanceTopologyItemsAzoneRoleList] = None,
        character_type: str = None,
        connection_ip: List[main_models.DescribeDBInstanceTopologyResponseBodyDataLogicInstanceTopologyItemsConnectionIp] = None,
        dbinstance_conn_type: int = None,
        dbinstance_create_time: str = None,
        dbinstance_description: str = None,
        dbinstance_id: str = None,
        dbinstance_name: str = None,
        dbinstance_status: int = None,
        dbinstance_status_description: str = None,
        disk_size: int = None,
        engine: str = None,
        engine_version: str = None,
        lock_mode: int = None,
        lock_reason: str = None,
        maintain_end_time: str = None,
        maintain_start_time: str = None,
        max_connections: int = None,
        max_iops: int = None,
        node_class: str = None,
        phy_instance_name: str = None,
        region: str = None,
        role: str = None,
        status: str = None,
        storage_used: str = None,
        version: str = None,
    ):
        self.activated = activated
        self.azone = azone
        self.azone_role_list = azone_role_list
        self.character_type = character_type
        self.connection_ip = connection_ip
        self.dbinstance_conn_type = dbinstance_conn_type
        self.dbinstance_create_time = dbinstance_create_time
        self.dbinstance_description = dbinstance_description
        self.dbinstance_id = dbinstance_id
        self.dbinstance_name = dbinstance_name
        self.dbinstance_status = dbinstance_status
        self.dbinstance_status_description = dbinstance_status_description
        self.disk_size = disk_size
        self.engine = engine
        self.engine_version = engine_version
        self.lock_mode = lock_mode
        self.lock_reason = lock_reason
        self.maintain_end_time = maintain_end_time
        self.maintain_start_time = maintain_start_time
        self.max_connections = max_connections
        self.max_iops = max_iops
        self.node_class = node_class
        self.phy_instance_name = phy_instance_name
        self.region = region
        self.role = role
        self.status = status
        self.storage_used = storage_used
        self.version = version

    def validate(self):
        if self.azone_role_list:
            for v1 in self.azone_role_list:
                 if v1:
                    v1.validate()
        if self.connection_ip:
            for v1 in self.connection_ip:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activated is not None:
            result['Activated'] = self.activated

        if self.azone is not None:
            result['Azone'] = self.azone

        result['AzoneRoleList'] = []
        if self.azone_role_list is not None:
            for k1 in self.azone_role_list:
                result['AzoneRoleList'].append(k1.to_map() if k1 else None)

        if self.character_type is not None:
            result['CharacterType'] = self.character_type

        result['ConnectionIp'] = []
        if self.connection_ip is not None:
            for k1 in self.connection_ip:
                result['ConnectionIp'].append(k1.to_map() if k1 else None)

        if self.dbinstance_conn_type is not None:
            result['DBInstanceConnType'] = self.dbinstance_conn_type

        if self.dbinstance_create_time is not None:
            result['DBInstanceCreateTime'] = self.dbinstance_create_time

        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.dbinstance_status is not None:
            result['DBInstanceStatus'] = self.dbinstance_status

        if self.dbinstance_status_description is not None:
            result['DBInstanceStatusDescription'] = self.dbinstance_status_description

        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode

        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason

        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time

        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time

        if self.max_connections is not None:
            result['MaxConnections'] = self.max_connections

        if self.max_iops is not None:
            result['MaxIops'] = self.max_iops

        if self.node_class is not None:
            result['NodeClass'] = self.node_class

        if self.phy_instance_name is not None:
            result['PhyInstanceName'] = self.phy_instance_name

        if self.region is not None:
            result['Region'] = self.region

        if self.role is not None:
            result['Role'] = self.role

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_used is not None:
            result['StorageUsed'] = self.storage_used

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Activated') is not None:
            self.activated = m.get('Activated')

        if m.get('Azone') is not None:
            self.azone = m.get('Azone')

        self.azone_role_list = []
        if m.get('AzoneRoleList') is not None:
            for k1 in m.get('AzoneRoleList'):
                temp_model = main_models.DescribeDBInstanceTopologyResponseBodyDataLogicInstanceTopologyItemsAzoneRoleList()
                self.azone_role_list.append(temp_model.from_map(k1))

        if m.get('CharacterType') is not None:
            self.character_type = m.get('CharacterType')

        self.connection_ip = []
        if m.get('ConnectionIp') is not None:
            for k1 in m.get('ConnectionIp'):
                temp_model = main_models.DescribeDBInstanceTopologyResponseBodyDataLogicInstanceTopologyItemsConnectionIp()
                self.connection_ip.append(temp_model.from_map(k1))

        if m.get('DBInstanceConnType') is not None:
            self.dbinstance_conn_type = m.get('DBInstanceConnType')

        if m.get('DBInstanceCreateTime') is not None:
            self.dbinstance_create_time = m.get('DBInstanceCreateTime')

        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('DBInstanceStatus') is not None:
            self.dbinstance_status = m.get('DBInstanceStatus')

        if m.get('DBInstanceStatusDescription') is not None:
            self.dbinstance_status_description = m.get('DBInstanceStatusDescription')

        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')

        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')

        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')

        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')

        if m.get('MaxConnections') is not None:
            self.max_connections = m.get('MaxConnections')

        if m.get('MaxIops') is not None:
            self.max_iops = m.get('MaxIops')

        if m.get('NodeClass') is not None:
            self.node_class = m.get('NodeClass')

        if m.get('PhyInstanceName') is not None:
            self.phy_instance_name = m.get('PhyInstanceName')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageUsed') is not None:
            self.storage_used = m.get('StorageUsed')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class DescribeDBInstanceTopologyResponseBodyDataLogicInstanceTopologyItemsConnectionIp(DaraModel):
    def __init__(
        self,
        connection_string: str = None,
        dbinstance_net_type: int = None,
        port: str = None,
    ):
        self.connection_string = connection_string
        self.dbinstance_net_type = dbinstance_net_type
        self.port = port

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

        if self.port is not None:
            result['Port'] = self.port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('DBInstanceNetType') is not None:
            self.dbinstance_net_type = m.get('DBInstanceNetType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        return self

class DescribeDBInstanceTopologyResponseBodyDataLogicInstanceTopologyItemsAzoneRoleList(DaraModel):
    def __init__(
        self,
        azone: str = None,
        role: str = None,
    ):
        self.azone = azone
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.azone is not None:
            result['Azone'] = self.azone

        if self.role is not None:
            result['Role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Azone') is not None:
            self.azone = m.get('Azone')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        return self

class DescribeDBInstanceTopologyResponseBodyDataLogicInstanceTopologyHistoryItems(DaraModel):
    def __init__(
        self,
        activated: bool = None,
        azone: str = None,
        character_type: str = None,
        dbinstance_id: str = None,
        dbinstance_name: str = None,
        phy_instance_name: str = None,
        region: str = None,
        role: str = None,
    ):
        self.activated = activated
        self.azone = azone
        self.character_type = character_type
        self.dbinstance_id = dbinstance_id
        self.dbinstance_name = dbinstance_name
        self.phy_instance_name = phy_instance_name
        self.region = region
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activated is not None:
            result['Activated'] = self.activated

        if self.azone is not None:
            result['Azone'] = self.azone

        if self.character_type is not None:
            result['CharacterType'] = self.character_type

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.phy_instance_name is not None:
            result['PhyInstanceName'] = self.phy_instance_name

        if self.region is not None:
            result['Region'] = self.region

        if self.role is not None:
            result['Role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Activated') is not None:
            self.activated = m.get('Activated')

        if m.get('Azone') is not None:
            self.azone = m.get('Azone')

        if m.get('CharacterType') is not None:
            self.character_type = m.get('CharacterType')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('PhyInstanceName') is not None:
            self.phy_instance_name = m.get('PhyInstanceName')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        return self

