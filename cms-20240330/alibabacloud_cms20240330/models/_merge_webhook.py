# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class MergeWebhook(DaraModel):
    def __init__(
        self,
        content_type: str = None,
        extend: str = None,
        gmt_create: str = None,
        gmt_modified: Dict[str, Any] = None,
        headers: str = None,
        identifier: str = None,
        lang: str = None,
        method: str = None,
        name: str = None,
        source: str = None,
        type: str = None,
        webhook: str = None,
    ):
        # The content type.
        self.content_type = content_type
        # An extension field used to store additional configurations.
        self.extend = extend
        # The creation time.
        self.gmt_create = gmt_create
        # The last modification time.
        self.gmt_modified = gmt_modified
        # The request header.
        self.headers = headers
        # The unique identifier of the webhook.
        self.identifier = identifier
        # The language preference.
        self.lang = lang
        # The HTTP request method.
        self.method = method
        # The name of the webhook.
        self.name = name
        # The source system of the webhook.
        self.source = source
        # The type of the webhook. It indicates the destination platform.
        self.type = type
        # The webhook URL used to send requests.
        self.webhook = webhook

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_type is not None:
            result['contentType'] = self.content_type

        if self.extend is not None:
            result['extend'] = self.extend

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.headers is not None:
            result['headers'] = self.headers

        if self.identifier is not None:
            result['identifier'] = self.identifier

        if self.lang is not None:
            result['lang'] = self.lang

        if self.method is not None:
            result['method'] = self.method

        if self.name is not None:
            result['name'] = self.name

        if self.source is not None:
            result['source'] = self.source

        if self.type is not None:
            result['type'] = self.type

        if self.webhook is not None:
            result['webhook'] = self.webhook

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')

        if m.get('extend') is not None:
            self.extend = m.get('extend')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('headers') is not None:
            self.headers = m.get('headers')

        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')

        if m.get('lang') is not None:
            self.lang = m.get('lang')

        if m.get('method') is not None:
            self.method = m.get('method')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('webhook') is not None:
            self.webhook = m.get('webhook')

        return self

