# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAppGroupRequest(DaraModel):
    def __init__(
        self,
        delete_jobs: bool = None,
        group_id: str = None,
        namespace: str = None,
        region_id: str = None,
    ):
        # Specifies whether to delete the jobs in the application group. Valid values:
        # 
        # true: deletes the jobs in the application group.
        # false: does not delete the jobs in the application group.
        self.delete_jobs = delete_jobs
        # The ID of the application. You can obtain the ID of the application on the Application Management page in the SchedulerX console.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The ID of the namespace. You can obtain the ID of the namespace on the Namespace page in the SchedulerX console.
        # 
        # This parameter is required.
        self.namespace = namespace
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
        if self.delete_jobs is not None:
            result['DeleteJobs'] = self.delete_jobs

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteJobs') is not None:
            self.delete_jobs = m.get('DeleteJobs')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

