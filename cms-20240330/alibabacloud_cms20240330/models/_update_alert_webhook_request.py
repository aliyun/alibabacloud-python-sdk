# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class UpdateAlertWebhookRequest(DaraModel):
    def __init__(
        self,
        content_type: str = None,
        headers: Dict[str, str] = None,
        lang: str = None,
        method: str = None,
        name: str = None,
        url: str = None,
    ):
        self.content_type = content_type
        # headers
        self.headers = headers
        self.lang = lang
        self.method = method
        self.name = name
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_type is not None:
            result['contentType'] = self.content_type

        if self.headers is not None:
            result['headers'] = self.headers

        if self.lang is not None:
            result['lang'] = self.lang

        if self.method is not None:
            result['method'] = self.method

        if self.name is not None:
            result['name'] = self.name

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')

        if m.get('headers') is not None:
            self.headers = m.get('headers')

        if m.get('lang') is not None:
            self.lang = m.get('lang')

        if m.get('method') is not None:
            self.method = m.get('method')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

