# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteChangeSetRequest(DaraModel):
    def __init__(
        self,
        change_set_id: str = None,
        region_id: str = None,
    ):
        # The ID of the change set.
        # 
        # This parameter is required.
        self.change_set_id = change_set_id
        # The region ID of the change set. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/131035.html) operation to query the most recent region list.
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
        if self.change_set_id is not None:
            result['ChangeSetId'] = self.change_set_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeSetId') is not None:
            self.change_set_id = m.get('ChangeSetId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

