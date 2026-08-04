# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aicontent20240611 import models as main_models
from darabonba.model import DaraModel

class DeptBalanceSummaryDTO(DaraModel):
    def __init__(
        self,
        monthly: main_models.BalancePoolSummaryDTO = None,
        permanent: main_models.BalancePoolSummaryDTO = None,
    ):
        self.monthly = monthly
        self.permanent = permanent

    def validate(self):
        if self.monthly:
            self.monthly.validate()
        if self.permanent:
            self.permanent.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.monthly is not None:
            result['monthly'] = self.monthly.to_map()

        if self.permanent is not None:
            result['permanent'] = self.permanent.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('monthly') is not None:
            temp_model = main_models.BalancePoolSummaryDTO()
            self.monthly = temp_model.from_map(m.get('monthly'))

        if m.get('permanent') is not None:
            temp_model = main_models.BalancePoolSummaryDTO()
            self.permanent = temp_model.from_map(m.get('permanent'))

        return self

