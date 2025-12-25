# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class ListWarningConfigResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListWarningConfigResponseBodyData = None,
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
            temp_model = main_models.ListWarningConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListWarningConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        warning_config_info: List[main_models.ListWarningConfigResponseBodyDataWarningConfigInfo] = None,
    ):
        self.warning_config_info = warning_config_info

    def validate(self):
        if self.warning_config_info:
            for v1 in self.warning_config_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['WarningConfigInfo'] = []
        if self.warning_config_info is not None:
            for k1 in self.warning_config_info:
                result['WarningConfigInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.warning_config_info = []
        if m.get('WarningConfigInfo') is not None:
            for k1 in m.get('WarningConfigInfo'):
                temp_model = main_models.ListWarningConfigResponseBodyDataWarningConfigInfo()
                self.warning_config_info.append(temp_model.from_map(k1))

        return self

class ListWarningConfigResponseBodyDataWarningConfigInfo(DaraModel):
    def __init__(
        self,
        channels: main_models.ListWarningConfigResponseBodyDataWarningConfigInfoChannels = None,
        config_id: int = None,
        config_name: str = None,
        create_time: str = None,
        rid_list: main_models.ListWarningConfigResponseBodyDataWarningConfigInfoRidList = None,
        rule_list: main_models.ListWarningConfigResponseBodyDataWarningConfigInfoRuleList = None,
        status: int = None,
        update_time: str = None,
    ):
        self.channels = channels
        self.config_id = config_id
        self.config_name = config_name
        self.create_time = create_time
        self.rid_list = rid_list
        self.rule_list = rule_list
        self.status = status
        self.update_time = update_time

    def validate(self):
        if self.channels:
            self.channels.validate()
        if self.rid_list:
            self.rid_list.validate()
        if self.rule_list:
            self.rule_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channels is not None:
            result['Channels'] = self.channels.to_map()

        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.config_name is not None:
            result['ConfigName'] = self.config_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.rid_list is not None:
            result['RidList'] = self.rid_list.to_map()

        if self.rule_list is not None:
            result['RuleList'] = self.rule_list.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channels') is not None:
            temp_model = main_models.ListWarningConfigResponseBodyDataWarningConfigInfoChannels()
            self.channels = temp_model.from_map(m.get('Channels'))

        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('ConfigName') is not None:
            self.config_name = m.get('ConfigName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('RidList') is not None:
            temp_model = main_models.ListWarningConfigResponseBodyDataWarningConfigInfoRidList()
            self.rid_list = temp_model.from_map(m.get('RidList'))

        if m.get('RuleList') is not None:
            temp_model = main_models.ListWarningConfigResponseBodyDataWarningConfigInfoRuleList()
            self.rule_list = temp_model.from_map(m.get('RuleList'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class ListWarningConfigResponseBodyDataWarningConfigInfoRuleList(DaraModel):
    def __init__(
        self,
        warning_rule: List[main_models.ListWarningConfigResponseBodyDataWarningConfigInfoRuleListWarningRule] = None,
    ):
        self.warning_rule = warning_rule

    def validate(self):
        if self.warning_rule:
            for v1 in self.warning_rule:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['WarningRule'] = []
        if self.warning_rule is not None:
            for k1 in self.warning_rule:
                result['WarningRule'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.warning_rule = []
        if m.get('WarningRule') is not None:
            for k1 in m.get('WarningRule'):
                temp_model = main_models.ListWarningConfigResponseBodyDataWarningConfigInfoRuleListWarningRule()
                self.warning_rule.append(temp_model.from_map(k1))

        return self

class ListWarningConfigResponseBodyDataWarningConfigInfoRuleListWarningRule(DaraModel):
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

class ListWarningConfigResponseBodyDataWarningConfigInfoRidList(DaraModel):
    def __init__(
        self,
        rid_list: List[str] = None,
    ):
        self.rid_list = rid_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rid_list is not None:
            result['RidList'] = self.rid_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RidList') is not None:
            self.rid_list = m.get('RidList')

        return self

class ListWarningConfigResponseBodyDataWarningConfigInfoChannels(DaraModel):
    def __init__(
        self,
        channel: List[main_models.ListWarningConfigResponseBodyDataWarningConfigInfoChannelsChannel] = None,
    ):
        self.channel = channel

    def validate(self):
        if self.channel:
            for v1 in self.channel:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Channel'] = []
        if self.channel is not None:
            for k1 in self.channel:
                result['Channel'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.channel = []
        if m.get('Channel') is not None:
            for k1 in m.get('Channel'):
                temp_model = main_models.ListWarningConfigResponseBodyDataWarningConfigInfoChannelsChannel()
                self.channel.append(temp_model.from_map(k1))

        return self

class ListWarningConfigResponseBodyDataWarningConfigInfoChannelsChannel(DaraModel):
    def __init__(
        self,
        type: int = None,
        url: str = None,
    ):
        self.type = type
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['Type'] = self.type

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

