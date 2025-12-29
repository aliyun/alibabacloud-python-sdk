# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeHistoryTasksStatRequest(DaraModel):
    def __init__(
        self,
        from_exec_time: int = None,
        from_start_time: str = None,
        instance_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        status: str = None,
        task_id: str = None,
        task_type: str = None,
        to_exec_time: int = None,
        to_start_time: str = None,
    ):
        # The minimum execution duration of the task. This parameter is used to filter tasks whose execution duration is longer than the minimum execution duration. Unit: seconds. The default value is 0, which indicates that no limit is imposed for the query.
        self.from_exec_time = from_exec_time
        # The start time of the O\\&M task to perform. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. You can query data within the last 30 days.
        # 
        # This parameter is required.
        self.from_start_time = from_start_time
        # The instance ID. Separate multiple instance IDs with commas (,). You can specify up to 30 instance IDs. This parameter is empty by default, which indicates that the tasks of all instances are queried.
        self.instance_id = instance_id
        # The region ID of the pending event. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/61933.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The task status. Valid values:
        # 
        # *   Scheduled: The task is waiting to be executed.
        # *   Running: The task is running.
        # *   Succeed: The task is successful.
        # *   Failed: The task failed.
        # *   Cancelling: The task is being terminated.
        # *   Canceled: The task has been terminated.
        # *   Waiting: The task is waiting for scheduled time.
        # 
        # Separate multiple states with commas (,). This parameter is empty by default, which indicates that tasks in all states are queried.
        self.status = status
        # The task ID. Separate multiple task IDs with commas (,). You can specify up to 30 task IDs. This parameter is empty by default, which indicates that all tasks are queried.
        self.task_id = task_id
        # The task type. This parameter is left empty by default, which indicates that all types of tasks are queried. Valid values:
        # 
        # *   CreateIns: Create an instance.
        # *   DeleteIns: Delete an instance.
        # *   ChangeVariable: Modify parameter settings for an instance.
        # *   ModifyInsConfig: Change the configurations of an instance.
        # *   RestartIns: Restart an instance.
        # *   HaSwitch: Perform a primary/secondary switchover on an instance.
        # *   CloneIns: Clone an instance.
        # *   KernelVersionUpgrade: Update the minor version of an instance.
        # *   ProxyVersionUpgrade: Upgrade the agent version of an instance.
        # *   ModifyAccount: Change the account of an instance.
        # *   ModifyInsSpec: Change the specifications of an instance or perform a data migration on the instance.
        # *   CreateReadIns: Create a read-only instance.
        # *   StartIns: Start an instance.
        # *   StopIns: Stop an instance.
        # *   ModifyNetwork: Modify the network type for an instance.
        # *   LockIns: Lock an instance.
        # *   UnlockIns: Unlock an instance.
        # *   DiskOnlineExpansion: Scale out the disks of an instance online.
        # *   StorageOnlineExpansion: Expend the storage capacity of an instance online.
        # *   AddInsNode: Add a node to an instance.
        # *   DeleteInsNode: Delete a node from an instance.
        # *   ManualBackupIns: Manually back up an instance.
        # *   ModifyInsStorageType: Modify the storage type for an instance.
        self.task_type = task_type
        # The maximum execution duration of the task. This parameter is used to filter tasks whose execution duration is shorter than or equal to the maximum execution duration. Unit: seconds. The default value is 0, which indicates that no limit is imposed for the query.
        self.to_exec_time = to_exec_time
        # The end time of the O\\&M task to perform. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. You can query data within the last 30 days.
        # 
        # This parameter is required.
        self.to_start_time = to_start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_exec_time is not None:
            result['FromExecTime'] = self.from_exec_time

        if self.from_start_time is not None:
            result['FromStartTime'] = self.from_start_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.to_exec_time is not None:
            result['ToExecTime'] = self.to_exec_time

        if self.to_start_time is not None:
            result['ToStartTime'] = self.to_start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromExecTime') is not None:
            self.from_exec_time = m.get('FromExecTime')

        if m.get('FromStartTime') is not None:
            self.from_start_time = m.get('FromStartTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('ToExecTime') is not None:
            self.to_exec_time = m.get('ToExecTime')

        if m.get('ToStartTime') is not None:
            self.to_start_time = m.get('ToStartTime')

        return self

