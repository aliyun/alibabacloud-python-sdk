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
        # The content type of the sensitive data detection rule. Valid values:
        # 
        # *   **0**: keyword
        # *   **2**: regular expression
        self.category = category
        # The type of the content in the sensitive data detection rule. Valid values include **1**, **2**, **3**, **4**, and **5**. The value 1 indicates attempts to exploit SQL injections. The value 2 indicates bypass by using SQL injections. The value 3 indicates abuse of stored procedures. The value 4 indicates buffer overflow. The value 5 indicates SQL injections based on errors.
        self.content_category = content_category
        # The external cooperation channel. Valid values:
        # 
        # *   DAS
        # *   YAOCHI
        self.cooperation_channel = cooperation_channel
        # The page number of the page to return.
        self.current_page = current_page
        # The type of the sensitive data detection rule. Valid values:
        # 
        # *   **0**: built-in rule
        # *   **1**: custom rule
        self.custom_type = custom_type
        # This parameter is deprecated.
        self.feature_type = feature_type
        # The parent group type of the rule.
        self.group_id = group_id
        # Specifies whether to allow earlier versions of request parameters to support keywords that are supported in later versions of request parameters. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        # 
        # > To specify keywords as the content type of the sensitive data detection rule, you can set the Category parameter to 0 for earlier versions of request parameters and set the Category parameter to 5 for later versions of request parameters. You can specify the KeywordCompatible parameter based on your business requirements.
        self.keyword_compatible = keyword_compatible
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The match type. Valid values:
        # 
        # *   1: rule-based match
        # *   2: dictionary-based match
        self.match_type = match_type
        # The name of the sensitive data detection rule. Fuzzy match is supported.
        self.name = name
        # The number of entries to return on each page.
        self.page_size = page_size
        # The name of the service to which the data asset belongs. Valid values include **MaxCompute, OSS, ADS, OTS, and RDS**.
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
        # *   **1**: sensitive data detection rule
        # *   **2**: audit rule
        # *   **3**: anomalous event detection rule
        # *   **99**: custom rule
        self.rule_type = rule_type
        # Specifies whether to query a simplified rule. The simplified rule contains only the rule name. Valid values:
        # 
        # *   true
        # *   false
        self.simplify = simplify
        # The status of the sensitive data detection rule. Valid values:
        # 
        # *   **1**: enabled
        # *   **0**: disabled
        self.status = status
        # The type of the data asset. Valid values:
        # 
        # *   **0**: all data assets
        # *   **1**: structured data asset
        # *   **2**: unstructured data asset
        # 
        # > If you set the parameter to 1 or 2, rules that support all data assets and rules that support the queried data asset type are returned.
        self.support_form = support_form
        # The severity level of the alert. Valid values:
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

