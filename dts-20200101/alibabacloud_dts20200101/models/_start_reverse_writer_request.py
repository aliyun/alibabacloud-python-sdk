# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartReverseWriterRequest(DaraModel):
    def __init__(
        self,
        check_point: str = None,
        dts_job_id: str = None,
        resource_group_id: str = None,
    ):
        # The offset of the Incremental Write module. Specify a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. 
        # 
        # > The default value is the offset that is automatically saved by DTS when the task is paused.
        self.check_point = check_point
        # The ID of the reverse task that was created by calling the CreateReverseDtsJob operation.
        # 
        # This parameter is required.
        self.dts_job_id = dts_job_id
        # Resource group ID.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_point is not None:
            result['CheckPoint'] = self.check_point

        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckPoint') is not None:
            self.check_point = m.get('CheckPoint')

        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

