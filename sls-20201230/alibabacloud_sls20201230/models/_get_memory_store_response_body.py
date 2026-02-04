# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMemoryStoreResponseBody(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        custom_instructions: str = None,
        description: str = None,
        enable_graph: bool = None,
        name: str = None,
        request_id: str = None,
        short_term_ttl: int = None,
        strategy: str = None,
        update_time: int = None,
    ):
        self.create_time = create_time
        self.custom_instructions = custom_instructions
        self.description = description
        self.enable_graph = enable_graph
        self.name = name
        self.request_id = request_id
        self.short_term_ttl = short_term_ttl
        self.strategy = strategy
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.custom_instructions is not None:
            result['customInstructions'] = self.custom_instructions

        if self.description is not None:
            result['description'] = self.description

        if self.enable_graph is not None:
            result['enableGraph'] = self.enable_graph

        if self.name is not None:
            result['name'] = self.name

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.short_term_ttl is not None:
            result['shortTermTtl'] = self.short_term_ttl

        if self.strategy is not None:
            result['strategy'] = self.strategy

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('customInstructions') is not None:
            self.custom_instructions = m.get('customInstructions')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('enableGraph') is not None:
            self.enable_graph = m.get('enableGraph')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('shortTermTtl') is not None:
            self.short_term_ttl = m.get('shortTermTtl')

        if m.get('strategy') is not None:
            self.strategy = m.get('strategy')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

