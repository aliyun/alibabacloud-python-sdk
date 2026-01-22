# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeComponentPropetiesRequest(DaraModel):
    def __init__(
        self,
        commodity_code: str = None,
        component_name: str = None,
        region_id: str = None,
        storage_type: str = None,
    ):
        # This parameter is required.
        self.commodity_code = commodity_code
        # This parameter is required.
        self.component_name = component_name
        # This parameter is required.
        self.region_id = region_id
        self.storage_type = storage_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.component_name is not None:
            result['ComponentName'] = self.component_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        return self

