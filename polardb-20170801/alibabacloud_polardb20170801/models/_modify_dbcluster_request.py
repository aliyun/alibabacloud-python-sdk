# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBClusterRequest(DaraModel):
    def __init__(
        self,
        compress_storage: str = None,
        connection_resource_quota: int = None,
        dbcluster_id: str = None,
        dbnode_crash_list: str = None,
        data_sync_mode: str = None,
        fault_injection_type: str = None,
        fault_simulate_mode: str = None,
        imci_auto_index: str = None,
        modify_row_compression: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        standby_hamode: str = None,
        storage_auto_scale: str = None,
        storage_upper_bound: int = None,
        table_meta: str = None,
    ):
        # Enables storage compression. Set the value to **ON**.
        self.compress_storage = compress_storage
        self.connection_resource_quota = connection_resource_quota
        # The cluster ID.
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/173433.html) operation to query information about all clusters in the specified region, including cluster IDs.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The list of node instance names for the disaster recovery drill.
        # > Node-level drills support only a single node. For zone-level drills, you can leave this parameter empty or specify all nodes.
        self.dbnode_crash_list = dbnode_crash_list
        # The cross-zone data replication mode of the cluster. Valid values:
        # 
        # - **AsyncSync**: asynchronous
        # - **SemiSync**: semi-synchronous
        self.data_sync_mode = data_sync_mode
        # The fault injection method. Valid values:
        # 
        # - 0: instance fault injection based on `Crash SQL`
        self.fault_injection_type = fault_injection_type
        # The dimension of the disaster recovery drill for the cluster. Valid values:
        # - `0` or `FaultInjection`: primary zone-level disaster recovery drill.
        # - `1`: node-level disaster recovery drill.
        # > - In the **primary zone-level disaster recovery drill** scenario, all compute nodes in the primary zone become unavailable. The failover in this scenario causes service interruptions.
        # > - In the **node-level disaster recovery drill** scenario, only a single compute node is supported for the drill. Specify the desired compute node name by using `DBNodeCrashList`.
        self.fault_simulate_mode = fault_simulate_mode
        # The automatic IMCI-based query acceleration feature. Valid values:
        # - `ON`: enabled.
        # - `OFF`: disabled.
        # 
        # > - Only PolarDB for MySQL clusters are supported.
        # > - For cluster version requirements, see [Automatic acceleration (AutoIndex)](https://help.aliyun.com/document_detail/2854119.html).
        self.imci_auto_index = imci_auto_index
        # Modifies the row compression settings.
        self.modify_row_compression = modify_row_compression
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The cross-zone automatic switchover mode of the cluster. Valid values:
        # 
        # - **ON**: enables cross-zone automatic switchover.
        # - **OFF**: disables cross-zone automatic switchover.
        self.standby_hamode = standby_hamode
        # Specifies whether to enable automatic storage scaling for the Standard Edition cluster. Valid values:
        # 
        # - Enable: enables automatic storage scaling.
        # - Disable: disables automatic storage scaling.
        self.storage_auto_scale = storage_auto_scale
        # The upper limit for automatic storage scaling of the Standard Edition cluster. Unit: GB.
        # 
        # > The maximum value is 32000.
        self.storage_upper_bound = storage_upper_bound
        # The JSON string that contains the information about the databases and tables to be restored. The values of the database and table information are strings.
        # Example: `[
        #    {
        #        "tables":[
        #            {
        #                "name":"testtb",
        #                "type":"table",
        #                "newname":"testtb_restore"
        #            }
        #        ],
        #        "name":"testdb",
        #        "type":"db",
        #        "newname":"testdb_restore"
        #    }
        # ]`.
        # > You can call the [DescribeMetaList](https://help.aliyun.com/document_detail/194770.html) operation to query the names of databases and tables that can be restored, and then specify the information in the corresponding fields in the preceding example.
        self.table_meta = table_meta

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compress_storage is not None:
            result['CompressStorage'] = self.compress_storage

        if self.connection_resource_quota is not None:
            result['ConnectionResourceQuota'] = self.connection_resource_quota

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbnode_crash_list is not None:
            result['DBNodeCrashList'] = self.dbnode_crash_list

        if self.data_sync_mode is not None:
            result['DataSyncMode'] = self.data_sync_mode

        if self.fault_injection_type is not None:
            result['FaultInjectionType'] = self.fault_injection_type

        if self.fault_simulate_mode is not None:
            result['FaultSimulateMode'] = self.fault_simulate_mode

        if self.imci_auto_index is not None:
            result['ImciAutoIndex'] = self.imci_auto_index

        if self.modify_row_compression is not None:
            result['ModifyRowCompression'] = self.modify_row_compression

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.standby_hamode is not None:
            result['StandbyHAMode'] = self.standby_hamode

        if self.storage_auto_scale is not None:
            result['StorageAutoScale'] = self.storage_auto_scale

        if self.storage_upper_bound is not None:
            result['StorageUpperBound'] = self.storage_upper_bound

        if self.table_meta is not None:
            result['TableMeta'] = self.table_meta

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompressStorage') is not None:
            self.compress_storage = m.get('CompressStorage')

        if m.get('ConnectionResourceQuota') is not None:
            self.connection_resource_quota = m.get('ConnectionResourceQuota')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBNodeCrashList') is not None:
            self.dbnode_crash_list = m.get('DBNodeCrashList')

        if m.get('DataSyncMode') is not None:
            self.data_sync_mode = m.get('DataSyncMode')

        if m.get('FaultInjectionType') is not None:
            self.fault_injection_type = m.get('FaultInjectionType')

        if m.get('FaultSimulateMode') is not None:
            self.fault_simulate_mode = m.get('FaultSimulateMode')

        if m.get('ImciAutoIndex') is not None:
            self.imci_auto_index = m.get('ImciAutoIndex')

        if m.get('ModifyRowCompression') is not None:
            self.modify_row_compression = m.get('ModifyRowCompression')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('StandbyHAMode') is not None:
            self.standby_hamode = m.get('StandbyHAMode')

        if m.get('StorageAutoScale') is not None:
            self.storage_auto_scale = m.get('StorageAutoScale')

        if m.get('StorageUpperBound') is not None:
            self.storage_upper_bound = m.get('StorageUpperBound')

        if m.get('TableMeta') is not None:
            self.table_meta = m.get('TableMeta')

        return self

