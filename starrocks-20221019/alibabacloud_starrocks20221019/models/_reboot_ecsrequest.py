# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RebootECSRequest(DaraModel):
    def __init__(
        self,
        event_id: str = None,
        instance_id: str = None,
        reboot_time: int = None,
    ):
        self.event_id = event_id
        self.instance_id = instance_id
        self.reboot_time = reboot_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.reboot_time is not None:
            result['RebootTime'] = self.reboot_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RebootTime') is not None:
            self.reboot_time = m.get('RebootTime')

        return self

