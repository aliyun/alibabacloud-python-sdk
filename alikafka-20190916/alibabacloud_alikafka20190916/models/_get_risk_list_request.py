# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRiskListRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        page_size: int = None,
        region_id: str = None,
        start_index: int = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.page_size = page_size
        # This parameter is required.
        self.region_id = region_id
        self.start_index = start_index

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_index is not None:
            result['StartIndex'] = self.start_index

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartIndex') is not None:
            self.start_index = m.get('StartIndex')

        return self

