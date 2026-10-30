# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_hcs_mgw20240626 import models as main_models
from darabonba.model import DaraModel

class PrefixFilters(DaraModel):
    def __init__(
        self,
        includes: main_models.PrefixFiltersIncludeItem = None,
    ):
        # The collection of object prefixes to migrate, where multiple prefixes are matched using OR logic.
        self.includes = includes

    def validate(self):
        if self.includes:
            self.includes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.includes is not None:
            result['Includes'] = self.includes.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Includes') is not None:
            temp_model = main_models.PrefixFiltersIncludeItem()
            self.includes = temp_model.from_map(m.get('Includes'))

        return self

