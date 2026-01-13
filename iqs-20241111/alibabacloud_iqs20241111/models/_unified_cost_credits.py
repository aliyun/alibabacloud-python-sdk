# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_iqs20241111 import models as main_models
from darabonba.model import DaraModel

class UnifiedCostCredits(DaraModel):
    def __init__(
        self,
        search: main_models.SearchCredits = None,
        value_added: main_models.ValueAddedCredits = None,
    ):
        self.search = search
        self.value_added = value_added

    def validate(self):
        if self.search:
            self.search.validate()
        if self.value_added:
            self.value_added.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.search is not None:
            result['search'] = self.search.to_map()

        if self.value_added is not None:
            result['valueAdded'] = self.value_added.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('search') is not None:
            temp_model = main_models.SearchCredits()
            self.search = temp_model.from_map(m.get('search'))

        if m.get('valueAdded') is not None:
            temp_model = main_models.ValueAddedCredits()
            self.value_added = temp_model.from_map(m.get('valueAdded'))

        return self

