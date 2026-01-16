# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from darabonba.model import DaraModel

class CDNTriggerConfig(DaraModel):
    def __init__(
        self,
        event_name: str = None,
        event_version: str = None,
        filter: Dict[str, List[str]] = None,
        notes: str = None,
    ):
        self.event_name = event_name
        self.event_version = event_version
        self.filter = filter
        self.notes = notes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_name is not None:
            result['eventName'] = self.event_name

        if self.event_version is not None:
            result['eventVersion'] = self.event_version

        if self.filter is not None:
            result['filter'] = self.filter

        if self.notes is not None:
            result['notes'] = self.notes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('eventName') is not None:
            self.event_name = m.get('eventName')

        if m.get('eventVersion') is not None:
            self.event_version = m.get('eventVersion')

        if m.get('filter') is not None:
            self.filter = m.get('filter')

        if m.get('notes') is not None:
            self.notes = m.get('notes')

        return self

