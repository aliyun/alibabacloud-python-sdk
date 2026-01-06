# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class SetEventSubscriptionResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.SetEventSubscriptionResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The HTTP status code returned.
        self.code = code
        # The detailed information.
        self.data = data
        # The returned message.
        # 
        # >  If the request was successful, **Successful** is returned. If the request failed, an error message such as an error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
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
            temp_model = main_models.SetEventSubscriptionResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class SetEventSubscriptionResponseBodyData(DaraModel):
    def __init__(
        self,
        active: int = None,
        channel_type: str = None,
        contact_group_name: str = None,
        contact_name: str = None,
        event_context: str = None,
        instance_id: str = None,
        lang: str = None,
        level: str = None,
        min_interval: int = None,
        user_id: str = None,
    ):
        # Indicates whether the event subscription feature is enabled. Valid values:
        # 
        # *   **0**: The event subscription feature is disabled.
        # *   **1**: The event subscription feature is enabled.
        self.active = active
        # The notification method. Valid values:
        # 
        # *   **hdm_alarm_sms**: text message.
        # *   **dingtalk**: DingTalk chatbot.
        # *   **hdm_alarm_sms_and_email**: text message and email.
        # *   **hdm_alarm_sms,dingtalk**: text message and DingTalk chatbot.
        self.channel_type = channel_type
        # The name of the contact group that receives alert notifications. Multiple names are separated by commas (,).
        self.contact_group_name = contact_group_name
        # The name of the contact who receives alert notifications. Multiple names are separated by commas (,).
        self.contact_name = contact_name
        # The supported event scenarios. Only **AllContext** is returned for this parameter, which indicates that all scenarios are supported.
        self.event_context = event_context
        # The instance ID.
        self.instance_id = instance_id
        # The language of event notifications. Only **zh-CN** is returned for this parameter, which indicates that event notifications are sent in Chinese.
        self.lang = lang
        # The risk level of the events. Valid values:
        # 
        # *   **Notice**
        # *   **Optimization**
        # *   **Warn**
        # *   **Critical**
        self.level = level
        # The minimum interval between consecutive event notifications. Unit: seconds.
        self.min_interval = min_interval
        # The user ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active is not None:
            result['active'] = self.active

        if self.channel_type is not None:
            result['channelType'] = self.channel_type

        if self.contact_group_name is not None:
            result['contactGroupName'] = self.contact_group_name

        if self.contact_name is not None:
            result['contactName'] = self.contact_name

        if self.event_context is not None:
            result['eventContext'] = self.event_context

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.lang is not None:
            result['lang'] = self.lang

        if self.level is not None:
            result['level'] = self.level

        if self.min_interval is not None:
            result['minInterval'] = self.min_interval

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')

        if m.get('channelType') is not None:
            self.channel_type = m.get('channelType')

        if m.get('contactGroupName') is not None:
            self.contact_group_name = m.get('contactGroupName')

        if m.get('contactName') is not None:
            self.contact_name = m.get('contactName')

        if m.get('eventContext') is not None:
            self.event_context = m.get('eventContext')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('lang') is not None:
            self.lang = m.get('lang')

        if m.get('level') is not None:
            self.level = m.get('level')

        if m.get('minInterval') is not None:
            self.min_interval = m.get('minInterval')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

