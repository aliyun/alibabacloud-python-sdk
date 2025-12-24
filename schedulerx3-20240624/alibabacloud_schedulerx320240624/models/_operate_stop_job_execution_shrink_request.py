# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OperateStopJobExecutionShrinkRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
        job_execution_id: str = None,
        task_list_shrink: str = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.job_execution_id = job_execution_id
        self.task_list_shrink = task_list_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.job_execution_id is not None:
            result['JobExecutionId'] = self.job_execution_id

        if self.task_list_shrink is not None:
            result['TaskList'] = self.task_list_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('JobExecutionId') is not None:
            self.job_execution_id = m.get('JobExecutionId')

        if m.get('TaskList') is not None:
            self.task_list_shrink = m.get('TaskList')

        return self

