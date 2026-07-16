# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDiagnosisSettingsRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        body: str = None,
        lang: str = None,
    ):
        # A unique token used to ensure idempotence of the request. The client generates this value. The value must be unique among different requests and cannot exceed 64 ASCII characters in length.
        self.client_token = client_token
        self.body = body
        # The language of the response. Default value: en.
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.body is not None:
            result['body'] = self.body

        if self.lang is not None:
            result['lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('body') is not None:
            self.body = m.get('body')

        if m.get('lang') is not None:
            self.lang = m.get('lang')

        return self

