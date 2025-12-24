# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RestartLivePullToPushRequest(DaraModel):
    def __init__(
        self,
        owner_id: int = None,
        region: str = None,
        region_id: str = None,
        task_id: str = None,
    ):
        self.owner_id = owner_id
        # The region of the live center. Valid values:
        # 
        # *   ap-southeast-1: Singapore
        # *   ap-southeast-5: Indonesia (Jakarta)
        # *   cn-beijing: China (Beijing)
        # *   cn-shanghai: China (Shanghai)
        # 
        # This parameter is required.
        self.region = region
        self.region_id = region_id
        # The task ID.
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region is not None:
            result['Region'] = self.region

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

