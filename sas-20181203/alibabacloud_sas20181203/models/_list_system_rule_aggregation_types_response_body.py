# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListSystemRuleAggregationTypesResponseBody(DaraModel):
    def __init__(
        self,
        aggregation_type_list: List[main_models.ListSystemRuleAggregationTypesResponseBodyAggregationTypeList] = None,
        request_id: str = None,
    ):
        # An array that consists of the aggregation types.
        self.aggregation_type_list = aggregation_type_list
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.aggregation_type_list:
            for v1 in self.aggregation_type_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AggregationTypeList'] = []
        if self.aggregation_type_list is not None:
            for k1 in self.aggregation_type_list:
                result['AggregationTypeList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.aggregation_type_list = []
        if m.get('AggregationTypeList') is not None:
            for k1 in m.get('AggregationTypeList'):
                temp_model = main_models.ListSystemRuleAggregationTypesResponseBodyAggregationTypeList()
                self.aggregation_type_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListSystemRuleAggregationTypesResponseBodyAggregationTypeList(DaraModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
    ):
        # The ID of the aggregation type.
        self.id = id
        # The name of the aggregation type.
        self.name = name

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

