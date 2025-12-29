# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dds20151201 import models as main_models
from darabonba.model import DaraModel

class DescribeHistoryTasksResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeHistoryTasksResponseBodyItems] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The task objects.
        self.items = items
        # The page number of the returned page.
        self.page_number = page_number
        # The maximum number of entries returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of tasks that meet these conditions without taking pagination into account.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeHistoryTasksResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeHistoryTasksResponseBodyItems(DaraModel):
    def __init__(
        self,
        action_info: str = None,
        caller_source: str = None,
        caller_uid: str = None,
        current_step_name: str = None,
        db_type: str = None,
        end_time: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_type: str = None,
        product: str = None,
        progress: float = None,
        reason_code: str = None,
        region_id: str = None,
        remain_time: int = None,
        start_time: str = None,
        status: str = None,
        task_detail: str = None,
        task_id: str = None,
        task_type: str = None,
        uid: str = None,
    ):
        # A set of allowed actions that can be taken on the task. The system matches the current step name and status of the task to the available actions specified by ActionInfo. If no matching action is found, the current status of the task does not support any action. Example:
        # 
        #        "steps": [
        #         {
        #           "step_name": "exec_task", // The name of the step, which matches the value of CurrentStepName.
        #           "action_info": {    // The actions supported for this step.
        #             "Waiting": [      // The status, which matches the value of Status.
        #               "modifySwitchTime" // The action. Multiple actions are supported.
        #             ]
        #           }
        #         },
        #         {
        #           "step_name": "init_task", // The name of the step.
        #           "action_info": {    // The actions supported for this step.
        #             "Running": [      // The status.
        #               "cancel",       // The action.
        #               "pause"
        #             ]
        #           }
        #         }
        #       ]
        #     }
        # 
        # The system may support the following actions:
        # 
        # *   retry: makes another attempt.
        # *   cancel: makes a cancellation.
        # *   modifySwitchTime: changes the switching or restoration time.
        self.action_info = action_info
        # The request source. Valid values: System and User.
        self.caller_source = caller_source
        # The ID of the user who made the request. If CallerSource is set to User, CallerUid indicates the unique ID (UID) of the user.
        self.caller_uid = caller_uid
        # The name of the current step. If this parameter is left empty, the task is not started.
        self.current_step_name = current_step_name
        # The database type. The value is fixed to mongodb.
        self.db_type = db_type
        # The end time of the performed O\\&M task. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.end_time = end_time
        # The instance ID
        self.instance_id = instance_id
        # The name of the instance.
        self.instance_name = instance_name
        # The instance type of the instance. The value is fixed to Instance.
        self.instance_type = instance_type
        # The product. The value is fixed to dds.
        self.product = product
        # The current progress of the task. The valid values range from 0 to 100.
        self.progress = progress
        # The reason why the current task was initiated.
        self.reason_code = reason_code
        # The region ID of the instance.
        self.region_id = region_id
        # The estimated remaining execution time. Unit: seconds. The value 0 indicates that the task is completed.
        self.remain_time = remain_time
        # The start time of the performed O\\&M task. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.start_time = start_time
        # The task status. Valid values:
        # 
        # *   Scheduled: The task is waiting to be executed.
        # *   Running: The task is running.
        # *   Succeed: The task is successful.
        # *   Failed: The task failed.
        # *   Cancelling: The task is being terminated.
        # *   Canceled: The task has been terminated.
        # *   Waiting: The task is waiting for scheduled time.
        self.status = status
        # The details of the task. The task details vary based on the value of the taskType parameter.
        self.task_detail = task_detail
        # The task ID.
        self.task_id = task_id
        # The task type.
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
        # The ID of the user to which the resource belongs.
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_info is not None:
            result['ActionInfo'] = self.action_info

        if self.caller_source is not None:
            result['CallerSource'] = self.caller_source

        if self.caller_uid is not None:
            result['CallerUid'] = self.caller_uid

        if self.current_step_name is not None:
            result['CurrentStepName'] = self.current_step_name

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.product is not None:
            result['Product'] = self.product

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.remain_time is not None:
            result['RemainTime'] = self.remain_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.task_detail is not None:
            result['TaskDetail'] = self.task_detail

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.uid is not None:
            result['Uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionInfo') is not None:
            self.action_info = m.get('ActionInfo')

        if m.get('CallerSource') is not None:
            self.caller_source = m.get('CallerSource')

        if m.get('CallerUid') is not None:
            self.caller_uid = m.get('CallerUid')

        if m.get('CurrentStepName') is not None:
            self.current_step_name = m.get('CurrentStepName')

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RemainTime') is not None:
            self.remain_time = m.get('RemainTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskDetail') is not None:
            self.task_detail = m.get('TaskDetail')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        return self

