# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeCloudDiskGroupsRequest(DaraModel):
    def __init__(
        self,
        cds_id: str = None,
        group_id: List[str] = None,
        group_name: str = None,
        parent_org_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.cds_id = cds_id
        self.group_id = group_id
        self.group_name = group_name
        self.parent_org_id = parent_org_id
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cds_id is not None:
            result['CdsId'] = self.cds_id

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.parent_org_id is not None:
            result['ParentOrgId'] = self.parent_org_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdsId') is not None:
            self.cds_id = m.get('CdsId')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('ParentOrgId') is not None:
            self.parent_org_id = m.get('ParentOrgId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

