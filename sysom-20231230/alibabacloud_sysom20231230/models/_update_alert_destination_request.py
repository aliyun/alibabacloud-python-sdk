# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class UpdateAlertDestinationRequest(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        params: main_models.UpdateAlertDestinationRequestParams = None,
        source: str = None,
        target: str = None,
    ):
        self.id = id
        self.name = name
        self.params = params
        self.source = source
        self.target = target

    def validate(self):
        if self.params:
            self.params.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.params is not None:
            result['params'] = self.params.to_map()

        if self.source is not None:
            result['source'] = self.source

        if self.target is not None:
            result['target'] = self.target

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('params') is not None:
            temp_model = main_models.UpdateAlertDestinationRequestParams()
            self.params = temp_model.from_map(m.get('params'))

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('target') is not None:
            self.target = m.get('target')

        return self

class UpdateAlertDestinationRequestParams(DaraModel):
    def __init__(
        self,
        email: str = None,
        phone: str = None,
        sec: str = None,
        webhook: str = None,
    ):
        self.email = email
        self.phone = phone
        self.sec = sec
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

