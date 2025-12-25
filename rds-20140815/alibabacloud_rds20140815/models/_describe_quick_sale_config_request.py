# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeQuickSaleConfigRequest(DaraModel):
    def __init__(
        self,
        commodity: str = None,
        engine: str = None,
        region_id: str = None,
    ):
        # The product code. Valid values:
        # 
        # *   rds: The instance is a subscription instance.
        # *   bards: The instance is a pay-as-you-go instance.
        self.commodity = commodity
        # The database engine of the instance. Valid values:
        # 
        # *   **MySQL**
        # *   **SQLServer**
        # *   **PostgreSQL**
        # *   **MariaDB**
        self.engine = engine
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/26243.html) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commodity is not None:
            result['Commodity'] = self.commodity

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Commodity') is not None:
            self.commodity = m.get('Commodity')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

