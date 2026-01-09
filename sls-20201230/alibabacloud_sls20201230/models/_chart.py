# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class Chart(DaraModel):
    def __init__(
        self,
        action: Dict[str, Any] = None,
        display: Dict[str, Any] = None,
        search: Dict[str, Any] = None,
        title: str = None,
        type: str = None,
    ):
        # This parameter is required.
        self.action = action
        # This parameter is required.
        self.display = display
        # This parameter is required.
        self.search = search
        # This parameter is required.
        self.title = title
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['action'] = self.action

        if self.display is not None:
            result['display'] = self.display

        if self.search is not None:
            result['search'] = self.search

        if self.title is not None:
            result['title'] = self.title

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')

        if m.get('display') is not None:
            self.display = m.get('display')

        if m.get('search') is not None:
            self.search = m.get('search')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

