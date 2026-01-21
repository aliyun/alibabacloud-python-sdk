# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class PutContactRequest(DaraModel):
    def __init__(
        self,
        channels: main_models.PutContactRequestChannels = None,
        contact_name: str = None,
        describe: str = None,
        lang: str = None,
    ):
        self.channels = channels
        # The name of the alert contact.
        # 
        # This parameter is required.
        self.contact_name = contact_name
        # The description of the alert contact.
        # 
        # This parameter is required.
        self.describe = describe
        # The language in which the alert information is displayed. Valid values:
        # 
        # *   zh-cn: simplified Chinese
        # *   en: English
        # 
        # >  If you do not specify this parameter, CloudMonitor identifies the language of the alert information based on the region of your Alibaba Cloud account.
        self.lang = lang

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

        if self.contact_name is not None:
            result['ContactName'] = self.contact_name

        if self.describe is not None:
            result['Describe'] = self.describe

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channels') is not None:
            temp_model = main_models.PutContactRequestChannels()
            self.channels = temp_model.from_map(m.get('Channels'))

        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')

        if m.get('Describe') is not None:
            self.describe = m.get('Describe')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

class PutContactRequestChannels(DaraModel):
    def __init__(
        self,
        ali_im: str = None,
        ding_web_hook: str = None,
        mail: str = None,
        sms: str = None,
    ):
        # The TradeManager ID of the alert contact.
        # 
        # Specify at least one of the following alert notification methods: email address and DingTalk chatbot.
        self.ali_im = ali_im
        # The webhook URL of the DingTalk chatbot.
        # 
        # Specify at least one of the following alert notification methods: email address and DingTalk chatbot.
        self.ding_web_hook = ding_web_hook
        # The email address. After you add or modify an email address, the recipient receives an email that contains an activation link. The system adds the recipient to the list of alert contacts only after the recipient activates the email address.
        # 
        # Specify at least one of the following alert notification methods: email address and DingTalk chatbot.
        self.mail = mail
        # The phone number of the alert contact. After you add or modify a phone number, the recipient receives a text message that contains an activation link. The system adds the recipient to the list of alert contacts only after the recipient activates the phone number.
        # 
        # Specify at least one of the following alert notification methods: email address and DingTalk chatbot.
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

