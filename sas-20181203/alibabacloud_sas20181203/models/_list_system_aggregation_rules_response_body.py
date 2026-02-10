# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListSystemAggregationRulesResponseBody(DaraModel):
    def __init__(
        self,
        aggregation_list: List[main_models.ListSystemAggregationRulesResponseBodyAggregationList] = None,
        page_info: main_models.ListSystemAggregationRulesResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # An array that consists of the details about the aggregation types.
        self.aggregation_list = aggregation_list
        # The pagination information.
        self.page_info = page_info
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.aggregation_list:
            for v1 in self.aggregation_list:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AggregationList'] = []
        if self.aggregation_list is not None:
            for k1 in self.aggregation_list:
                result['AggregationList'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.aggregation_list = []
        if m.get('AggregationList') is not None:
            for k1 in m.get('AggregationList'):
                temp_model = main_models.ListSystemAggregationRulesResponseBodyAggregationList()
                self.aggregation_list.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.ListSystemAggregationRulesResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListSystemAggregationRulesResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListSystemAggregationRulesResponseBodyAggregationList(DaraModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
        rule_count: int = None,
    ):
        # The ID of the aggregation type.
        self.id = id
        # The name of the aggregation type.
        self.name = name
        # The number of rules that are of the aggregation type.
        self.rule_count = rule_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.rule_count is not None:
            result['RuleCount'] = self.rule_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RuleCount') is not None:
            self.rule_count = m.get('RuleCount')

        return self

