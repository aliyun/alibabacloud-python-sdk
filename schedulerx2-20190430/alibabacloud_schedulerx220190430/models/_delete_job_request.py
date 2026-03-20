# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteJobRequest(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        job_id: int = None,
        namespace: str = None,
        namespace_source: str = None,
        region_id: str = None,
    ):
        # The ID of the application. You can obtain the application ID on the **Application Management** page in the SchedulerX console.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The ID of the job. You can obtain the ID on the **Task Management** page in the SchedulerX console.
        # 
        # This parameter is required.
        self.job_id = job_id
        # The ID of the namespace. You can obtain the ID of the namespace on the **Namespace** page in the SchedulerX console.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The source of the namespace. This parameter is required only for a special third party.
        self.namespace_source = namespace_source
        # The ID of the region.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

