# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class Hook(DaraModel):
    def __init__(
        self,
        api_version: str = None,
        description: str = None,
        enabled: bool = None,
        event: str = None,
        headers: Dict[str, str] = None,
        timeout: int = None,
        url: str = None,
    ):
        self.api_version = api_version
        self.description = description
        self.enabled = enabled
        # This parameter is required.
        self.event = event
        self.headers = headers
        self.timeout = timeout
        # This parameter is required.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_version is not None:
            result['apiVersion'] = self.api_version

        if self.description is not None:
            result['description'] = self.description

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.event is not None:
            result['event'] = self.event

        if self.headers is not None:
            result['headers'] = self.headers

        if self.timeout is not None:
            result['timeout'] = self.timeout

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('event') is not None:
            self.event = m.get('event')

        if m.get('headers') is not None:
            self.headers = m.get('headers')

        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

