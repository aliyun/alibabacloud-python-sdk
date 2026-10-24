# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csasedr20241122 import models as main_models
from darabonba.model import DaraModel

class ListClientRuleStrategyResponseBody(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListClientRuleStrategyResponseBodyList] = None,
        page_info: main_models.ListClientRuleStrategyResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The list of policies.
        self.list = list
        # The pagination information.
        self.page_info = page_info
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.ListClientRuleStrategyResponseBodyList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.ListClientRuleStrategyResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListClientRuleStrategyResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The page number of the current page for the paged query with paging.
        self.current_page = current_page
        # The maximum number of entries returned per page for the paged query with paging.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

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

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListClientRuleStrategyResponseBodyList(DaraModel):
    def __init__(
        self,
        action_type: int = None,
        all_group: int = None,
        approval_id: str = None,
        create_time: int = None,
        description: str = None,
        exclude_user_name_list: List[str] = None,
        id: int = None,
        in_switch: bool = None,
        include_group_id_list: List[str] = None,
        main_button_text_ch: str = None,
        main_button_text_en: str = None,
        match_mode: str = None,
        match_target_ids: List[str] = None,
        minor_button_text_ch: str = None,
        minor_button_text_en: str = None,
        name: str = None,
        out_switch: bool = None,
        policy_type: int = None,
        port_on_list: List[str] = None,
        priority: int = None,
        selection_key: str = None,
        soft_ware_on_list: List[str] = None,
        status: int = None,
        strategy_source_type: str = None,
        supports_approval: int = None,
        us_content: str = None,
        us_title: str = None,
        zh_content: str = None,
        zh_title: str = None,
    ):
        # The policy action. Valid values:
        # 
        # - **0**: Monitor mode.
        # - **1**: Block startup.
        # - **2**: Block mode.
        # 
        # Valid values for custom rules of proactive defense (PolicyType=2):
        # 
        # - **0**: Allow.
        # - **1**: Block.
        self.action_type = action_type
        # Specifies whether the policy applies to all user groups. Valid values:
        # 
        # - **0**: No.
        # - **1**: Yes.
        self.all_group = all_group
        # The instance ID of the approval.
        self.approval_id = approval_id
        # The timestamp when the policy was created. Unit: milliseconds.
        self.create_time = create_time
        # The description of the policy.
        self.description = description
        # The list of usernames to which the policy does not apply.
        self.exclude_user_name_list = exclude_user_name_list
        # The ID of the policy.
        self.id = id
        # The switch for inbound network traffic.
        self.in_switch = in_switch
        # The list of targets in the effective scope.
        self.include_group_id_list = include_group_id_list
        # The text of the primary button in Chinese.
        self.main_button_text_ch = main_button_text_ch
        # The text of the primary button in English.
        self.main_button_text_en = main_button_text_en
        # The effective scope mode. Valid values:
        # 
        # - **UserGroupAll**: All user groups.
        # - **UserGroupNormal**: Specified user groups.
        # - **DeviceGroupNormal**: Specified device groups.
        # - **DevTagNormal**: Specified device tags.
        # 
        # The meaning of MatchTargetIds is determined by this field.
        self.match_mode = match_mode
        # The list of targets in the effective scope. UserGroupNormal corresponds to user group IDs, DeviceGroupNormal corresponds to device group IDs, and DevTagNormal corresponds to device tags. If MatchMode is set to UserGroupAll, you do not need to specify targets.
        self.match_target_ids = match_target_ids
        # The text of the secondary button in Chinese.
        self.minor_button_text_ch = minor_button_text_ch
        # The text of the secondary button in English.
        self.minor_button_text_en = minor_button_text_en
        # The Policy Name.
        self.name = name
        # The switch for outbound network traffic.
        self.out_switch = out_switch
        # The policy type. Valid values:
        # 
        # - **0**: Software hardening.
        # - **1**: Firewall.
        # - **2**: Proactive defense.
        self.policy_type = policy_type
        # The list of enabled ports.
        self.port_on_list = port_on_list
        # The policy priority. A smaller value indicates a higher priority. Valid values: greater than 0.
        self.priority = priority
        # The association key of the policy configuration, which is used to associate the policy with its process or switch configuration.
        self.selection_key = selection_key
        # The list of main process names of the software for which integrity check is enabled. The elements correspond to the Process field returned by GetSwitchInfoListByType.
        self.soft_ware_on_list = soft_ware_on_list
        # The status of the policy. Valid values:
        # 
        # - **0**: Disabled.
        # - **1**: Enabled.
        self.status = status
        # The source of the rule for proactive defense (PolicyType=2). Valid values:
        # 
        # - **SYSTEM**: System rule.
        # - **CUSTOM**: Custom rule.
        self.strategy_source_type = strategy_source_type
        # Specifies whether reporting and approval are supported. Valid values:
        # 
        # - **0**: Not supported.
        # - **1**: Supported.
        self.supports_approval = supports_approval
        # The content of the pop-up prompt in English.
        self.us_content = us_content
        # The title of the pop-up prompt in English.
        self.us_title = us_title
        # The content of the pop-up prompt in Chinese.
        self.zh_content = zh_content
        # The title of the pop-up prompt in Chinese.
        self.zh_title = zh_title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_type is not None:
            result['ActionType'] = self.action_type

        if self.all_group is not None:
            result['AllGroup'] = self.all_group

        if self.approval_id is not None:
            result['ApprovalId'] = self.approval_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.exclude_user_name_list is not None:
            result['ExcludeUserNameList'] = self.exclude_user_name_list

        if self.id is not None:
            result['Id'] = self.id

        if self.in_switch is not None:
            result['InSwitch'] = self.in_switch

        if self.include_group_id_list is not None:
            result['IncludeGroupIdList'] = self.include_group_id_list

        if self.main_button_text_ch is not None:
            result['MainButtonTextCh'] = self.main_button_text_ch

        if self.main_button_text_en is not None:
            result['MainButtonTextEn'] = self.main_button_text_en

        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode

        if self.match_target_ids is not None:
            result['MatchTargetIds'] = self.match_target_ids

        if self.minor_button_text_ch is not None:
            result['MinorButtonTextCh'] = self.minor_button_text_ch

        if self.minor_button_text_en is not None:
            result['MinorButtonTextEn'] = self.minor_button_text_en

        if self.name is not None:
            result['Name'] = self.name

        if self.out_switch is not None:
            result['OutSwitch'] = self.out_switch

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        if self.port_on_list is not None:
            result['PortOnList'] = self.port_on_list

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.selection_key is not None:
            result['SelectionKey'] = self.selection_key

        if self.soft_ware_on_list is not None:
            result['SoftWareOnList'] = self.soft_ware_on_list

        if self.status is not None:
            result['Status'] = self.status

        if self.strategy_source_type is not None:
            result['StrategySourceType'] = self.strategy_source_type

        if self.supports_approval is not None:
            result['SupportsApproval'] = self.supports_approval

        if self.us_content is not None:
            result['UsContent'] = self.us_content

        if self.us_title is not None:
            result['UsTitle'] = self.us_title

        if self.zh_content is not None:
            result['ZhContent'] = self.zh_content

        if self.zh_title is not None:
            result['ZhTitle'] = self.zh_title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')

        if m.get('AllGroup') is not None:
            self.all_group = m.get('AllGroup')

        if m.get('ApprovalId') is not None:
            self.approval_id = m.get('ApprovalId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExcludeUserNameList') is not None:
            self.exclude_user_name_list = m.get('ExcludeUserNameList')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InSwitch') is not None:
            self.in_switch = m.get('InSwitch')

        if m.get('IncludeGroupIdList') is not None:
            self.include_group_id_list = m.get('IncludeGroupIdList')

        if m.get('MainButtonTextCh') is not None:
            self.main_button_text_ch = m.get('MainButtonTextCh')

        if m.get('MainButtonTextEn') is not None:
            self.main_button_text_en = m.get('MainButtonTextEn')

        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')

        if m.get('MatchTargetIds') is not None:
            self.match_target_ids = m.get('MatchTargetIds')

        if m.get('MinorButtonTextCh') is not None:
            self.minor_button_text_ch = m.get('MinorButtonTextCh')

        if m.get('MinorButtonTextEn') is not None:
            self.minor_button_text_en = m.get('MinorButtonTextEn')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OutSwitch') is not None:
            self.out_switch = m.get('OutSwitch')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        if m.get('PortOnList') is not None:
            self.port_on_list = m.get('PortOnList')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('SelectionKey') is not None:
            self.selection_key = m.get('SelectionKey')

        if m.get('SoftWareOnList') is not None:
            self.soft_ware_on_list = m.get('SoftWareOnList')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StrategySourceType') is not None:
            self.strategy_source_type = m.get('StrategySourceType')

        if m.get('SupportsApproval') is not None:
            self.supports_approval = m.get('SupportsApproval')

        if m.get('UsContent') is not None:
            self.us_content = m.get('UsContent')

        if m.get('UsTitle') is not None:
            self.us_title = m.get('UsTitle')

        if m.get('ZhContent') is not None:
            self.zh_content = m.get('ZhContent')

        if m.get('ZhTitle') is not None:
            self.zh_title = m.get('ZhTitle')

        return self

