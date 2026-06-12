# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSkillFileDetectResultRequest(DaraModel):
    def __init__(
        self,
        hash_key: str = None,
        region_id: str = None,
    ):
        # The unique identifier for the detection task.
        # 
        # This parameter is required.
        self.hash_key = hash_key
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hash_key is not None:
            result['HashKey'] = self.hash_key

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HashKey') is not None:
            self.hash_key = m.get('HashKey')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

