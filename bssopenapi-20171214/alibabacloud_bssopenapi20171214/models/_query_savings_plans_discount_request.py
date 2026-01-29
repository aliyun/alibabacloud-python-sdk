# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QuerySavingsPlansDiscountRequest(DaraModel):
    def __init__(
        self,
        commodity_code: str = None,
        cycle: str = None,
        locale: str = None,
        module_code: str = None,
        page_num: int = None,
        page_size: int = None,
        pay_mode: str = None,
        region: str = None,
        spec: str = None,
        spn_commodity_code: str = None,
        spn_type: str = None,
    ):
        # The code of the service.
        # 
        # This parameter is required.
        self.commodity_code = commodity_code
        # The cycle based on which queries are performed.
        # 
        # This parameter is required.
        self.cycle = cycle
        # The identifier of the language.
        # 
        # Valid values:
        # 
        # *   EN: English.
        # *   ZH: Chinese.
        self.locale = locale
        # The code of the pricing module.
        self.module_code = module_code
        # The number of the page to return.
        self.page_num = page_num
        # The number of entries to return on each page.
        self.page_size = page_size
        # The payment mode. Valid values: total: all upfront. half: half upfront. zero: no upfront.
        # 
        # This parameter is required.
        self.pay_mode = pay_mode
        # The ID of the region.
        self.region = region
        # The type of the resource.
        self.spec = spec
        self.spn_commodity_code = spn_commodity_code
        # The type of the savings plan. Valid values: ecs: Elastic Compute Service (ECS) compute type. universal: general-purpose type.
        # 
        # This parameter is required.
        self.spn_type = spn_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.cycle is not None:
            result['Cycle'] = self.cycle

        if self.locale is not None:
            result['Locale'] = self.locale

        if self.module_code is not None:
            result['ModuleCode'] = self.module_code

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pay_mode is not None:
            result['PayMode'] = self.pay_mode

        if self.region is not None:
            result['Region'] = self.region

        if self.spec is not None:
            result['Spec'] = self.spec

        if self.spn_commodity_code is not None:
            result['SpnCommodityCode'] = self.spn_commodity_code

        if self.spn_type is not None:
            result['SpnType'] = self.spn_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('Cycle') is not None:
            self.cycle = m.get('Cycle')

        if m.get('Locale') is not None:
            self.locale = m.get('Locale')

        if m.get('ModuleCode') is not None:
            self.module_code = m.get('ModuleCode')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PayMode') is not None:
            self.pay_mode = m.get('PayMode')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('SpnCommodityCode') is not None:
            self.spn_commodity_code = m.get('SpnCommodityCode')

        if m.get('SpnType') is not None:
            self.spn_type = m.get('SpnType')

        return self

