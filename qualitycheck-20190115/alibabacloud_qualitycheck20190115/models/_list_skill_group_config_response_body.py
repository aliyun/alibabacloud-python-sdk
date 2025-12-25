# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class ListSkillGroupConfigResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListSkillGroupConfigResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListSkillGroupConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListSkillGroupConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        skill_group_config: List[main_models.ListSkillGroupConfigResponseBodyDataSkillGroupConfig] = None,
    ):
        self.skill_group_config = skill_group_config

    def validate(self):
        if self.skill_group_config:
            for v1 in self.skill_group_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SkillGroupConfig'] = []
        if self.skill_group_config is not None:
            for k1 in self.skill_group_config:
                result['SkillGroupConfig'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.skill_group_config = []
        if m.get('SkillGroupConfig') is not None:
            for k1 in m.get('SkillGroupConfig'):
                temp_model = main_models.ListSkillGroupConfigResponseBodyDataSkillGroupConfig()
                self.skill_group_config.append(temp_model.from_map(k1))

        return self

class ListSkillGroupConfigResponseBodyDataSkillGroupConfig(DaraModel):
    def __init__(
        self,
        all_content_quality_check: int = None,
        all_rids: str = None,
        all_rule_list: main_models.ListSkillGroupConfigResponseBodyDataSkillGroupConfigAllRuleList = None,
        create_time: str = None,
        id: int = None,
        instance_id: str = None,
        model_id: int = None,
        model_name: str = None,
        name: str = None,
        quality_check_type: int = None,
        rid: str = None,
        rule_list: main_models.ListSkillGroupConfigResponseBodyDataSkillGroupConfigRuleList = None,
        screen_switch: bool = None,
        skill_group_from: int = None,
        skill_group_id: str = None,
        skill_group_name: str = None,
        skill_group_screens: main_models.ListSkillGroupConfigResponseBodyDataSkillGroupConfigSkillGroupScreens = None,
        status: int = None,
        type: int = None,
        update_time: str = None,
        vocab_id: int = None,
        vocab_name: str = None,
    ):
        self.all_content_quality_check = all_content_quality_check
        self.all_rids = all_rids
        self.all_rule_list = all_rule_list
        self.create_time = create_time
        self.id = id
        self.instance_id = instance_id
        self.model_id = model_id
        self.model_name = model_name
        self.name = name
        self.quality_check_type = quality_check_type
        self.rid = rid
        self.rule_list = rule_list
        self.screen_switch = screen_switch
        self.skill_group_from = skill_group_from
        self.skill_group_id = skill_group_id
        self.skill_group_name = skill_group_name
        self.skill_group_screens = skill_group_screens
        self.status = status
        self.type = type
        self.update_time = update_time
        self.vocab_id = vocab_id
        self.vocab_name = vocab_name

    def validate(self):
        if self.all_rule_list:
            self.all_rule_list.validate()
        if self.rule_list:
            self.rule_list.validate()
        if self.skill_group_screens:
            self.skill_group_screens.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all_content_quality_check is not None:
            result['AllContentQualityCheck'] = self.all_content_quality_check

        if self.all_rids is not None:
            result['AllRids'] = self.all_rids

        if self.all_rule_list is not None:
            result['AllRuleList'] = self.all_rule_list.to_map()

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.model_id is not None:
            result['ModelId'] = self.model_id

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.name is not None:
            result['Name'] = self.name

        if self.quality_check_type is not None:
            result['QualityCheckType'] = self.quality_check_type

        if self.rid is not None:
            result['Rid'] = self.rid

        if self.rule_list is not None:
            result['RuleList'] = self.rule_list.to_map()

        if self.screen_switch is not None:
            result['ScreenSwitch'] = self.screen_switch

        if self.skill_group_from is not None:
            result['SkillGroupFrom'] = self.skill_group_from

        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id

        if self.skill_group_name is not None:
            result['SkillGroupName'] = self.skill_group_name

        if self.skill_group_screens is not None:
            result['SkillGroupScreens'] = self.skill_group_screens.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.vocab_id is not None:
            result['VocabId'] = self.vocab_id

        if self.vocab_name is not None:
            result['VocabName'] = self.vocab_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllContentQualityCheck') is not None:
            self.all_content_quality_check = m.get('AllContentQualityCheck')

        if m.get('AllRids') is not None:
            self.all_rids = m.get('AllRids')

        if m.get('AllRuleList') is not None:
            temp_model = main_models.ListSkillGroupConfigResponseBodyDataSkillGroupConfigAllRuleList()
            self.all_rule_list = temp_model.from_map(m.get('AllRuleList'))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('QualityCheckType') is not None:
            self.quality_check_type = m.get('QualityCheckType')

        if m.get('Rid') is not None:
            self.rid = m.get('Rid')

        if m.get('RuleList') is not None:
            temp_model = main_models.ListSkillGroupConfigResponseBodyDataSkillGroupConfigRuleList()
            self.rule_list = temp_model.from_map(m.get('RuleList'))

        if m.get('ScreenSwitch') is not None:
            self.screen_switch = m.get('ScreenSwitch')

        if m.get('SkillGroupFrom') is not None:
            self.skill_group_from = m.get('SkillGroupFrom')

        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')

        if m.get('SkillGroupName') is not None:
            self.skill_group_name = m.get('SkillGroupName')

        if m.get('SkillGroupScreens') is not None:
            temp_model = main_models.ListSkillGroupConfigResponseBodyDataSkillGroupConfigSkillGroupScreens()
            self.skill_group_screens = temp_model.from_map(m.get('SkillGroupScreens'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('VocabId') is not None:
            self.vocab_id = m.get('VocabId')

        if m.get('VocabName') is not None:
            self.vocab_name = m.get('VocabName')

        return self

class ListSkillGroupConfigResponseBodyDataSkillGroupConfigSkillGroupScreens(DaraModel):
    def __init__(
        self,
        skill_group_screen: List[main_models.ListSkillGroupConfigResponseBodyDataSkillGroupConfigSkillGroupScreensSkillGroupScreen] = None,
    ):
        self.skill_group_screen = skill_group_screen

    def validate(self):
        if self.skill_group_screen:
            for v1 in self.skill_group_screen:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SkillGroupScreen'] = []
        if self.skill_group_screen is not None:
            for k1 in self.skill_group_screen:
                result['SkillGroupScreen'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.skill_group_screen = []
        if m.get('SkillGroupScreen') is not None:
            for k1 in m.get('SkillGroupScreen'):
                temp_model = main_models.ListSkillGroupConfigResponseBodyDataSkillGroupConfigSkillGroupScreensSkillGroupScreen()
                self.skill_group_screen.append(temp_model.from_map(k1))

        return self

class ListSkillGroupConfigResponseBodyDataSkillGroupConfigSkillGroupScreensSkillGroupScreen(DaraModel):
    def __init__(
        self,
        data_type: int = None,
        name: str = None,
        symbol: int = None,
        value: str = None,
    ):
        self.data_type = data_type
        self.name = name
        self.symbol = symbol
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.name is not None:
            result['Name'] = self.name

        if self.symbol is not None:
            result['Symbol'] = self.symbol

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Symbol') is not None:
            self.symbol = m.get('Symbol')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListSkillGroupConfigResponseBodyDataSkillGroupConfigRuleList(DaraModel):
    def __init__(
        self,
        rule_name_info: List[main_models.ListSkillGroupConfigResponseBodyDataSkillGroupConfigRuleListRuleNameInfo] = None,
    ):
        self.rule_name_info = rule_name_info

    def validate(self):
        if self.rule_name_info:
            for v1 in self.rule_name_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RuleNameInfo'] = []
        if self.rule_name_info is not None:
            for k1 in self.rule_name_info:
                result['RuleNameInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rule_name_info = []
        if m.get('RuleNameInfo') is not None:
            for k1 in m.get('RuleNameInfo'):
                temp_model = main_models.ListSkillGroupConfigResponseBodyDataSkillGroupConfigRuleListRuleNameInfo()
                self.rule_name_info.append(temp_model.from_map(k1))

        return self

class ListSkillGroupConfigResponseBodyDataSkillGroupConfigRuleListRuleNameInfo(DaraModel):
    def __init__(
        self,
        rid: int = None,
        rule_name: str = None,
    ):
        self.rid = rid
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rid is not None:
            result['Rid'] = self.rid

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        return self

class ListSkillGroupConfigResponseBodyDataSkillGroupConfigAllRuleList(DaraModel):
    def __init__(
        self,
        rule_name_info: List[main_models.ListSkillGroupConfigResponseBodyDataSkillGroupConfigAllRuleListRuleNameInfo] = None,
    ):
        self.rule_name_info = rule_name_info

    def validate(self):
        if self.rule_name_info:
            for v1 in self.rule_name_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RuleNameInfo'] = []
        if self.rule_name_info is not None:
            for k1 in self.rule_name_info:
                result['RuleNameInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rule_name_info = []
        if m.get('RuleNameInfo') is not None:
            for k1 in m.get('RuleNameInfo'):
                temp_model = main_models.ListSkillGroupConfigResponseBodyDataSkillGroupConfigAllRuleListRuleNameInfo()
                self.rule_name_info.append(temp_model.from_map(k1))

        return self

class ListSkillGroupConfigResponseBodyDataSkillGroupConfigAllRuleListRuleNameInfo(DaraModel):
    def __init__(
        self,
        rid: int = None,
        rule_name: str = None,
    ):
        self.rid = rid
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rid is not None:
            result['Rid'] = self.rid

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        return self

