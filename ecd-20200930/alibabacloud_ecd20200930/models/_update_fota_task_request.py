# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateFotaTaskRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        task_uid: str = None,
        user_status: str = None,
    ):
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the regions supported by Elastic Desktop Service.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the image update task. You can call the [DescribeFotaTasks](https://help.aliyun.com/document_detail/437001.html) operation to obtain the value of this parameter.
        # 
        # This parameter is required.
        self.task_uid = task_uid
        # Specifies whether to automatically push the image update task.
        # 
        # Valid values:
        # 
        # *   Running: automatically pushes the image update task.
        # *   Pending: does not automatically push the image update task.
        self.user_status = user_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.task_uid is not None:
            result['TaskUid'] = self.task_uid

        if self.user_status is not None:
            result['UserStatus'] = self.user_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TaskUid') is not None:
            self.task_uid = m.get('TaskUid')

        if m.get('UserStatus') is not None:
            self.user_status = m.get('UserStatus')

        return self

