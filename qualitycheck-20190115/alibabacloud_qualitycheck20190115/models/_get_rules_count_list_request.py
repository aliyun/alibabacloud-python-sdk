# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetRulesCountListRequest(DaraModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        business_name: str = None,
        business_range: int = None,
        category_name: str = None,
        count_total: bool = None,
        create_empid: str = None,
        create_user_id: int = None,
        current_page: int = None,
        end_time: str = None,
        last_update_empid: str = None,
        page_number: int = None,
        page_size: int = None,
        require_infos: List[str] = None,
        rid: int = None,
        rule_id_or_rule_name: str = None,
        rule_score_single_type: int = None,
        rule_type: int = None,
        scheme_id: int = None,
        source_type: int = None,
        start_time: str = None,
        status: int = None,
        type: int = None,
        type_name: str = None,
        update_end_time: str = None,
        update_start_time: str = None,
        update_user_id: int = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        self.business_name = business_name
        self.business_range = business_range
        self.category_name = category_name
        self.count_total = count_total
        self.create_empid = create_empid
        self.create_user_id = create_user_id
        self.current_page = current_page
        self.end_time = end_time
        self.last_update_empid = last_update_empid
        self.page_number = page_number
        self.page_size = page_size
        self.require_infos = require_infos
        self.rid = rid
        self.rule_id_or_rule_name = rule_id_or_rule_name
        self.rule_score_single_type = rule_score_single_type
        self.rule_type = rule_type
        self.scheme_id = scheme_id
        self.source_type = source_type
        self.start_time = start_time
        self.status = status
        self.type = type
        self.type_name = type_name
        self.update_end_time = update_end_time
        self.update_start_time = update_start_time
        self.update_user_id = update_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id

        if self.business_name is not None:
            result['BusinessName'] = self.business_name

        if self.business_range is not None:
            result['BusinessRange'] = self.business_range

        if self.category_name is not None:
            result['CategoryName'] = self.category_name

        if self.count_total is not None:
            result['CountTotal'] = self.count_total

        if self.create_empid is not None:
            result['CreateEmpid'] = self.create_empid

        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.last_update_empid is not None:
            result['LastUpdateEmpid'] = self.last_update_empid

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.require_infos is not None:
            result['RequireInfos'] = self.require_infos

        if self.rid is not None:
            result['Rid'] = self.rid

        if self.rule_id_or_rule_name is not None:
            result['RuleIdOrRuleName'] = self.rule_id_or_rule_name

        if self.rule_score_single_type is not None:
            result['RuleScoreSingleType'] = self.rule_score_single_type

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        if self.scheme_id is not None:
            result['SchemeId'] = self.scheme_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.type_name is not None:
            result['TypeName'] = self.type_name

        if self.update_end_time is not None:
            result['UpdateEndTime'] = self.update_end_time

        if self.update_start_time is not None:
            result['UpdateStartTime'] = self.update_start_time

        if self.update_user_id is not None:
            result['UpdateUserId'] = self.update_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')

        if m.get('BusinessName') is not None:
            self.business_name = m.get('BusinessName')

        if m.get('BusinessRange') is not None:
            self.business_range = m.get('BusinessRange')

        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')

        if m.get('CountTotal') is not None:
            self.count_total = m.get('CountTotal')

        if m.get('CreateEmpid') is not None:
            self.create_empid = m.get('CreateEmpid')

        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('LastUpdateEmpid') is not None:
            self.last_update_empid = m.get('LastUpdateEmpid')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequireInfos') is not None:
            self.require_infos = m.get('RequireInfos')

        if m.get('Rid') is not None:
            self.rid = m.get('Rid')

        if m.get('RuleIdOrRuleName') is not None:
            self.rule_id_or_rule_name = m.get('RuleIdOrRuleName')

        if m.get('RuleScoreSingleType') is not None:
            self.rule_score_single_type = m.get('RuleScoreSingleType')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('SchemeId') is not None:
            self.scheme_id = m.get('SchemeId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')

        if m.get('UpdateEndTime') is not None:
            self.update_end_time = m.get('UpdateEndTime')

        if m.get('UpdateStartTime') is not None:
            self.update_start_time = m.get('UpdateStartTime')

        if m.get('UpdateUserId') is not None:
            self.update_user_id = m.get('UpdateUserId')

        return self

