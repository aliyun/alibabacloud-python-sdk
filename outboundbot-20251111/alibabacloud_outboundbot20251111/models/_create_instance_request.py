# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateInstanceRequest(DaraModel):
    def __init__(
        self,
        concurrency: int = None,
        description: str = None,
        name: str = None,
        service_mode: str = None,
    ):
        # The number of concurrent calls.
        self.concurrency = concurrency
        # The instance description.
        self.description = description
        # The instance name.
        self.name = name
        # The service mode.
        self.service_mode = service_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.service_mode is not None:
            result['ServiceMode'] = self.service_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Concurrency') is not None:
            self.concurrency = m.get('Concurrency')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ServiceMode') is not None:
            self.service_mode = m.get('ServiceMode')

        return self

