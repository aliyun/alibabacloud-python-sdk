# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class ListNormalizationRuleCapacitiesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        normalization_rule_capacities: List[main_models.ListNormalizationRuleCapacitiesResponseBodyNormalizationRuleCapacities] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        total_page: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.normalization_rule_capacities = normalization_rule_capacities
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.total_page = total_page

    def validate(self):
        if self.normalization_rule_capacities:
            for v1 in self.normalization_rule_capacities:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['NormalizationRuleCapacities'] = []
        if self.normalization_rule_capacities is not None:
            for k1 in self.normalization_rule_capacities:
                result['NormalizationRuleCapacities'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.normalization_rule_capacities = []
        if m.get('NormalizationRuleCapacities') is not None:
            for k1 in m.get('NormalizationRuleCapacities'):
                temp_model = main_models.ListNormalizationRuleCapacitiesResponseBodyNormalizationRuleCapacities()
                self.normalization_rule_capacities.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class ListNormalizationRuleCapacitiesResponseBodyNormalizationRuleCapacities(DaraModel):
    def __init__(
        self,
        capacities: List[str] = None,
        capacity_type: str = None,
        normalization_rule_id: str = None,
    ):
        self.capacities = capacities
        self.capacity_type = capacity_type
        self.normalization_rule_id = normalization_rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capacities is not None:
            result['Capacities'] = self.capacities

        if self.capacity_type is not None:
            result['CapacityType'] = self.capacity_type

        if self.normalization_rule_id is not None:
            result['NormalizationRuleId'] = self.normalization_rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capacities') is not None:
            self.capacities = m.get('Capacities')

        if m.get('CapacityType') is not None:
            self.capacity_type = m.get('CapacityType')

        if m.get('NormalizationRuleId') is not None:
            self.normalization_rule_id = m.get('NormalizationRuleId')

        return self

