# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hcs_mgw20240626 import models as main_models
from darabonba.model import DaraModel

class LastModifyFilterItem(DaraModel):
    def __init__(
        self,
        time_filter: List[main_models.TimeFilter] = None,
    ):
        self.time_filter = time_filter

    def validate(self):
        if self.time_filter:
            for v1 in self.time_filter:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TimeFilter'] = []
        if self.time_filter is not None:
            for k1 in self.time_filter:
                result['TimeFilter'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.time_filter = []
        if m.get('TimeFilter') is not None:
            for k1 in m.get('TimeFilter'):
                temp_model = main_models.TimeFilter()
                self.time_filter.append(temp_model.from_map(k1))

        return self

