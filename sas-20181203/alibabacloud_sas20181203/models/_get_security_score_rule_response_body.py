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
        # The status of the custom settings of the security score feature.
        # 
        # *   true: enabled
        # *   false: disabled
        self.enable_status = enable_status
        # The request ID.
        self.request_id = request_id
        # The information about the new version of the security score rule.
        self.security_score_category_list = security_score_category_list
        # The information about the old version of the security score rule.
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
        # The deduction module that is supported by the security score feature. Valid values:
        # 
        # *   SS_REINFORCE: issue in key feature configuration
        # *   SS_ALARM: unhandled alert
        # *   SS_VUL: unfixed vulnerability
        # *   SS_HC: baseline risk
        # *   SS_CLOUD_HC: risk item of configuration assessment
        # *   SS_AK: risk of AccessKey pair leaks
        self.rule_type = rule_type
        # The deduction threshold of the deduction module.
        # 
        # >  Valid values: 0 to 100. The sum of the deduction thresholds for all deduction modules must be equal to 100.
        self.score = score
        # The deduction items of the deduction module.
        self.security_score_item_list = security_score_item_list
        # The description of the deduction module.
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
        # The penalty point of the deduction item.
        self.score = score
        # The threshold for the deduction item.
        # 
        # >  Valid values: 0 to the deduction threshold of the deduction module.
        self.score_threshold = score_threshold
        # The deduction item of the deduction module. The following list describes the deduction modules and their deduction items:
        # 
        # *   SS_REINFORCE: issue in key feature configuration
        # 
        #     *   XPRESS_INSTALL: Security Center is not authorized.
        #     *   REINFORCE_SUSPICIOUS: The antivirus feature is disabled.
        #     *   RANSOMWARE: The anti-ransomware policy is disabled.
        #     *   WEB_LOCK: The web tamper proofing feature is disabled.
        #     *   VIRUS_SCHEDULE_SCAN: The periodic virus scan policy is disabled.
        #     *   IMAGE_REPO_SCAN: The range of container image scan is not configured.
        #     *   IMAGE_SCAN_TASK: The feature of one-click scan of container images for security risks is not performed.
        # 
        # *   SS_ALARM: unhandled alert.
        # 
        #     *   ALARM_SERIOUS: An unhandled high-risk alert event is detected.
        #     *   ALARM_SUSPICIOUS: An unhandled medium-risk alarm event is detected.
        #     *   ALARM_REMIND: An unhandled low-risk alarm event is detected.
        # 
        # *   SS_VUL: unfixed vulnerability
        # 
        #     *   CMS_UNFIX: An unfixed Web-CMS vulnerability is detected.
        #     *   WIN_UNFIX: An unfixed Windows host vulnerability is detected.
        #     *   CVE_UNFIX: An unfixed Linux host vulnerability is detected.
        #     *   ERM_UNFIX: An unfixed urgent vulnerability is detected.
        #     *   ERM_UNCHECK: An undetected urgent vulnerability exists.
        # 
        # *   SS_HC: baseline risks
        # 
        #     *   WEAK_EXPLOIT: Weak passwords are exposed to the Internet.
        #     *   WEAK_PASSWORD: Weak passwords exist.
        #     *   HC_EXPLOIT: The data source may be hacked.
        #     *   HC_OTHER_WARNING: Security configuration risks exist.
        # 
        # *   SS_CLOUD_HC: Cloud platform configuration check item problem.
        # 
        #     *   CSPM_CIEM_NOT_PASS: A CIEM check item failed the check.
        #     *   CSPM_RISK_NOT_PASS: A security risk check item failed the check.
        #     *   CSPM_COMPLIANCE_NOT_PASS: A compliance check item failed the check.
        # 
        # *   SS_AK: risk of AccessKey pair leaks
        self.sub_rule_type = sub_rule_type
        # The description of the deduction item in a deduction module.
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
        # 
        # *   **SS_SAS_HANDLE**: security governance.
        # *   **SS_SAS_RESPOND**: security response.
        self.category = category
        # The threshold of deduction for the security score rule type.
        self.score = score
        # The deduction items of the security score rule.
        self.security_rule_list = security_rule_list
        # The category of the security score rule.
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
        # The threshold of deduction for the security score rule type.
        self.score = score
        # The sub-deduction items of the security score rule.
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
        # The deduction score for the item.
        self.score = score
        # The threshold of the deduction score for the item.
        self.score_threshold = score_threshold
        # The type of the sub-deduction item. Valid values:
        # 
        # *   **SS_SAS_WEAK_PW**: unhandled weak password risk.
        # *   **SS_SAS_ALARM**: unhandled alert in Security Center.
        # *   **SS_SAS_EMG_VUL**: unfixed urgent vulnerability.
        # *   **SS_SAS_APP_VUL**: unfixed application vulnerability.
        # *   **SS_SAS_SYS_VUL**: unfixed system vulnerability.
        # *   **SS_SAS_CLOUD_HC**: unhandled cloud security posture management (CSPM) risk.
        # *   **SS_SDDP_DATA_RISK**: unhandled data security risk.
        # *   **SS_WAF_API_RISK**: unhandled API security risk.
        # *   **SS_DDOS_BH_ASSET**: asset on which blackhole filtering is triggered.
        # *   **SS_SAS_AK_LEAK**: unhandled AK/SK leak event.
        # *   **SS_PRODUCT_CONNECT**: security service not integrated.
        # *   **SS_KEY_CONFIG**: key feature configuration.
        # *   **SS_PRODUCT_EXPIRE**: service that is about to expire.
        # *   **SS_AI_RISK**: AI application risk.
        self.sub_rule_type = sub_rule_type
        # The name of the sub-deduction item of the security score rule.
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

