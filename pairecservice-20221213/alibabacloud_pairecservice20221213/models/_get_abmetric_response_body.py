# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetABMetricResponseBody(DaraModel):
    def __init__(
        self,
        aggregation_by_user: bool = None,
        definition: str = None,
        denominator: str = None,
        description: str = None,
        is_binomial_distribution: bool = None,
        left_metric_id: str = None,
        name: str = None,
        need_significance: bool = None,
        numerator: str = None,
        operator: str = None,
        realtime: str = None,
        request_id: str = None,
        result_resource_id: str = None,
        result_table_meta_id: str = None,
        right_metric_id: str = None,
        scene_id: str = None,
        scene_name: str = None,
        statistics_cycle: int = None,
        table_meta_id: str = None,
        type: str = None,
    ):
        # Indicates whether to calculate significance by user dimension. Two aggregation logics are available: by user and by sample.
        self.aggregation_by_user = aggregation_by_user
        # The definition of the metric.
        self.definition = definition
        # The denominator used for significance calculation.
        self.denominator = denominator
        # The description of the metric.
        self.description = description
        # Indicates whether the metric follows a binomial distribution when the metric type is derived. If yes, the mean and variance of the metric are calculated based on the binomial distribution.
        self.is_binomial_distribution = is_binomial_distribution
        # The ID of the left metric for the derived metric.
        self.left_metric_id = left_metric_id
        # The name of the metric.
        self.name = name
        # Indicates whether to calculate significance.
        self.need_significance = need_significance
        # The numerator used for significance calculation.
        self.numerator = numerator
        # The operator used to calculate the derived metric. Valid values:
        # - Plus: addition
        # - Minus: subtraction
        # - Multiplication: multiplication
        # - Division: division
        self.operator = operator
        # Indicates whether the metric is a real-time metric. Valid values:
        # - true: yes
        # - false: no
        self.realtime = realtime
        # The request ID.
        self.request_id = request_id
        # The ID of the data source for the write-back data table.
        self.result_resource_id = result_resource_id
        # The ID of the data table to which data is written back.
        self.result_table_meta_id = result_table_meta_id
        # The ID of the right metric for the derived metric.
        self.right_metric_id = right_metric_id
        # The scenario ID.
        self.scene_id = scene_id
        # The name of the scenario.
        self.scene_name = scene_name
        # The statistical period.
        self.statistics_cycle = statistics_cycle
        # The ID of the source data table.
        self.table_meta_id = table_meta_id
        # The metric type. Valid values:
        # - Single: single metric
        # - Derived: derived metric
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregation_by_user is not None:
            result['AggregationByUser'] = self.aggregation_by_user

        if self.definition is not None:
            result['Definition'] = self.definition

        if self.denominator is not None:
            result['Denominator'] = self.denominator

        if self.description is not None:
            result['Description'] = self.description

        if self.is_binomial_distribution is not None:
            result['IsBinomialDistribution'] = self.is_binomial_distribution

        if self.left_metric_id is not None:
            result['LeftMetricId'] = self.left_metric_id

        if self.name is not None:
            result['Name'] = self.name

        if self.need_significance is not None:
            result['NeedSignificance'] = self.need_significance

        if self.numerator is not None:
            result['Numerator'] = self.numerator

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.realtime is not None:
            result['Realtime'] = self.realtime

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_resource_id is not None:
            result['ResultResourceId'] = self.result_resource_id

        if self.result_table_meta_id is not None:
            result['ResultTableMetaId'] = self.result_table_meta_id

        if self.right_metric_id is not None:
            result['RightMetricId'] = self.right_metric_id

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.scene_name is not None:
            result['SceneName'] = self.scene_name

        if self.statistics_cycle is not None:
            result['StatisticsCycle'] = self.statistics_cycle

        if self.table_meta_id is not None:
            result['TableMetaId'] = self.table_meta_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregationByUser') is not None:
            self.aggregation_by_user = m.get('AggregationByUser')

        if m.get('Definition') is not None:
            self.definition = m.get('Definition')

        if m.get('Denominator') is not None:
            self.denominator = m.get('Denominator')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('IsBinomialDistribution') is not None:
            self.is_binomial_distribution = m.get('IsBinomialDistribution')

        if m.get('LeftMetricId') is not None:
            self.left_metric_id = m.get('LeftMetricId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NeedSignificance') is not None:
            self.need_significance = m.get('NeedSignificance')

        if m.get('Numerator') is not None:
            self.numerator = m.get('Numerator')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Realtime') is not None:
            self.realtime = m.get('Realtime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultResourceId') is not None:
            self.result_resource_id = m.get('ResultResourceId')

        if m.get('ResultTableMetaId') is not None:
            self.result_table_meta_id = m.get('ResultTableMetaId')

        if m.get('RightMetricId') is not None:
            self.right_metric_id = m.get('RightMetricId')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')

        if m.get('StatisticsCycle') is not None:
            self.statistics_cycle = m.get('StatisticsCycle')

        if m.get('TableMetaId') is not None:
            self.table_meta_id = m.get('TableMetaId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

