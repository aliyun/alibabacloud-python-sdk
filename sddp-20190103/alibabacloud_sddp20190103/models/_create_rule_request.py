# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRuleRequest(DaraModel):
    def __init__(
        self,
        category: int = None,
        content: str = None,
        content_category: int = None,
        description: str = None,
        lang: str = None,
        match_type: int = None,
        model_rule_ids: str = None,
        name: str = None,
        product_code: str = None,
        product_id: int = None,
        risk_level_id: int = None,
        rule_type: int = None,
        source_ip: str = None,
        stat_express: str = None,
        status: int = None,
        support_form: int = None,
        target: str = None,
        template_rule_ids: str = None,
        warn_level: int = None,
    ):
        # The content type of the sensitive data detection rule. Valid values:
        # 
        # *   **0**: keyword
        # *   **2**: regular expression
        self.category = category
        # The content of the sensitive data detection rule. You can specify a regular expression or keywords that are used to match sensitive fields or text.
        # 
        # This parameter is required.
        self.content = content
        # The type of the content in the sensitive data detection rule. Valid values include **1**, **2**, **3**, **4**, and **5**. The value 1 indicates attempts to exploit SQL injections. The value 2 indicates bypass by using SQL injections. The value 3 indicates abuse of stored procedures. The value 4 indicates buffer overflow. The value 5 indicates SQL injections based on errors.
        self.content_category = content_category
        # The description of the rule.
        self.description = description
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
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
        # This parameter is required.
        self.name = name
        # The name of the service to which data in the column of the table belongs. Valid values include **MaxCompute**, **OSS**, **ADS**, **OTS**, and **RDS**.
        self.product_code = product_code
        # The ID of the service to which the data asset belongs. Valid values include **1**, **2**, **3**, **4**, and **5**. The value 1 indicates MaxCompute. The value 2 indicates Object Storage Service (OSS). The value 3 indicates AnalyticDB for MySQL. The value 4 indicates Tablestore. The value 5 indicates ApsaraDB RDS.
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
        # *   **1**: sensitive data detection rule
        # *   **2**: audit rule
        # *   **3**: anomalous event detection rule
        # *   **99**: custom rule
        self.rule_type = rule_type
        # This parameter is deprecated.
        self.source_ip = source_ip
        # The statistical expression.
        self.stat_express = stat_express
        # Specifies whether to enable the sensitive data detection rule. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.status = status
        # The type of the data asset. Valid values:
        # 
        # *   **0**: all data assets
        # *   **1**: structured data asset
        # *   **2**: unstructured data asset
        # 
        # > If you set the parameter to 1 or 2, rules that support all data assets and rules that support the queried data asset type are returned.
        self.support_form = support_form
        # The code of the service to which the sensitive data detection rule is applied. Valid values include **MaxCompute**, **OSS**, **ADS**, **OTS**, and **RDS**.
        self.target = target
        # The IDs of the templates that are used to audit sensitive data.
        self.template_rule_ids = template_rule_ids
        # The risk level of the alert that is triggered. Valid values:
        # 
        # *   **1**: low
        # *   **2**: medium
        # *   **3**: high
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

        if self.content_category is not None:
            result['ContentCategory'] = self.content_category

        if self.description is not None:
            result['Description'] = self.description

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

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.stat_express is not None:
            result['StatExpress'] = self.stat_express

        if self.status is not None:
            result['Status'] = self.status

        if self.support_form is not None:
            result['SupportForm'] = self.support_form

        if self.target is not None:
            result['Target'] = self.target

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

        if m.get('ContentCategory') is not None:
            self.content_category = m.get('ContentCategory')

        if m.get('Description') is not None:
            self.description = m.get('Description')

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

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('StatExpress') is not None:
            self.stat_express = m.get('StatExpress')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SupportForm') is not None:
            self.support_form = m.get('SupportForm')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('TemplateRuleIds') is not None:
            self.template_rule_ids = m.get('TemplateRuleIds')

        if m.get('WarnLevel') is not None:
            self.warn_level = m.get('WarnLevel')

        return self

