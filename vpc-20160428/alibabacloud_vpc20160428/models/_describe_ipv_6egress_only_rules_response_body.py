# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeIpv6EgressOnlyRulesResponseBody(DaraModel):
    def __init__(
        self,
        ipv_6egress_only_rules: main_models.DescribeIpv6EgressOnlyRulesResponseBodyIpv6EgressOnlyRules = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The details about the egress-only rules.
        self.ipv_6egress_only_rules = ipv_6egress_only_rules
        # The number of the returned page. Default value: **1**.
        self.page_number = page_number
        # The number of entries returned per page. Maximum value: **50**. Default value: **10**.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.ipv_6egress_only_rules:
            self.ipv_6egress_only_rules.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_6egress_only_rules is not None:
            result['Ipv6EgressOnlyRules'] = self.ipv_6egress_only_rules.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ipv6EgressOnlyRules') is not None:
            temp_model = main_models.DescribeIpv6EgressOnlyRulesResponseBodyIpv6EgressOnlyRules()
            self.ipv_6egress_only_rules = temp_model.from_map(m.get('Ipv6EgressOnlyRules'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeIpv6EgressOnlyRulesResponseBodyIpv6EgressOnlyRules(DaraModel):
    def __init__(
        self,
        ipv_6egress_only_rule: List[main_models.DescribeIpv6EgressOnlyRulesResponseBodyIpv6EgressOnlyRulesIpv6EgressOnlyRule] = None,
    ):
        self.ipv_6egress_only_rule = ipv_6egress_only_rule

    def validate(self):
        if self.ipv_6egress_only_rule:
            for v1 in self.ipv_6egress_only_rule:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Ipv6EgressOnlyRule'] = []
        if self.ipv_6egress_only_rule is not None:
            for k1 in self.ipv_6egress_only_rule:
                result['Ipv6EgressOnlyRule'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ipv_6egress_only_rule = []
        if m.get('Ipv6EgressOnlyRule') is not None:
            for k1 in m.get('Ipv6EgressOnlyRule'):
                temp_model = main_models.DescribeIpv6EgressOnlyRulesResponseBodyIpv6EgressOnlyRulesIpv6EgressOnlyRule()
                self.ipv_6egress_only_rule.append(temp_model.from_map(k1))

        return self

class DescribeIpv6EgressOnlyRulesResponseBodyIpv6EgressOnlyRulesIpv6EgressOnlyRule(DaraModel):
    def __init__(
        self,
        description: str = None,
        instance_id: str = None,
        instance_type: str = None,
        ipv_6egress_only_rule_id: str = None,
        name: str = None,
        status: str = None,
    ):
        # The description of the egress-only rule.
        self.description = description
        # The ID of the instance to which the egress-only rule applies.
        self.instance_id = instance_id
        # The type of the instance to which the egress-only rule applies.
        self.instance_type = instance_type
        # The ID of the egress-only rule.
        self.ipv_6egress_only_rule_id = ipv_6egress_only_rule_id
        # The name of the egress-only rule.
        self.name = name
        # The status of the egress-only rule.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.ipv_6egress_only_rule_id is not None:
            result['Ipv6EgressOnlyRuleId'] = self.ipv_6egress_only_rule_id

        if self.name is not None:
            result['Name'] = self.name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Ipv6EgressOnlyRuleId') is not None:
            self.ipv_6egress_only_rule_id = m.get('Ipv6EgressOnlyRuleId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

