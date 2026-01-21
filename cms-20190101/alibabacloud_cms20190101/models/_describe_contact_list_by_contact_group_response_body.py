# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeContactListByContactGroupResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        contacts: main_models.DescribeContactListByContactGroupResponseBodyContacts = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        # 
        # >  The status code 200 indicates that the request was successful.
        self.code = code
        # The alert contacts that receive alert notifications.
        self.contacts = contacts
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Contacts') is not None:
            temp_model = main_models.DescribeContactListByContactGroupResponseBodyContacts()
            self.contacts = temp_model.from_map(m.get('Contacts'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeContactListByContactGroupResponseBodyContacts(DaraModel):
    def __init__(
        self,
        contact: List[main_models.DescribeContactListByContactGroupResponseBodyContactsContact] = None,
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
                temp_model = main_models.DescribeContactListByContactGroupResponseBodyContactsContact()
                self.contact.append(temp_model.from_map(k1))

        return self

class DescribeContactListByContactGroupResponseBodyContactsContact(DaraModel):
    def __init__(
        self,
        channels: main_models.DescribeContactListByContactGroupResponseBodyContactsContactChannels = None,
        create_time: int = None,
        desc: str = None,
        name: str = None,
        update_time: int = None,
    ):
        # The alert notification methods.
        self.channels = channels
        # The time when the alert contact was created.
        # 
        # Unit: milliseconds.
        self.create_time = create_time
        # The description of the alert contact.
        self.desc = desc
        # The name of the alert contact.
        self.name = name
        # The time when the alert contact was modified.
        # 
        # Unit: milliseconds.
        self.update_time = update_time

    def validate(self):
        if self.channels:
            self.channels.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channels is not None:
            result['Channels'] = self.channels.to_map()

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.desc is not None:
            result['Desc'] = self.desc

        if self.name is not None:
            result['Name'] = self.name

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channels') is not None:
            temp_model = main_models.DescribeContactListByContactGroupResponseBodyContactsContactChannels()
            self.channels = temp_model.from_map(m.get('Channels'))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class DescribeContactListByContactGroupResponseBodyContactsContactChannels(DaraModel):
    def __init__(
        self,
        ali_im: str = None,
        ding_web_hook: str = None,
        mail: str = None,
        sms: str = None,
    ):
        # The TradeManager ID of the alert contact.
        # 
        # >  This parameter can be returned only on the China site (aliyun.com).
        self.ali_im = ali_im
        # The webhook URL of the DingTalk chatbot.
        self.ding_web_hook = ding_web_hook
        # The email address of the alert contact.
        self.mail = mail
        # The mobile number of the alert contact.
        # 
        # >  This parameter can be returned only on the China site (aliyun.com).
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

