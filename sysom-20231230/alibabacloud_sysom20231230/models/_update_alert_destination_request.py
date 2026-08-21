# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class UpdateAlertDestinationRequest(DaraModel):
    def __init__(
        self,
        x_debug_id: str = None,
        app_id: str = None,
        app_secret: str = None,
        group_id: List[str] = None,
        id: str = None,
        imbot: bool = None,
        name: str = None,
        params: main_models.UpdateAlertDestinationRequestParams = None,
        source: str = None,
        target: str = None,
        x_sysom_invoke_source: str = None,
    ):
        self.x_debug_id = x_debug_id
        self.app_id = app_id
        self.app_secret = app_secret
        self.group_id = group_id
        # The ID of the alert contact.
        self.id = id
        self.imbot = imbot
        # The name of the alert contact.
        self.name = name
        # The configuration parameters.
        self.params = params
        # The configuration source.
        self.source = source
        # The alert notification target. Currently, only DingTalk contacts are supported.
        self.target = target
        self.x_sysom_invoke_source = x_sysom_invoke_source

    def validate(self):
        if self.params:
            self.params.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x_debug_id is not None:
            result['X-Debug-Id'] = self.x_debug_id

        if self.app_id is not None:
            result['app_id'] = self.app_id

        if self.app_secret is not None:
            result['app_secret'] = self.app_secret

        if self.group_id is not None:
            result['group_id'] = self.group_id

        if self.id is not None:
            result['id'] = self.id

        if self.imbot is not None:
            result['imbot'] = self.imbot

        if self.name is not None:
            result['name'] = self.name

        if self.params is not None:
            result['params'] = self.params.to_map()

        if self.source is not None:
            result['source'] = self.source

        if self.target is not None:
            result['target'] = self.target

        if self.x_sysom_invoke_source is not None:
            result['x-sysom-invoke-source'] = self.x_sysom_invoke_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Debug-Id') is not None:
            self.x_debug_id = m.get('X-Debug-Id')

        if m.get('app_id') is not None:
            self.app_id = m.get('app_id')

        if m.get('app_secret') is not None:
            self.app_secret = m.get('app_secret')

        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('imbot') is not None:
            self.imbot = m.get('imbot')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('params') is not None:
            temp_model = main_models.UpdateAlertDestinationRequestParams()
            self.params = temp_model.from_map(m.get('params'))

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('target') is not None:
            self.target = m.get('target')

        if m.get('x-sysom-invoke-source') is not None:
            self.x_sysom_invoke_source = m.get('x-sysom-invoke-source')

        return self

class UpdateAlertDestinationRequestParams(DaraModel):
    def __init__(
        self,
        email: str = None,
        phone: str = None,
        sec: str = None,
        webhook: str = None,
    ):
        # The email address.
        self.email = email
        # The phone number.
        self.phone = phone
        # The secret key of the chatbot.
        self.sec = sec
        # The webhook URL of the chatbot.
        self.webhook = webhook

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.email is not None:
            result['email'] = self.email

        if self.phone is not None:
            result['phone'] = self.phone

        if self.sec is not None:
            result['sec'] = self.sec

        if self.webhook is not None:
            result['webhook'] = self.webhook

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('email') is not None:
            self.email = m.get('email')

        if m.get('phone') is not None:
            self.phone = m.get('phone')

        if m.get('sec') is not None:
            self.sec = m.get('sec')

        if m.get('webhook') is not None:
            self.webhook = m.get('webhook')

        return self

