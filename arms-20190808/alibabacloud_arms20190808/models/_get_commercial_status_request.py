# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCommercialStatusRequest(DaraModel):
    def __init__(
        self,
        commodity_code: str = None,
        region_id: str = None,
    ):
        # The product code.
        # 
        # *   arms_app_post
        # *   arms_web_post
        # *   arms_promethues_public_cn
        # *   prometheus_pay_public_cn
        # *   xtrace
        # *   arms_serverless_public_cn
        # *   arms_rumserverless_public_cn
        # *   prometheus_serverless_public_cn
        # *   xtrace_serverless_public_cn
        # 
        # This parameter is required.
        self.commodity_code = commodity_code
        # The region ID.
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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

