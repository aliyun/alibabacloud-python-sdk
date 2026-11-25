# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeHybridCloudClusterRuleResponseBody(DaraModel):
    def __init__(
        self,
        cluster_rule: main_models.DescribeHybridCloudClusterRuleResponseBodyClusterRule = None,
        request_id: str = None,
    ):
        # The rule information.
        self.cluster_rule = cluster_rule
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.cluster_rule:
            self.cluster_rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_rule is not None:
            result['ClusterRule'] = self.cluster_rule.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterRule') is not None:
            temp_model = main_models.DescribeHybridCloudClusterRuleResponseBodyClusterRule()
            self.cluster_rule = temp_model.from_map(m.get('ClusterRule'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeHybridCloudClusterRuleResponseBodyClusterRule(DaraModel):
    def __init__(
        self,
        cluster_rule_resource_id: str = None,
        rule_config: str = None,
        rule_status: str = None,
        rule_type: str = None,
    ):
        # The ID of the cluster rule resource.
        self.cluster_rule_resource_id = cluster_rule_resource_id
        # The traffic diversion rule configuration:
        # 
        # - **check_mode**: The mode selection. Valid values:
        #   - **all**: full traffic diversion
        #   - **part**: specified partial traffic diversion
        # - **type**: The rule match type. Valid values:
        #   - **exact**: exact match
        #   - **regex**: regular expression
        # - **substance**: The rule value.
        self.rule_config = rule_config
        # The rule status. Valid values:
        # 
        # - **on**: Enabled.
        # 
        # - **off**: Disabled.
        self.rule_status = rule_status
        # The rule type. Valid values:
        # 
        # - pullin: traffic diversion rule
        self.rule_type = rule_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_rule_resource_id is not None:
            result['ClusterRuleResourceId'] = self.cluster_rule_resource_id

        if self.rule_config is not None:
            result['RuleConfig'] = self.rule_config

        if self.rule_status is not None:
            result['RuleStatus'] = self.rule_status

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterRuleResourceId') is not None:
            self.cluster_rule_resource_id = m.get('ClusterRuleResourceId')

        if m.get('RuleConfig') is not None:
            self.rule_config = m.get('RuleConfig')

        if m.get('RuleStatus') is not None:
            self.rule_status = m.get('RuleStatus')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        return self

