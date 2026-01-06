# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_selectdb20230522 import models as main_models
from darabonba.model import DaraModel

class ModifyElasticRuleResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ModifyElasticRuleResponseBodyData = None,
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
            temp_model = main_models.ModifyElasticRuleResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ModifyElasticRuleResponseBodyData(DaraModel):
    def __init__(
        self,
        cluster_class: str = None,
        cluster_id: str = None,
        db_instance_id: str = None,
        elastic_rule_start_time: str = None,
        execution_period: str = None,
        rule_id: int = None,
    ):
        # The rule for computing resources of the required cluster.
        self.cluster_class = cluster_class
        # The cluster ID.
        self.cluster_id = cluster_id
        # The instance ID.
        self.db_instance_id = db_instance_id
        # The time when the scheduled scaling rule is executed.
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

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id

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

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')

        if m.get('ElasticRuleStartTime') is not None:
            self.elastic_rule_start_time = m.get('ElasticRuleStartTime')

        if m.get('ExecutionPeriod') is not None:
            self.execution_period = m.get('ExecutionPeriod')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        return self

