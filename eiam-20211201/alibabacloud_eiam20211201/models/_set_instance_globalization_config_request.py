# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetInstanceGlobalizationConfigRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        language: str = None,
        time_zone: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The language type.
        # 
        # This parameter is required.
        self.language = language
        # The time zone.
        # 
        # This parameter is required.
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.language is not None:
            result['Language'] = self.language

        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')

        return self

