# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_modelstudio20260210 import models as main_models
from darabonba.model import DaraModel

class GetBillingOverviewRequest(DaraModel):
    def __init__(
        self,
        bill_month: str = None,
        filter: main_models.GetBillingOverviewRequestFilter = None,
        group_by: List[main_models.GetBillingOverviewRequestGroupBy] = None,
        locale: str = None,
        region_id: str = None,
        top_num: int = None,
        zero_filter: bool = None,
    ):
        self.bill_month = bill_month
        self.filter = filter
        self.group_by = group_by
        self.locale = locale
        self.region_id = region_id
        self.top_num = top_num
        self.zero_filter = zero_filter

    def validate(self):
        if self.filter:
            self.filter.validate()
        if self.group_by:
            for v1 in self.group_by:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bill_month is not None:
            result['billMonth'] = self.bill_month

        if self.filter is not None:
            result['filter'] = self.filter.to_map()

        result['groupBy'] = []
        if self.group_by is not None:
            for k1 in self.group_by:
                result['groupBy'].append(k1.to_map() if k1 else None)

        if self.locale is not None:
            result['locale'] = self.locale

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.top_num is not None:
            result['topNum'] = self.top_num

        if self.zero_filter is not None:
            result['zeroFilter'] = self.zero_filter

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billMonth') is not None:
            self.bill_month = m.get('billMonth')

        if m.get('filter') is not None:
            temp_model = main_models.GetBillingOverviewRequestFilter()
            self.filter = temp_model.from_map(m.get('filter'))

        self.group_by = []
        if m.get('groupBy') is not None:
            for k1 in m.get('groupBy'):
                temp_model = main_models.GetBillingOverviewRequestGroupBy()
                self.group_by.append(temp_model.from_map(k1))

        if m.get('locale') is not None:
            self.locale = m.get('locale')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('topNum') is not None:
            self.top_num = m.get('topNum')

        if m.get('zeroFilter') is not None:
            self.zero_filter = m.get('zeroFilter')

        return self

class GetBillingOverviewRequestGroupBy(DaraModel):
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

class GetBillingOverviewRequestFilter(DaraModel):
    def __init__(
        self,
        dimensions: List[main_models.GetBillingOverviewRequestFilterDimensions] = None,
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
                temp_model = main_models.GetBillingOverviewRequestFilterDimensions()
                self.dimensions.append(temp_model.from_map(k1))

        return self

class GetBillingOverviewRequestFilterDimensions(DaraModel):
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

