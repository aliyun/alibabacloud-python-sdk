# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListRiskItemsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        risk_items: List[main_models.ListRiskItemsResponseBodyRiskItems] = None,
        total_num: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The list of risk events.
        self.risk_items = risk_items
        # The total number of risk events that meet the query conditions.
        self.total_num = total_num

    def validate(self):
        if self.risk_items:
            for v1 in self.risk_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['RiskItems'] = []
        if self.risk_items is not None:
            for k1 in self.risk_items:
                result['RiskItems'].append(k1.to_map() if k1 else None)

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.risk_items = []
        if m.get('RiskItems') is not None:
            for k1 in m.get('RiskItems'):
                temp_model = main_models.ListRiskItemsResponseBodyRiskItems()
                self.risk_items.append(temp_model.from_map(k1))

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        return self

class ListRiskItemsResponseBodyRiskItems(DaraModel):
    def __init__(
        self,
        agent_name: str = None,
        ai_conclusion: str = None,
        ai_risk_confirm: str = None,
        check_name: str = None,
        department: str = None,
        group_info: str = None,
        hostname: str = None,
        inner_ip: str = None,
        report: str = None,
        risk_analysis_policy_names: List[str] = None,
        risk_category: str = None,
        risk_confirm: str = None,
        risk_confirm_desc: str = None,
        risk_desc: str = None,
        risk_end_time: str = None,
        risk_feature_ids: List[str] = None,
        risk_found_time: str = None,
        risk_id: str = None,
        risk_level: str = None,
        risk_scene: str = None,
        risk_start_time: str = None,
        sase_user_id: str = None,
        skill_name: str = None,
        solution: str = None,
        status: str = None,
        support_analysis: bool = None,
        username: str = None,
    ):
        # The name of the Agent that generated the risk event. An empty string is returned for non-Agent risk scenarios.
        self.agent_name = agent_name
        # The AI risk analysis conclusion.
        self.ai_conclusion = ai_conclusion
        # The risk judgment provided by AI. An empty string is returned if no AI analysis results exist. Valid values:
        # * `Risk`: determined as risky.
        # * `Ignore`: determined as not risky.
        self.ai_risk_confirm = ai_risk_confirm
        # The name of the risk detection item.
        self.check_name = check_name
        # The department to which the user associated with the risk event belongs.
        self.department = department
        # The original organizational structure information of the user associated with the risk event.
        self.group_info = group_info
        # The name of the endpoint device associated with the risk event.
        self.hostname = hostname
        # The internal IP address of the endpoint associated with the risk event.
        self.inner_ip = inner_ip
        # The risk detection report or risk evidence.
        self.report = report
        # The list of risk analysis policy names that were hit.
        self.risk_analysis_policy_names = risk_analysis_policy_names
        # The risk category. Valid values:
        # - `data_safe`: data security.
        # - `identify_safe`: identity security.
        # - `device_safe`: device security.
        # - `access_safe`: access security.
        # - `ai_agent_safe`: Agent security.
        self.risk_category = risk_category
        # The manually confirmed risk conclusion. An empty string is returned if not confirmed. Valid values:
        # * `Risk`: confirmed as risky.
        # * `Ignore`: confirmed as not risky.
        # * `Invalid`: confirmed as a false positive.
        self.risk_confirm = risk_confirm
        # The description of the risk event disposition.
        self.risk_confirm_desc = risk_confirm_desc
        # The risk description.
        self.risk_desc = risk_desc
        # The end time of the risky behavior, in the format of `yyyy-MM-dd HH:mm:ss`.
        self.risk_end_time = risk_end_time
        # The list of detection feature or detection item identifiers that triggered the risk event. A risk event may hit multiple identifiers. The specific values vary based on the risk scenario and detection rules.
        self.risk_feature_ids = risk_feature_ids
        # The time when the risk was detected, in the format of `yyyy-MM-dd HH:mm:ss`.
        self.risk_found_time = risk_found_time
        # The risk event ID.
        self.risk_id = risk_id
        # The risk level. Valid values:
        # - `High`: high risk.
        # - `Medium`: medium risk.
        # - `Low`: low risk.
        self.risk_level = risk_level
        # The risk scenario. Valid values:
        # - `account_share`: account sharing.
        # - `account_stolen`: account theft.
        # - `device_share`: device sharing.
        # - `remote_logon`: remote logon from an unusual location.
        # - `sensitive_data_leakage`: sensitive data exfiltration.
        # - `lateral_scanning`: lateral scanning.
        # - `ai_skill_malware`: malicious Skill.
        # - `ai_config_check`: AI configuration check.
        # - `openclaw_vulnerability`: OpenClaw vulnerability.
        self.risk_scene = risk_scene
        # The start time of the risky behavior, in the format of `yyyy-MM-dd HH:mm:ss`.
        self.risk_start_time = risk_start_time
        # The SASE user ID associated with the risk event.
        self.sase_user_id = sase_user_id
        # The name of the Agent Skill that generated the risk event. An empty string is returned for non-Agent risk scenarios.
        self.skill_name = skill_name
        # The recommended remediation action for the risk event.
        self.solution = solution
        # The disposition status of the risk event. Valid values:
        # * `Unprocess`: unprocessed.
        # * `Processing`: being processed.
        # * `Processed`: processed.
        self.status = status
        # Indicates whether AI risk analysis results exist. Valid values:
        # * `true`: AI risk analysis results exist.
        # * `false`: AI risk analysis results do not exist.
        self.support_analysis = support_analysis
        # The username associated with the risk event.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.ai_conclusion is not None:
            result['AiConclusion'] = self.ai_conclusion

        if self.ai_risk_confirm is not None:
            result['AiRiskConfirm'] = self.ai_risk_confirm

        if self.check_name is not None:
            result['CheckName'] = self.check_name

        if self.department is not None:
            result['Department'] = self.department

        if self.group_info is not None:
            result['GroupInfo'] = self.group_info

        if self.hostname is not None:
            result['Hostname'] = self.hostname

        if self.inner_ip is not None:
            result['InnerIp'] = self.inner_ip

        if self.report is not None:
            result['Report'] = self.report

        if self.risk_analysis_policy_names is not None:
            result['RiskAnalysisPolicyNames'] = self.risk_analysis_policy_names

        if self.risk_category is not None:
            result['RiskCategory'] = self.risk_category

        if self.risk_confirm is not None:
            result['RiskConfirm'] = self.risk_confirm

        if self.risk_confirm_desc is not None:
            result['RiskConfirmDesc'] = self.risk_confirm_desc

        if self.risk_desc is not None:
            result['RiskDesc'] = self.risk_desc

        if self.risk_end_time is not None:
            result['RiskEndTime'] = self.risk_end_time

        if self.risk_feature_ids is not None:
            result['RiskFeatureIds'] = self.risk_feature_ids

        if self.risk_found_time is not None:
            result['RiskFoundTime'] = self.risk_found_time

        if self.risk_id is not None:
            result['RiskId'] = self.risk_id

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.risk_scene is not None:
            result['RiskScene'] = self.risk_scene

        if self.risk_start_time is not None:
            result['RiskStartTime'] = self.risk_start_time

        if self.sase_user_id is not None:
            result['SaseUserId'] = self.sase_user_id

        if self.skill_name is not None:
            result['SkillName'] = self.skill_name

        if self.solution is not None:
            result['Solution'] = self.solution

        if self.status is not None:
            result['Status'] = self.status

        if self.support_analysis is not None:
            result['SupportAnalysis'] = self.support_analysis

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('AiConclusion') is not None:
            self.ai_conclusion = m.get('AiConclusion')

        if m.get('AiRiskConfirm') is not None:
            self.ai_risk_confirm = m.get('AiRiskConfirm')

        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')

        if m.get('Department') is not None:
            self.department = m.get('Department')

        if m.get('GroupInfo') is not None:
            self.group_info = m.get('GroupInfo')

        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')

        if m.get('InnerIp') is not None:
            self.inner_ip = m.get('InnerIp')

        if m.get('Report') is not None:
            self.report = m.get('Report')

        if m.get('RiskAnalysisPolicyNames') is not None:
            self.risk_analysis_policy_names = m.get('RiskAnalysisPolicyNames')

        if m.get('RiskCategory') is not None:
            self.risk_category = m.get('RiskCategory')

        if m.get('RiskConfirm') is not None:
            self.risk_confirm = m.get('RiskConfirm')

        if m.get('RiskConfirmDesc') is not None:
            self.risk_confirm_desc = m.get('RiskConfirmDesc')

        if m.get('RiskDesc') is not None:
            self.risk_desc = m.get('RiskDesc')

        if m.get('RiskEndTime') is not None:
            self.risk_end_time = m.get('RiskEndTime')

        if m.get('RiskFeatureIds') is not None:
            self.risk_feature_ids = m.get('RiskFeatureIds')

        if m.get('RiskFoundTime') is not None:
            self.risk_found_time = m.get('RiskFoundTime')

        if m.get('RiskId') is not None:
            self.risk_id = m.get('RiskId')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('RiskScene') is not None:
            self.risk_scene = m.get('RiskScene')

        if m.get('RiskStartTime') is not None:
            self.risk_start_time = m.get('RiskStartTime')

        if m.get('SaseUserId') is not None:
            self.sase_user_id = m.get('SaseUserId')

        if m.get('SkillName') is not None:
            self.skill_name = m.get('SkillName')

        if m.get('Solution') is not None:
            self.solution = m.get('Solution')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SupportAnalysis') is not None:
            self.support_analysis = m.get('SupportAnalysis')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

