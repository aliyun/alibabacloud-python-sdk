# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class DescribeSavingsPlansUsageTotalRequest(DaraModel):
    def __init__(
        self,
        bill_owner_id: int = None,
        end_period: str = None,
        filter_param: main_models.DescribeSavingsPlansUsageTotalRequestFilterParam = None,
        period_type: str = None,
        start_period: str = None,
    ):
        # The ID of the account for which you want to query usage summary. If you do not set this parameter, the data of the current Alibaba Cloud account and its RAM users is queried. To query the data of a RAM user, specify the ID of the RAM user.
        self.bill_owner_id = bill_owner_id
        # The end of the time range to query. The end is excluded from the time range. If you do not set this parameter, the end time is the current time. Specify the time in the format of yyyy-MM-dd HH:mm:ss.
        self.end_period = end_period
        self.filter_param = filter_param
        # The time granularity at which usage summary are queried. Valid values: MONTH, DAY, and HOUR.
        # 
        # This parameter is required.
        self.period_type = period_type
        # The beginning of the time range to query. The beginning is included in the time range. Specify the time in the format of yyyy-MM-dd HH:mm:ss.
        # 
        # This parameter is required.
        self.start_period = start_period

    def validate(self):
        if self.filter_param:
            self.filter_param.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bill_owner_id is not None:
            result['BillOwnerId'] = self.bill_owner_id

        if self.end_period is not None:
            result['EndPeriod'] = self.end_period

        if self.filter_param is not None:
            result['FilterParam'] = self.filter_param.to_map()

        if self.period_type is not None:
            result['PeriodType'] = self.period_type

        if self.start_period is not None:
            result['StartPeriod'] = self.start_period

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillOwnerId') is not None:
            self.bill_owner_id = m.get('BillOwnerId')

        if m.get('EndPeriod') is not None:
            self.end_period = m.get('EndPeriod')

        if m.get('FilterParam') is not None:
            temp_model = main_models.DescribeSavingsPlansUsageTotalRequestFilterParam()
            self.filter_param = temp_model.from_map(m.get('FilterParam'))

        if m.get('PeriodType') is not None:
            self.period_type = m.get('PeriodType')

        if m.get('StartPeriod') is not None:
            self.start_period = m.get('StartPeriod')

        return self

class DescribeSavingsPlansUsageTotalRequestFilterParam(DaraModel):
    def __init__(
        self,
        dimensions: List[main_models.DescribeSavingsPlansUsageTotalRequestFilterParamDimensions] = None,
        tags: List[main_models.DescribeSavingsPlansUsageTotalRequestFilterParamTags] = None,
    ):
        self.dimensions = dimensions
        self.tags = tags

    def validate(self):
        if self.dimensions:
            for v1 in self.dimensions:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Dimensions'] = []
        if self.dimensions is not None:
            for k1 in self.dimensions:
                result['Dimensions'].append(k1.to_map() if k1 else None)

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k1 in m.get('Dimensions'):
                temp_model = main_models.DescribeSavingsPlansUsageTotalRequestFilterParamDimensions()
                self.dimensions.append(temp_model.from_map(k1))

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeSavingsPlansUsageTotalRequestFilterParamTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class DescribeSavingsPlansUsageTotalRequestFilterParamTags(DaraModel):
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
            result['Code'] = self.code

        if self.select_type is not None:
            result['SelectType'] = self.select_type

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('SelectType') is not None:
            self.select_type = m.get('SelectType')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

class DescribeSavingsPlansUsageTotalRequestFilterParamDimensions(DaraModel):
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
            result['Code'] = self.code

        if self.select_type is not None:
            result['SelectType'] = self.select_type

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('SelectType') is not None:
            self.select_type = m.get('SelectType')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

