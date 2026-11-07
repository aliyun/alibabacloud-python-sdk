# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QuerySessionDataRequest(DaraModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        biz_region_id: str = None,
        region_id: str = None,
        stat_date: str = None,
    ):
        self.app_instance_group_id = app_instance_group_id
        self.biz_region_id = biz_region_id
        self.region_id = region_id
        self.stat_date = stat_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.stat_date is not None:
            result['StatDate'] = self.stat_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StatDate') is not None:
            self.stat_date = m.get('StatDate')

        return self

