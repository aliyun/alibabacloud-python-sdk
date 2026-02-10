# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateOrUpdateDingTalkRequest(DaraModel):
    def __init__(
        self,
        config_list: str = None,
        ding_talk_lang: str = None,
        group_id_list: str = None,
        id: int = None,
        interval_time: int = None,
        rule_action_name: str = None,
        send_url: str = None,
    ):
        # The alerts for which you want the chatbot to send notifications. The value is a JSON array that contains the following fields:
        # 
        # *   **type**: the types of alerts. The valid values are listed in the "Additional description of parameters" section in this topic.
        # 
        # *   **configItemList**: the list of check items. The value is a JSON array that contains the following fields:
        # 
        #     *   **key**: the key of the check item.
        #     *   **valueList**: the values of the check item. The value of valueList is a JSON array.
        # 
        # > For more information about the value of this parameter, see the "Addition description of parameters" section in this topic.
        self.config_list = config_list
        # The language of the notifications. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.ding_talk_lang = ding_talk_lang
        # The IDs of asset groups for which you want the chatbot to send notifications. The value is a JSON array.
        # 
        # > You can call the [DescribeGroupStruct](~~DescribeGroupStruct~~) operation to query the IDs of asset groups.
        self.group_id_list = group_id_list
        # The ID of the chatbot.
        # 
        # > You can call the [DescribeDingTalk](https://www.alibabacloud.com/help/en/security-center/developer-reference/api-sas-2018-12-03-describedingtalk/?spm=a2c63.p38356.0.0.681e4360Qd1eb1) operation to query the IDs of chatbots.
        self.id = id
        # The time interval at which the chatbot sends notifications.
        # 
        # > The value **0** indicates unlimited.
        self.interval_time = interval_time
        # The name of the chatbot.
        # 
        # > The name of a chatbot must be 2 to 64 characters in length.
        # 
        # This parameter is required.
        self.rule_action_name = rule_action_name
        # The webhook URL.
        # 
        # This parameter is required.
        self.send_url = send_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_list is not None:
            result['ConfigList'] = self.config_list

        if self.ding_talk_lang is not None:
            result['DingTalkLang'] = self.ding_talk_lang

        if self.group_id_list is not None:
            result['GroupIdList'] = self.group_id_list

        if self.id is not None:
            result['Id'] = self.id

        if self.interval_time is not None:
            result['IntervalTime'] = self.interval_time

        if self.rule_action_name is not None:
            result['RuleActionName'] = self.rule_action_name

        if self.send_url is not None:
            result['SendUrl'] = self.send_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigList') is not None:
            self.config_list = m.get('ConfigList')

        if m.get('DingTalkLang') is not None:
            self.ding_talk_lang = m.get('DingTalkLang')

        if m.get('GroupIdList') is not None:
            self.group_id_list = m.get('GroupIdList')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IntervalTime') is not None:
            self.interval_time = m.get('IntervalTime')

        if m.get('RuleActionName') is not None:
            self.rule_action_name = m.get('RuleActionName')

        if m.get('SendUrl') is not None:
            self.send_url = m.get('SendUrl')

        return self

