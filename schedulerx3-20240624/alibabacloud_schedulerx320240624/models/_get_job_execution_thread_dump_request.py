# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetJobExecutionThreadDumpRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
        executor_addr: str = None,
        job_execution_id: str = None,
    ):
        self.app_name = app_name
        self.cluster_id = cluster_id
        self.executor_addr = executor_addr
        self.job_execution_id = job_execution_id

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

        if self.executor_addr is not None:
            result['ExecutorAddr'] = self.executor_addr

        if self.job_execution_id is not None:
            result['JobExecutionId'] = self.job_execution_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ExecutorAddr') is not None:
            self.executor_addr = m.get('ExecutorAddr')

        if m.get('JobExecutionId') is not None:
            self.job_execution_id = m.get('JobExecutionId')

        return self

