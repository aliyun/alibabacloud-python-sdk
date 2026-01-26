# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDispatchRuleRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        region_id: str = None,
        system: bool = None,
    ):
        # The name of the notification policy. Fuzzy match is supported.
        self.name = name
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # *   The type of notification policies to be queried. Valid values: `false` (default): notification policies created in Application Real-Time Monitoring Service (ARMS).
        # *   `true`: notification policies created in an external system.
        # 
        # >  You cannot use the ARMS console to modify the dispatch rules of a notification policy that is created in an external system.
        self.system = system

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.system is not None:
            result['System'] = self.system

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('System') is not None:
            self.system = m.get('System')

        return self

