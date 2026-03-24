# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeHybridCloudClusterRulesResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeHybridCloudClusterRulesResponseBodyData] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The response data.
        self.data = data
        # The ID of the request.
        self.request_id = request_id
        # The total number of cloud native mode entries returned.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeHybridCloudClusterRulesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeHybridCloudClusterRulesResponseBodyData(DaraModel):
    def __init__(
        self,
        cluster_id: int = None,
        cluster_rule_resource_id: str = None,
        rule_config: str = None,
        rule_type: str = None,
        status: str = None,
        version: int = None,
    ):
        # The ID of the hybrid cloud cluster.
        self.cluster_id = cluster_id
        # The resource ID of the cluster rule.
        self.cluster_rule_resource_id = cluster_rule_resource_id
        # The configuration of the traffic redirection rule:
        # 
        # - **check_mode**
        # 
        #   : the mode. Valid values:
        # 
        #   - **all**: redirects all traffic.
        # 
        #   - **part**: redirects a portion of traffic.
        # 
        # - **type**
        # 
        #   : the match type of the rule. Valid values:
        # 
        #   - **exact**: exact match.
        # 
        #   - **regex**: regular expression match.
        # 
        # - **substance**: the value of the rule.
        self.rule_config = rule_config
        # The type of the rule. Valid value:
        # 
        # - **pullin**: traffic redirection
        self.rule_type = rule_type
        # The status of the rule. Valid values:
        # 
        # - **1**: enabled.
        # 
        # - **0**: disabled.
        self.status = status
        # The version number.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_rule_resource_id is not None:
            result['ClusterRuleResourceId'] = self.cluster_rule_resource_id

        if self.rule_config is not None:
            result['RuleConfig'] = self.rule_config

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        if self.status is not None:
            result['Status'] = self.status

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterRuleResourceId') is not None:
            self.cluster_rule_resource_id = m.get('ClusterRuleResourceId')

        if m.get('RuleConfig') is not None:
            self.rule_config = m.get('RuleConfig')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

