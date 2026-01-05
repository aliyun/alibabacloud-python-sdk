# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPluginClassesRequest(DaraModel):
    def __init__(
        self,
        alias_like: str = None,
        direction: str = None,
        exclude_builtin_ai_proxy: bool = None,
        gateway_id: str = None,
        gateway_type: str = None,
        installed: bool = None,
        name_like: str = None,
        page_number: int = None,
        page_size: int = None,
        source: str = None,
        type: str = None,
    ):
        self.alias_like = alias_like
        self.direction = direction
        self.exclude_builtin_ai_proxy = exclude_builtin_ai_proxy
        self.gateway_id = gateway_id
        self.gateway_type = gateway_type
        self.installed = installed
        self.name_like = name_like
        self.page_number = page_number
        self.page_size = page_size
        self.source = source
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias_like is not None:
            result['aliasLike'] = self.alias_like

        if self.direction is not None:
            result['direction'] = self.direction

        if self.exclude_builtin_ai_proxy is not None:
            result['excludeBuiltinAiProxy'] = self.exclude_builtin_ai_proxy

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.gateway_type is not None:
            result['gatewayType'] = self.gateway_type

        if self.installed is not None:
            result['installed'] = self.installed

        if self.name_like is not None:
            result['nameLike'] = self.name_like

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.source is not None:
            result['source'] = self.source

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliasLike') is not None:
            self.alias_like = m.get('aliasLike')

        if m.get('direction') is not None:
            self.direction = m.get('direction')

        if m.get('excludeBuiltinAiProxy') is not None:
            self.exclude_builtin_ai_proxy = m.get('excludeBuiltinAiProxy')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('gatewayType') is not None:
            self.gateway_type = m.get('gatewayType')

        if m.get('installed') is not None:
            self.installed = m.get('installed')

        if m.get('nameLike') is not None:
            self.name_like = m.get('nameLike')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

