# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from darabonba.model import DaraModel

class DLSkewedInfo(DaraModel):
    def __init__(
        self,
        skewed_col_names: List[str] = None,
        skewed_col_value_location_maps: Dict[str, Any] = None,
        skewed_col_values: List[List[str]] = None,
    ):
        self.skewed_col_names = skewed_col_names
        self.skewed_col_value_location_maps = skewed_col_value_location_maps
        self.skewed_col_values = skewed_col_values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.skewed_col_names is not None:
            result['SkewedColNames'] = self.skewed_col_names

        if self.skewed_col_value_location_maps is not None:
            result['SkewedColValueLocationMaps'] = self.skewed_col_value_location_maps

        if self.skewed_col_values is not None:
            result['SkewedColValues'] = self.skewed_col_values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SkewedColNames') is not None:
            self.skewed_col_names = m.get('SkewedColNames')

        if m.get('SkewedColValueLocationMaps') is not None:
            self.skewed_col_value_location_maps = m.get('SkewedColValueLocationMaps')

        if m.get('SkewedColValues') is not None:
            self.skewed_col_values = m.get('SkewedColValues')

        return self

