# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateClientRuleStrategyShrinkRequest(DaraModel):
    def __init__(
        self,
        action_type: int = None,
        all_group: int = None,
        approval_id: str = None,
        cmdline: str = None,
        description: str = None,
        exclude_user_name_list_shrink: str = None,
        file_path: str = None,
        id: int = None,
        in_switch: bool = None,
        include_group_id_list_shrink: str = None,
        ip: str = None,
        main_button_text_ch: str = None,
        main_button_text_en: str = None,
        match_mode: str = None,
        match_target_ids: List[str] = None,
        md_5list: str = None,
        minor_button_text_ch: str = None,
        minor_button_text_en: str = None,
        name: str = None,
        new_file_path: str = None,
        out_switch: bool = None,
        parent_cmdline: str = None,
        parent_proc_path: str = None,
        platform: str = None,
        policy_type: int = None,
        port: str = None,
        port_on_list_shrink: str = None,
        priority: int = None,
        proc_path: str = None,
        registry_content: str = None,
        registry_key: str = None,
        rule_type: int = None,
        soft_ware_on_list_shrink: str = None,
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
        # - **0**: monitor mode
        # - **1**: prevent startup
        # - **2**: block mode
        # 
        # Valid values for custom rules of proactive defense (PolicyType=2):
        # 
        # - **0**: whitelist and allow
        # - **1**: blacklist and block
        self.action_type = action_type
        # Specifies whether the policy takes effect for all user groups. Valid values:
        # 
        # - **0**: no
        # - **1**: yes
        self.all_group = all_group
        # The ID of the approval process.
        self.approval_id = approval_id
        # The matched process command line.
        self.cmdline = cmdline
        # The policy description.
        # > The maximum length is 128 characters.
        self.description = description
        # The list of usernames for which the policy does not take effect.
        self.exclude_user_name_list_shrink = exclude_user_name_list_shrink
        # The matched file path.
        self.file_path = file_path
        # The policy ID.
        # 
        # This parameter is required.
        self.id = id
        # The inbound network switch.
        self.in_switch = in_switch
        # The list of IDs of the user groups for which the policy takes effect.
        self.include_group_id_list_shrink = include_group_id_list_shrink
        # The matched IP address.
        self.ip = ip
        # The text of the primary button in the Chinese button configuration.
        self.main_button_text_ch = main_button_text_ch
        # The text of the primary button in the English button configuration.
        self.main_button_text_en = main_button_text_en
        # The effective scope mode. Valid values:
        # 
        # - **UserGroupAll**: all user groups
        # - **UserGroupNormal**: specified user groups
        # - **DeviceGroupNormal**: specified device groups
        # - **DevTagNormal**: specified device tags
        self.match_mode = match_mode
        # The list of targets in the effective scope. The meaning of the targets is determined by MatchMode.
        self.match_target_ids = match_target_ids
        # The MD5 match string for the file.
        self.md_5list = md_5list
        # The text of the secondary button in the Chinese button configuration.
        self.minor_button_text_ch = minor_button_text_ch
        # The text of the secondary button in the English button configuration.
        self.minor_button_text_en = minor_button_text_en
        # The policy name.
        # > The maximum length is 128 characters.
        self.name = name
        # The matched new file path.
        self.new_file_path = new_file_path
        # The outbound network switch.
        self.out_switch = out_switch
        # The matched parent process command line.
        self.parent_cmdline = parent_cmdline
        # The matched parent process path.
        self.parent_proc_path = parent_proc_path
        # The platform to which the rule applies. Valid values:
        # 
        # - **linux**
        # - **windows**
        # - **mac**
        # - **all**: all platforms
        self.platform = platform
        # The policy type. Valid values:
        # 
        # - **0**: software hardening
        # - **1**: firewall
        # - **2**: proactive defense
        # 
        # This parameter is required.
        self.policy_type = policy_type
        # The matched port.
        self.port = port
        # The list of enabled ports.
        # > This parameter is valid only when the policy type is firewall.
        self.port_on_list_shrink = port_on_list_shrink
        # The policy priority. A smaller value indicates a higher priority. Valid values: greater than 0.
        self.priority = priority
        # The matched process path.
        self.proc_path = proc_path
        # The matched registry content.
        self.registry_content = registry_content
        # The matched registry key.
        self.registry_key = registry_key
        # The defense rule type. Valid values: 1 to 7.
        self.rule_type = rule_type
        # The list of main process names of the software for which integrity check is enabled. The elements correspond to the Process returned by GetSwitchInfoListByType.
        self.soft_ware_on_list_shrink = soft_ware_on_list_shrink
        # The policy status. Valid values:
        # 
        # - **0**: disabled
        # - **1**: enabled
        self.status = status
        # The rule source for proactive defense (PolicyType=2). Valid values:
        # 
        # - **SYSTEM**: system rules
        # - **CUSTOM**: custom rules
        self.strategy_source_type = strategy_source_type
        # Specifies whether approval requests are supported. Valid values:
        # 
        # - **0**: not supported
        # - **1**: supported
        self.supports_approval = supports_approval
        # The English content in the pop-up prompt configuration.
        self.us_content = us_content
        # The English title in the pop-up prompt configuration.
        self.us_title = us_title
        # The Chinese content in the pop-up prompt configuration.
        self.zh_content = zh_content
        # The Chinese title in the pop-up prompt configuration.
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

        if self.cmdline is not None:
            result['Cmdline'] = self.cmdline

        if self.description is not None:
            result['Description'] = self.description

        if self.exclude_user_name_list_shrink is not None:
            result['ExcludeUserNameList'] = self.exclude_user_name_list_shrink

        if self.file_path is not None:
            result['FilePath'] = self.file_path

        if self.id is not None:
            result['Id'] = self.id

        if self.in_switch is not None:
            result['InSwitch'] = self.in_switch

        if self.include_group_id_list_shrink is not None:
            result['IncludeGroupIdList'] = self.include_group_id_list_shrink

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.main_button_text_ch is not None:
            result['MainButtonTextCh'] = self.main_button_text_ch

        if self.main_button_text_en is not None:
            result['MainButtonTextEn'] = self.main_button_text_en

        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode

        if self.match_target_ids is not None:
            result['MatchTargetIds'] = self.match_target_ids

        if self.md_5list is not None:
            result['Md5List'] = self.md_5list

        if self.minor_button_text_ch is not None:
            result['MinorButtonTextCh'] = self.minor_button_text_ch

        if self.minor_button_text_en is not None:
            result['MinorButtonTextEn'] = self.minor_button_text_en

        if self.name is not None:
            result['Name'] = self.name

        if self.new_file_path is not None:
            result['NewFilePath'] = self.new_file_path

        if self.out_switch is not None:
            result['OutSwitch'] = self.out_switch

        if self.parent_cmdline is not None:
            result['ParentCmdline'] = self.parent_cmdline

        if self.parent_proc_path is not None:
            result['ParentProcPath'] = self.parent_proc_path

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        if self.port is not None:
            result['Port'] = self.port

        if self.port_on_list_shrink is not None:
            result['PortOnList'] = self.port_on_list_shrink

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.proc_path is not None:
            result['ProcPath'] = self.proc_path

        if self.registry_content is not None:
            result['RegistryContent'] = self.registry_content

        if self.registry_key is not None:
            result['RegistryKey'] = self.registry_key

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        if self.soft_ware_on_list_shrink is not None:
            result['SoftWareOnList'] = self.soft_ware_on_list_shrink

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

        if m.get('Cmdline') is not None:
            self.cmdline = m.get('Cmdline')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExcludeUserNameList') is not None:
            self.exclude_user_name_list_shrink = m.get('ExcludeUserNameList')

        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InSwitch') is not None:
            self.in_switch = m.get('InSwitch')

        if m.get('IncludeGroupIdList') is not None:
            self.include_group_id_list_shrink = m.get('IncludeGroupIdList')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('MainButtonTextCh') is not None:
            self.main_button_text_ch = m.get('MainButtonTextCh')

        if m.get('MainButtonTextEn') is not None:
            self.main_button_text_en = m.get('MainButtonTextEn')

        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')

        if m.get('MatchTargetIds') is not None:
            self.match_target_ids = m.get('MatchTargetIds')

        if m.get('Md5List') is not None:
            self.md_5list = m.get('Md5List')

        if m.get('MinorButtonTextCh') is not None:
            self.minor_button_text_ch = m.get('MinorButtonTextCh')

        if m.get('MinorButtonTextEn') is not None:
            self.minor_button_text_en = m.get('MinorButtonTextEn')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NewFilePath') is not None:
            self.new_file_path = m.get('NewFilePath')

        if m.get('OutSwitch') is not None:
            self.out_switch = m.get('OutSwitch')

        if m.get('ParentCmdline') is not None:
            self.parent_cmdline = m.get('ParentCmdline')

        if m.get('ParentProcPath') is not None:
            self.parent_proc_path = m.get('ParentProcPath')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('PortOnList') is not None:
            self.port_on_list_shrink = m.get('PortOnList')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ProcPath') is not None:
            self.proc_path = m.get('ProcPath')

        if m.get('RegistryContent') is not None:
            self.registry_content = m.get('RegistryContent')

        if m.get('RegistryKey') is not None:
            self.registry_key = m.get('RegistryKey')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('SoftWareOnList') is not None:
            self.soft_ware_on_list_shrink = m.get('SoftWareOnList')

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

