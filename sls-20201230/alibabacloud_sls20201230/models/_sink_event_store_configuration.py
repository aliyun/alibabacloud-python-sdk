# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SinkEventStoreConfiguration(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        endpoint: str = None,
        event_store: str = None,
        project: str = None,
        role_arn: str = None,
    ):
        self.enabled = enabled
        self.endpoint = endpoint
        self.event_store = event_store
        self.project = project
        self.role_arn = role_arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.endpoint is not None:
            result['endpoint'] = self.endpoint

        if self.event_store is not None:
            result['eventStore'] = self.event_store

        if self.project is not None:
            result['project'] = self.project

        if self.role_arn is not None:
            result['roleArn'] = self.role_arn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')

        if m.get('eventStore') is not None:
            self.event_store = m.get('eventStore')

        if m.get('project') is not None:
            self.project = m.get('project')

        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')

        return self

