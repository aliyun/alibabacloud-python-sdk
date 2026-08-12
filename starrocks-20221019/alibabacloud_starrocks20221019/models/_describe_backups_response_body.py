# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_starrocks20221019 import models as main_models
from darabonba.model import DaraModel

class DescribeBackupsResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeBackupsResponseBodyData] = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        # The returned data.
        self.data = data
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP request status code.
        self.http_status_code = http_status_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success
        # The total number of query results.
        self.total = total

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeBackupsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeBackupsResponseBodyData(DaraModel):
    def __init__(
        self,
        backup_finished_time: int = None,
        backup_start_time: int = None,
        backup_task_id: str = None,
        backup_type: str = None,
        description: str = None,
        expire_time: int = None,
        instance_id: str = None,
        instance_snapshot: main_models.DescribeBackupsResponseBodyDataInstanceSnapshot = None,
        region_id: str = None,
        size: int = None,
        status: str = None,
        sub_tasks: List[main_models.DescribeBackupsResponseBodyDataSubTasks] = None,
    ):
        # The end time of this backup.
        self.backup_finished_time = backup_finished_time
        # The start time of this backup.
        self.backup_start_time = backup_start_time
        # The backup task ID.
        self.backup_task_id = backup_task_id
        # The backup type:
        # 
        # - **0**: Fast backup.
        # 
        # - **1**: Consistent backup.
        self.backup_type = backup_type
        # The task description.
        self.description = description
        # The expiration time of the backup data.
        self.expire_time = expire_time
        # The instance ID.
        self.instance_id = instance_id
        # The backup instance information.
        self.instance_snapshot = instance_snapshot
        # The region ID.
        self.region_id = region_id
        # The cloud disk size in GiB.
        self.size = size
        # The backup job status.
        self.status = status
        # The list of backup subtasks.
        self.sub_tasks = sub_tasks

    def validate(self):
        if self.instance_snapshot:
            self.instance_snapshot.validate()
        if self.sub_tasks:
            for v1 in self.sub_tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_finished_time is not None:
            result['BackupFinishedTime'] = self.backup_finished_time

        if self.backup_start_time is not None:
            result['BackupStartTime'] = self.backup_start_time

        if self.backup_task_id is not None:
            result['BackupTaskId'] = self.backup_task_id

        if self.backup_type is not None:
            result['BackupType'] = self.backup_type

        if self.description is not None:
            result['Description'] = self.description

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_snapshot is not None:
            result['InstanceSnapshot'] = self.instance_snapshot.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.size is not None:
            result['Size'] = self.size

        if self.status is not None:
            result['Status'] = self.status

        result['SubTasks'] = []
        if self.sub_tasks is not None:
            for k1 in self.sub_tasks:
                result['SubTasks'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupFinishedTime') is not None:
            self.backup_finished_time = m.get('BackupFinishedTime')

        if m.get('BackupStartTime') is not None:
            self.backup_start_time = m.get('BackupStartTime')

        if m.get('BackupTaskId') is not None:
            self.backup_task_id = m.get('BackupTaskId')

        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceSnapshot') is not None:
            temp_model = main_models.DescribeBackupsResponseBodyDataInstanceSnapshot()
            self.instance_snapshot = temp_model.from_map(m.get('InstanceSnapshot'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.sub_tasks = []
        if m.get('SubTasks') is not None:
            for k1 in m.get('SubTasks'):
                temp_model = main_models.DescribeBackupsResponseBodyDataSubTasks()
                self.sub_tasks.append(temp_model.from_map(k1))

        return self

class DescribeBackupsResponseBodyDataSubTasks(DaraModel):
    def __init__(
        self,
        data_base: str = None,
        detail: str = None,
        finished_time: int = None,
        size: int = None,
        snapshot_name: str = None,
        start_time: int = None,
        status: str = None,
        table: str = None,
    ):
        # The database name.
        self.data_base = data_base
        # The snapshot ID.
        self.detail = detail
        # The task end time.
        self.finished_time = finished_time
        # The data size in GiB.
        self.size = size
        # The snapshot name.
        self.snapshot_name = snapshot_name
        # The task start date.
        self.start_time = start_time
        # The backup job status.
        self.status = status
        # The data table name.
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_base is not None:
            result['DataBase'] = self.data_base

        if self.detail is not None:
            result['Detail'] = self.detail

        if self.finished_time is not None:
            result['FinishedTime'] = self.finished_time

        if self.size is not None:
            result['Size'] = self.size

        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.table is not None:
            result['Table'] = self.table

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataBase') is not None:
            self.data_base = m.get('DataBase')

        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('FinishedTime') is not None:
            self.finished_time = m.get('FinishedTime')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Table') is not None:
            self.table = m.get('Table')

        return self

class DescribeBackupsResponseBodyDataInstanceSnapshot(DaraModel):
    def __init__(
        self,
        instance_name: str = None,
        minor_version: str = None,
        node_groups: List[main_models.DescribeBackupsResponseBodyDataInstanceSnapshotNodeGroups] = None,
        region_id: str = None,
        resource_group_id: str = None,
        run_mode: str = None,
        spec_type: str = None,
        tags: List[main_models.DescribeBackupsResponseBodyDataInstanceSnapshotTags] = None,
        version: str = None,
        vpc_id: str = None,
    ):
        # The instance name.
        self.instance_name = instance_name
        # The minor version number.
        self.minor_version = minor_version
        # The compute group information.
        self.node_groups = node_groups
        # The region ID of the instance.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The cluster\\"s running mode:
        # 
        # - Shared-nothing.
        # 
        # - Shared-data.
        self.run_mode = run_mode
        # The compute group specification type. Includes the following types:
        # 
        # - standard: Standard Edition.
        # 
        # - localSSD: Local SSD.
        # 
        # - bigData: Large-capacity storage.
        # 
        # - ramEnhanced: Memory-enhanced instance family.
        # 
        # - networkEnhanced: Network-enhanced.
        self.spec_type = spec_type
        # The tag information.
        self.tags = tags
        # The cluster version.
        self.version = version
        # The VPC ID.
        self.vpc_id = vpc_id

    def validate(self):
        if self.node_groups:
            for v1 in self.node_groups:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version

        result['NodeGroups'] = []
        if self.node_groups is not None:
            for k1 in self.node_groups:
                result['NodeGroups'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.run_mode is not None:
            result['RunMode'] = self.run_mode

        if self.spec_type is not None:
            result['SpecType'] = self.spec_type

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.version is not None:
            result['Version'] = self.version

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')

        self.node_groups = []
        if m.get('NodeGroups') is not None:
            for k1 in m.get('NodeGroups'):
                temp_model = main_models.DescribeBackupsResponseBodyDataInstanceSnapshotNodeGroups()
                self.node_groups.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RunMode') is not None:
            self.run_mode = m.get('RunMode')

        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeBackupsResponseBodyDataInstanceSnapshotTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeBackupsResponseBodyDataInstanceSnapshotTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeBackupsResponseBodyDataInstanceSnapshotNodeGroups(DaraModel):
    def __init__(
        self,
        component_type: str = None,
        cu: int = None,
        disk_number: str = None,
        local_storage_instance_type: str = None,
        resident_node_number: str = None,
        spec_type: str = None,
        storage_performance_level: str = None,
        storage_size: int = None,
    ):
        # The compute group type. Includes the following values:
        # 
        # - FE
        # 
        # - BE
        # 
        # - CN
        # 
        # - OBSERVER
        # 
        # - AGENT
        self.component_type = component_type
        # The number of CUs. A CU (Compute Unit) is the basic unit of measurement for the service. 1 CU equals 1 CPU core + 4 GiB memory. If SpecType is memory-enhanced instance family, 1 CU equals 1 CPU core + 8 GiB memory.
        self.cu = cu
        # The number of disks.
        self.disk_number = disk_number
        # The node group\\"s local SSD instance type. This value is only meaningful for ECS instances where SpecType is local SSD or large-capacity storage.
        self.local_storage_instance_type = local_storage_instance_type
        # The number of nodes.
        self.resident_node_number = resident_node_number
        # The compute group specification type. Includes the following types:
        # 
        # - standard: Standard Edition.
        # 
        # - localSSD: Local SSD.
        # 
        # - bigData: Large-capacity storage.
        # 
        # - ramEnhanced: Memory-enhanced instance family.
        # 
        # - networkEnhanced: Network-enhanced.
        self.spec_type = spec_type
        # The performance level (PL) of the cloud disk. Includes the following values:
        # 
        # - pl0: Maximum random read/write IOPS of 10,000 per disk.
        # 
        # - pl1: Maximum random read/write IOPS of 50,000 per disk.
        # 
        # - pl2: Maximum random read/write IOPS of 100,000 per disk.
        # 
        # - pl3: Maximum random read/write IOPS of 1,000,000 per disk.
        self.storage_performance_level = storage_performance_level
        # The storage size in GiB.
        self.storage_size = storage_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_type is not None:
            result['ComponentType'] = self.component_type

        if self.cu is not None:
            result['Cu'] = self.cu

        if self.disk_number is not None:
            result['DiskNumber'] = self.disk_number

        if self.local_storage_instance_type is not None:
            result['LocalStorageInstanceType'] = self.local_storage_instance_type

        if self.resident_node_number is not None:
            result['ResidentNodeNumber'] = self.resident_node_number

        if self.spec_type is not None:
            result['SpecType'] = self.spec_type

        if self.storage_performance_level is not None:
            result['StoragePerformanceLevel'] = self.storage_performance_level

        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentType') is not None:
            self.component_type = m.get('ComponentType')

        if m.get('Cu') is not None:
            self.cu = m.get('Cu')

        if m.get('DiskNumber') is not None:
            self.disk_number = m.get('DiskNumber')

        if m.get('LocalStorageInstanceType') is not None:
            self.local_storage_instance_type = m.get('LocalStorageInstanceType')

        if m.get('ResidentNodeNumber') is not None:
            self.resident_node_number = m.get('ResidentNodeNumber')

        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')

        if m.get('StoragePerformanceLevel') is not None:
            self.storage_performance_level = m.get('StoragePerformanceLevel')

        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')

        return self

