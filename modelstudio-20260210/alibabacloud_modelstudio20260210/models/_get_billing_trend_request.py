# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_modelstudio20260210 import models as main_models
from darabonba.model import DaraModel

class GetBillingTrendRequest(DaraModel):
    def __init__(
        self,
        filter: main_models.GetBillingTrendRequestFilter = None,
        granularity: str = None,
        group_by: List[main_models.GetBillingTrendRequestGroupBy] = None,
        locale: str = None,
        region_id: str = None,
        time_period: main_models.GetBillingTrendRequestTimePeriod = None,
        top_num: int = None,
        zero_filter: bool = None,
    ):
        self.filter = filter
        self.granularity = granularity
        self.group_by = group_by
        self.locale = locale
        self.region_id = region_id
        self.time_period = time_period
        self.top_num = top_num
        self.zero_filter = zero_filter

    def validate(self):
        if self.filter:
            self.filter.validate()
        if self.group_by:
            for v1 in self.group_by:
                 if v1:
                    v1.validate()
        if self.time_period:
            self.time_period.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter is not None:
            result['filter'] = self.filter.to_map()

        if self.granularity is not None:
            result['granularity'] = self.granularity

        result['groupBy'] = []
        if self.group_by is not None:
            for k1 in self.group_by:
                result['groupBy'].append(k1.to_map() if k1 else None)

        if self.locale is not None:
            result['locale'] = self.locale

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.time_period is not None:
            result['timePeriod'] = self.time_period.to_map()

        if self.top_num is not None:
            result['topNum'] = self.top_num

        if self.zero_filter is not None:
            result['zeroFilter'] = self.zero_filter

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filter') is not None:
            temp_model = main_models.GetBillingTrendRequestFilter()
            self.filter = temp_model.from_map(m.get('filter'))

        if m.get('granularity') is not None:
            self.granularity = m.get('granularity')

        self.group_by = []
        if m.get('groupBy') is not None:
            for k1 in m.get('groupBy'):
                temp_model = main_models.GetBillingTrendRequestGroupBy()
                self.group_by.append(temp_model.from_map(k1))

        if m.get('locale') is not None:
            self.locale = m.get('locale')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('timePeriod') is not None:
            temp_model = main_models.GetBillingTrendRequestTimePeriod()
            self.time_period = temp_model.from_map(m.get('timePeriod'))

        if m.get('topNum') is not None:
            self.top_num = m.get('topNum')

        if m.get('zeroFilter') is not None:
            self.zero_filter = m.get('zeroFilter')

        return self

class GetBillingTrendRequestTimePeriod(DaraModel):
    def __init__(
        self,
        end: str = None,
        start: str = None,
    ):
        self.end = end
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end is not None:
            result['end'] = self.end

        if self.start is not None:
            result['start'] = self.start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('end') is not None:
            self.end = m.get('end')

        if m.get('start') is not None:
            self.start = m.get('start')

        return self

class GetBillingTrendRequestGroupBy(DaraModel):
    def __init__(
        self,
        code: str = None,
    ):
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        return self

class GetBillingTrendRequestFilter(DaraModel):
    def __init__(
        self,
        dimensions: List[main_models.GetBillingTrendRequestFilterDimensions] = None,
    ):
        self.dimensions = dimensions

    def validate(self):
        if self.dimensions:
            for v1 in self.dimensions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['dimensions'] = []
        if self.dimensions is not None:
            for k1 in self.dimensions:
                result['dimensions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dimensions = []
        if m.get('dimensions') is not None:
            for k1 in m.get('dimensions'):
                temp_model = main_models.GetBillingTrendRequestFilterDimensions()
                self.dimensions.append(temp_model.from_map(k1))

        return self

class GetBillingTrendRequestFilterDimensions(DaraModel):
    def __init__(
        self,
        code: str = None,
        select_type: str = None,
        values: List[str] = None,
    ):
        self.code = code
        self.select_type = select_type
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.select_type is not None:
            result['selectType'] = self.select_type

        if self.values is not None:
            result['values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('selectType') is not None:
            self.select_type = m.get('selectType')

        if m.get('values') is not None:
            self.values = m.get('values')

        return self

