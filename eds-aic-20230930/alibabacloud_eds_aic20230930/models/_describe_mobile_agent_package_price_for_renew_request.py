# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeMobileAgentPackagePriceForRenewRequest(DaraModel):
    def __init__(
        self,
        mobile_agent_package_ids: List[str] = None,
        period: str = None,
        period_unit: str = None,
        promotion_id: str = None,
    ):
        # The IDs of the MobileAgent resource plans.
        self.mobile_agent_package_ids = mobile_agent_package_ids
        # The subscription period of the resource. The unit is specified by PeriodUnit. Valid values: 1 month, 2 months, 3 months, 6 months, and 1 year.
        self.period = period
        # The unit of the subscription period. Valid values:
        # - **Month**: Month.
        # - **Year**: Year.
        self.period_unit = period_unit
        # The promotion ID.
        self.promotion_id = promotion_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mobile_agent_package_ids is not None:
            result['MobileAgentPackageIds'] = self.mobile_agent_package_ids

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MobileAgentPackageIds') is not None:
            self.mobile_agent_package_ids = m.get('MobileAgentPackageIds')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        return self

