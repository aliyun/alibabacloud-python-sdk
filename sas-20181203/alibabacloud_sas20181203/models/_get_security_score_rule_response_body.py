# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetSecurityScoreRuleResponseBody(DaraModel):
    def __init__(
        self,
        enable_status: bool = None,
        request_id: str = None,
        security_score_category_list: List[main_models.GetSecurityScoreRuleResponseBodySecurityScoreCategoryList] = None,
        security_score_rule_list: List[main_models.GetSecurityScoreRuleResponseBodySecurityScoreRuleList] = None,
    ):
        # The enabling status of the custom security scoring rule. Valid values:
        # - true: Enabled.
        # - false: Not enabled.
        self.enable_status = enable_status
        # The ID of the request. Alibaba Cloud generates a unique identifier for each request. You can use the ID to troubleshoot issues.
        self.request_id = request_id
        # The list of new security score rules.
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
        if self.enable_status is not None:
            result['EnableStatus'] = self.enable_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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
        if m.get('EnableStatus') is not None:
            self.enable_status = m.get('EnableStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.security_score_category_list = []
        if m.get('SecurityScoreCategoryList') is not None:
            for k1 in m.get('SecurityScoreCategoryList'):
                temp_model = main_models.GetSecurityScoreRuleResponseBodySecurityScoreCategoryList()
                self.security_score_category_list.append(temp_model.from_map(k1))

        self.security_score_rule_list = []
        if m.get('SecurityScoreRuleList') is not None:
            for k1 in m.get('SecurityScoreRuleList'):
                temp_model = main_models.GetSecurityScoreRuleResponseBodySecurityScoreRuleList()
                self.security_score_rule_list.append(temp_model.from_map(k1))

        return self

class GetSecurityScoreRuleResponseBodySecurityScoreRuleList(DaraModel):
    def __init__(
        self,
        rule_type: str = None,
        score: int = None,
        security_score_item_list: List[main_models.GetSecurityScoreRuleResponseBodySecurityScoreRuleListSecurityScoreItemList] = None,
        title: str = None,
    ):
        # The type of the security score rule. Valid values:
        # - SS_REINFORCE: Key feature configuration.
        # - SS_ALARM: Pending alerts.
        # - SS_VUL: Pending vulnerabilities to fix.
        # - SS_HC: Baseline issues.
        # - SS_CLOUD_HC: Cloud platform configuration check item issues.
        # - SS_AK: AccessKey leakage risk exists.
        self.rule_type = rule_type
        # The deduction value of the security score rule.
        # 
        # > The configurable range is 0 to 100 points. The sum of all security score rule deduction thresholds must equal 100 points.
        self.score = score
        # The list of individual deduction items for the security score rule.
        self.security_score_item_list = security_score_item_list
        # The description of the security score rule.
        self.title = title

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

        if self.title is not None:
            result['Title'] = self.title

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
                temp_model = main_models.GetSecurityScoreRuleResponseBodySecurityScoreRuleListSecurityScoreItemList()
                self.security_score_item_list.append(temp_model.from_map(k1))

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class GetSecurityScoreRuleResponseBodySecurityScoreRuleListSecurityScoreItemList(DaraModel):
    def __init__(
        self,
        score: int = None,
        score_threshold: int = None,
        sub_rule_type: str = None,
        title: str = None,
    ):
        # The deduction value of the individual item.
        self.score = score
        # The deduction threshold of the individual item.
        # 
        # > The configurable range is 0 to the deduction threshold of the security score rule.
        self.score_threshold = score_threshold
        # The sub-rule type of the security score deduction item. The relationship between security score categorization types and sub-rule types is as follows:
        # - SS_REINFORCE: Key feature configuration.
        #   - XPRESS_INSTALL: Security Center service authorization is not enabled.
        #   - REINFORCE_SUSPICIOUS: Anti-virus feature is not enabled.
        #   - RANSOMWARE: Anti-ransomware policy is not enabled.
        #   - WEB_LOCK: Web tamper-proofing feature is not enabled.
        #   - VIRUS_SCHEDULE_SCAN: Periodic virus scan policy is not enabled.
        #   - IMAGE_REPO_SCAN: Container image scan scope is not configured.
        #   - IMAGE_SCAN_TASK: One-click container image security risk scan has not been executed.
        # 
        # - SS_ALARM: Pending alerts.
        #   - ALARM_SERIOUS: One unhandled high-risk alert event exists.
        #   - ALARM_SUSPICIOUS: One unhandled medium-risk alert event exists.
        #   - ALARM_REMIND: One unhandled low-risk alert event exists.
        # 
        # - SS_VUL: Pending vulnerabilities to fix.
        #   - CMS_UNFIX: One unfixed CMS vulnerability exists.
        #   - WIN_UNFIX: One unfixed Windows host vulnerability exists.
        #   - CVE_UNFIX: One unfixed Linux host vulnerability exists.
        #   - ERM_UNFIX: One unfixed emergency vulnerability exists.
        #   - ERM_UNCHECK: One undetected emergency vulnerability exists.
        # 
        # - SS_HC: Baseline issues.
        #   - WEAK_EXPLOIT: Weak password risk exposed to the Internet exists.
        #   - WEAK_PASSWORD: Weak password risk exists.
        #   - HC_EXPLOIT: High-risk intrusion vulnerability exists.
        #   - HC_OTHER_WARNING: Security configuration risk exists.
        # 
        # - SS_CLOUD_HC: Cloud platform configuration check item issues.
        #   - CSPM_CIEM_NOT_PASS: One failed CIEM check item exists.
        #   - CSPM_RISK_NOT_PASS: One failed security risk check item exists.
        #   - CSPM_COMPLIANCE_NOT_PASS: One failed compliance check item exists.
        # 
        # - SS_AK: AccessKey leakage risk exists.
        self.sub_rule_type = sub_rule_type
        # The description of the sub-rule type for the security score deduction item.
        self.title = title

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

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('ScoreThreshold') is not None:
            self.score_threshold = m.get('ScoreThreshold')

        if m.get('SubRuleType') is not None:
            self.sub_rule_type = m.get('SubRuleType')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class GetSecurityScoreRuleResponseBodySecurityScoreCategoryList(DaraModel):
    def __init__(
        self,
        category: str = None,
        score: int = None,
        security_rule_list: List[main_models.GetSecurityScoreRuleResponseBodySecurityScoreCategoryListSecurityRuleList] = None,
        title: str = None,
    ):
        # The category of the security score rule. Valid values:
        # - **SS_SAS_HANDLE**: Security governance.
        # - **SS_SAS_RESPOND**: Security response.
        self.category = category
        # The deduction threshold of the security score rule category.
        self.score = score
        # The deduction list of security score rule types.
        self.security_rule_list = security_rule_list
        # The name of the security score rule category.
        self.title = title

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

        if self.score is not None:
            result['Score'] = self.score

        result['SecurityRuleList'] = []
        if self.security_rule_list is not None:
            for k1 in self.security_rule_list:
                result['SecurityRuleList'].append(k1.to_map() if k1 else None)

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        self.security_rule_list = []
        if m.get('SecurityRuleList') is not None:
            for k1 in m.get('SecurityRuleList'):
                temp_model = main_models.GetSecurityScoreRuleResponseBodySecurityScoreCategoryListSecurityRuleList()
                self.security_rule_list.append(temp_model.from_map(k1))

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class GetSecurityScoreRuleResponseBodySecurityScoreCategoryListSecurityRuleList(DaraModel):
    def __init__(
        self,
        rule_type: str = None,
        score: int = None,
        security_score_item_list: List[main_models.GetSecurityScoreRuleResponseBodySecurityScoreCategoryListSecurityRuleListSecurityScoreItemList] = None,
        title: str = None,
    ):
        # The type of the security score rule.
        self.rule_type = rule_type
        # The deduction threshold of the security score rule type.
        self.score = score
        # The deduction list of security score rule sub-items.
        self.security_score_item_list = security_score_item_list
        # The name of the security score rule type.
        self.title = title

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

        if self.title is not None:
            result['Title'] = self.title

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
                temp_model = main_models.GetSecurityScoreRuleResponseBodySecurityScoreCategoryListSecurityRuleListSecurityScoreItemList()
                self.security_score_item_list.append(temp_model.from_map(k1))

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class GetSecurityScoreRuleResponseBodySecurityScoreCategoryListSecurityRuleListSecurityScoreItemList(DaraModel):
    def __init__(
        self,
        score: int = None,
        score_threshold: int = None,
        sub_rule_type: str = None,
        title: str = None,
    ):
        # The deduction value of the individual item.
        self.score = score
        # The deduction threshold of the individual item.
        self.score_threshold = score_threshold
        # The type of the security score rule sub-item. Valid values:
        # 
        # - **SS_SAS_WEAK_PW**: Pending weak passwords to fix.
        # - **SS_SAS_ALARM**: Pending Security Center alerts.
        # - **SS_SAS_EMG_VUL**: Pending emergency vulnerabilities to fix.
        # - **SS_SAS_APP_VUL**: Pending application vulnerabilities to fix.
        # - **SS_SAS_SYS_VUL**: Pending system vulnerabilities to fix.
        # - **SS_SAS_CLOUD_HC**: Pending Cloud Security Posture Management (CSPM) risks.
        # - **SS_SDDP_DATA_RISK**: Pending data security risks to remediate.
        # - **SS_WAF_API_RISK**: Pending API security risks.
        # - **SS_DDOS_BH_ASSET**: Assets in Black Hole Activated status.
        # - **SS_SAS_AK_LEAK**: Unhandled AccessKey/SecretKey leakage events.
        # - **SS_PRODUCT_CONNECT**: Security products not in Normal connection status.
        # - **SS_KEY_CONFIG**: Key feature configuration.
        # - **SS_PRODUCT_EXPIRE**: Products about to expire.
        # - **SS_AI_RISK**: AI application risks.
        self.sub_rule_type = sub_rule_type
        # The name of the security score rule sub-item.
        self.title = title

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

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('ScoreThreshold') is not None:
            self.score_threshold = m.get('ScoreThreshold')

        if m.get('SubRuleType') is not None:
            self.sub_rule_type = m.get('SubRuleType')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

