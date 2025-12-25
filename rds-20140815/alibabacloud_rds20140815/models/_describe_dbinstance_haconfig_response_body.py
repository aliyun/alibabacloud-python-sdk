# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstanceHAConfigResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        hamode: str = None,
        host_instance_infos: main_models.DescribeDBInstanceHAConfigResponseBodyHostInstanceInfos = None,
        request_id: str = None,
        sync_mode: str = None,
    ):
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The high availability mode of the instance. Valid values:
        # 
        # *   **RPO**: Data consistency is preferred. The instance ensures data reliability to minimize data losses. If you have high requirements on data consistency, select this mode.
        # *   **RTO**: Service availability is preferred. The instance restores the database service at the earliest opportunity to ensure service availability. If you have high requirements on instance availability, select this mode.
        # 
        # > This parameter is returned only for instances that run MySQL.
        self.hamode = hamode
        # An array that consists of the information of the primary and secondary instances.
        self.host_instance_infos = host_instance_infos
        # The request ID.
        self.request_id = request_id
        # The data replication mode of the instance. Valid values:
        # 
        # *   **Sync**: the synchronous mode
        # *   **Semi-sync**: the semi-synchronous replication mode
        # *   **Async**: the asynchronous mode
        # 
        # > This parameter is returned only for instances that run MySQL.
        self.sync_mode = sync_mode

    def validate(self):
        if self.host_instance_infos:
            self.host_instance_infos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.hamode is not None:
            result['HAMode'] = self.hamode

        if self.host_instance_infos is not None:
            result['HostInstanceInfos'] = self.host_instance_infos.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sync_mode is not None:
            result['SyncMode'] = self.sync_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('HAMode') is not None:
            self.hamode = m.get('HAMode')

        if m.get('HostInstanceInfos') is not None:
            temp_model = main_models.DescribeDBInstanceHAConfigResponseBodyHostInstanceInfos()
            self.host_instance_infos = temp_model.from_map(m.get('HostInstanceInfos'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SyncMode') is not None:
            self.sync_mode = m.get('SyncMode')

        return self

class DescribeDBInstanceHAConfigResponseBodyHostInstanceInfos(DaraModel):
    def __init__(
        self,
        node_info: List[main_models.DescribeDBInstanceHAConfigResponseBodyHostInstanceInfosNodeInfo] = None,
    ):
        self.node_info = node_info

    def validate(self):
        if self.node_info:
            for v1 in self.node_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NodeInfo'] = []
        if self.node_info is not None:
            for k1 in self.node_info:
                result['NodeInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node_info = []
        if m.get('NodeInfo') is not None:
            for k1 in m.get('NodeInfo'):
                temp_model = main_models.DescribeDBInstanceHAConfigResponseBodyHostInstanceInfosNodeInfo()
                self.node_info.append(temp_model.from_map(k1))

        return self

class DescribeDBInstanceHAConfigResponseBodyHostInstanceInfosNodeInfo(DaraModel):
    def __init__(
        self,
        data_sync_time: str = None,
        log_sync_time: str = None,
        node_id: str = None,
        node_type: str = None,
        region_id: str = None,
        sync_status: str = None,
        zone_id: str = None,
    ):
        # The time when the secondary instance completed the synchronization of data from the primary instance. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.data_sync_time = data_sync_time
        # The time when the secondary instance received logs from the primary instance. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.log_sync_time = log_sync_time
        # The ID of the instance.
        self.node_id = node_id
        # The type of the node. Valid values:
        # 
        # *   **Master**: the primary node
        # *   **Slave**: the secondary node
        self.node_type = node_type
        # The region ID of the instance.
        self.region_id = region_id
        # The synchronization status. Valid values:
        # 
        # *   **NotAvailable**: The synchronization fails. This means that faults occur.
        # *   **Syncing**: The synchronization is in process. In this case, a primary/secondary switchover may cause data losses.
        # *   **Synchronized**: The synchronization is completed.
        # *   **NotSupport**: The database engine or database engine version does not involve the synchronization between the primary and secondary instances.
        self.sync_status = sync_status
        # The ID of the zone.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_sync_time is not None:
            result['DataSyncTime'] = self.data_sync_time

        if self.log_sync_time is not None:
            result['LogSyncTime'] = self.log_sync_time

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sync_status is not None:
            result['SyncStatus'] = self.sync_status

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSyncTime') is not None:
            self.data_sync_time = m.get('DataSyncTime')

        if m.get('LogSyncTime') is not None:
            self.log_sync_time = m.get('LogSyncTime')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SyncStatus') is not None:
            self.sync_status = m.get('SyncStatus')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

