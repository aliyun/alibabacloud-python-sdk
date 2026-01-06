# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyElasticRuleRequest(DaraModel):
    def __init__(
        self,
        cluster_class: str = None,
        cluster_id: str = None,
        db_instance_id: str = None,
        elastic_rule_start_time: str = None,
        execution_period: str = None,
        product: str = None,
        region_id: str = None,
        resource_owner_id: int = None,
        rule_id: int = None,
    ):
        # The rule for computing resources of the required cluster.
        self.cluster_class = cluster_class
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The instance ID.
        # 
        # This parameter is required.
        self.db_instance_id = db_instance_id
        # The time when you want to execute the scheduled scaling rule.
        self.elastic_rule_start_time = elastic_rule_start_time
        # The execution cycle.
        # 
        # Valid value:
        # 
        # *   Day
        self.execution_period = execution_period
        # The cloud service.
        self.product = product
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id
        # The rule ID.
        # 
        # This parameter is required.
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

        if self.product is not None:
            result['Product'] = self.product

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

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

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        return self

