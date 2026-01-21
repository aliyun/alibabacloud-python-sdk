# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeContactListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        contacts: main_models.DescribeContactListResponseBodyContacts = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        # The HTTP status code.
        # 
        # >  The status code 200 indicates that the request was successful.
        self.code = code
        # The alert contacts.
        self.contacts = contacts
        # The error message returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.contacts:
            self.contacts.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.contacts is not None:
            result['Contacts'] = self.contacts.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Contacts') is not None:
            temp_model = main_models.DescribeContactListResponseBodyContacts()
            self.contacts = temp_model.from_map(m.get('Contacts'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeContactListResponseBodyContacts(DaraModel):
    def __init__(
        self,
        contact: List[main_models.DescribeContactListResponseBodyContactsContact] = None,
    ):
        self.contact = contact

    def validate(self):
        if self.contact:
            for v1 in self.contact:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Contact'] = []
        if self.contact is not None:
            for k1 in self.contact:
                result['Contact'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contact = []
        if m.get('Contact') is not None:
            for k1 in m.get('Contact'):
                temp_model = main_models.DescribeContactListResponseBodyContactsContact()
                self.contact.append(temp_model.from_map(k1))

        return self

class DescribeContactListResponseBodyContactsContact(DaraModel):
    def __init__(
        self,
        channels: main_models.DescribeContactListResponseBodyContactsContactChannels = None,
        channels_state: main_models.DescribeContactListResponseBodyContactsContactChannelsState = None,
        contact_groups: main_models.DescribeContactListResponseBodyContactsContactContactGroups = None,
        create_time: int = None,
        desc: str = None,
        lang: str = None,
        name: str = None,
        update_time: int = None,
    ):
        # The alert notification method.
        self.channels = channels
        # The status of the alert notification method. Valid values: PENDING and OK.
        # 
        # The email address must be activated after it is added as the value specified for the alert notification method. The value PENDING indicates that the email address is not activated. The value OK indicates that the email address is activated.
        self.channels_state = channels_state
        # None.
        self.contact_groups = contact_groups
        # The timestamp when the alert contact was created.
        # 
        # Unit: milliseconds.
        self.create_time = create_time
        # The description.
        self.desc = desc
        # The language in which the alert information is displayed. Valid values:
        # 
        # *   zh-cn: simplified Chinese
        # *   en: English
        self.lang = lang
        # The name of the alert contact.
        self.name = name
        # The timestamp when the alert contact was updated.
        # 
        # Unit: milliseconds.
        self.update_time = update_time

    def validate(self):
        if self.channels:
            self.channels.validate()
        if self.channels_state:
            self.channels_state.validate()
        if self.contact_groups:
            self.contact_groups.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channels is not None:
            result['Channels'] = self.channels.to_map()

        if self.channels_state is not None:
            result['ChannelsState'] = self.channels_state.to_map()

        if self.contact_groups is not None:
            result['ContactGroups'] = self.contact_groups.to_map()

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.desc is not None:
            result['Desc'] = self.desc

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.name is not None:
            result['Name'] = self.name

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channels') is not None:
            temp_model = main_models.DescribeContactListResponseBodyContactsContactChannels()
            self.channels = temp_model.from_map(m.get('Channels'))

        if m.get('ChannelsState') is not None:
            temp_model = main_models.DescribeContactListResponseBodyContactsContactChannelsState()
            self.channels_state = temp_model.from_map(m.get('ChannelsState'))

        if m.get('ContactGroups') is not None:
            temp_model = main_models.DescribeContactListResponseBodyContactsContactContactGroups()
            self.contact_groups = temp_model.from_map(m.get('ContactGroups'))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class DescribeContactListResponseBodyContactsContactContactGroups(DaraModel):
    def __init__(
        self,
        contact_group: List[str] = None,
    ):
        self.contact_group = contact_group

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_group is not None:
            result['ContactGroup'] = self.contact_group

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroup') is not None:
            self.contact_group = m.get('ContactGroup')

        return self

class DescribeContactListResponseBodyContactsContactChannelsState(DaraModel):
    def __init__(
        self,
        ali_im: str = None,
        ding_web_hook: str = None,
        mail: str = None,
        sms: str = None,
    ):
        # The status of the TradeManager ID.
        # 
        # Valid value: OK. The value OK indicates that the TradeManager ID is valid and can receive alert notifications.
        # 
        # >  This parameter applies only to the Alibaba Cloud China site (aliyun.com).
        self.ali_im = ali_im
        # The status of the DingTalk chatbot.
        # 
        # Valid value: OK. The value OK indicates that the DingTalk chatbot is normal and alert notifications can be received in a DingTalk group.
        self.ding_web_hook = ding_web_hook
        # The status of the email address. Valid values:
        # 
        # *   PENDING: The phone number is not activated. Alert notifications can be sent to the phone number by using text messages only after the phone number is activated.
        # *   OK: The phone number is activated and can receive alert notifications.
        self.mail = mail
        # The status of the phone number. Valid values:
        # 
        # *   PENDING: The phone number is not activated. Alert notifications can be sent to the phone number by using text messages only after the phone number is activated.
        # *   OK: The phone number is activated and can receive alert notifications.
        # 
        # >  This parameter applies only to the Alibaba Cloud China site (aliyun.com).
        self.sms = sms

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_im is not None:
            result['AliIM'] = self.ali_im

        if self.ding_web_hook is not None:
            result['DingWebHook'] = self.ding_web_hook

        if self.mail is not None:
            result['Mail'] = self.mail

        if self.sms is not None:
            result['SMS'] = self.sms

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliIM') is not None:
            self.ali_im = m.get('AliIM')

        if m.get('DingWebHook') is not None:
            self.ding_web_hook = m.get('DingWebHook')

        if m.get('Mail') is not None:
            self.mail = m.get('Mail')

        if m.get('SMS') is not None:
            self.sms = m.get('SMS')

        return self

class DescribeContactListResponseBodyContactsContactChannels(DaraModel):
    def __init__(
        self,
        ali_im: str = None,
        ding_web_hook: str = None,
        mail: str = None,
        sms: str = None,
    ):
        # The TradeManager ID of the alert contact.
        self.ali_im = ali_im
        # The webhook URL of the DingTalk chatbot.
        self.ding_web_hook = ding_web_hook
        # The email address of the alert contact.
        self.mail = mail
        # The phone number of the alert contac.
        self.sms = sms

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_im is not None:
            result['AliIM'] = self.ali_im

        if self.ding_web_hook is not None:
            result['DingWebHook'] = self.ding_web_hook

        if self.mail is not None:
            result['Mail'] = self.mail

        if self.sms is not None:
            result['SMS'] = self.sms

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliIM') is not None:
            self.ali_im = m.get('AliIM')

        if m.get('DingWebHook') is not None:
            self.ding_web_hook = m.get('DingWebHook')

        if m.get('Mail') is not None:
            self.mail = m.get('Mail')

        if m.get('SMS') is not None:
            self.sms = m.get('SMS')

        return self

