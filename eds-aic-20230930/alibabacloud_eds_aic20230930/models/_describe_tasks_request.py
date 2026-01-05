# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeTasksRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_name: str = None,
        invoke_id: str = None,
        level: int = None,
        max_results: int = None,
        next_token: str = None,
        param: str = None,
        parent_task_id: str = None,
        resource_ids: List[str] = None,
        task_ids: List[str] = None,
        task_status: str = None,
        task_statuses: List[str] = None,
        task_type: str = None,
        task_types: List[str] = None,
    ):
        # The ID of the cloud phone instance.
        self.instance_id = instance_id
        # The name of the cloud phone instance.
        self.instance_name = instance_name
        # The ID of the command execution. You can set the value to the last returned request ID.
        self.invoke_id = invoke_id
        # The level of the task. A value of 1 specifies a batch task. A value of 2 specifies an instance-level task.
        self.level = level
        # The maximum number of entries per page. Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. If the parameter is left empty, the data is queried from the first entry.
        self.next_token = next_token
        # The extension field.
        self.param = param
        # The ID of the parent task.
        self.parent_task_id = parent_task_id
        # The IDs of the resources.
        self.resource_ids = resource_ids
        # The IDs of the tasks.
        self.task_ids = task_ids
        # The state of the task.
        # 
        # Valid values:
        # 
        # *   PartFinished: The task is partially successful.
        # *   Finished: The task is completed.
        # *   Failed: The task failed.
        # *   Skipped: The task is skipped.
        # *   Processing: The task is running.
        # *   Waiting: The task is in queue.
        self.task_status = task_status
        # The status of the tasks.
        self.task_statuses = task_statuses
        # The type of the task.
        # 
        # Valid values:
        # 
        # *   BackupFile: backs up files.
        # *   StopInstance: stops cloud phone instances.
        # *   RebootInstance: restarts cloud phone instances.
        # *   StartApp: starts apps.
        # *   SendFile: uploads files.
        # *   RunCommand: sends remote command.
        # *   RestartApp: restarts apps.
        # *   ResetInstance: resets cloud phone instances.
        # *   RecoverFile: recovers files.
        # *   UninstallApp: uninstalls apps.
        # *   StopApp: stops apps.
        # *   Screenshot: takes screenshots.
        # *   InstallApp: installs apps.
        # *   FetchFile: downloads files.
        # *   UpdateGroupImage: replaces images.
        # *   StartInstance: starts instances.
        self.task_type = task_type
        # The types of the tasks.
        self.task_types = task_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id

        if self.level is not None:
            result['Level'] = self.level

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.param is not None:
            result['Param'] = self.param

        if self.parent_task_id is not None:
            result['ParentTaskId'] = self.parent_task_id

        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids

        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.task_statuses is not None:
            result['TaskStatuses'] = self.task_statuses

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.task_types is not None:
            result['TaskTypes'] = self.task_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Param') is not None:
            self.param = m.get('Param')

        if m.get('ParentTaskId') is not None:
            self.parent_task_id = m.get('ParentTaskId')

        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')

        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('TaskStatuses') is not None:
            self.task_statuses = m.get('TaskStatuses')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('TaskTypes') is not None:
            self.task_types = m.get('TaskTypes')

        return self

