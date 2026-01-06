# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class GetEventSubscriptionResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetEventSubscriptionResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The HTTP status code returned.
        self.code = code
        # The data returned.
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
            temp_model = main_models.GetEventSubscriptionResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetEventSubscriptionResponseBodyData(DaraModel):
    def __init__(
        self,
        active: int = None,
        channel_type: str = None,
        contact_group_name: str = None,
        contact_groups: List[main_models.GetEventSubscriptionResponseBodyDataContactGroups] = None,
        contact_name: str = None,
        contacts: List[main_models.GetEventSubscriptionResponseBodyDataContacts] = None,
        event_context: str = None,
        event_send_group: List[str] = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: int = None,
        instance_id: str = None,
        lang: str = None,
        level: str = None,
        min_interval: str = None,
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
        # The alert contact groups.
        self.contact_groups = contact_groups
        # The name of the subscriber who receives alert notifications. Multiple names are separated by commas (,).
        self.contact_name = contact_name
        # The user ID.
        self.contacts = contacts
        # The supported event scenarios. Only **AllContext** may be returned, which indicates that all scenarios are supported.
        self.event_context = event_context
        # The supported event scenarios in which event subscription can be sent.
        self.event_send_group = event_send_group
        # The time when event subscription was enabled. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.gmt_create = gmt_create
        # The time when the event subscription settings were most recently modified. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.gmt_modified = gmt_modified
        # The primary key ID of the database.
        self.id = id
        # The instance ID.
        self.instance_id = instance_id
        # The language of event notifications. Only **zh-CN** may be returned, which indicates that event notifications are sent in Chinese.
        self.lang = lang
        # The risk level of the events that trigger notifications. Valid values:
        # 
        # *   **Notice**
        # *   **Optimization**
        # *   **Warn**
        # *   **Critical**
        self.level = level
        # The minimum interval between event notifications. Unit: seconds.
        self.min_interval = min_interval
        # The user ID.
        self.user_id = user_id

    def validate(self):
        if self.contact_groups:
            for v1 in self.contact_groups:
                 if v1:
                    v1.validate()
        if self.contacts:
            for v1 in self.contacts:
                 if v1:
                    v1.validate()

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

        result['contactGroups'] = []
        if self.contact_groups is not None:
            for k1 in self.contact_groups:
                result['contactGroups'].append(k1.to_map() if k1 else None)

        if self.contact_name is not None:
            result['contactName'] = self.contact_name

        result['contacts'] = []
        if self.contacts is not None:
            for k1 in self.contacts:
                result['contacts'].append(k1.to_map() if k1 else None)

        if self.event_context is not None:
            result['eventContext'] = self.event_context

        if self.event_send_group is not None:
            result['eventSendGroup'] = self.event_send_group

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

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

        self.contact_groups = []
        if m.get('contactGroups') is not None:
            for k1 in m.get('contactGroups'):
                temp_model = main_models.GetEventSubscriptionResponseBodyDataContactGroups()
                self.contact_groups.append(temp_model.from_map(k1))

        if m.get('contactName') is not None:
            self.contact_name = m.get('contactName')

        self.contacts = []
        if m.get('contacts') is not None:
            for k1 in m.get('contacts'):
                temp_model = main_models.GetEventSubscriptionResponseBodyDataContacts()
                self.contacts.append(temp_model.from_map(k1))

        if m.get('eventContext') is not None:
            self.event_context = m.get('eventContext')

        if m.get('eventSendGroup') is not None:
            self.event_send_group = m.get('eventSendGroup')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

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

class GetEventSubscriptionResponseBodyDataContacts(DaraModel):
    def __init__(
        self,
        dingtalk_hook: str = None,
        email: str = None,
        groups: List[str] = None,
        is_cms_reduplicated: bool = None,
        name: str = None,
        phone: str = None,
        user_id: str = None,
    ):
        # The webhook URL of the DingTalk chatbot.
        self.dingtalk_hook = dingtalk_hook
        # The email address of the alert contact.
        self.email = email
        # The contact groups to which the alert contact belongs.
        self.groups = groups
        # Indicates whether the alert contact name is the same as the contact name on CloudMonitor.
        # 
        # * **true**
        # * **false**
        self.is_cms_reduplicated = is_cms_reduplicated
        # The name of the alert contact.
        self.name = name
        # The mobile number of the alert contact.
        self.phone = phone
        # The user ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dingtalk_hook is not None:
            result['dingtalkHook'] = self.dingtalk_hook

        if self.email is not None:
            result['email'] = self.email

        if self.groups is not None:
            result['groups'] = self.groups

        if self.is_cms_reduplicated is not None:
            result['isCmsReduplicated'] = self.is_cms_reduplicated

        if self.name is not None:
            result['name'] = self.name

        if self.phone is not None:
            result['phone'] = self.phone

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dingtalkHook') is not None:
            self.dingtalk_hook = m.get('dingtalkHook')

        if m.get('email') is not None:
            self.email = m.get('email')

        if m.get('groups') is not None:
            self.groups = m.get('groups')

        if m.get('isCmsReduplicated') is not None:
            self.is_cms_reduplicated = m.get('isCmsReduplicated')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('phone') is not None:
            self.phone = m.get('phone')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

class GetEventSubscriptionResponseBodyDataContactGroups(DaraModel):
    def __init__(
        self,
        contacts: str = None,
        description: str = None,
        name: str = None,
        user_id: str = None,
    ):
        # The members of the alert contact group.
        self.contacts = contacts
        # The description of the alert contact group.
        self.description = description
        # The name of the alert contact group.
        self.name = name
        # The user ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contacts is not None:
            result['contacts'] = self.contacts

        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contacts') is not None:
            self.contacts = m.get('contacts')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

