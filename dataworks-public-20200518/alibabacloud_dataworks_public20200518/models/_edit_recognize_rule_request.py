# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EditRecognizeRuleRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        col_exclude: str = None,
        col_scan: str = None,
        comment_scan: str = None,
        content_scan: str = None,
        hit_threshold: int = None,
        level_name: str = None,
        node_id: str = None,
        node_parent: str = None,
        operation_type: int = None,
        recognize_rules: str = None,
        recognize_rules_type: str = None,
        sensitive_description: str = None,
        sensitive_id: str = None,
        sensitive_name: str = None,
        status: int = None,
        template_id: str = None,
        tenant_id: str = None,
        level: str = None,
    ):
        # The Alibaba Cloud account that is used to create the sensitive data identification rule. Enter the username of the Alibaba Cloud account.
        # 
        # This parameter is required.
        self.account_name = account_name
        # Excludes fields. The system does not identify fields that are assigned with values.
        # 
        # *   The value must be in the ${Project name}.${Table name}.${Field name} or ${Project name}.${Schema name}.${Table name}.${Field name} format.
        # *   *Wildcards are supported. For example, the asterisk (\\*) in default.table.column1\\* can be used to match any content following default.table.column1, such as default.table.column10.
        self.col_exclude = col_exclude
        # Scans fields. The system identifies only fields that are assigned with values.
        # 
        # *   The value must be in the ${Project name}.${Table name}.${Field name} or ${Project name}.${Schema name}.${Table name}.${Field name} format.
        # *   *Wildcards are supported. For example, the asterisk (\\*) in default.table.column1\\* can be used to match any content following default.table.column1, such as default.table.column10.
        self.col_scan = col_scan
        # Scans content. The value is the text of each field comment in your data asset. Fuzzy match is supported.
        self.comment_scan = comment_scan
        # Identifies content. You can call the [QuerySensNodeInfo](https://help.aliyun.com/document_detail/2747189.html) operation to query the value of the current parameter for a built-in sensitive field.
        self.content_scan = content_scan
        # The hit ratio threshold. If more than 60%, which is a sample hit ratio threshold, of all sample data records hit the Name Entity Recognition (NER) model, the sensitive field is hit. The value can be an integer from 0 to 100.
        self.hit_threshold = hit_threshold
        # The name of the sensitivity level. You can call the [QueryDefaultTemplate](https://help.aliyun.com/document_detail/2743948.html) operation to obtain the name of the sensitivity level in the related template.
        self.level_name = level_name
        # The ID of the data category. You can call the [QuerySensClassification](https://help.aliyun.com/document_detail/2746850.html) operation to query the ID of all data categories. Then, you can select a data category to create a sensitive field. Enter the ID of the selected data category.
        # 
        # This parameter is required.
        self.node_id = node_id
        # The information about the parent data category of the current data category. You can call the [QuerySensClassification](https://help.aliyun.com/document_detail/2746850.html) operation to obtain the ID of a data category.
        # 
        # This parameter is required.
        self.node_parent = node_parent
        # The type of the arithmetic operation. Valid values:
        # 
        # *   0: OR
        # *   1: AND
        # 
        # This parameter is required.
        self.operation_type = operation_type
        # The content of the sensitive data identification rule. You can call the [QuerySensNodeInfo](https://help.aliyun.com/document_detail/2747189.html) operation to query the value of the current parameter for a built-in sensitive field.
        self.recognize_rules = recognize_rules
        # The type of the sensitive data identification rule. Valid values:
        # 
        # *   1: regular expression
        # *   2: built-in rule
        # *   3: sample library
        # *   4: self-generated data identification model
        self.recognize_rules_type = recognize_rules_type
        # The description of the sensitive field. Enter a string that is less than 128 characters in length.
        self.sensitive_description = sensitive_description
        # The sensitive field ID. You can call the [QuerySensNodeInfo](https://help.aliyun.com/document_detail/2747189.html) operation to query the IDs of all sensitive fields. You can also call the [QueryRecognizeRuleDetail](https://help.aliyun.com/document_detail/2766023.html) operation to query the IDs of specific sensitive fields.
        # 
        # This parameter is required.
        self.sensitive_id = sensitive_id
        # The name of the custom sensitive field. Enter a string that is less than 128 characters in length.
        # 
        # This parameter is required.
        self.sensitive_name = sensitive_name
        # The status of the sensitive field. Valid values:
        # 
        # *   0: draft
        # *   1: effective
        self.status = status
        # The template ID. You can call the [QueryDefaultTemplate](https://help.aliyun.com/document_detail/2743948.html) operation to obtain the template ID.
        # 
        # This parameter is required.
        self.template_id = template_id
        # The tenant ID. To obtain the tenant ID, perform the following steps: Log on to the [DataWorks console](https://workbench.data.aliyun.com/console). Find your workspace and go to the DataStudio page. On the DataStudio page, click the logon username in the upper-right corner and click User Info in the Menu section.
        # 
        # This parameter is required.
        self.tenant_id = tenant_id
        # The sensitivity level of the sensitive field. You can select one from all sensitivity levels that are defined in a template as the sensitivity level of the sensitive field, such as level 1 to level 10.
        # 
        # This parameter is required.
        self.level = level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.col_exclude is not None:
            result['ColExclude'] = self.col_exclude

        if self.col_scan is not None:
            result['ColScan'] = self.col_scan

        if self.comment_scan is not None:
            result['CommentScan'] = self.comment_scan

        if self.content_scan is not None:
            result['ContentScan'] = self.content_scan

        if self.hit_threshold is not None:
            result['HitThreshold'] = self.hit_threshold

        if self.level_name is not None:
            result['LevelName'] = self.level_name

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_parent is not None:
            result['NodeParent'] = self.node_parent

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.recognize_rules is not None:
            result['RecognizeRules'] = self.recognize_rules

        if self.recognize_rules_type is not None:
            result['RecognizeRulesType'] = self.recognize_rules_type

        if self.sensitive_description is not None:
            result['SensitiveDescription'] = self.sensitive_description

        if self.sensitive_id is not None:
            result['SensitiveId'] = self.sensitive_id

        if self.sensitive_name is not None:
            result['SensitiveName'] = self.sensitive_name

        if self.status is not None:
            result['Status'] = self.status

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.level is not None:
            result['level'] = self.level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('ColExclude') is not None:
            self.col_exclude = m.get('ColExclude')

        if m.get('ColScan') is not None:
            self.col_scan = m.get('ColScan')

        if m.get('CommentScan') is not None:
            self.comment_scan = m.get('CommentScan')

        if m.get('ContentScan') is not None:
            self.content_scan = m.get('ContentScan')

        if m.get('HitThreshold') is not None:
            self.hit_threshold = m.get('HitThreshold')

        if m.get('LevelName') is not None:
            self.level_name = m.get('LevelName')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeParent') is not None:
            self.node_parent = m.get('NodeParent')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('RecognizeRules') is not None:
            self.recognize_rules = m.get('RecognizeRules')

        if m.get('RecognizeRulesType') is not None:
            self.recognize_rules_type = m.get('RecognizeRulesType')

        if m.get('SensitiveDescription') is not None:
            self.sensitive_description = m.get('SensitiveDescription')

        if m.get('SensitiveId') is not None:
            self.sensitive_id = m.get('SensitiveId')

        if m.get('SensitiveName') is not None:
            self.sensitive_name = m.get('SensitiveName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('level') is not None:
            self.level = m.get('level')

        return self

