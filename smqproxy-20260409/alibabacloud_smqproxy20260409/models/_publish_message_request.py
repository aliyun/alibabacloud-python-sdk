# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_smqproxy20260409 import models as main_models
from darabonba.model import DaraModel

class PublishMessageRequest(DaraModel):
    def __init__(
        self,
        message_attributes: main_models.PublishMessageRequestMessageAttributes = None,
        message_body: str = None,
        message_tag: str = None,
    ):
        self.message_attributes = message_attributes
        self.message_body = message_body
        self.message_tag = message_tag

    def validate(self):
        if self.message_attributes:
            self.message_attributes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message_attributes is not None:
            result['MessageAttributes'] = self.message_attributes.to_map()

        if self.message_body is not None:
            result['MessageBody'] = self.message_body

        if self.message_tag is not None:
            result['MessageTag'] = self.message_tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageAttributes') is not None:
            temp_model = main_models.PublishMessageRequestMessageAttributes()
            self.message_attributes = temp_model.from_map(m.get('MessageAttributes'))

        if m.get('MessageBody') is not None:
            self.message_body = m.get('MessageBody')

        if m.get('MessageTag') is not None:
            self.message_tag = m.get('MessageTag')

        return self

class PublishMessageRequestMessageAttributes(DaraModel):
    def __init__(
        self,
        direct_mail: str = None,
        direct_sms: str = None,
        push: str = None,
    ):
        self.direct_mail = direct_mail
        self.direct_sms = direct_sms
        self.push = push

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.direct_mail is not None:
            result['DirectMail'] = self.direct_mail

        if self.direct_sms is not None:
            result['DirectSMS'] = self.direct_sms

        if self.push is not None:
            result['Push'] = self.push

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectMail') is not None:
            self.direct_mail = m.get('DirectMail')

        if m.get('DirectSMS') is not None:
            self.direct_sms = m.get('DirectSMS')

        if m.get('Push') is not None:
            self.push = m.get('Push')

        return self

