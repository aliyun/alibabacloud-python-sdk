# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnWafGroupsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        waf_groups: List[main_models.DescribeDcdnWafGroupsResponseBodyWafGroups] = None,
    ):
        # The page number of the returned page. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: **20**.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The number of WAF rule groups.
        self.total_count = total_count
        # The list of WAF rule groups.
        self.waf_groups = waf_groups

    def validate(self):
        if self.waf_groups:
            for v1 in self.waf_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['WafGroups'] = []
        if self.waf_groups is not None:
            for k1 in self.waf_groups:
                result['WafGroups'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.waf_groups = []
        if m.get('WafGroups') is not None:
            for k1 in m.get('WafGroups'):
                temp_model = main_models.DescribeDcdnWafGroupsResponseBodyWafGroups()
                self.waf_groups.append(temp_model.from_map(k1))

        return self

class DescribeDcdnWafGroupsResponseBodyWafGroups(DaraModel):
    def __init__(
        self,
        gmt_modified: str = None,
        id: int = None,
        name: str = None,
        policies: List[main_models.DescribeDcdnWafGroupsResponseBodyWafGroupsPolicies] = None,
        rule_count: int = None,
        subscribe: str = None,
        template_id: int = None,
    ):
        # The time when the WAF rule group was modified.
        self.gmt_modified = gmt_modified
        # The ID of the custom WAF rule group.
        self.id = id
        # The name of the WAF rule.
        self.name = name
        # The policy that is associated with the WAF rule group.
        self.policies = policies
        # The number of WAF rules.
        self.rule_count = rule_count
        # Indicates whether to enable subscription. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.subscribe = subscribe
        # The ID of the template.
        self.template_id = template_id

    def validate(self):
        if self.policies:
            for v1 in self.policies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        result['Policies'] = []
        if self.policies is not None:
            for k1 in self.policies:
                result['Policies'].append(k1.to_map() if k1 else None)

        if self.rule_count is not None:
            result['RuleCount'] = self.rule_count

        if self.subscribe is not None:
            result['Subscribe'] = self.subscribe

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.policies = []
        if m.get('Policies') is not None:
            for k1 in m.get('Policies'):
                temp_model = main_models.DescribeDcdnWafGroupsResponseBodyWafGroupsPolicies()
                self.policies.append(temp_model.from_map(k1))

        if m.get('RuleCount') is not None:
            self.rule_count = m.get('RuleCount')

        if m.get('Subscribe') is not None:
            self.subscribe = m.get('Subscribe')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

class DescribeDcdnWafGroupsResponseBodyWafGroupsPolicies(DaraModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
        type: str = None,
    ):
        # The ID of the policy.
        self.id = id
        # The name of the policy.
        self.name = name
        # The type of the policy. Valid values:
        # 
        # *   **custom**: a custom policy
        # *   **default**: the default policy
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

