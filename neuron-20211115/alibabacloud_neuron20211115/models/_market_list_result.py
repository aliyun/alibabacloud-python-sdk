# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class MarketListResult(DaraModel):
    def __init__(
        self,
        markets: List[main_models.MarketInfo] = None,
    ):
        self.markets = markets

    def validate(self):
        if self.markets:
            for v1 in self.markets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['markets'] = []
        if self.markets is not None:
            for k1 in self.markets:
                result['markets'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.markets = []
        if m.get('markets') is not None:
            for k1 in m.get('markets'):
                temp_model = main_models.MarketInfo()
                self.markets.append(temp_model.from_map(k1))

        return self

