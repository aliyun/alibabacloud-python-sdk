# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class MoveHiveEdgeWorkersRequest(DaraModel):
    def __init__(
        self,
        hive_id: str = None,
        instance_ids: List[str] = None,
    ):
        # This parameter is required.
        self.hive_id = hive_id
        # This parameter is required.
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hive_id is not None:
            result['HiveId'] = self.hive_id

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HiveId') is not None:
            self.hive_id = m.get('HiveId')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        return self

