# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeCostRulesResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeCostRulesResponseBodyItems] = None,
        page_number: int = None,
        page_record_count: int = None,
        page_size: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # A list of cost rules.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The number of records on the current page.
        self.page_record_count = page_record_count
        # The number of entries returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of records.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeCostRulesResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeCostRulesResponseBodyItems(DaraModel):
    def __init__(
        self,
        cache_cost_points_per_million: str = None,
        cost_rule_id: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        gw_cluster_id: str = None,
        input_cost_points_per_million: str = None,
        model: str = None,
        model_service_id: str = None,
        output_cost_points_per_million: str = None,
    ):
        # The cost in points per one million cached tokens.
        self.cache_cost_points_per_million = cache_cost_points_per_million
        # The cost rule ID.
        self.cost_rule_id = cost_rule_id
        # The time when the cost rule was created.
        self.gmt_created = gmt_created
        # The time when the cost rule was last updated.
        self.gmt_modified = gmt_modified
        # The gateway instance ID.
        self.gw_cluster_id = gw_cluster_id
        # The cost in points per one million input tokens.
        self.input_cost_points_per_million = input_cost_points_per_million
        # The model name.
        self.model = model
        # The model service ID.
        self.model_service_id = model_service_id
        # The cost in points per one million output tokens.
        self.output_cost_points_per_million = output_cost_points_per_million

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cache_cost_points_per_million is not None:
            result['CacheCostPointsPerMillion'] = self.cache_cost_points_per_million

        if self.cost_rule_id is not None:
            result['CostRuleId'] = self.cost_rule_id

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.gw_cluster_id is not None:
            result['GwClusterId'] = self.gw_cluster_id

        if self.input_cost_points_per_million is not None:
            result['InputCostPointsPerMillion'] = self.input_cost_points_per_million

        if self.model is not None:
            result['Model'] = self.model

        if self.model_service_id is not None:
            result['ModelServiceId'] = self.model_service_id

        if self.output_cost_points_per_million is not None:
            result['OutputCostPointsPerMillion'] = self.output_cost_points_per_million

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheCostPointsPerMillion') is not None:
            self.cache_cost_points_per_million = m.get('CacheCostPointsPerMillion')

        if m.get('CostRuleId') is not None:
            self.cost_rule_id = m.get('CostRuleId')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('GwClusterId') is not None:
            self.gw_cluster_id = m.get('GwClusterId')

        if m.get('InputCostPointsPerMillion') is not None:
            self.input_cost_points_per_million = m.get('InputCostPointsPerMillion')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('ModelServiceId') is not None:
            self.model_service_id = m.get('ModelServiceId')

        if m.get('OutputCostPointsPerMillion') is not None:
            self.output_cost_points_per_million = m.get('OutputCostPointsPerMillion')

        return self

