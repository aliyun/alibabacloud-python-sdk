# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyRuleRequest(DaraModel):
    def __init__(
        self,
        category: int = None,
        content: str = None,
        id: int = None,
        lang: str = None,
        match_type: int = None,
        model_rule_ids: str = None,
        name: str = None,
        product_code: str = None,
        product_id: int = None,
        risk_level_id: int = None,
        rule_type: int = None,
        support_form: int = None,
        template_rule_ids: str = None,
        warn_level: int = None,
    ):
        # The content type of the sensitive data detection rule. Valid values:
        # 
        # *   **2**: regular expression
        # *   **3**: algorithm
        # *   **5**: keyword
        self.category = category
        # The content of the sensitive data detection rule. You can specify a regular expression, an algorithm, or keywords that are used to match sensitive fields or text.
        # 
        # This parameter is required.
        self.content = content
        # The ID of the sensitive data detection rule.
        # 
        # You can call the [DescribeRules](~~DescribeRules~~) operation to obtain the rule ID.
        # 
        # This parameter is required.
        self.id = id
        # The language of the content within the request and response. Default value: **zh_cn**. Valid values:
        # 
        # *   **zh_cn**: Simplified Chinese
        # *   **en_us**: English
        self.lang = lang
        # The match type. Valid values:
        # 
        # *   **1**: rule-based match
        # *   **2**: dictionary-based match
        self.match_type = match_type
        # The IDs of the models for sensitive data audit.
        self.model_rule_ids = model_rule_ids
        # The name of the sensitive data detection rule.
        # 
        # You can call the [DescribeRules](~~DescribeRules~~) operation to obtain the rule name.
        # 
        # This parameter is required.
        self.name = name
        # The service to which the sensitive data detection rule is applied. Valid values include **MaxCompute, OSS, ADS, OTS, and RDS**.
        self.product_code = product_code
        # The ID of the service to which the sensitive data detection rule is applied. Valid values include **1**, **2**, **3**, **4**, and **5**. The value 1 indicates MaxCompute. The value 2 indicates Object Storage Service (OSS). The value 3 indicates AnalyticDB for MySQL. The value 4 indicates Tablestore. The value 5 indicates ApsaraDB RDS.
        self.product_id = product_id
        # The sensitivity level of the sensitive data that hits the sensitive data detection rule. Valid values:
        # 
        # *   **1**: N/A, which indicates that no sensitive data is detected.
        # *   **2**: S1, which indicates the low sensitivity level.
        # *   **3**: S2, which indicates the medium sensitivity level.
        # *   **4**: S3, which indicates the high sensitivity level.
        # *   **5**: S4, which indicates the highest sensitivity level.
        self.risk_level_id = risk_level_id
        # The type of the sensitive data detection rule. Valid values:
        # 
        # *   **1**: data detection rule
        # *   **2**: audit rule
        # *   **3**: anomalous event detection rule
        self.rule_type = rule_type
        # The data assets supported by the sensitive data detection rule. Valid values:
        # 
        # *   **0**: all data assets
        # *   **1**: structured data assets
        # *   **2**: unstructured data assets
        self.support_form = support_form
        # The IDs of the templates that are used to audit sensitive data.
        self.template_rule_ids = template_rule_ids
        # The risk level of the alert that is triggered by the sensitive data detection rule. Valid values:
        # 
        # *   **1**: low level
        # *   **2**: medium level
        # *   **3**: high level
        self.warn_level = warn_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.content is not None:
            result['Content'] = self.content

        if self.id is not None:
            result['Id'] = self.id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.match_type is not None:
            result['MatchType'] = self.match_type

        if self.model_rule_ids is not None:
            result['ModelRuleIds'] = self.model_rule_ids

        if self.name is not None:
            result['Name'] = self.name

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        if self.support_form is not None:
            result['SupportForm'] = self.support_form

        if self.template_rule_ids is not None:
            result['TemplateRuleIds'] = self.template_rule_ids

        if self.warn_level is not None:
            result['WarnLevel'] = self.warn_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')

        if m.get('ModelRuleIds') is not None:
            self.model_rule_ids = m.get('ModelRuleIds')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('SupportForm') is not None:
            self.support_form = m.get('SupportForm')

        if m.get('TemplateRuleIds') is not None:
            self.template_rule_ids = m.get('TemplateRuleIds')

        if m.get('WarnLevel') is not None:
            self.warn_level = m.get('WarnLevel')

        return self

