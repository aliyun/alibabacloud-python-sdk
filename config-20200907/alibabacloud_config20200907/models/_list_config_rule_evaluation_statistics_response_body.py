# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class ListConfigRuleEvaluationStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        evaluation_results: List[main_models.ListConfigRuleEvaluationStatisticsResponseBodyEvaluationResults] = None,
        request_id: str = None,
    ):
        # The statistics of compliance evaluation results.
        self.evaluation_results = evaluation_results
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.evaluation_results:
            for v1 in self.evaluation_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EvaluationResults'] = []
        if self.evaluation_results is not None:
            for k1 in self.evaluation_results:
                result['EvaluationResults'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.evaluation_results = []
        if m.get('EvaluationResults') is not None:
            for k1 in m.get('EvaluationResults'):
                temp_model = main_models.ListConfigRuleEvaluationStatisticsResponseBodyEvaluationResults()
                self.evaluation_results.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListConfigRuleEvaluationStatisticsResponseBodyEvaluationResults(DaraModel):
    def __init__(
        self,
        non_compliant_resource_cnt: int = None,
        non_compliant_rule_cnt: int = None,
        statistic_date: str = None,
        total_resource_cnt: int = None,
        total_rule_cnt: int = None,
    ):
        # The number of resources that are evaluated as non-compliant.
        self.non_compliant_resource_cnt = non_compliant_resource_cnt
        # The number of rules based on which resources are evaluated as non-compliant.
        self.non_compliant_rule_cnt = non_compliant_rule_cnt
        # The date on which the statistics are obtained.
        self.statistic_date = statistic_date
        # The total number of resources.
        self.total_resource_cnt = total_resource_cnt
        # The total number of rules.
        self.total_rule_cnt = total_rule_cnt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.non_compliant_resource_cnt is not None:
            result['NonCompliantResourceCnt'] = self.non_compliant_resource_cnt

        if self.non_compliant_rule_cnt is not None:
            result['NonCompliantRuleCnt'] = self.non_compliant_rule_cnt

        if self.statistic_date is not None:
            result['StatisticDate'] = self.statistic_date

        if self.total_resource_cnt is not None:
            result['TotalResourceCnt'] = self.total_resource_cnt

        if self.total_rule_cnt is not None:
            result['TotalRuleCnt'] = self.total_rule_cnt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NonCompliantResourceCnt') is not None:
            self.non_compliant_resource_cnt = m.get('NonCompliantResourceCnt')

        if m.get('NonCompliantRuleCnt') is not None:
            self.non_compliant_rule_cnt = m.get('NonCompliantRuleCnt')

        if m.get('StatisticDate') is not None:
            self.statistic_date = m.get('StatisticDate')

        if m.get('TotalResourceCnt') is not None:
            self.total_resource_cnt = m.get('TotalResourceCnt')

        if m.get('TotalRuleCnt') is not None:
            self.total_rule_cnt = m.get('TotalRuleCnt')

        return self

