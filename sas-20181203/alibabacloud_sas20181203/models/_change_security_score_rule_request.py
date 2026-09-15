# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ChangeSecurityScoreRuleRequest(DaraModel):
    def __init__(
        self,
        cal_type: str = None,
        reset_security_score_rule: bool = None,
        resource_directory_account_id: int = None,
        security_score_category_list: List[main_models.ChangeSecurityScoreRuleRequestSecurityScoreCategoryList] = None,
        security_score_rule_list: List[main_models.ChangeSecurityScoreRuleRequestSecurityScoreRuleList] = None,
    ):
        # Specifies whether to modify the new version or legacy security score rules. If the value is **home_security_score**, the new version security score rules are modified. Otherwise, the legacy security score rules are modified by default.
        self.cal_type = cal_type
        # Specifies whether to reset to the system default rules. Valid values:
        # - true: Yes.
        # - false: No.
        self.reset_security_score_rule = reset_security_score_rule
        # The ID of the member account in the resource directory.
        # > Call the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to obtain this parameter.
        self.resource_directory_account_id = resource_directory_account_id
        # The list of new version security score rule deductions.
        self.security_score_category_list = security_score_category_list
        # The list of legacy security score rules.
        self.security_score_rule_list = security_score_rule_list

    def validate(self):
        if self.security_score_category_list:
            for v1 in self.security_score_category_list:
                 if v1:
                    v1.validate()
        if self.security_score_rule_list:
            for v1 in self.security_score_rule_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cal_type is not None:
            result['CalType'] = self.cal_type

        if self.reset_security_score_rule is not None:
            result['ResetSecurityScoreRule'] = self.reset_security_score_rule

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        result['SecurityScoreCategoryList'] = []
        if self.security_score_category_list is not None:
            for k1 in self.security_score_category_list:
                result['SecurityScoreCategoryList'].append(k1.to_map() if k1 else None)

        result['SecurityScoreRuleList'] = []
        if self.security_score_rule_list is not None:
            for k1 in self.security_score_rule_list:
                result['SecurityScoreRuleList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalType') is not None:
            self.cal_type = m.get('CalType')

        if m.get('ResetSecurityScoreRule') is not None:
            self.reset_security_score_rule = m.get('ResetSecurityScoreRule')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        self.security_score_category_list = []
        if m.get('SecurityScoreCategoryList') is not None:
            for k1 in m.get('SecurityScoreCategoryList'):
                temp_model = main_models.ChangeSecurityScoreRuleRequestSecurityScoreCategoryList()
                self.security_score_category_list.append(temp_model.from_map(k1))

        self.security_score_rule_list = []
        if m.get('SecurityScoreRuleList') is not None:
            for k1 in m.get('SecurityScoreRuleList'):
                temp_model = main_models.ChangeSecurityScoreRuleRequestSecurityScoreRuleList()
                self.security_score_rule_list.append(temp_model.from_map(k1))

        return self

class ChangeSecurityScoreRuleRequestSecurityScoreRuleList(DaraModel):
    def __init__(
        self,
        rule_type: str = None,
        score: int = None,
        security_score_item_list: List[main_models.ChangeSecurityScoreRuleRequestSecurityScoreRuleListSecurityScoreItemList] = None,
    ):
        # The type of the security score rule. Valid values:
        # - SS_REINFORCE: Key feature configuration.
        # - SS_ALARM: Pending alerts.
        # - SS_VUL: Pending vulnerabilities.
        # - SS_HC: Baseline issues.
        # - SS_CLOUD_HC: Cloud platform configuration check item issues.
        # - SS_AK: AccessKey pair leak risk.
        self.rule_type = rule_type
        # The deduction value of the security score rule.
        # 
        # > The valid range is 0 to 100. The sum of all security score rule deduction thresholds must equal 100.
        self.score = score
        # The list of individual deduction items for the security score rule.
        self.security_score_item_list = security_score_item_list

    def validate(self):
        if self.security_score_item_list:
            for v1 in self.security_score_item_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        if self.score is not None:
            result['Score'] = self.score

        result['SecurityScoreItemList'] = []
        if self.security_score_item_list is not None:
            for k1 in self.security_score_item_list:
                result['SecurityScoreItemList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        self.security_score_item_list = []
        if m.get('SecurityScoreItemList') is not None:
            for k1 in m.get('SecurityScoreItemList'):
                temp_model = main_models.ChangeSecurityScoreRuleRequestSecurityScoreRuleListSecurityScoreItemList()
                self.security_score_item_list.append(temp_model.from_map(k1))

        return self

class ChangeSecurityScoreRuleRequestSecurityScoreRuleListSecurityScoreItemList(DaraModel):
    def __init__(
        self,
        score: int = None,
        score_threshold: int = None,
        sub_rule_type: str = None,
    ):
        # The deduction value for the individual item.
        self.score = score
        # The deduction threshold for the individual item.
        # 
        # > The valid range is 0 to the deduction threshold of the security score rule.
        self.score_threshold = score_threshold
        # The sub-rule type of the individual deduction item. The mapping between security score types and sub-rule types is as follows:
        # - SS_REINFORCE: Key feature configuration.
        #   - XPRESS_INSTALL: Security Center service authorization is not enabled.
        #   - REINFORCE_SUSPICIOUS: The anti-virus feature is not enabled.
        #   - RANSOMWARE: The anti-ransomware policy is not enabled.
        #   - WEB_LOCK: The web tamper-proofing feature is not enabled.
        #   - VIRUS_SCHEDULE_SCAN: The periodic virus scan policy is not enabled.
        #   - IMAGE_REPO_SCAN: The container image scan scope is not configured.
        #   - IMAGE_SCAN_TASK: The one-click container image security risk scan has not been executed.
        # 
        # - SS_ALARM: Pending alerts.
        #   - ALARM_SERIOUS: One unhandled high-risk alert event exists.
        #   - ALARM_SUSPICIOUS: One unhandled medium-risk alert event exists.
        #   - ALARM_REMIND: One unhandled low-risk alert event exists.
        # 
        # - SS_VUL: Pending vulnerabilities.
        #   - CMS_UNFIX: One unfixed CMS vulnerability exists.
        #   - WIN_UNFIX: One unfixed Windows host vulnerability exists.
        #   - CVE_UNFIX: One unfixed Linux host vulnerability exists.
        #   - ERM_UNFIX: One unfixed emergency vulnerability exists.
        #   - ERM_UNCHECK: One unscanned emergency vulnerability exists.
        # 
        # - SS_HC: Baseline issues.
        #   - WEAK_EXPLOIT: A weak password risk exposed to the Internet exists.
        #   - WEAK_PASSWORD: A weak password risk exists.
        #   - HC_EXPLOIT: A high-risk intrusion vulnerability exists.
        #   - HC_OTHER_WARNING: A security configuration risk exists.
        # 
        # - SS_CLOUD_HC: Cloud platform configuration check item issues.
        #   - CSPM_CIEM_NOT_PASS: One failed CIEM check item exists.
        #   - CSPM_RISK_NOT_PASS: One failed security risk check item exists.
        #   - CSPM_COMPLIANCE_NOT_PASS: One failed compliance check item exists.
        # 
        # - SS_AK: AccessKey pair leak risk. Categorization not applicable.
        self.sub_rule_type = sub_rule_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.score is not None:
            result['Score'] = self.score

        if self.score_threshold is not None:
            result['ScoreThreshold'] = self.score_threshold

        if self.sub_rule_type is not None:
            result['SubRuleType'] = self.sub_rule_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('ScoreThreshold') is not None:
            self.score_threshold = m.get('ScoreThreshold')

        if m.get('SubRuleType') is not None:
            self.sub_rule_type = m.get('SubRuleType')

        return self

class ChangeSecurityScoreRuleRequestSecurityScoreCategoryList(DaraModel):
    def __init__(
        self,
        category: str = None,
        score_threshold: int = None,
        security_rule_list: List[main_models.ChangeSecurityScoreRuleRequestSecurityScoreCategoryListSecurityRuleList] = None,
    ):
        # The category of the security score rule. Valid values:
        # - **SS_SAS_HANDLE**: Security governance.
        # - **SS_SAS_RESPOND**: Security response.
        self.category = category
        # The deduction threshold for the security score rule category.
        # 
        # > The valid range is 0 to 100. The sum of all security score rule category deduction thresholds must equal 100.
        self.score_threshold = score_threshold
        # The list of deductions by security score rule type.
        self.security_rule_list = security_rule_list

    def validate(self):
        if self.security_rule_list:
            for v1 in self.security_rule_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.score_threshold is not None:
            result['ScoreThreshold'] = self.score_threshold

        result['SecurityRuleList'] = []
        if self.security_rule_list is not None:
            for k1 in self.security_rule_list:
                result['SecurityRuleList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('ScoreThreshold') is not None:
            self.score_threshold = m.get('ScoreThreshold')

        self.security_rule_list = []
        if m.get('SecurityRuleList') is not None:
            for k1 in m.get('SecurityRuleList'):
                temp_model = main_models.ChangeSecurityScoreRuleRequestSecurityScoreCategoryListSecurityRuleList()
                self.security_rule_list.append(temp_model.from_map(k1))

        return self

class ChangeSecurityScoreRuleRequestSecurityScoreCategoryListSecurityRuleList(DaraModel):
    def __init__(
        self,
        rule_type: str = None,
        score: int = None,
        security_score_item_list: List[main_models.ChangeSecurityScoreRuleRequestSecurityScoreCategoryListSecurityRuleListSecurityScoreItemList] = None,
    ):
        # The type of the security score rule sub-item. Valid values:
        # 
        # - **SS_SAS_WEAK_PW**: Pending weak passwords to fix.
        # - **SS_SAS_ALARM**: Pending Security Center alerts.
        # - **SS_SAS_EMG_VUL**: Pending emergency vulnerabilities to fix.
        # - **SS_SAS_APP_VUL**: Pending application vulnerabilities to fix.
        # - **SS_SAS_SYS_VUL**: Pending system vulnerabilities to fix.
        # - **SS_SAS_CLOUD_HC**: Pending Cloud Security Posture Management (CSPM) risks.
        # - **SS_SDDP_DATA_RISK**: Pending data security risks to address.
        # - **SS_WAF_API_RISK**: Pending API security risks.
        # - **SS_DDOS_BH_ASSET**: Assets in DDoS blackhole filtering status.
        # - **SS_SAS_AK_LEAK**: Unhandled AccessKey/SecretKey leak events.
        # - **SS_PRODUCT_CONNECT**: Security products not properly connected.
        # - **SS_KEY_CONFIG**: Key feature configuration.
        # - **SS_PRODUCT_EXPIRE**: Products about to expire.
        # - **SS_AI_RISK**: AI application risks.
        self.rule_type = rule_type
        # The deduction threshold for the security score rule type.
        # 
        # > The valid range is 0 to the deduction threshold of the security score rule category.
        self.score = score
        # The list of deductions for security score rule sub-items.
        self.security_score_item_list = security_score_item_list

    def validate(self):
        if self.security_score_item_list:
            for v1 in self.security_score_item_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        if self.score is not None:
            result['Score'] = self.score

        result['SecurityScoreItemList'] = []
        if self.security_score_item_list is not None:
            for k1 in self.security_score_item_list:
                result['SecurityScoreItemList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        self.security_score_item_list = []
        if m.get('SecurityScoreItemList') is not None:
            for k1 in m.get('SecurityScoreItemList'):
                temp_model = main_models.ChangeSecurityScoreRuleRequestSecurityScoreCategoryListSecurityRuleListSecurityScoreItemList()
                self.security_score_item_list.append(temp_model.from_map(k1))

        return self

class ChangeSecurityScoreRuleRequestSecurityScoreCategoryListSecurityRuleListSecurityScoreItemList(DaraModel):
    def __init__(
        self,
        score: int = None,
        score_threshold: int = None,
        sub_rule_type: str = None,
    ):
        # The deduction value for the individual item.
        self.score = score
        # The deduction threshold for the individual item.
        # 
        # > The valid range is 0 to the deduction threshold of the security score rule type.
        self.score_threshold = score_threshold
        # The security score rule sub-item.
        self.sub_rule_type = sub_rule_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.score is not None:
            result['Score'] = self.score

        if self.score_threshold is not None:
            result['ScoreThreshold'] = self.score_threshold

        if self.sub_rule_type is not None:
            result['SubRuleType'] = self.sub_rule_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('ScoreThreshold') is not None:
            self.score_threshold = m.get('ScoreThreshold')

        if m.get('SubRuleType') is not None:
            self.sub_rule_type = m.get('SubRuleType')

        return self

