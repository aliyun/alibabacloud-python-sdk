# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class NotifyExecutionRequest(DaraModel):
    def __init__(
        self,
        execution_id: str = None,
        execution_status: str = None,
        loop_item: str = None,
        notify_note: str = None,
        notify_type: str = None,
        parameters: str = None,
        region_id: str = None,
        task_execution_id: str = None,
        task_execution_ids: str = None,
        task_name: str = None,
    ):
        # The ID of the execution.
        # 
        # This parameter is required.
        self.execution_id = execution_id
        # The state of the terminated execution. This parameter is valid if you set the NotifyType parameter to CompleteExecution.
        self.execution_status = execution_status
        # The items of the child node in the loop task.
        self.loop_item = loop_item
        # The description for the notification.
        self.notify_note = notify_note
        # The type of the notification. Valid values:
        # 
        # *   **ExecuteTask**: starts to run a specific task. This value is used if you perform debugging in the Debug mode. If you set this parameter to ExecuteTask, you also need to set the Parameters parameter.
        # *   **CancelTask**: cancels a current task. This value is used if you perform debugging in the Debug mode.
        # *   **CompleteExecution**: manually terminates an execution if you perform debugging in the Debug mode. You can specify the state of the terminated execution by using the **ExecutionStatus** parameter.
        # *   **Approve**: approves an execution. For example, you are aware of the risks of an operation task and agree to approve the execution.
        # *   **Reject**: rejects an execution. For example, you want to reject the execution of a high-risk operation task.
        # *   **RetryTask**: retries a failed task whose execution mode is Suspend upon Failure.
        # *   **SkipTask**: skips a failed task whose execution mode is Suspend upon Failure.
        # 
        # This parameter is required.
        self.notify_type = notify_type
        # The parameters of the subsequent task. This parameter is valid if you set the NotifyType parameter to ExecuteTask.
        self.parameters = parameters
        # The ID of the region in which the execution resides.
        self.region_id = region_id
        # The execution ID of the task.
        self.task_execution_id = task_execution_id
        # The execution IDs of the tasks.
        self.task_execution_ids = task_execution_ids
        # The name of the subsequent task.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id

        if self.execution_status is not None:
            result['ExecutionStatus'] = self.execution_status

        if self.loop_item is not None:
            result['LoopItem'] = self.loop_item

        if self.notify_note is not None:
            result['NotifyNote'] = self.notify_note

        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.task_execution_id is not None:
            result['TaskExecutionId'] = self.task_execution_id

        if self.task_execution_ids is not None:
            result['TaskExecutionIds'] = self.task_execution_ids

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')

        if m.get('ExecutionStatus') is not None:
            self.execution_status = m.get('ExecutionStatus')

        if m.get('LoopItem') is not None:
            self.loop_item = m.get('LoopItem')

        if m.get('NotifyNote') is not None:
            self.notify_note = m.get('NotifyNote')

        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TaskExecutionId') is not None:
            self.task_execution_id = m.get('TaskExecutionId')

        if m.get('TaskExecutionIds') is not None:
            self.task_execution_ids = m.get('TaskExecutionIds')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

