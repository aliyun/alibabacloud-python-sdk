# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRulesRequest(DaraModel):
    def __init__(
        self,
        category: int = None,
        content_category: int = None,
        cooperation_channel: str = None,
        current_page: int = None,
        custom_type: int = None,
        feature_type: int = None,
        group_id: str = None,
        keyword_compatible: bool = None,
        lang: str = None,
        match_type: int = None,
        name: str = None,
        page_size: int = None,
        product_code: int = None,
        product_id: int = None,
        risk_level_id: int = None,
        rule_type: int = None,
        simplify: bool = None,
        status: int = None,
        support_form: int = None,
        warn_level: int = None,
    ):
        # The type of content in the sensitive data detection rule. Valid values:
        # 
        # - **0**: keyword
        # 
        # - **2**: regular expression
        self.category = category
        # The content type. Valid values:
        # 
        # - **1**: SQL injection exploits
        # 
        # - **2**: SQL injection bypass attempts
        # 
        # - **3**: stored procedure abuse
        # 
        # - **4**: buffer overflows
        # 
        # - **5**: error-based SQL injections
        self.content_category = content_category
        # The source of the external cooperation request. Valid values:
        # 
        # - DAS
        # 
        # - YAOCHI
        self.cooperation_channel = cooperation_channel
        # The page number of the paged query.
        self.current_page = current_page
        # The type of the sensitive data detection rule. Valid values:
        # 
        # - **0**: built-in
        # 
        # - **1**: custom
        self.custom_type = custom_type
        # This parameter is deprecated.
        self.feature_type = feature_type
        # The parent group of the rule.
        self.group_id = group_id
        # Specifies whether the keyword is compatible with earlier versions. Valid values:
        # 
        # - **true**
        # 
        # - **false**
        # 
        # > In earlier versions, the Category parameter for keywords had a value of 0. In the current version, it has a value of 5. Enable this parameter based on your business needs.
        self.keyword_compatible = keyword_compatible
        # The language of the request and response messages. Valid values:
        # 
        # - **zh**: Chinese
        # 
        # - **en**: English
        self.lang = lang
        # The match type. Valid values:
        # 
        # - 1: rule-based match
        # 
        # - 2: dictionary-based match
        self.match_type = match_type
        # The name of the sensitive data detection rule. Fuzzy match is supported.
        self.name = name
        # The number of entries to return on each page.
        self.page_size = page_size
        # The name of the service to which the data asset belongs. Valid values:
        # 
        # - **MaxCompute**
        # 
        # - **OSS**
        # 
        # - **ADS**
        # 
        # - **OTS**
        # 
        # - **RDS**
        # 
        # - **SELF_DB**
        self.product_code = product_code
        # The ID of the service to which the data asset belongs. Valid values:
        # 
        # - **1**: MaxCompute
        # 
        # - **2**: OSS
        # 
        # - **3**: ADS
        # 
        # - **4**: OTS
        # 
        # - **5**: RDS
        # 
        # - **6**: SELF_DB
        self.product_id = product_id
        # The sensitivity level ID of the sensitive data detection rule. Valid values:
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
        # - **1**: data detection rule
        # 
        # - **2**: audit policy
        # 
        # - **3**: anomaly detection rule
        # 
        # - **99**: custom rule
        self.rule_type = rule_type
        # Specifies whether to return a simplified version of the rule that contains only the rule name. Valid values:
        # 
        # - true
        # 
        # - false
        self.simplify = simplify
        # The status. Valid values:
        # 
        # - **1**: Normal
        # 
        # - **0**: Disabled
        self.status = status
        # The type of data asset that the rule supports. Valid values:
        # 
        # - **0**: all assets
        # 
        # - **1**: structured assets
        # 
        # - **2**: unstructured assets
        # 
        # > When you query for rules that support structured or unstructured assets, the response also includes rules that support all asset types.
        self.support_form = support_form
        # The risk level.
        # 
        # - **1**: Low
        # 
        # - **2**: Medium
        # 
        # - **3**: High
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

        if self.content_category is not None:
            result['ContentCategory'] = self.content_category

        if self.cooperation_channel is not None:
            result['CooperationChannel'] = self.cooperation_channel

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.custom_type is not None:
            result['CustomType'] = self.custom_type

        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.keyword_compatible is not None:
            result['KeywordCompatible'] = self.keyword_compatible

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.match_type is not None:
            result['MatchType'] = self.match_type

        if self.name is not None:
            result['Name'] = self.name

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        if self.simplify is not None:
            result['Simplify'] = self.simplify

        if self.status is not None:
            result['Status'] = self.status

        if self.support_form is not None:
            result['SupportForm'] = self.support_form

        if self.warn_level is not None:
            result['WarnLevel'] = self.warn_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('ContentCategory') is not None:
            self.content_category = m.get('ContentCategory')

        if m.get('CooperationChannel') is not None:
            self.cooperation_channel = m.get('CooperationChannel')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('CustomType') is not None:
            self.custom_type = m.get('CustomType')

        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('KeywordCompatible') is not None:
            self.keyword_compatible = m.get('KeywordCompatible')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('Simplify') is not None:
            self.simplify = m.get('Simplify')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SupportForm') is not None:
            self.support_form = m.get('SupportForm')

        if m.get('WarnLevel') is not None:
            self.warn_level = m.get('WarnLevel')

        return self

