# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_epg20260715 import models as main_models
from darabonba.model import DaraModel

class CreateEgressProxyRuleGroupResponseBody(DaraModel):
    def __init__(
        self,
        egress_proxy_rule_group_id: str = None,
        egress_proxy_rules: main_models.CreateEgressProxyRuleGroupResponseBodyEgressProxyRules = None,
        request_id: str = None,
    ):
        # The ID of the egress proxy rule group.
        self.egress_proxy_rule_group_id = egress_proxy_rule_group_id
        # The list of egress rules grouped by phase (PreDns, PreRequest, and PostResponse).
        self.egress_proxy_rules = egress_proxy_rules
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.egress_proxy_rules:
            self.egress_proxy_rules.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.egress_proxy_rule_group_id is not None:
            result['EgressProxyRuleGroupId'] = self.egress_proxy_rule_group_id

        if self.egress_proxy_rules is not None:
            result['EgressProxyRules'] = self.egress_proxy_rules.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EgressProxyRuleGroupId') is not None:
            self.egress_proxy_rule_group_id = m.get('EgressProxyRuleGroupId')

        if m.get('EgressProxyRules') is not None:
            temp_model = main_models.CreateEgressProxyRuleGroupResponseBodyEgressProxyRules()
            self.egress_proxy_rules = temp_model.from_map(m.get('EgressProxyRules'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateEgressProxyRuleGroupResponseBodyEgressProxyRules(DaraModel):
    def __init__(
        self,
        post_response: List[main_models.CreateEgressProxyRuleGroupResponseBodyEgressProxyRulesPostResponse] = None,
        pre_dns: List[main_models.CreateEgressProxyRuleGroupResponseBodyEgressProxyRulesPreDns] = None,
        pre_request: List[main_models.CreateEgressProxyRuleGroupResponseBodyEgressProxyRulesPreRequest] = None,
    ):
        # The list of rules in the PostResponse stage, which is executed after the response is returned.
        self.post_response = post_response
        # The list of rules in the PreDns stage, which is executed before DNS resolution.
        self.pre_dns = pre_dns
        # The list of rules in the PreRequest stage, which is executed before the request is forwarded.
        self.pre_request = pre_request

    def validate(self):
        if self.post_response:
            for v1 in self.post_response:
                 if v1:
                    v1.validate()
        if self.pre_dns:
            for v1 in self.pre_dns:
                 if v1:
                    v1.validate()
        if self.pre_request:
            for v1 in self.pre_request:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PostResponse'] = []
        if self.post_response is not None:
            for k1 in self.post_response:
                result['PostResponse'].append(k1.to_map() if k1 else None)

        result['PreDns'] = []
        if self.pre_dns is not None:
            for k1 in self.pre_dns:
                result['PreDns'].append(k1.to_map() if k1 else None)

        result['PreRequest'] = []
        if self.pre_request is not None:
            for k1 in self.pre_request:
                result['PreRequest'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.post_response = []
        if m.get('PostResponse') is not None:
            for k1 in m.get('PostResponse'):
                temp_model = main_models.CreateEgressProxyRuleGroupResponseBodyEgressProxyRulesPostResponse()
                self.post_response.append(temp_model.from_map(k1))

        self.pre_dns = []
        if m.get('PreDns') is not None:
            for k1 in m.get('PreDns'):
                temp_model = main_models.CreateEgressProxyRuleGroupResponseBodyEgressProxyRulesPreDns()
                self.pre_dns.append(temp_model.from_map(k1))

        self.pre_request = []
        if m.get('PreRequest') is not None:
            for k1 in m.get('PreRequest'):
                temp_model = main_models.CreateEgressProxyRuleGroupResponseBodyEgressProxyRulesPreRequest()
                self.pre_request.append(temp_model.from_map(k1))

        return self

class CreateEgressProxyRuleGroupResponseBodyEgressProxyRulesPreRequest(DaraModel):
    def __init__(
        self,
        egress_proxy_rule_id: str = None,
        priority: int = None,
    ):
        # The ID of the egress proxy rule.
        self.egress_proxy_rule_id = egress_proxy_rule_id
        # The priority of the egress proxy rule in the stage to which it belongs. Valid values: 1 to 1000. A smaller value indicates a higher priority.
        self.priority = priority

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.egress_proxy_rule_id is not None:
            result['EgressProxyRuleId'] = self.egress_proxy_rule_id

        if self.priority is not None:
            result['Priority'] = self.priority

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EgressProxyRuleId') is not None:
            self.egress_proxy_rule_id = m.get('EgressProxyRuleId')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        return self

class CreateEgressProxyRuleGroupResponseBodyEgressProxyRulesPreDns(DaraModel):
    def __init__(
        self,
        egress_proxy_rule_id: str = None,
        priority: int = None,
    ):
        # The ID of the egress proxy rule.
        self.egress_proxy_rule_id = egress_proxy_rule_id
        # The priority of the egress proxy rule in the stage to which it belongs. Valid values: 1 to 1000. A smaller value indicates a higher priority.
        self.priority = priority

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.egress_proxy_rule_id is not None:
            result['EgressProxyRuleId'] = self.egress_proxy_rule_id

        if self.priority is not None:
            result['Priority'] = self.priority

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EgressProxyRuleId') is not None:
            self.egress_proxy_rule_id = m.get('EgressProxyRuleId')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        return self

class CreateEgressProxyRuleGroupResponseBodyEgressProxyRulesPostResponse(DaraModel):
    def __init__(
        self,
        egress_proxy_rule_id: str = None,
        priority: int = None,
    ):
        # The ID of the egress proxy rule.
        self.egress_proxy_rule_id = egress_proxy_rule_id
        # The priority of the egress proxy rule in the stage to which it belongs. Valid values: 1 to 1000. A smaller value indicates a higher priority.
        self.priority = priority

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.egress_proxy_rule_id is not None:
            result['EgressProxyRuleId'] = self.egress_proxy_rule_id

        if self.priority is not None:
            result['Priority'] = self.priority

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EgressProxyRuleId') is not None:
            self.egress_proxy_rule_id = m.get('EgressProxyRuleId')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        return self

