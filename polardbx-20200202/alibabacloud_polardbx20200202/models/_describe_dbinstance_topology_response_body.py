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
        # The data struct.
        self.data = data
        # The request ID.
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
        # The topology information.
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
        # Indicates that LVS is used for load balancing.
        self.dbinstance_conn_type = dbinstance_conn_type
        # The time when the instance was created. Format: yyyy-MM-dd HH:mm:ss.
        self.dbinstance_create_time = dbinstance_create_time
        # The instance description.
        self.dbinstance_description = dbinstance_description
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The instance name.
        self.dbinstance_name = dbinstance_name
        # The instance status.
        self.dbinstance_status = dbinstance_status
        # The description of the instance status.
        self.dbinstance_status_description = dbinstance_status_description
        # The number of storage nodes.
        self.dbinstance_storage = dbinstance_storage
        # The engine type. Default value: polarx.
        self.engine = engine
        # The engine version. Default value: 2.0.
        self.engine_version = engine_version
        # The list of historical nodes.
        self.history_items = history_items
        # The list of nodes.
        self.items = items
        # The lock status. Valid values:
        # 
        # - **0**: Not locked.
        # - **1**: Locked.
        self.lock_mode = lock_mode
        # The reason why the instance is locked.
        self.lock_reason = lock_reason
        # The end time of the O&M window. Format: HH:mm:ss.
        self.maintain_end_time = maintain_end_time
        # The start time of the O&M window. Format: HH:mm:ss.
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
        instance_cluster_name: str = None,
        lock_mode: int = None,
        lock_reason: str = None,
        maintain_end_time: str = None,
        maintain_start_time: str = None,
        max_connections: int = None,
        max_iops: int = None,
        node_class: str = None,
        phy_instance_name: str = None,
        read_type: str = None,
        region: str = None,
        role: str = None,
        status: str = None,
        storage_used: str = None,
        version: str = None,
    ):
        # Indicates whether the node is activated. For the compute layer, only the node in the primary zone is activated. After a primary/secondary switchover is performed on the instance, the standby compute node becomes the primary node. All storage layer nodes are activated.
        self.activated = activated
        # The zone of the node. If the node is an RDS node, the zones of multiple child nodes are separated with a delimiter (,).
        self.azone = azone
        # The data information list of the RDS three-node cluster.
        self.azone_role_list = azone_role_list
        # The node type. Valid values:
        # 
        # - **polarx_cn**: compute node.
        # - **polarx_store**: data node.
        # - **polarx_gms**: GMS node.
        self.character_type = character_type
        # The data struct.
        self.connection_ip = connection_ip
        # The connection type.
        self.dbinstance_conn_type = dbinstance_conn_type
        # The time when the instance was created.
        self.dbinstance_create_time = dbinstance_create_time
        # The instance description.
        self.dbinstance_description = dbinstance_description
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The instance name.
        self.dbinstance_name = dbinstance_name
        # The instance status.
        self.dbinstance_status = dbinstance_status
        # The description of the instance status.
        self.dbinstance_status_description = dbinstance_status_description
        # The disk size.
        self.disk_size = disk_size
        # The engine type. Valid values:
        # 
        # - **mysql**
        # - **polarx_cdc**
        # - **polarx_dn**
        self.engine = engine
        # The engine version. Default value: 2.0.
        self.engine_version = engine_version
        self.instance_cluster_name = instance_cluster_name
        # Indicates whether the node is locked. Valid values:
        # 
        # - **0**: Not locked.
        # - **1**: Locked.
        self.lock_mode = lock_mode
        # The reason why the instance is locked.
        self.lock_reason = lock_reason
        # The end time of the O&M window.
        self.maintain_end_time = maintain_end_time
        # The start time of the O&M window.
        self.maintain_start_time = maintain_start_time
        # The maximum number of connections.
        self.max_connections = max_connections
        # The maximum IOPS.
        self.max_iops = max_iops
        # The node specifications. Valid values:
        # 
        # - **polarx.x4.medium.2e**: 2 cores, 8 GB
        # - **polarx.x4.large.2e**: 4 cores, 16 GB
        # - **polarx.x8.large.2e**: 4 cores, 32 GB
        # - **polarx.x4.xlarge.2e**: 8 cores, 32 GB
        # - **polarx.x8.xlarge.2e**: 8 cores, 64 GB
        # - **polarx.x4.2xlarge.2e**: 16 cores, 64 GB
        # - **polarx.x8.2xlarge.2e**: 16 cores, 128 GB
        # - **polarx.x4.4xlarge.2e**: 32 cores, 128 GB
        # - **polarx.x8.4xlarge.2e**: 32 cores, 256 GB
        # - **polarx.st.8xlarge.2e**: 60 cores, 470 GB
        # - **polarx.st.12xlarge.2e**: 90 cores, 720 GB.
        self.node_class = node_class
        # The physical instance name.
        self.phy_instance_name = phy_instance_name
        self.read_type = read_type
        # The region of the node. If the node is an RDS node, the regions of multiple child nodes are separated with a delimiter (,).
        self.region = region
        # The role of the node. Valid values:
        # 
        # - **master**: primary node
        # - **standby**: secondary node.
        self.role = role
        # The node status. Valid values:
        # 
        # - **0**: Running.
        # - **1**: Creating.
        # - **2**: Abnormal.
        # - **3**: Expired.
        # - **4**: Releasing.
        # - **5**: Released.
        # - **6**: Locked.
        self.status = status
        # The storage usage, in MB.
        self.storage_used = storage_used
        # The logger node version.
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

        if self.instance_cluster_name is not None:
            result['InstanceClusterName'] = self.instance_cluster_name

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

        if self.read_type is not None:
            result['ReadType'] = self.read_type

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

        if m.get('InstanceClusterName') is not None:
            self.instance_cluster_name = m.get('InstanceClusterName')

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

        if m.get('ReadType') is not None:
            self.read_type = m.get('ReadType')

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
        # The connection information.
        self.connection_string = connection_string
        # The internal connection type. The value is fixed to 1, which indicates the classic network.
        self.dbinstance_net_type = dbinstance_net_type
        # The port.
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
        # The zone of a node in the RDS three-node cluster.
        self.azone = azone
        # The role of a node in the RDS three-node cluster. Valid values:
        # 
        # - **leader**: primary node
        # - **follower**: secondary node
        # - **logger**: logger node.
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
        # Indicates whether the node is activated. For the compute layer, only the node in the primary zone is activated. After a primary/secondary switchover is performed on the instance, the standby compute node becomes the primary node. All storage layer nodes are activated.
        self.activated = activated
        # The zone of the node. If the node is an RDS node, the zones of multiple child nodes are separated with a delimiter (,).
        self.azone = azone
        # The node type. Valid values:
        # 
        # - **polarx_cn**: compute node.
        # - **polarx_store**: data node.
        # - **polarx_gms**: GMS node.
        self.character_type = character_type
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The instance name.
        self.dbinstance_name = dbinstance_name
        # The physical instance name.
        self.phy_instance_name = phy_instance_name
        # The region of the node. If the node is an RDS node, the regions of multiple child nodes are separated with a delimiter (,).
        self.region = region
        # The role of the node. Valid values:
        # 
        # - **master**: primary node
        # - **standby**: secondary node.
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

