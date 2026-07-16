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
        # The type of the content in the sensitive data detection rule. Valid values:
        # 
        # - **2**: regular expression.
        # 
        # - **3**: algorithm.
        # 
        # - **5**: keyword.
        self.category = category
        # The content of the sensitive data detection rule. The rule can be a regular expression, an algorithm, or a keyword, and matches fields or text that contain sensitive data.
        # 
        # This parameter is required.
        self.content = content
        # The unique ID of the sensitive data detection rule.
        # 
        # You can call the [DescribeRules](~~DescribeRules~~) operation to obtain the ID.
        # 
        # This parameter is required.
        self.id = id
        # The language of the request and response. The default value is **zh_cn**. Valid values:
        # 
        # - **zh_cn**: Simplified Chinese.
        # 
        # - **en_us**: English.
        self.lang = lang
        # The match type. Valid values:
        # 
        # - **1**: rule-based match.
        # 
        # - **2**: dictionary-based match.
        self.match_type = match_type
        # A collection of model IDs for sensitive data auditing.
        self.model_rule_ids = model_rule_ids
        # The name of the sensitive data detection rule.
        # 
        # You can call the [DescribeRules](~~DescribeRules~~) operation to obtain the rule name.
        # 
        # This parameter is required.
        self.name = name
        # The type of the product resource that contains the sensitive data detection rule. Valid values:
        # 
        # - **MaxCompute**.
        # 
        # - **OSS**.
        # 
        # - **ADS**.
        # 
        # - **OTS**.
        # 
        # - **RDS**.
        # 
        # - **SELF_DB**.
        self.product_code = product_code
        # The ID of the product that contains the sensitive data detection rule. Valid values:
        # 
        # - **1**: MaxCompute.
        # 
        # - **2**: OSS.
        # 
        # - **3**: ADS.
        # 
        # - **4**: OTS.
        # 
        # - **5**: RDS.
        # 
        # - **6**: SELF_DB.
        self.product_id = product_id
        # The ID of the risk level for the sensitive data detection rule. Valid values:
        # 
        # - **1**: N/A. No sensitive data is detected.
        # 
        # - **2**: S1. Level 1 sensitive data.
        # 
        # - **3**: S2. Level 2 sensitive data.
        # 
        # - **4**: S3. Level 3 sensitive data.
        # 
        # - **5**: S4. Level 4 sensitive data.
        self.risk_level_id = risk_level_id
        # The type of the sensitive data detection rule. Valid values:
        # 
        # - **1**: data detection rule.
        # 
        # - **2**: audit policy.
        # 
        # - **3**: abnormal event rule.
        self.rule_type = rule_type
        # The type of data asset that the rule supports. Valid values:
        # 
        # - **0**: all assets.
        # 
        # - **1**: structured assets.
        # 
        # - **2**: unstructured assets.
        self.support_form = support_form
        # A collection of template IDs for sensitive data auditing.
        self.template_rule_ids = template_rule_ids
        # The risk level of the sensitive data detection rule. Valid values:
        # 
        # - **1**: low.
        # 
        # - **2**: medium.
        # 
        # - **3**: high.
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

