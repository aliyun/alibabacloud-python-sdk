# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class DescribeSavingsPlansUsageDetailRequest(DaraModel):
    def __init__(
        self,
        bill_owner_id: int = None,
        end_period: str = None,
        filter_param: main_models.DescribeSavingsPlansUsageDetailRequestFilterParam = None,
        max_results: int = None,
        period_type: str = None,
        start_period: str = None,
        token: str = None,
    ):
        # The ID of the account. If this parameter is left empty, data of the current account and its trusteeship linked accounts is queried. You can specify a trusteeship linked account ID to query data of that account.
        self.bill_owner_id = bill_owner_id
        # The end time. Format: yyyy-MM-dd HH:mm:ss. The query excludes data at this time. If this parameter is left empty, the query covers data up to the current time.
        self.end_period = end_period
        self.filter_param = filter_param
        # The maximum number of data records to return. Default value: 20. Maximum value: 300.
        self.max_results = max_results
        # The time granularity for querying usage details. Valid values:
        # 
        # - MONTH: monthly granularity.
        # - DAY: daily granularity.
        # - HOUR: hourly granularity.
        # 
        # This parameter is required.
        self.period_type = period_type
        # The start time. Format: yyyy-MM-dd HH:mm:ss. The query includes data at this time.
        # 
        # This parameter is required.
        self.start_period = start_period
        # The pagination token. Leave this parameter empty for the first page. The query result returns the token for the next page. If the returned token is empty, all data has been retrieved.
        self.token = token

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

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.period_type is not None:
            result['PeriodType'] = self.period_type

        if self.start_period is not None:
            result['StartPeriod'] = self.start_period

        if self.token is not None:
            result['Token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillOwnerId') is not None:
            self.bill_owner_id = m.get('BillOwnerId')

        if m.get('EndPeriod') is not None:
            self.end_period = m.get('EndPeriod')

        if m.get('FilterParam') is not None:
            temp_model = main_models.DescribeSavingsPlansUsageDetailRequestFilterParam()
            self.filter_param = temp_model.from_map(m.get('FilterParam'))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('PeriodType') is not None:
            self.period_type = m.get('PeriodType')

        if m.get('StartPeriod') is not None:
            self.start_period = m.get('StartPeriod')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        return self

class DescribeSavingsPlansUsageDetailRequestFilterParam(DaraModel):
    def __init__(
        self,
        dimensions: List[main_models.DescribeSavingsPlansUsageDetailRequestFilterParamDimensions] = None,
        tags: List[main_models.DescribeSavingsPlansUsageDetailRequestFilterParamTags] = None,
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
                temp_model = main_models.DescribeSavingsPlansUsageDetailRequestFilterParamDimensions()
                self.dimensions.append(temp_model.from_map(k1))

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeSavingsPlansUsageDetailRequestFilterParamTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class DescribeSavingsPlansUsageDetailRequestFilterParamTags(DaraModel):
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

class DescribeSavingsPlansUsageDetailRequestFilterParamDimensions(DaraModel):
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

