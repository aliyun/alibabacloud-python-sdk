# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeRelatedDefenseRulesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        rules: List[main_models.DescribeRelatedDefenseRulesResponseBodyRules] = None,
        total_count: int = None,
    ):
        # The number of entries to return on each page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The token that is used to query the next page of results. If more results are available, this parameter is returned.
        # 
        # > If this parameter is returned, more results are available. Use the returned NextToken value as a request parameter to retrieve the next page of data. Repeat this process until the **NextToken** parameter is not returned. This indicates that all data has been retrieved.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The list of associated rules.
        self.rules = rules
        # The total number of entries returned.
        self.total_count = total_count

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
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.DescribeRelatedDefenseRulesResponseBodyRules()
                self.rules.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeRelatedDefenseRulesResponseBodyRules(DaraModel):
    def __init__(
        self,
        defense_scene: str = None,
        defense_type: str = None,
        rule_id: int = None,
        rule_name: str = None,
        template_id: int = None,
    ):
        # The protection scenario of the rule. For more information, see the description of the **DefenseScene** parameter in [DescribeDefenseRules](https://help.aliyun.com/document_detail/461426.html).
        self.defense_scene = defense_scene
        # The type of the protection rule. Valid values:
        # 
        # - **template** (default): a template rule.
        # 
        # - **resource**: a rule for a protected object.
        # 
        # - **global**: a global rule.
        self.defense_type = defense_type
        # The ID of the protection rule.
        self.rule_id = rule_id
        # The name of the protection rule.
        self.rule_name = rule_name
        # The ID of the protection template.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.defense_scene is not None:
            result['DefenseScene'] = self.defense_scene

        if self.defense_type is not None:
            result['DefenseType'] = self.defense_type

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefenseScene') is not None:
            self.defense_scene = m.get('DefenseScene')

        if m.get('DefenseType') is not None:
            self.defense_type = m.get('DefenseType')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

