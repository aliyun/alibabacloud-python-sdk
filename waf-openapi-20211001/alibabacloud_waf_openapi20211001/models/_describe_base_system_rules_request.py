# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBaseSystemRulesRequest(DaraModel):
    def __init__(
        self,
        detect_type: str = None,
        instance_id: str = None,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
        risk_level: str = None,
        rule_action: str = None,
        rule_id: int = None,
        rule_name: str = None,
        rule_status: int = None,
        template_id: int = None,
    ):
        # The type of attack that the system protection rule detects. Valid values:
        # 
        # - **sqli**: SQL injection.
        # 
        # - **xss**: cross-site scripting (XSS).
        # 
        # - **cmdi**: OS command injection.
        # 
        # - **expression_injection**: expression injection.
        # 
        # - **java_deserialization**: Java deserialization.
        # 
        # - **dot_net_deserialization**: .NET deserialization.
        # 
        # - **php_deserialization**: PHP deserialization.
        # 
        # - **code_exec**: code execution.
        # 
        # - **ssrf**: server-side request forgery (SSRF).
        # 
        # - **path_traversal**: path traversal.
        # 
        # - **arbitrary_file_uploading**: arbitrary file upload.
        # 
        # - **webshell**: webshell.
        # 
        # - **rfilei**: remote file inclusion (RFI).
        # 
        # - **lfilei**: local file inclusion (LFI).
        # 
        # - **protocol_violation**: protocol violation.
        # 
        # - **scanner_behavior**: scanner behavior.
        # 
        # - **logic_flaw**: logic flaw.
        # 
        # - **arbitrary_file_reading**: arbitrary file read.
        # 
        # - **arbitrary_file_download**: arbitrary file download.
        # 
        # - **xxe**: external entity injection.
        # 
        # - **csrf**: cross-site request forgery (CSRF).
        # 
        # - **crlf**: CRLF injection.
        # 
        # - **other**: other.
        self.detect_type = detect_type
        # The ID of the WAF instance.
        # 
        # > Call [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) to query the ID of your WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The language of the response. Valid values:
        # 
        # - **zh** (default): Chinese.
        # 
        # - **en**: English.
        self.lang = lang
        # The number of the page to return. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: 100.
        self.page_size = page_size
        # The region where the WAF instance resides. Valid values:
        # 
        # - **cn-hangzhou**: the Chinese mainland.
        # 
        # - **ap-southeast-1**: outside the Chinese mainland.
        self.region_id = region_id
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The risk level of the system protection rule. Valid values:
        # 
        # - **super_strict**: Very Strict.
        # 
        # - **strict**: Strict.
        # 
        # - **medium**: Medium.
        # 
        # - **loose**: Loose.
        self.risk_level = risk_level
        # The action of the system protection rule. Valid values:
        # 
        # - **block**: Block.
        # 
        # - **monitor**: Monitor.
        self.rule_action = rule_action
        # The ID of the system protection rule to query.
        self.rule_id = rule_id
        # The name of the system protection rule.
        self.rule_name = rule_name
        # The status of the system protection rule. Valid values:
        # 
        # - **1**: disabled.
        # 
        # - **0**: enabled.
        self.rule_status = rule_status
        # The ID of the protection template.
        # 
        # > - Specify this parameter to query the system protection rules in a specific WAF protection template.
        # >
        # > - If you leave this parameter empty, the default configurations of the system protection rules are queried.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detect_type is not None:
            result['DetectType'] = self.detect_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.rule_action is not None:
            result['RuleAction'] = self.rule_action

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_status is not None:
            result['RuleStatus'] = self.rule_status

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetectType') is not None:
            self.detect_type = m.get('DetectType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('RuleAction') is not None:
            self.rule_action = m.get('RuleAction')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleStatus') is not None:
            self.rule_status = m.get('RuleStatus')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

