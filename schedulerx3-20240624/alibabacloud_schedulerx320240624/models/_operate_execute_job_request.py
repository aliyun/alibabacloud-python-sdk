# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OperateExecuteJobRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
        instance_parameters: str = None,
        job_id: int = None,
        label: str = None,
        worker: str = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.cluster_id = cluster_id
        self.instance_parameters = instance_parameters
        # This parameter is required.
        self.job_id = job_id
        self.label = label
        self.worker = worker

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

        if self.instance_parameters is not None:
            result['InstanceParameters'] = self.instance_parameters

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.label is not None:
            result['Label'] = self.label

        if self.worker is not None:
            result['Worker'] = self.worker

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('InstanceParameters') is not None:
            self.instance_parameters = m.get('InstanceParameters')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Worker') is not None:
            self.worker = m.get('Worker')

        return self

