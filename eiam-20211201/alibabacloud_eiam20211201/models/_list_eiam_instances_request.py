# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListEiamInstancesRequest(DaraModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        instance_region_id: str = None,
    ):
        # The instance ID list.
        self.instance_ids = instance_ids
        # The region in which the instance resides.
        self.instance_region_id = instance_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.instance_region_id is not None:
            result['InstanceRegionId'] = self.instance_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('InstanceRegionId') is not None:
            self.instance_region_id = m.get('InstanceRegionId')

        return self

