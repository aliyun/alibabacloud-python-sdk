# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class OperateRetryJobExecutionRequest(DaraModel):
    def __init__(
        self,
        app_group_id: int = None,
        app_name: str = None,
        cluster_id: str = None,
        job_execution_id: str = None,
        task_list: List[str] = None,
        trigger_child: bool = None,
    ):
        self.app_group_id = app_group_id
        # The application name.
        # 
        # This parameter is required.
        self.app_name = app_name
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The job execution ID.
        # 
        # This parameter is required.
        self.job_execution_id = job_execution_id
        # The list of subtask execution IDs (for broadcast jobs).
        # >To rerun a subtask of a broadcast job, set this field to the execution ID of the corresponding subtask.
        self.task_list = task_list
        # Specifies whether to trigger downstream nodes.
        self.trigger_child = trigger_child

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_group_id is not None:
            result['AppGroupId'] = self.app_group_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.job_execution_id is not None:
            result['JobExecutionId'] = self.job_execution_id

        if self.task_list is not None:
            result['TaskList'] = self.task_list

        if self.trigger_child is not None:
            result['TriggerChild'] = self.trigger_child

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppGroupId') is not None:
            self.app_group_id = m.get('AppGroupId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('JobExecutionId') is not None:
            self.job_execution_id = m.get('JobExecutionId')

        if m.get('TaskList') is not None:
            self.task_list = m.get('TaskList')

        if m.get('TriggerChild') is not None:
            self.trigger_child = m.get('TriggerChild')

        return self

