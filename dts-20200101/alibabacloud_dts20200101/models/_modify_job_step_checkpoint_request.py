# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyJobStepCheckpointRequest(DaraModel):
    def __init__(
        self,
        dts_job_id: str = None,
        job_step_id: str = None,
        new_check_point: int = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the migration, synchronization, or tracking task.
        self.dts_job_id = dts_job_id
        # The task step ID, which corresponds to the **synchronization** step ID returned by the ListJobStep API.
        self.job_step_id = job_step_id
        # The new offset as a UNIX timestamp in seconds. The specified value must fall within the offset range of the incremental data collection step.
        self.new_check_point = new_check_point
        # The region where the DTS instance resides.
        # 
        # > For regions that support dedicated clusters, see [DTS dedicated cluster](https://help.aliyun.com/document_detail/417481.html).
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id

        if self.job_step_id is not None:
            result['JobStepId'] = self.job_step_id

        if self.new_check_point is not None:
            result['NewCheckPoint'] = self.new_check_point

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')

        if m.get('JobStepId') is not None:
            self.job_step_id = m.get('JobStepId')

        if m.get('NewCheckPoint') is not None:
            self.new_check_point = m.get('NewCheckPoint')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

