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
        # The connection resource quota of the AgenticDB cluster.
        self.connection_resource_quota = connection_resource_quota
        # The cluster ID.
        # > You can call the DescribeDBClusters operation to query all clusters in the specified region, including cluster IDs.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The list of drill node instance names.
        # > Node dimension drills support only a single node. For zone dimension drills, you can omit this parameter or pass all nodes.
        self.dbnode_crash_list = dbnode_crash_list
        # The cross-zone data replication mode of the cluster. Valid values:
        # 
        # - **AsyncSync**: Asynchronous.
        # - **SemiSync**: Semi-synchronous.
        self.data_sync_mode = data_sync_mode
        # The fault injection method. Valid values:
        # 
        # - 0: Instance fault injection based on `Crash SQL`.
        self.fault_injection_type = fault_injection_type
        # The fault drill dimension for the cluster. Valid values:
        # - `0` or `FaultInjection`: Primary zone dimension fault drill.
        # - `1`: Node dimension fault drill.
        # > - In the **primary zone dimension fault drill** scenario, all compute nodes in the primary zone become unavailable, and the disaster recovery switchover in this scenario is lossy.
        # > - In the **node dimension fault drill** scenario, only a single compute node can be drilled. Pass the desired compute node name through `DBNodeCrashList`.
        self.fault_simulate_mode = fault_simulate_mode
        # The automatic IMCI-based query acceleration feature. Valid values:
        # - `ON`: Enabled.
        # - `OFF`: Disabled.
        # 
        # > - Only PolarDB for MySQL clusters are supported.
        # > - For cluster version limits, refer to [Automatic IMCI-based query acceleration (AutoIndex)](https://help.aliyun.com/document_detail/2854119.html).
        self.imci_auto_index = imci_auto_index
        # Modifies the row compression settings.
        self.modify_row_compression = modify_row_compression
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The cross-zone automatic switchover mode of the cluster. Valid values:
        # 
        # - **ON**: Enables cross-zone automatic switchover.
        # - **OFF**: Disables cross-zone automatic switchover.
        self.standby_hamode = standby_hamode
        # Specifies whether to enable automatic storage scaling for a Standard Edition cluster. Valid values:
        # 
        # - Enable: Enables automatic storage scaling.
        # - Disable: Disables automatic storage scaling.
        self.storage_auto_scale = storage_auto_scale
        # The upper limit for automatic storage scaling of a Standard Edition cluster. Unit: GB.
        # 
        # > The maximum value is 32000.
        self.storage_upper_bound = storage_upper_bound
        # The JSON string of the target database and table information to be restored. The values of the database and table information are all of the string type.
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
        # > You can call the [DescribeMetaList](https://help.aliyun.com/document_detail/194770.html) operation to view the details of the database and table names that support restoration, and fill the supported database and table information into the corresponding positions in the preceding example.
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

