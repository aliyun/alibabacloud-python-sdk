# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCommodityRequest(DaraModel):
    def __init__(
        self,
        commodity_code: str = None,
        order_type: str = None,
        region_id: str = None,
    ):
        # The commodity code.
        # 
        # Valid values on the China site (aliyun.com):
        # 
        # *   **ga_gapluspre_public_cn**: GA instance.
        # *   **ga_plusbwppre_public_cn**: basic bandwidth plan.
        # 
        # Valid values on the international site (alibabacloud.com):
        # 
        # *   **ga_pluspre_public_intl**: GA instance.
        # *   **ga_bwppreintl_public_intl:** basic bandwidth plan.
        # 
        # This parameter is required.
        self.commodity_code = commodity_code
        # The type of the order. Valid values:
        # 
        # *   **BUY**: purchase order.
        # *   **RENEW**: renewal order.
        # *   **UPGRADE**: upgrade order.
        # 
        # This parameter is required.
        self.order_type = order_type
        # The ID of the region where the Global Accelerator (GA) instance is deployed. Set the value to **cn-hangzhou**.
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
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

