# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_selectdb20230522 import models as main_models
from darabonba.model import DaraModel

class DescribeElasticRulesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeElasticRulesResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeElasticRulesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeElasticRulesResponseBodyData(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        db_instance_id: str = None,
        rules: List[main_models.DescribeElasticRulesResponseBodyDataRules] = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The instance ID.
        self.db_instance_id = db_instance_id
        # The details of the rules.
        self.rules = rules

    def validate(self):
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.DescribeElasticRulesResponseBodyDataRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class DescribeElasticRulesResponseBodyDataRules(DaraModel):
    def __init__(
        self,
        cluster_class: str = None,
        elastic_rule_start_time: str = None,
        execution_period: str = None,
        rule_id: int = None,
    ):
        # The rule for computing resources of the required cluster.
        self.cluster_class = cluster_class
        # The time when you want to execute the scheduled scaling rule.
        self.elastic_rule_start_time = elastic_rule_start_time
        # The execution cycle.
        # 
        # Valid value:
        # 
        # *   Day
        self.execution_period = execution_period
        # The rule ID.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_class is not None:
            result['ClusterClass'] = self.cluster_class

        if self.elastic_rule_start_time is not None:
            result['ElasticRuleStartTime'] = self.elastic_rule_start_time

        if self.execution_period is not None:
            result['ExecutionPeriod'] = self.execution_period

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterClass') is not None:
            self.cluster_class = m.get('ClusterClass')

        if m.get('ElasticRuleStartTime') is not None:
            self.elastic_rule_start_time = m.get('ElasticRuleStartTime')

        if m.get('ExecutionPeriod') is not None:
            self.execution_period = m.get('ExecutionPeriod')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        return self

