# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class ListConfigRulesResponseBody(DaraModel):
    def __init__(
        self,
        config_rules: main_models.ListConfigRulesResponseBodyConfigRules = None,
        request_id: str = None,
    ):
        # The information about the rules.
        self.config_rules = config_rules
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.config_rules:
            self.config_rules.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_rules is not None:
            result['ConfigRules'] = self.config_rules.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRules') is not None:
            temp_model = main_models.ListConfigRulesResponseBodyConfigRules()
            self.config_rules = temp_model.from_map(m.get('ConfigRules'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListConfigRulesResponseBodyConfigRules(DaraModel):
    def __init__(
        self,
        config_rule_list: List[main_models.ListConfigRulesResponseBodyConfigRulesConfigRuleList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The details of the rule.
        self.config_rule_list = config_rule_list
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of rules.
        self.total_count = total_count

    def validate(self):
        if self.config_rule_list:
            for v1 in self.config_rule_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConfigRuleList'] = []
        if self.config_rule_list is not None:
            for k1 in self.config_rule_list:
                result['ConfigRuleList'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_rule_list = []
        if m.get('ConfigRuleList') is not None:
            for k1 in m.get('ConfigRuleList'):
                temp_model = main_models.ListConfigRulesResponseBodyConfigRulesConfigRuleList()
                self.config_rule_list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListConfigRulesResponseBodyConfigRulesConfigRuleList(DaraModel):
    def __init__(
        self,
        account_id: int = None,
        automation_type: str = None,
        compliance: main_models.ListConfigRulesResponseBodyConfigRulesConfigRuleListCompliance = None,
        config_rule_arn: str = None,
        config_rule_id: str = None,
        config_rule_name: str = None,
        config_rule_state: str = None,
        create_by: main_models.ListConfigRulesResponseBodyConfigRulesConfigRuleListCreateBy = None,
        create_date: str = None,
        description: str = None,
        resource_types_scope: str = None,
        risk_level: int = None,
        source_identifier: str = None,
        source_owner: str = None,
        tags: List[main_models.ListConfigRulesResponseBodyConfigRulesConfigRuleListTags] = None,
    ):
        # The ID of the account to which the rule belongs.
        self.account_id = account_id
        # The type of the remediation template. Only OOS is returned, which indicates CloudOps Orchestration Service.
        self.automation_type = automation_type
        # The compliance aggregation result of the rule.
        self.compliance = compliance
        # The ARN of the rule.
        self.config_rule_arn = config_rule_arn
        # The rule ID.
        self.config_rule_id = config_rule_id
        # The name of the rule.
        self.config_rule_name = config_rule_name
        # The status of the rule. Valid values:
        # 
        # *   ACTIVE: The rule is enabled.
        # *   DELETING: The rule is being deleted.
        # *   EVALUATING: The rule is being used to evaluate resource configurations.
        # *   INACTIVE: The rule is disabled.
        self.config_rule_state = config_rule_state
        # The information about the creation of the rule.
        self.create_by = create_by
        self.create_date = create_date
        # The description of the rule.
        self.description = description
        # The types of resources evaluated by the rule. Multiple resource types are separated with commas (,).
        self.resource_types_scope = resource_types_scope
        # The risk level of the resources that do not comply with the rule. Valid values:
        # 
        # *   1: high.
        # *   2: medium.
        # *   3: low.
        self.risk_level = risk_level
        # The identifier of the rule.
        # 
        # *   If the rule is a managed rule, the value of this parameter is the identifier of the managed rule.
        # *   If the rule is a custom rule, the value of this parameter is the Alibaba Cloud Resource Name (ARN) of the rule.
        self.source_identifier = source_identifier
        # The type of the rule. Valid values:
        # 
        # *   CUSTOM_FC: a custom rule.
        # *   ALIYUN: a managed rule.
        self.source_owner = source_owner
        # The tags of the rule.
        self.tags = tags

    def validate(self):
        if self.compliance:
            self.compliance.validate()
        if self.create_by:
            self.create_by.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.automation_type is not None:
            result['AutomationType'] = self.automation_type

        if self.compliance is not None:
            result['Compliance'] = self.compliance.to_map()

        if self.config_rule_arn is not None:
            result['ConfigRuleArn'] = self.config_rule_arn

        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id

        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name

        if self.config_rule_state is not None:
            result['ConfigRuleState'] = self.config_rule_state

        if self.create_by is not None:
            result['CreateBy'] = self.create_by.to_map()

        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.description is not None:
            result['Description'] = self.description

        if self.resource_types_scope is not None:
            result['ResourceTypesScope'] = self.resource_types_scope

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.source_identifier is not None:
            result['SourceIdentifier'] = self.source_identifier

        if self.source_owner is not None:
            result['SourceOwner'] = self.source_owner

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AutomationType') is not None:
            self.automation_type = m.get('AutomationType')

        if m.get('Compliance') is not None:
            temp_model = main_models.ListConfigRulesResponseBodyConfigRulesConfigRuleListCompliance()
            self.compliance = temp_model.from_map(m.get('Compliance'))

        if m.get('ConfigRuleArn') is not None:
            self.config_rule_arn = m.get('ConfigRuleArn')

        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')

        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')

        if m.get('ConfigRuleState') is not None:
            self.config_rule_state = m.get('ConfigRuleState')

        if m.get('CreateBy') is not None:
            temp_model = main_models.ListConfigRulesResponseBodyConfigRulesConfigRuleListCreateBy()
            self.create_by = temp_model.from_map(m.get('CreateBy'))

        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ResourceTypesScope') is not None:
            self.resource_types_scope = m.get('ResourceTypesScope')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('SourceIdentifier') is not None:
            self.source_identifier = m.get('SourceIdentifier')

        if m.get('SourceOwner') is not None:
            self.source_owner = m.get('SourceOwner')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListConfigRulesResponseBodyConfigRulesConfigRuleListTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ListConfigRulesResponseBodyConfigRulesConfigRuleListTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the rule.
        self.key = key
        # The tag value of the rule.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListConfigRulesResponseBodyConfigRulesConfigRuleListCreateBy(DaraModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        compliance_pack_name: str = None,
    ):
        # The compliance package ID.
        self.compliance_pack_id = compliance_pack_id
        # The name of the compliance package.
        self.compliance_pack_name = compliance_pack_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id

        if self.compliance_pack_name is not None:
            result['CompliancePackName'] = self.compliance_pack_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')

        if m.get('CompliancePackName') is not None:
            self.compliance_pack_name = m.get('CompliancePackName')

        return self

class ListConfigRulesResponseBodyConfigRulesConfigRuleListCompliance(DaraModel):
    def __init__(
        self,
        compliance_type: str = None,
        count: int = None,
    ):
        # The compliance evaluation result of the rule. Valid values:
        # 
        # *   COMPLIANT: The resources are evaluated as compliant.
        # *   NON_COMPLIANT: The resources are evaluated as non-compliant.
        # *   NOT_APPLICABLE: The rule does not apply to the resources.
        # *   INSUFFICIENT_DATA: No resource data is available.
        self.compliance_type = compliance_type
        # The number of resources that are evaluated based on the rule.
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type

        if self.count is not None:
            result['Count'] = self.count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        return self

