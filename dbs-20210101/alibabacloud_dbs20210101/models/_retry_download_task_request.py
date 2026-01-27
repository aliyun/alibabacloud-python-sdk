# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RetryDownloadTaskRequest(DaraModel):
    def __init__(
        self,
        cluster_name: str = None,
        instance_name: str = None,
        region_code: str = None,
        task_id: str = None,
    ):
        self.cluster_name = cluster_name
        self.instance_name = instance_name
        self.region_code = region_code
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.region_code is not None:
            result['RegionCode'] = self.region_code

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

