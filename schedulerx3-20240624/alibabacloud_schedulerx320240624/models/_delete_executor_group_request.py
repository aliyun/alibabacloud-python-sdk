# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteExecutorGroupRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        delete_jobs: bool = None,
        id: int = None,
        name: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # Specifies whether to synchronously delete tasks.
        self.delete_jobs = delete_jobs
        # The ID.
        # 
        # This parameter is required.
        self.id = id
        # The name of the executor group.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.delete_jobs is not None:
            result['DeleteJobs'] = self.delete_jobs

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('DeleteJobs') is not None:
            self.delete_jobs = m.get('DeleteJobs')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

