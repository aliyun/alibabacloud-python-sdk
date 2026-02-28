# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExportDoNotCallNumbersRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        scope: str = None,
        search_pattern: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.scope = scope
        self.search_pattern = search_pattern

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.search_pattern is not None:
            result['SearchPattern'] = self.search_pattern

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('SearchPattern') is not None:
            self.search_pattern = m.get('SearchPattern')

        return self

