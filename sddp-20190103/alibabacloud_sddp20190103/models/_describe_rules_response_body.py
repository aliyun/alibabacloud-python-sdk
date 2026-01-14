# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sddp20190103 import models as main_models
from darabonba.model import DaraModel

class DescribeRulesResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[main_models.DescribeRulesResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.current_page = current_page
        # The sensitive data detection rules.
        self.items = items
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeRulesResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeRulesResponseBodyItems(DaraModel):
    def __init__(
        self,
        audit_mode: int = None,
        category: int = None,
        category_name: str = None,
        content: str = None,
        content_category: str = None,
        custom_type: int = None,
        description: str = None,
        display_name: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        group_id: str = None,
        hit_total_count: int = None,
        id: int = None,
        login_name: str = None,
        major_key: str = None,
        match_type: int = None,
        model_rule_ids: str = None,
        name: str = None,
        product_code: str = None,
        product_id: int = None,
        risk_level_id: int = None,
        risk_level_name: str = None,
        stat_express: str = None,
        status: int = None,
        support_form: int = None,
        target: str = None,
        template_rule_ids: str = None,
        threat_analysis_status: int = None,
        user_id: int = None,
        warn_level: int = None,
    ):
        self.audit_mode = audit_mode
        # The content type of the sensitive data detection rule. Valid values:
        # 
        # *   **0**: keyword
        # *   **2**: regular expression
        self.category = category
        # The name of the content type of the sensitive data detection rule.
        self.category_name = category_name
        # The content in the sensitive data detection rule.
        # 
        # >  A built-in detection rule whose CustomType is 0 does not return the content of the rule.
        self.content = content
        # The type of the content in the sensitive data detection rule. Valid values include **1**, **2**, **3**, **4**, and **5**. The value 1 indicates attempts to exploit SQL injections. The value 2 indicates bypass by using SQL injections. The value 3 indicates abuse of stored procedures. The value 4 indicates buffer overflow. The value 5 indicates SQL injections based on errors.
        self.content_category = content_category
        # The type of the sensitive data detection rule.
        # 
        # *   0: built-in rule
        # *   1: custom rule
        self.custom_type = custom_type
        # The description of the sensitive data detection rule.
        self.description = description
        # The display name of the account that is used to create the sensitive data detection rule.
        self.display_name = display_name
        # The time when the sensitive data detection rule is created. The value is a UNIX timestamp. Unit: milliseconds.
        self.gmt_create = gmt_create
        # The time when the sensitive data detection rule is modified. The value is a UNIX timestamp. Unit: milliseconds.
        self.gmt_modified = gmt_modified
        # The parent group type of the rule.
        self.group_id = group_id
        # The number of times that the sensitive data detection rule is hit.
        self.hit_total_count = hit_total_count
        # The ID of the sensitive data detection rule.
        self.id = id
        # The username of the account that is used to create the sensitive data detection rule.
        self.login_name = login_name
        # The key of the primary dimension.
        self.major_key = major_key
        # The match type. Valid values:
        # 
        # *   **1**: rule-based match
        # *   **2**: dictionary-based match
        self.match_type = match_type
        # The IDs of the models for sensitive data audit.
        self.model_rule_ids = model_rule_ids
        # The name of the sensitive data detection rule.
        self.name = name
        # The name of the service to which the data asset belongs. Valid values include **MaxCompute, OSS, ADS, OTS, and RDS**.
        self.product_code = product_code
        # The ID of the service to which the sensitive data detection rule is applied. Valid values include **1**, **2**, **3**, **4**, and **5**. The value 1 indicates MaxCompute. The value 2 indicates OSS. The value 3 indicates AnalyticDB for MySQL. The value 4 indicates Tablestore. The value 5 indicates ApsaraDB RDS.
        self.product_id = product_id
        # The sensitivity level of the sensitive data that hits the sensitive data detection rule. Valid values:
        # 
        # *   **1**: N/A, which indicates that no sensitive data is detected.
        # *   **2**: S1, which indicates the low sensitivity level.
        # *   **3**: S2, which indicates the medium sensitivity level.
        # *   **4**: S3, which indicates the high sensitivity level.
        # *   **5**: S4, which indicates the highest sensitivity level.
        self.risk_level_id = risk_level_id
        # The sensitivity level of data that hits the sensitive data detection rule. Valid values:
        # 
        # *   **N/A**: indicates that no sensitive data is detected.
        # *   **S1**: indicates the low sensitivity level.
        # *   **S2**: indicates the medium sensitivity level.
        # *   **S3**: indicates the high sensitivity level.
        # *   **S4**: indicates the highest sensitivity level.
        self.risk_level_name = risk_level_name
        # The statistical expression.
        self.stat_express = stat_express
        # The status of the sensitive data detection rule. Valid values:
        # 
        # *   **0**: disabled
        # *   **1**: enabled
        self.status = status
        # The data asset type that is supported by the sensitive data detection rule. Valid values:
        # 
        # *   **0**: all data assets
        # *   **1**: structured data assets
        # *   **2**: unstructured data assets
        self.support_form = support_form
        # The name of the service to which the data asset belongs. Valid values include **MaxCompute, OSS, ADS, OTS, and RDS**.
        self.target = target
        # The IDs of the templates that are used to audit sensitive data.
        self.template_rule_ids = template_rule_ids
        self.threat_analysis_status = threat_analysis_status
        # The ID of the account that is used to create the sensitive data detection rule.
        self.user_id = user_id
        # The severity level. Valid values:
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
        if self.audit_mode is not None:
            result['AuditMode'] = self.audit_mode

        if self.category is not None:
            result['Category'] = self.category

        if self.category_name is not None:
            result['CategoryName'] = self.category_name

        if self.content is not None:
            result['Content'] = self.content

        if self.content_category is not None:
            result['ContentCategory'] = self.content_category

        if self.custom_type is not None:
            result['CustomType'] = self.custom_type

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.hit_total_count is not None:
            result['HitTotalCount'] = self.hit_total_count

        if self.id is not None:
            result['Id'] = self.id

        if self.login_name is not None:
            result['LoginName'] = self.login_name

        if self.major_key is not None:
            result['MajorKey'] = self.major_key

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

        if self.risk_level_name is not None:
            result['RiskLevelName'] = self.risk_level_name

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

        if self.threat_analysis_status is not None:
            result['ThreatAnalysisStatus'] = self.threat_analysis_status

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.warn_level is not None:
            result['WarnLevel'] = self.warn_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditMode') is not None:
            self.audit_mode = m.get('AuditMode')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('ContentCategory') is not None:
            self.content_category = m.get('ContentCategory')

        if m.get('CustomType') is not None:
            self.custom_type = m.get('CustomType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('HitTotalCount') is not None:
            self.hit_total_count = m.get('HitTotalCount')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LoginName') is not None:
            self.login_name = m.get('LoginName')

        if m.get('MajorKey') is not None:
            self.major_key = m.get('MajorKey')

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

        if m.get('RiskLevelName') is not None:
            self.risk_level_name = m.get('RiskLevelName')

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

        if m.get('ThreatAnalysisStatus') is not None:
            self.threat_analysis_status = m.get('ThreatAnalysisStatus')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('WarnLevel') is not None:
            self.warn_level = m.get('WarnLevel')

        return self

