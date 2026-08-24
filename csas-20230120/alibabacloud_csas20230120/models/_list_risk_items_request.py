# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListRiskItemsRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        policy_name: str = None,
        risk_category: str = None,
        risk_id: str = None,
        risk_level: str = None,
        risk_scene: str = None,
        status: str = None,
        status_list: List[str] = None,
        username: str = None,
    ):
        # The page number of the current page in a paging query. Valid values: 1 to 10000.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The number of entries per page in a paging query. Valid values: 1 to 100.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The name of the risk analysis policy. Fuzzy match is supported.
        self.policy_name = policy_name
        # The risk category. Valid values:
        # * `data_safe`: data security.
        # * `identify_safe`: identity security.
        # * `device_safe`: device security.
        # * `access_safe`: access security.
        # * `ai_agent_safe`: Agent security.
        self.risk_category = risk_category
        # The risk event ID. If specified, the exact risk event is queried.
        self.risk_id = risk_id
        # The risk level. Valid values:
        # * `High`: high risk.
        # * `Medium`: medium risk.
        # * `Low`: low risk.
        self.risk_level = risk_level
        # The risk scenario. Valid values:
        # * `account_share`: account sharing.
        # * `account_stolen`: account theft.
        # * `device_share`: device sharing.
        # * `remote_logon`: remote logon from an unusual location.
        # * `sensitive_data_leakage`: sensitive data exfiltration.
        # * `compressed_archive_exfil`: compressed data exfiltration from the internal network.
        # * `lateral_scanning`: lateral scanning.
        # * `ai_skill_malware`: malicious Skill.
        # * `ai_config_check`: AI configuration check.
        # * `openclaw_vulnerability`: OpenClaw vulnerability.
        self.risk_scene = risk_scene
        # The disposition status of the risk event. This parameter cannot be set together with `StatusList`.
        self.status = status
        # The list of disposition statuses of risk events, in Flat serialization format. This parameter cannot be set together with Status.
        self.status_list = status_list
        # The username associated with the risk event. Fuzzy match is supported. Maximum length: 128 characters.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.risk_category is not None:
            result['RiskCategory'] = self.risk_category

        if self.risk_id is not None:
            result['RiskId'] = self.risk_id

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.risk_scene is not None:
            result['RiskScene'] = self.risk_scene

        if self.status is not None:
            result['Status'] = self.status

        if self.status_list is not None:
            result['StatusList'] = self.status_list

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('RiskCategory') is not None:
            self.risk_category = m.get('RiskCategory')

        if m.get('RiskId') is not None:
            self.risk_id = m.get('RiskId')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('RiskScene') is not None:
            self.risk_scene = m.get('RiskScene')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

