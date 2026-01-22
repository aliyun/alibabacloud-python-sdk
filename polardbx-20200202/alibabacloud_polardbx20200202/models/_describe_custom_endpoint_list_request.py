# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCustomEndpointListRequest(DaraModel):
    def __init__(
        self,
        check_delete_cn: bool = None,
        custom_endpoint_ids: str = None,
        dbinstance_name: str = None,
        region_id: str = None,
    ):
        self.check_delete_cn = check_delete_cn
        self.custom_endpoint_ids = custom_endpoint_ids
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_delete_cn is not None:
            result['CheckDeleteCN'] = self.check_delete_cn

        if self.custom_endpoint_ids is not None:
            result['CustomEndpointIds'] = self.custom_endpoint_ids

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckDeleteCN') is not None:
            self.check_delete_cn = m.get('CheckDeleteCN')

        if m.get('CustomEndpointIds') is not None:
            self.custom_endpoint_ids = m.get('CustomEndpointIds')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

