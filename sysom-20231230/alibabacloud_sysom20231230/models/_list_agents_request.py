# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAgentsRequest(DaraModel):
    def __init__(
        self,
        x_debug_id: str = None,
        current: int = None,
        name: str = None,
        page_size: int = None,
        type: str = None,
        x_sysom_invoke_source: str = None,
    ):
        self.x_debug_id = x_debug_id
        # The current page number (starting from page 1).
        self.current = current
        # Filters plug-ins by plug-in name.
        self.name = name
        # The number of entries per page.
        self.page_size = page_size
        # Filters the list by Agent type. For example, pass control to retrieve all Agents of the control type.
        self.type = type
        self.x_sysom_invoke_source = x_sysom_invoke_source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x_debug_id is not None:
            result['X-Debug-Id'] = self.x_debug_id

        if self.current is not None:
            result['current'] = self.current

        if self.name is not None:
            result['name'] = self.name

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.type is not None:
            result['type'] = self.type

        if self.x_sysom_invoke_source is not None:
            result['x-sysom-invoke-source'] = self.x_sysom_invoke_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Debug-Id') is not None:
            self.x_debug_id = m.get('X-Debug-Id')

        if m.get('current') is not None:
            self.current = m.get('current')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('x-sysom-invoke-source') is not None:
            self.x_sysom_invoke_source = m.get('x-sysom-invoke-source')

        return self

